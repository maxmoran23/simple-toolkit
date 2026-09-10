"""Small, shared Markdown helpers for the repository's inline-link dialect.

This is not a general Markdown renderer. Fenced/inline code is excluded, inline
links allow balanced destination parentheses, and GitHub-style heading IDs are
used for navigation checks. Reference links and raw HTML links are not rewritten.
"""
from __future__ import annotations

import html
import re
from collections import Counter
from dataclasses import dataclass
from urllib.parse import unquote

FENCE_OPEN = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
HEADING = re.compile(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$")


def fenced_lines(text: str):
    """Yield (line, in_code), matching closing fence character and length."""
    fence = None
    for line in text.splitlines(keepends=True):
        match = FENCE_OPEN.match(line.rstrip("\r\n"))
        if fence is None:
            if match and not (match[1][0] == "`" and "`" in match[2]):
                fence = match[1]
                yield line, True
            else:
                yield line, False
        else:
            yield line, True
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None


def unclosed_fence(text: str) -> bool:
    fence = None
    for line in text.splitlines():
        match = FENCE_OPEN.match(line)
        if fence is None:
            if match and not (match[1][0] == "`" and "`" in match[2]):
                fence = match[1]
        elif match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
            fence = None
    return fence is not None


def visible_text(text: str, inline: bool = True) -> str:
    """Mask code with spaces, preserving offsets and line numbers."""
    masked = "".join(re.sub(r"[^\r\n]", " ", line) if code else line for line, code in fenced_lines(text))
    if inline:
        # A matching run must have exactly the opener's length.
        masked = re.sub(r"(?<!`)(`+)(?!`)([\s\S]*?)(?<!`)\1(?!`)",
                        lambda m: re.sub(r"[^\r\n]", " ", m[0]), masked)
    return masked


def clean_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<"):
        end = target.find(">")
        if end >= 0:
            return target[1:end]
    return re.split(r"\s+[\"']", target, maxsplit=1)[0]


@dataclass(frozen=True)
class Link:
    start: int
    end: int
    label: str
    target: str
    image: bool = False


def links(text: str):
    """Find inline links outside code, supporting nested URL parentheses."""
    visible = visible_text(text)
    opener = re.compile(r"(?<!!)\[([^\]\n]*)\]\(|!\[([^\]\n]*)\]\(")
    cursor = 0
    while match := opener.search(visible, cursor):
        start = match.end()
        depth, end = 1, start
        while end < len(visible) and visible[end] != "\n":
            char = visible[end]
            if char == "\\":
                end += 2
                continue
            depth += (char == "(") - (char == ")")
            if depth == 0:
                label_group = 1 if match[1] is not None else 2
                yield Link(match.start(), end + 1, text[match.start(label_group):match.end(label_group)],
                           clean_target(text[start:end]), match[2] is not None)
                break
            end += 1
        cursor = max(end + 1, match.end())


def slug(text: str) -> str:
    text = html.unescape(re.sub(r"<[^>]*>", "", text)).lower()
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)
    return re.sub(r"[^\w\- ]", "", text).replace(" ", "-")


def headings(text: str):
    """Yield (zero-based line, level, label, GitHub-style unique anchor)."""
    counts: Counter[str] = Counter()
    for index, (line, code) in enumerate(fenced_lines(text)):
        match = HEADING.match(line.rstrip()) if not code else None
        if match:
            base = slug(match[2])
            anchor = base if counts[base] == 0 else f"{base}-{counts[base]}"
            counts[base] += 1
            yield index, len(match[1]), match[2], anchor


def anchors(text: str) -> set[str]:
    result = {anchor for _, _, _, anchor in headings(text)}
    result.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', visible_text(text)))
    return result
