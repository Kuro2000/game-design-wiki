# Game Design Wiki

A personal knowledge base on game design and game development, maintained collaboratively with [Claude Code](https://claude.com/claude-code). Inspired by Andrej Karpathy's LLM Wiki pattern.

## How it works

- `raw/` holds source documents (PDFs, markdown, HTML) — never edited.
- `wiki/` holds the curated, interlinked markdown pages Claude writes from those sources.
- `wiki/index.md` is the table of contents; `wiki/log.md` is an append-only changelog.
- `extract_pdfs.py` turns PDFs into markdown text plus selected page images.
- `build_site.py` renders `wiki/` into a static HTML site under `site/` (gitignored — rebuild locally).

See [CLAUDE.md](CLAUDE.md) for the full ingest workflow and page format.

## Setup

### 1. Clone

```bash
git clone git@github.com:Kuro2000/game-design-wiki.git
cd game-design-wiki
```

### 2. Install Python dependencies

The scripts need `markdown`, `pymupdf`, and `pypdf`:

```bash
python3 -m pip install --user markdown pymupdf pypdf
```

### 3. (Optional) Open the vault in Obsidian

Point Obsidian at the repo root. The committed `.obsidian/` files preserve plugin and graph settings; per-machine workspace state is gitignored.

### 4. Build the static site

```bash
python3 build_site.py
```

Output lands in `site/index.html`. Open it directly in a browser, or serve it:

```bash
python3 -m http.server -d site 8000
```

### 5. Ingest a new source

1. Drop the file into `raw/`.
2. For PDFs, add an entry to the `SOURCES` dict in `extract_pdfs.py` and run `python3 extract_pdfs.py`.
3. Ask Claude Code to ingest it — it will create the summary page, concept pages, wiki-links, update `index.md`, and append to `log.md`.
4. Re-run `python3 build_site.py`.

## Working with Claude Code

This repo is designed to be edited via Claude Code. The conventions in [CLAUDE.md](CLAUDE.md) — page format, citation rules, image discipline, lint checks — are picked up automatically when you open a Claude Code session here.

Common prompts:

- "Ingest the new PDF in `raw/`"
- "Lint the wiki"
- "What does the wiki say about \<topic\>?"

## Layout

```
raw/                        source documents (immutable)
wiki/                       curated markdown pages
wiki/index.md               table of contents
wiki/log.md                 changelog
wiki/assets/<source-slug>/  images extracted from sources
extract_pdfs.py             PDF → markdown + page images
build_site.py               wiki/ → site/ static HTML builder
site/                       generated HTML site (gitignored)
```
