#!/usr/bin/env python3
"""Build wiki/*.md into a static, interconnected HTML site under site/.

Re-run any time the wiki changes:
    python3 build_site.py

What it does:
  - Parses wiki/index.md to build a grouped sidebar nav.
  - Resolves [[wiki-link]] and [[wiki-link|alias]] syntax to <a href="link.html">.
  - Renders the Summary / Sources / Last updated header into a meta card.
  - Computes a "Linked from" backlinks panel for each page.
  - Mirrors wiki/assets/ → site/assets/ so embedded images resolve.
  - Flags broken wiki-links in the console output.
"""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
WIKI = ROOT / "wiki"
ASSETS_SRC = WIKI / "assets"
OUT = ROOT / "site"
ASSETS_OUT = OUT / "assets"

WIKI_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def parse_link_inner(content: str):
    """Split [[target|alias]] or [[target\\|alias]] (table-escaped) into parts."""
    for sep in ("\\|", "|"):
        if sep in content:
            target, alias = content.split(sep, 1)
            return target.strip(), alias.strip()
    return content.strip(), None
META_LINE_RE = re.compile(
    r"^\*\*(Summary|Sources|Last updated)\*\*:\s*(.*)$", re.IGNORECASE
)
INLINE_CODE_RE = re.compile(r"`([^`]+)`")


def slugify(name: str) -> str:
    return name.strip().lower().replace(" ", "-")


def title_from_slug(slug: str) -> str:
    # Preserve our existing page-name casing convention.
    return slug.replace("-", " ").title()


def collect_pages() -> dict:
    pages: dict = {}
    for path in sorted(WIKI.glob("*.md")):
        pages[path.stem] = {"path": path, "raw": path.read_text(encoding="utf-8")}
    return pages


def split_meta(text: str):
    """Return (title, meta_dict, body) by extracting the H1 + summary header."""
    lines = text.splitlines()
    title = None
    meta: dict = {}
    body_start = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("# ") and title is None:
            title = line.strip()[2:].strip()
            body_start = i + 1
            break
    i = body_start
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        m = META_LINE_RE.match(line)
        if m:
            meta[m.group(1).lower()] = m.group(2).strip()
            i += 1
            continue
        if line == "---":
            i += 1
            break
        break
    body = "\n".join(lines[i:]).strip()
    return title, meta, body


def replace_wiki_links(text: str, pages: dict, broken: set) -> str:
    def sub(m):
        target, alias = parse_link_inner(m.group(1))
        slug = slugify(target)
        label = alias or target
        if slug not in pages:
            broken.add(slug)
            return (
                f'<a class="wiki broken" href="#" '
                f'title="missing page: {html.escape(slug)}">'
                f"{html.escape(label)}</a>"
            )
        return f'<a class="wiki" href="{slug}.html">{html.escape(label)}</a>'

    return WIKI_LINK_RE.sub(sub, text)


def collect_backlinks(pages: dict) -> dict:
    backlinks = {slug: set() for slug in pages}
    for slug, page in pages.items():
        for m in WIKI_LINK_RE.finditer(page["raw"]):
            target, _ = parse_link_inner(m.group(1))
            target_slug = slugify(target)
            if target_slug != slug and target_slug in pages:
                backlinks[target_slug].add(slug)
    return {k: sorted(v) for k, v in backlinks.items()}


def parse_index_groups(index_raw: str):
    """Return [(group_name, [(slug, blurb), ...])] from wiki/index.md."""
    groups: list = []
    current = None
    for line in index_raw.splitlines():
        if line.startswith("## "):
            current = (line[3:].strip(), [])
            groups.append(current)
        elif current is not None and line.lstrip().startswith("- "):
            m = WIKI_LINK_RE.search(line)
            if not m:
                continue
            target, _ = parse_link_inner(m.group(1))
            slug = slugify(target)
            after = WIKI_LINK_RE.sub("", line, count=1)
            blurb = after.lstrip(" -—").strip()
            current[1].append((slug, blurb))
    return groups


def render_inline(value: str, pages: dict, broken: set) -> str:
    value = replace_wiki_links(value, pages, broken)
    value = INLINE_CODE_RE.sub(
        lambda m: f"<code>{html.escape(m.group(1))}</code>", value
    )
    return value


def render_meta_card(meta: dict, pages: dict, broken: set) -> str:
    if not meta:
        return ""
    fields = [("Summary", "summary"), ("Sources", "sources"), ("Last updated", "last updated")]
    rows = []
    for label, key in fields:
        if key in meta:
            rows.append(f"<dt>{label}</dt><dd>{render_inline(meta[key], pages, broken)}</dd>")
    return f'<div class="meta-card"><dl>{"".join(rows)}</dl></div>'


def render_sidebar(groups, current_slug: str) -> str:
    parts: list = []
    for group_name, items in groups:
        parts.append(f"<h3>{html.escape(group_name)}</h3><ul>")
        for slug, blurb in items:
            cls = ' class="current"' if slug == current_slug else ""
            title_attr = f' title="{html.escape(blurb)}"' if blurb else ""
            parts.append(
                f'<li><a href="{slug}.html"{cls}{title_attr}>'
                f"{html.escape(title_from_slug(slug))}</a></li>"
            )
        parts.append("</ul>")
    parts.append('<h3>Meta</h3><ul>')
    for slug, label in (("index", "Index"), ("log", "Log")):
        cls = ' class="current"' if slug == current_slug else ""
        parts.append(f'<li><a href="{slug}.html"{cls}>{label}</a></li>')
    parts.append("</ul>")
    return "".join(parts)


FIGURE_RE = re.compile(
    r'<p>\s*(<img\s+[^>]*?alt="([^"]*)"[^>]*?/?>)\s*</p>',
    re.IGNORECASE,
)


def figurize(html_str: str) -> str:
    """Wrap paragraphs that contain only an image into <figure><figcaption>."""
    def sub(m):
        img, alt = m.group(1), m.group(2)
        if not alt.strip():
            return f'<figure>{img}</figure>'
        return f'<figure>{img}<figcaption>{alt}</figcaption></figure>'
    return FIGURE_RE.sub(sub, html_str)


def copy_assets():
    if not ASSETS_SRC.exists():
        return 0
    if ASSETS_OUT.exists():
        shutil.rmtree(ASSETS_OUT)
    shutil.copytree(ASSETS_SRC, ASSETS_OUT)
    return sum(1 for _ in ASSETS_OUT.rglob("*") if _.is_file())


def render_backlinks(slug: str, backlinks: dict) -> str:
    refs = backlinks.get(slug, [])
    if not refs:
        return ""
    items = "".join(
        f'<li><a href="{r}.html">{html.escape(title_from_slug(r))}</a></li>'
        for r in refs
    )
    return (
        f'<aside class="backlinks"><h3>Linked from</h3>'
        f"<ul>{items}</ul></aside>"
    )


PAGE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — LLM Wiki</title>
<style>{css}</style>
</head>
<body>
<header class="topbar">
  <a class="brand" href="index.html">LLM Wiki</a>
  <nav class="topnav">
    <a href="index.html">Index</a>
    <a href="log.html">Log</a>
  </nav>
</header>
<div class="layout">
  <aside class="sidebar">{sidebar}</aside>
  <main class="content">
    <article>
      <h1>{title}</h1>
      {meta_card}
      {body_html}
    </article>
    {backlinks_html}
  </main>
</div>
</body>
</html>
"""

CSS = """
:root {
  --bg: #fafaf7;
  --bg-alt: #f1efe9;
  --fg: #1d1d1b;
  --fg-mute: #5a594f;
  --accent: #7c3a13;
  --accent-mute: #b67648;
  --border: #d8d3c4;
  --link: #1f4d8c;
  --broken: #b03030;
  --code-bg: #ece8da;
  --max-content: 760px;
  font-size: 16px;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1c1d1a;
    --bg-alt: #25261f;
    --fg: #ece8db;
    --fg-mute: #a09c89;
    --accent: #e0a872;
    --accent-mute: #c08545;
    --border: #3a3b34;
    --link: #8fb3e6;
    --broken: #e88080;
    --code-bg: #2c2d25;
  }
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: var(--bg); color: var(--fg); }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", sans-serif;
  line-height: 1.55;
}
.topbar {
  display: flex; align-items: baseline; gap: 1.5rem;
  padding: 0.75rem 1.5rem; border-bottom: 1px solid var(--border);
  background: var(--bg-alt); position: sticky; top: 0; z-index: 10;
}
.brand {
  font-weight: 700; color: var(--accent); text-decoration: none;
  font-size: 1.05rem; letter-spacing: 0.01em;
}
.topnav a {
  color: var(--fg-mute); text-decoration: none; margin-right: 1rem; font-size: 0.9rem;
}
.topnav a:hover { color: var(--accent); }
.layout {
  display: grid; grid-template-columns: 280px 1fr; gap: 0;
  min-height: calc(100vh - 50px);
}
.sidebar {
  border-right: 1px solid var(--border); padding: 1.25rem 1rem;
  background: var(--bg-alt); overflow-y: auto;
  max-height: calc(100vh - 50px); position: sticky; top: 50px;
  font-size: 0.88rem;
}
.sidebar h3 {
  font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--fg-mute); margin: 1.25rem 0 0.4rem; font-weight: 600;
}
.sidebar h3:first-child { margin-top: 0; }
.sidebar ul { list-style: none; padding: 0; margin: 0; }
.sidebar li { margin: 0.1rem 0; }
.sidebar a {
  color: var(--fg); text-decoration: none; display: block;
  padding: 0.2rem 0.4rem; border-radius: 3px;
}
.sidebar a:hover { background: var(--border); color: var(--accent); }
.sidebar a.current { background: var(--accent); color: var(--bg-alt); font-weight: 500; }
.content { padding: 2rem 2.5rem 4rem; max-width: 100%; overflow-x: hidden; }
.content article { max-width: var(--max-content); }
.content h1 { font-size: 1.85rem; margin: 0 0 1rem; color: var(--accent); line-height: 1.2; }
.content h2 {
  font-size: 1.25rem; margin: 2rem 0 0.6rem;
  padding-bottom: 0.3rem; border-bottom: 1px solid var(--border);
}
.content h3 { font-size: 1.05rem; margin: 1.5rem 0 0.4rem; color: var(--fg); }
.content p { margin: 0.7rem 0; }
.content blockquote {
  margin: 1rem 0; padding: 0.5rem 1rem;
  border-left: 3px solid var(--accent-mute);
  color: var(--fg-mute); font-style: italic; background: var(--bg-alt);
}
.content code {
  background: var(--code-bg); padding: 0.1rem 0.35rem; border-radius: 3px;
  font-size: 0.92em; font-family: ui-monospace, "SF Mono", Menlo, monospace;
}
.content pre {
  background: var(--code-bg); padding: 0.85rem 1rem; border-radius: 4px;
  overflow-x: auto;
}
.content pre code { background: transparent; padding: 0; font-size: 0.85rem; }
.content table { border-collapse: collapse; margin: 1rem 0; font-size: 0.92rem; }
.content th, .content td {
  border: 1px solid var(--border); padding: 0.4rem 0.7rem; text-align: left;
}
.content th { background: var(--bg-alt); font-weight: 600; }
.content hr { border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }
.content ul, .content ol { padding-left: 1.4rem; }
.content li { margin: 0.2rem 0; }
.content a {
  color: var(--link); text-decoration: none;
  border-bottom: 1px solid transparent;
}
.content a:hover { border-bottom-color: var(--link); }
.content a.wiki { color: var(--accent); }
.content a.wiki:hover { border-bottom-color: var(--accent); }
.content a.wiki.broken {
  color: var(--broken); cursor: help;
  border-bottom: 1px dashed var(--broken);
}
.content figure {
  margin: 1.5rem 0; text-align: center;
}
.content figure img {
  max-width: 100%; height: auto; display: block; margin: 0 auto;
  border-radius: 5px; border: 1px solid var(--border);
  box-shadow: 0 2px 14px rgba(0,0,0,0.08);
  background: #fff;
}
.content figcaption {
  color: var(--fg-mute); font-size: 0.85rem; font-style: italic;
  margin-top: 0.5rem; padding: 0 0.5rem;
}
.content img { max-width: 100%; height: auto; }
.meta-card {
  border: 1px solid var(--border); background: var(--bg-alt);
  border-radius: 6px; padding: 0.7rem 1rem; margin: 0 0 1.5rem;
  font-size: 0.92rem;
}
.meta-card dl {
  margin: 0; display: grid;
  grid-template-columns: max-content 1fr; gap: 0.25rem 0.9rem;
}
.meta-card dt { font-weight: 600; color: var(--fg-mute); }
.meta-card dd { margin: 0; }
.backlinks {
  margin-top: 3rem; max-width: var(--max-content);
  padding: 1rem 1.25rem; background: var(--bg-alt);
  border-radius: 6px; border: 1px solid var(--border);
  font-size: 0.92rem;
}
.backlinks h3 {
  margin: 0 0 0.5rem; font-size: 0.78rem;
  text-transform: uppercase; letter-spacing: 0.08em; color: var(--fg-mute);
}
.backlinks ul {
  list-style: none; padding: 0; margin: 0;
  display: flex; flex-wrap: wrap; gap: 0.4rem 0.8rem;
}
.backlinks a { color: var(--accent); text-decoration: none; }
.backlinks a:hover { text-decoration: underline; }
@media (max-width: 800px) {
  .layout { grid-template-columns: 1fr; }
  .sidebar {
    position: static; max-height: none;
    border-right: none; border-bottom: 1px solid var(--border);
  }
  .content { padding: 1.25rem; }
}
"""


def main():
    OUT.mkdir(exist_ok=True)
    pages = collect_pages()
    if not pages:
        raise SystemExit("No wiki pages found in wiki/")
    backlinks = collect_backlinks(pages)
    broken: set = set()
    groups = parse_index_groups(pages["index"]["raw"]) if "index" in pages else []

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "attr_list", "sane_lists"]
    )

    for slug, page in pages.items():
        title, meta, body = split_meta(page["raw"])
        if title is None:
            title = title_from_slug(slug)

        body_with_links = replace_wiki_links(body, pages, broken)
        md.reset()
        body_html = figurize(md.convert(body_with_links))

        html_out = PAGE_TEMPLATE.format(
            title=html.escape(title),
            css=CSS,
            sidebar=render_sidebar(groups, slug),
            meta_card=render_meta_card(meta, pages, broken),
            body_html=body_html,
            backlinks_html=render_backlinks(slug, backlinks),
        )
        (OUT / f"{slug}.html").write_text(html_out, encoding="utf-8")

    n_assets = copy_assets()
    print(f"Built {len(pages)} pages → {OUT} (mirrored {n_assets} asset files)")
    if broken:
        print(
            f"Warning: {len(broken)} unresolved wiki-link target(s): "
            f"{', '.join(sorted(broken))}"
        )


if __name__ == "__main__":
    main()
