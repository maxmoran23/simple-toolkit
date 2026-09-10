"""Offline regression and negative-control tests; fixtures are synthetic."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import bundle
import context_report
import linkcheck
import markdown_utils as md
import validate


class MarkdownTests(unittest.TestCase):
    def test_mixed_fences_do_not_close(self):
        text = '# Title\n````md\n```\n# Example\n~~~\n````\n## Real\n'
        self.assertEqual([row[2] for row in md.headings(text)], ['Title', 'Real'])
        self.assertFalse(md.unclosed_fence(text))
        self.assertTrue(md.unclosed_fence('```\n~~~\n'))

    def test_inline_code_and_fenced_links_are_not_live(self):
        text = '`[ignore](missing.md)`\n~~~\n[ignore](missing.md)\n~~~\n[`keep`](real.md)'
        links = list(md.links(text))
        self.assertEqual([(item.label, item.target) for item in links], [('`keep`', 'real.md')])

    def test_balanced_parentheses_and_encoded_urls(self):
        text = '[one](https://example.org/a_(b)) [two](https://example.org/a%20b)'
        self.assertEqual([item.target for item in md.links(text)],
                         ['https://example.org/a_(b)', 'https://example.org/a%20b'])

    def test_duplicate_slug_suffixes(self):
        self.assertEqual(md.anchors('# A\n## Repeated\n## Repeated\n'), {'a', 'repeated', 'repeated-1'})


class BundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.files = {'00': self.root / '00-operating.md', '01': self.root / '01-research.md'}
        self.files['00'].write_text('# Operating\n## Scope\n[local](#scope)\n[other](01-research.md#scope)\n')
        self.files['01'].write_text('# Research\n## Scope\n[excluded](02-sources.md#guidance)\n')

    def test_fragment_links_are_namespaced(self):
        text = '[local](#scope) [`other`](01-research.md#scope)\n`[sample](01-research.md)`'
        rewritten, count, flagged = bundle.rewrite_links(text, {'00', '01'}, self.files, '00')
        self.assertIn('[local](#module-00-scope)', rewritten)
        self.assertIn('[`other`](#module-01-scope)', rewritten)
        self.assertIn('`[sample](01-research.md)`', rewritten)
        self.assertEqual((count, flagged), (2, 0))

    def test_rewritten_heading_retains_source_fragment_identity(self):
        self.files['00'].write_text('# Operating\n## [Scope](01-research.md)\n[go](#scope)\n')
        (self.root / 'README.md').write_text('# Readme\nCurrent release: `v1.3.0`\n')
        with patch.object(bundle, 'ROOT', self.root), patch.object(bundle, 'TOOLKIT', self.root):
            document, _ = bundle.build(['00'], 'fragment-regression', None)
        self.assertIn('[Scope](https://github.com/maxmoran23/simple-toolkit/blob/main/toolkit/01-research.md) (not loaded)', document)
        self.assertIn('<a id="module-00-scope"></a>', document)
        self.assertIn('[go](#module-00-scope)', document)
        known = md.anchors(document)
        self.assertTrue(all(link.target[1:] in known for link in md.links(document) if link.target.startswith('#')))

    def test_missing_fragment_fails(self):
        with self.assertRaisesRegex(ValueError, 'missing section'):
            bundle.rewrite_links('[x](01-research.md#absent)', {'01'}, self.files, '00')

    def test_unknown_filename_fails(self):
        with self.assertRaisesRegex(ValueError, 'filename'):
            bundle.rewrite_links('[x](01-invented.md)', {'01'}, self.files)

    def test_excluded_fragment_is_preserved(self):
        text, _, flagged = bundle.rewrite_links('[x](01-research.md#scope)', {'00'}, self.files)
        self.assertIn('01-research.md#scope) (not loaded)', text)
        self.assertEqual(flagged, 1)

    def test_only_referenced_anchors_added(self):
        text = '# Title\n## Referenced\n## Other\n'
        result = bundle.demote_headings(text, '00', {'referenced'})
        self.assertIn('id="module-00-referenced"', result)
        self.assertNotIn('id="module-00-other"', result)

    def test_empty_duplicate_and_unsafe_name_rejected(self):
        for modules, name in [([], 'empty'), (['00', '00'], 'dup'), (['00'], '../../escape')]:
            with self.subTest(modules=modules, name=name), self.assertRaises(ValueError):
                bundle.build(modules, name, None)

    def test_duplicate_disk_module_rejected(self):
        (self.root / '00-duplicate.md').write_text('# Duplicate\n')
        with patch.object(bundle, 'TOOLKIT', self.root), self.assertRaisesRegex(ValueError, 'duplicate module'):
            bundle.module_files()

    def test_symlink_module_rejected(self):
        folder = self.root / 'links'
        folder.mkdir()
        (folder / '00-operating.md').symlink_to(self.files['00'])
        with patch.object(bundle, 'TOOLKIT', folder), self.assertRaisesRegex(ValueError, 'symlink'):
            bundle.module_files()

    def test_ceil_token_estimate(self):
        self.assertEqual(bundle.estimate_tokens('12345'), 2)

    def test_stdout_has_only_bundle(self):
        result = self.cli('--bundle', 'core', '--stdout')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(result.stdout.startswith('# Simple Toolkit'))
        self.assertNotIn('- estimated tokens:', result.stdout)
        self.assertIn('- estimated tokens:', result.stderr)

    def test_strict_budget_produces_no_output(self):
        out = self.root / 'strict'
        result = self.cli('--bundle', 'core', '--budget', '1', '--strict-budget', '--out', str(out))
        self.assertEqual(result.returncode, 1)
        self.assertFalse(out.exists())
        self.assertEqual(result.stdout, '')

    def test_external_output_directory_and_manifest_are_deterministic(self):
        args = ('--bundle', 'core', '--out', str(self.root), '--manifest')
        first = self.cli(*args)
        self.assertEqual(first.returncode, 0, first.stderr)
        document = self.root / 'simple-toolkit-core.md'
        manifest = document.with_suffix('.json')
        before = (document.read_bytes(), manifest.read_bytes())
        self.assertEqual(self.cli(*args).returncode, 0)
        self.assertEqual(before, (document.read_bytes(), manifest.read_bytes()))
        payload = json.loads(manifest.read_text())
        self.assertEqual(payload['output_sha256'], hashlib.sha256(document.read_bytes()).hexdigest())
        self.assertEqual(payload['statistics']['tokens'], bundle.estimate_tokens(document.read_text()))
        self.assertTrue(all(not Path(row['path']).is_absolute() for row in payload['sources']))

    def test_invalid_cli_inputs_are_usage_errors(self):
        for args in [('--modules', ','), ('--modules', '00,,01'), ('--modules', '00', '--name', '../x'),
                     ('--bundle', 'core', '--budget', '0'), ('--bundle', 'core', '--strict-budget')]:
            with self.subTest(args=args):
                result = self.cli(*args)
                self.assertEqual(result.returncode, 2)
                self.assertNotIn('Traceback', result.stderr)

    def cli(self, *args):
        return subprocess.run([sys.executable, str(ROOT / 'bundle.py'), *args], text=True, capture_output=True)


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.page = self.root / 'README.md'

    def link_errors(self, text):
        self.page.write_text(text)
        errors = []
        with patch.object(validate, 'ROOT', self.root):
            validate.check_links({'README.md': self.page}, errors)
        return errors

    def test_broken_same_page_fragment_rejected(self):
        self.assertTrue(self.link_errors('# Title\n[x](#absent)'))
        self.assertEqual(self.link_errors('# Title\n[x](#title)'), [])

    def test_encoded_path_and_fragment_resolve(self):
        (self.root / 'other page.md').write_text('# Some title\n')
        self.assertEqual(self.link_errors('# Title\n[x](other%20page.md#some-title)'), [])

    def test_unsafe_schemes_and_credentials_rejected(self):
        for url in ['http://example.org', 'ftp://example.org', 'javascript:alert(1)', '//example.org',
                    'https://user:secret@example.org', 'https://']:
            with self.subTest(url=url):
                self.assertTrue(self.link_errors(f'# Title\n[x]({url})'))

    def test_code_samples_are_not_navigation(self):
        self.assertEqual(self.link_errors('# Title\n```md\n[x](absent.md)\n```\n'), [])

    def test_escaping_link_rejected(self):
        self.assertTrue(self.link_errors('# Title\n[x](../outside.md)'))

    def test_wrong_fence_and_extra_h1_fail(self):
        self.page.write_text('# Title\n# Extra\n```\n~~~\n' + '\n' * 40)
        errors = []
        validate.check_text({'README.md': self.page}, errors)
        self.assertTrue(any('H1' in item for item in errors))
        self.assertTrue(any('unbalanced' in item for item in errors))

    def test_budget_duplicate_module_cannot_hide_omission(self):
        files = validate.markdown_files()
        text = files['README.md'].read_text()
        rows = list(validate.BUDGET_ROW.finditer(text))
        self.assertEqual(len(rows), 12)
        text = text[:rows[1].start()] + text[rows[1].start():].replace(rows[1]['file'], rows[0]['file'], 1)
        self.page.write_text(text)
        files['README.md'] = self.page
        errors = []
        validate.check_budget_table(files, errors)
        self.assertTrue(any('exactly once' in item for item in errors))

    def test_bundle_membership_is_checked_on_its_own_row(self):
        files = validate.markdown_files()
        text = files['README.md'].read_text()
        text = text.replace('| `core` | `00`, `07`, `09` |', '| `core` | `00`, `07` |')
        text += '\nThe original list still appears elsewhere: `00`, `07`, `09`.\n'
        self.page.write_text(text)
        files['README.md'] = self.page
        errors = []
        validate.check_bundles(files, errors)
        self.assertTrue(any('bundle `core` module list' in item for item in errors))

    def test_context_report_matches_actual_bundle(self):
        report = context_report.report()
        core = next(row for row in report['bundles'] if row['bundle'] == 'core')
        text, _ = bundle.build(['00', '07', '09'], 'core', None)
        self.assertEqual(core['tokens'], bundle.estimate_tokens(text))


class ProbeHandler(BaseHTTPRequestHandler):
    calls = []
    def log_message(self, *args):
        pass

    def do_HEAD(self):
        type(self).calls.append(('HEAD', self.path))
        code = {'/ok': 204, '/blocked': 403, '/missing': 404, '/fallback': 405, '/redirect': 302}.get(self.path, 500)
        self.send_response(code)
        if code == 302:
            self.send_header('Location', 'http://127.0.0.1/private')
        self.end_headers()

    def do_GET(self):
        type(self).calls.append(('GET', self.path))
        self.send_response(200)
        self.end_headers()


class LinkcheckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), ProbeHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f'http://127.0.0.1:{cls.server.server_port}'

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_real_http_response_classification(self):
        for path, expected in [('/ok', linkcheck.OK), ('/blocked', linkcheck.BLOCKED), ('/missing', linkcheck.ERROR)]:
            self.assertEqual(linkcheck.probe(self.base + path, 2)[0], expected)

    def test_real_head_fallback_and_no_blocked_retry(self):
        ProbeHandler.calls.clear()
        self.assertEqual(linkcheck.probe(self.base + '/fallback', 2)[0], linkcheck.OK)
        self.assertEqual(ProbeHandler.calls, [('HEAD', '/fallback'), ('GET', '/fallback')])
        ProbeHandler.calls.clear()
        linkcheck.probe(self.base + '/blocked', 2)
        self.assertEqual(ProbeHandler.calls, [('HEAD', '/blocked')])

    def test_https_downgrade_redirect_blocked(self):
        status, detail = linkcheck.probe(self.base + '/redirect', 2)
        self.assertEqual(status, linkcheck.ERROR)
        self.assertIn('HTTPS', detail)

    def test_url_validation(self):
        for url in ['file:///etc/passwd', 'http://example.org', 'https://user:password@example.org',
                    'https://example.org:bad', 'https://example.org:0', 'https://example.org/white space']:
            with self.subTest(url=url), self.assertRaises(ValueError):
                linkcheck.validate_url(url)
        linkcheck.validate_url('https://example.org/white%20space')

    def test_numeric_options_rejected_without_network(self):
        for args in [('--timeout', 'nan'), ('--timeout', 'inf'), ('--timeout', '0'),
                     ('--workers', '0'), ('--workers', '33'), ('--ids', ',')]:
            result = subprocess.run([sys.executable, str(ROOT / 'linkcheck.py'), *args], text=True, capture_output=True)
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertNotIn('Traceback', result.stderr)

    def test_json_path_rejects_directory_escape_and_symlink(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            build = root / 'build'
            build.mkdir()
            (build / 'escape').symlink_to(root, target_is_directory=True)
            with patch.object(linkcheck, 'ROOT', root), patch.object(linkcheck, 'BUILD', build):
                for target in ['build', 'build/report.md', 'report.json', 'build/escape/report.json']:
                    with self.subTest(target=target), self.assertRaises(ValueError):
                        linkcheck.resolved_json_path(target)
                self.assertEqual(linkcheck.resolved_json_path('build/good.json'), (build / 'good.json').resolve())

    def test_build_directory_symlink_rejected_before_write(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            toolkit = root / 'toolkit'
            toolkit.mkdir()
            build = root / 'build'
            build.symlink_to(toolkit, target_is_directory=True)
            with patch.object(linkcheck, 'ROOT', root), patch.object(linkcheck, 'BUILD', build):
                with self.assertRaisesRegex(ValueError, 'not a symlink'):
                    linkcheck.resolved_json_path('build/report.json')
            self.assertEqual(list(toolkit.iterdir()), [])

    def test_invalid_register_tier_fails_before_any_probe(self):
        with tempfile.TemporaryDirectory() as folder:
            register = Path(folder) / 'sources.md'
            register.write_text('| 01.001 | T1 | [valid](https://example.org/a) |\n'
                                '| 01.002 | TYPO | [invalid](https://example.org/b) |\n')
            args = argparse.Namespace(json=None, url=None, ids='01.001', workers=1, timeout=1, strict=False)
            with patch.object(linkcheck, 'REGISTER', register), patch.object(linkcheck, 'probe') as probe:
                with self.assertRaisesRegex(ValueError, '01.002.*invalid tier'):
                    linkcheck.run_report(args)
                probe.assert_not_called()

    def test_missing_source_link_fails_closed(self):
        with tempfile.TemporaryDirectory() as folder:
            register = Path(folder) / 'sources.md'
            register.write_text('| 01.001 | T1 | missing |\n')
            with patch.object(linkcheck, 'REGISTER', register), self.assertRaisesRegex(ValueError, 'exactly one'):
                linkcheck.register_rows()


if __name__ == '__main__':
    unittest.main()
