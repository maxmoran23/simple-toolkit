"""Focused register assembly: exact inclusion, dependency closure, and transport safety."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import bundle
import context_report
import markdown_utils as md

REGISTER = '''# Sources

## 1. Governance
Always retain this instruction.

## 8. Registry

### 8.1 First domain

| 01.001 | T1 | [one](https://example.org/one) |

### 8.2 Second domain

| 02.001 | T1 | [two](https://example.org/two) |
[related](#83-third-domain)

### 8.3 Third domain

| 03.001 | T1 | [three](https://example.org/three) |

## 9. Workflow packs
These can refer to sources that are not loaded.

## 10. Maintenance
Keep the review date.
'''


class SourceFocusTests(unittest.TestCase):
    def test_subset_keeps_governance_and_exact_rows(self):
        texts = {'02': REGISTER}
        selection = bundle.select_source_domains(texts, ['01'])
        self.assertEqual(selection['included_domains'], ['01'])
        self.assertEqual(selection['included_source_rows'], 1)
        self.assertEqual(selection['total_source_rows'], 3)
        self.assertIn('Always retain this instruction.', texts['02'])
        self.assertIn('Keep the review date.', texts['02'])
        self.assertIn('| 01.001 |', texts['02'])
        self.assertNotIn('| 02.001 |', texts['02'])
        self.assertNotIn('| 03.001 |', texts['02'])

    def test_explicit_dependencies_expand_transitively(self):
        texts = {'02': REGISTER, '00': '# Operating\n[need](02-sources.md#82-second-domain)\n'}
        selection = bundle.select_source_domains(texts, ['01'])
        self.assertEqual(selection['included_domains'], ['01', '02', '03'])
        self.assertEqual(selection['dependency_domains'], ['02', '03'])
        self.assertEqual(texts['02'], REGISTER)

    def test_invalid_domains_and_missing_module_rejected(self):
        for selectors in [[], [''], ['1'], ['99'], ['01', '01']]:
            with self.subTest(selectors=selectors), self.assertRaises(ValueError):
                bundle.select_source_domains({'02': REGISTER}, selectors)
        with self.assertRaisesRegex(ValueError, 'requires module 02'):
            bundle.select_source_domains({'00': '# Operating'}, ['01'])

    def test_changed_register_structure_rejects_instead_of_guessing(self):
        for text in [REGISTER.replace('## 8. Registry', '## Registry'),
                     REGISTER.replace('### 8.3 Third domain', '### New unnumbered domain'),
                     REGISTER.replace('### 8.3 Third domain', '### 8.2 Duplicated domain'),
                     REGISTER.replace('| 01.001 |', '| Source |')]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                bundle.source_domain_sections(text)

    def test_focused_real_bundle_is_deterministic_and_links_resolve(self):
        modules = list(bundle.BUNDLES['research']['modules'])
        text, stats = bundle.build(modules, 'focused', None, ['16', '01'])
        again, duplicate = bundle.build(modules, 'focused', None, ['01', '16'])
        self.assertEqual((text, stats), (again, duplicate))
        _, full_stats = bundle.build(modules, 'focused', None)
        self.assertLess(stats['tokens'], full_stats['tokens'] * .75)
        self.assertEqual(stats['tokens'], (len(text) + 3) // 4)
        self.assertIn('complete task coverage or current source verification', text)
        self.assertIn('## 10. Registry maintenance controls', text)
        anchors = md.anchors(text)
        self.assertTrue(all(link.target[1:] in anchors for link in md.links(text) if link.target.startswith('#')))
        self.assertEqual(len([row for row in md.headings(text) if row[1] == 1]), 1)

    def test_every_real_domain_can_be_selected_without_dangling_links(self):
        original = bundle.module_files()['02'].read_text()
        sections = bundle.source_domain_sections(original)
        for code, section in sections.items():
            with self.subTest(domain=code):
                text, stats = bundle.build(['02'], 'single-domain', None, [code])
                self.assertEqual(stats['source_selection']['included_domains'], [code])
                self.assertEqual(stats['source_selection']['included_source_rows'], section['rows'])
                anchors = md.anchors(text)
                self.assertTrue(all(link.target[1:] in anchors for link in md.links(text) if link.target.startswith('#')))
                self.assertTrue(all(link.target.startswith(('#', 'https://', 'mailto:')) for link in md.links(text)))

    def test_all_domains_matches_unfiltered_module_content(self):
        original = bundle.module_files()['02'].read_text()
        texts = {'02': original}
        selection = bundle.select_source_domains(texts, list(bundle.source_domain_sections(original)))
        self.assertEqual(texts['02'], original)
        self.assertEqual(selection['included_source_rows'], 525)
        self.assertEqual(selection['omitted_domains'], [])

    def test_manifest_identifies_original_input_and_exact_selection(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.cli('--bundle', 'research', '--source-domains', '01,16', '--name', 'focused', '--manifest', '--out', directory)
            self.assertEqual(result.returncode, 0, result.stderr)
            document = Path(directory) / 'simple-toolkit-focused.md'
            payload = json.loads(document.with_suffix('.json').read_text())
            self.assertEqual(payload['statistics']['source_selection']['requested_domains'], ['01', '16'])
            self.assertEqual(payload['output_sha256'], hashlib.sha256(document.read_bytes()).hexdigest())
            source = next(row for row in payload['sources'] if '/02-' in row['path'])
            self.assertEqual(source['sha256'], hashlib.sha256(bundle.module_files()['02'].read_bytes()).hexdigest())
            before = (document.read_bytes(), document.with_suffix('.json').read_bytes())
            self.assertEqual(self.cli('--bundle', 'research', '--source-domains', '16,01', '--name', 'focused', '--manifest', '--out', directory).returncode, 0)
            self.assertEqual(before, (document.read_bytes(), document.with_suffix('.json').read_bytes()))

    def test_focused_budget_failure_and_unknown_selector_write_nothing(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / 'unused'
            for arguments, code in [(('--bundle', 'research', '--source-domains', '01', '--strict-budget', '--budget', '1'), 1),
                                    (('--bundle', 'research', '--source-domains', '99'), 2),
                                    (('--bundle', 'core', '--source-domains', '01'), 2),
                                    (('--source-domains', '01'), 2),
                                    (('--list', '--source-domains', '01'), 2)]:
                with self.subTest(arguments=arguments):
                    result = self.cli(*arguments, '--out', str(out))
                    self.assertEqual(result.returncode, code, result.stderr)
                    self.assertFalse(out.exists())
                    self.assertNotIn('Traceback', result.stderr)

    def test_domain_inventory_lists_all_nineteen_codes(self):
        result = self.cli('--list-source-domains')
        self.assertEqual(result.returncode, 0, result.stderr)
        for code in range(1, 20):
            self.assertRegex(result.stdout, rf'(?m)^{code:02d}  ')

    def test_context_report_keeps_raw_counts_and_focuses_only_relevant_bundles(self):
        baseline = context_report.report()
        focused = context_report.report(['01', '16'])
        self.assertEqual(baseline['modules'], focused['modules'])
        full = {row['bundle']: row for row in baseline['bundles']}
        for row in focused['bundles']:
            self.assertEqual(row['module_ids'], list(bundle.BUNDLES[row['bundle']]['modules']))
            if '02' in row['module_ids']:
                self.assertLess(row['tokens'], full[row['bundle']]['tokens'])
            else:
                self.assertEqual(row, full[row['bundle']])

    def cli(self, *arguments):
        return subprocess.run([sys.executable, str(ROOT / 'bundle.py'), *arguments], text=True, capture_output=True)


if __name__ == '__main__':
    unittest.main()
