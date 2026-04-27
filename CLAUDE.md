# LLM Wiki

A personal knowledge base maintained by Claude Code.
Based on Andrej Karpathy's LLM Wiki pattern.

## Purpose

This wiki is a structured, interlinked knowledge base of Game Development, mainly Game Design to support my personal career.
Claude maintains the wiki. The human curates sources, asks questions, and guides the analysis.

## Folder structure

```
raw/                        -- source documents (immutable -- never modify these)
wiki/                       -- markdown pages maintained by Claude
wiki/index.md               -- table of contents for the entire wiki
wiki/log.md                 -- append-only record of all operations
wiki/assets/<source-slug>/  -- rendered images extracted from sources
extract_pdfs.py             -- PDF → markdown text + selected page images
build_site.py               -- wiki/ → site/ static HTML builder
site/                       -- generated HTML site (re-runnable, do not hand-edit)
```

## Ingest workflow

When the user adds a new source to `raw/` and asks you to ingest it:

1. **Read the full source document.**
   - For PDFs: extend `extract_pdfs.py`'s `SOURCES` dict with a new entry, run it, and read the resulting `raw/<name>.md`. While reading, identify which slide/page numbers contain key visuals (charts, frameworks, diagrams, comparison tables) — list them in the `image_pages` config and re-run so they get rendered to `wiki/assets/<source-slug>/`.
   - For markdown / HTML / text sources: read directly. If the source contains useful images, save them under `wiki/assets/<source-slug>/` with descriptive filenames.
2. **Discuss key takeaways with the user before writing anything.** A short summary plus a proposed page list is enough.
3. **Create a summary page** in `wiki/` named after the source (lowercase-hyphenated).
4. **Create or update concept pages** for each major idea or entity.
5. **Embed key images** from the source on the concept pages they support, using:
   `![Descriptive caption](assets/<source-slug>/page-NN.png)`
   The caption becomes the figure caption in the rendered HTML site. Don't dump every image — pick the ones that genuinely add information beyond the prose.
6. **Add wiki-links** (`[[page-name]]`) to connect related pages.
7. **Update `wiki/index.md`** with new pages and one-line descriptions, grouped under the right section.
8. **Append an entry to `wiki/log.md`** with the date, source name, and what changed.
9. **Re-run the build**: `python3 build_site.py` (this also mirrors `wiki/assets/` → `site/assets/`).

A single source may touch 10–15 wiki pages, with 5–15 reference images. That is normal.

## Image extraction guidelines

- **What's worth keeping**: original frameworks, charts, comparison tables, diagrams the source author drew specifically to communicate the idea, screenshots that anchor a discussion. Skip: title slides, agenda slides, decorative photos, generic stock imagery, the "thank you" / contact slide.
- **Where they go**: always under `wiki/assets/<source-slug>/page-NN.png` for PDF pages (or a meaningful name for non-PDF sources).
- **How to embed in markdown**: `![caption](assets/<slug>/page-NN.png)` — path is relative to the wiki page itself. Both Obsidian and the HTML build resolve it correctly.
- **Caption discipline**: write the caption as a complete description of what the figure shows — it appears beneath the image in the HTML site and serves as alt text everywhere.

## Page format

Every wiki page should follow this structure:

```markdown
# Page Title

**Summary**: One to two sentences describing this page.

**Sources**: List of raw source files this page draws from.

**Last updated**: Date of most recent update.

---

Main content goes here. Use clear headings and short paragraphs.

Link to related concepts using [[wiki-links]] throughout the text.

## Related pages

- [[related-concept-1]]
- [[related-concept-2]]
```

## Citation rules

- Every factual claim should reference its source file
- Use the format (source: filename.pdf) after the claim
- If two sources disagree, note the contradiction explicitly
- If a claim has no source, mark it as needing verification

## Question answering

When the user asks a question:

1. Read `wiki/index.md` first to find relevant pages
2. Read those pages and synthesize an answer
3. Cite specific wiki pages in your response
4. If the answer is not in the wiki, say so clearly
5. If the answer is valuable, offer to save it as a new wiki page

Good answers should be filed back into the wiki so they compound over time.

## Lint

When the user asks you to lint or audit the wiki:

- Check for contradictions between pages
- Find orphan pages (no inbound links from other pages)
- Identify concepts mentioned in pages that lack their own page
- Flag claims that may be outdated based on newer sources
- Check that all pages follow the page format above
- Report findings as a numbered list with suggested fixes

## Rules

- Never modify anything in the `raw/` folder
- Always update `wiki/index.md` and `wiki/log.md` after changes
- Keep page names lowercase with hyphens (e.g. `machine-learning.md`)
- Write in clear, plain language
- When uncertain about how to categorize something, ask the user
