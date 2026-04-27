# Wiki Log

Append-only record of wiki operations.

## 2026-04-25

### Initial setup
- Created wiki structure (`index.md`, `log.md`).

### Ingest 1: Kolibri Games — Making a Hit Idle Game
- Source: `Making a Hit Idle Game – Eight Lessons from Kolibri Games.md` (Nate Barker / GameAnalytics, 2019).
- Created source summary: [[making-a-hit-idle-game-kolibri]].
- Created concept pages: [[idle-games]], [[kolibri-games]], [[idle-miner-tycoon]], [[idle-factory-tycoon]], [[core-gameplay-loop]], [[choke-points]], [[mvp-prototyping]], [[live-ops-features]], [[pay-or-wait-monetization]], [[rewarded-ads]], [[d1-retention]], [[lean-development]], [[staged-rollout]].
- Flagged: source contains a contradictory revenue split (ads 60% + IAP 60% = 120%) — noted on [[making-a-hit-idle-game-kolibri]] and [[pay-or-wait-monetization]] for later verification.

### HTML site generator
- Added `build_site.py` — converts wiki/*.md into a static interconnected HTML site under `site/`. Sidebar parsed from `index.md`; backlinks computed automatically; broken double-bracket references flagged.

### Ingest 2: King — GDC 2020 Blockers (Lucien Chen) + GDC 2016 Level Design Saga (Jeremy Kang)
- Sources extracted from PDF via `extract_pdfs.py`:
  - `GDC2020 Blockers - Lucien Chen.md` (71 pages).
  - `Level Design Saga - Jeremy Kang.md` (72 pages).
- Created source summaries: [[gdc2020-blockers-lucien-chen]], [[level-design-saga-jeremy-kang]].
- Created studio/franchise pages: [[king-games]], [[candy-crush-franchise]].
- Created genre pages: [[match-3-games]], [[saga-games]].
- Created match-3 design pages: [[blockers]], [[blocker-framework]], [[four-ways-of-raising-difficulty]], [[match-3-design-styles]].
- Created level design pages: [[level-design]], [[level-design-process]], [[level-hooks]], [[level-difficulty]], [[level-flow]], [[level-rhythm]], [[mda-framework]], [[ki-sho-ten-ketsu]], [[flow-theory]], [[level-testing]].
- Reorganised `index.md` into clearer sub-clusters now that the wiki spans two genres.

### Image extraction added to ingest workflow
- Extended `extract_pdfs.py` to render selected slides via PyMuPDF → `wiki/assets/<source-slug>/page-NN.png`.
- Extended `build_site.py` to mirror `wiki/assets/` → `site/assets/` and wrap image paragraphs in `<figure>` with captions.
- Added 13 reference images for [[gdc2020-blockers-lucien-chen]] and 12 for [[level-design-saga-jeremy-kang]]; embedded the most relevant ones in each concept page.
- Updated `CLAUDE.md` ingest workflow to include image extraction as a standard step.

### Ingest 3: Player motivation & MDA cluster
- Sources:
  - `MDA Framework.pdf` — Hunicke, LeBlanc, Zubek (2004) — the canonical paper. Extracted to `MDA Framework - Hunicke LeBlanc Zubek.md`. 1 figure rendered.
  - `Gamer-Motivation-Model-Reference.pdf` — Quantic Foundry. Extracted to `Gamer Motivation Model - Quantic Foundry.md`. 6 figures rendered.
  - `Bartle's Player Types for Gamification.md` — Kumar, Herger, Dam (IxDF, 2017). Markdown article, no figures.
  - `MDA & 8 Kinds of Fun.md` — Jenny Wang (Medium, 2020). Markdown article, no figures.
- Created source summaries: [[mda-framework-paper]], [[gamer-motivation-model-quantic-foundry]], [[bartles-player-types-article]], [[mda-and-8-kinds-of-fun-jenny-wang]].
- Created concept pages: [[eight-kinds-of-fun]], [[bartle-player-types]], [[gamer-motivation-model]], [[player-motivation-models]] (cross-comparison page).
- **Updated [[mda-framework]]**: significantly expanded with content from the original paper (was thin, built only on Kang's mention). Added the designer/player perspective asymmetry, aesthetic-driven design discussion, and worked examples.
- **Flagged**: [[bartle-player-types]] population fractions (~80% Socializers / <1% Killers) come from MUD-era observation and don't match modern empirical data — noted on the Bartle pages and on [[player-motivation-models]] for verification.
- Reorganised [[index]]: split off a new "Game Design Frameworks" section since the wiki now covers cross-cutting frameworks alongside the genre-specific clusters.

## 2026-04-26

### Ingest 4: Feedback loops cluster
- Sources (both markdown articles, no PDF extraction needed):
  - `Feedback Loops in Games.md` — Akshat Sultania (Medium, 2023). Survey + dampening focus + XCOM cautionary tale.
  - `Game systems Feedback loops and how they help craft player experiences.md` — Machinations.io (2021). Frames loops as dynamic-difficulty sliders.
- Created source summaries: [[feedback-loops-akshat-sultania]], [[game-systems-feedback-loops-machinations]].
- Created concept pages: [[feedback-loops]] (comprehensive umbrella covering positive/negative/dampening/combined-loop patterns), [[dynamic-difficulty]] (focused on the hidden-DDA pattern, e.g., Resident Evil 4).
- Cross-linked feedback loops to [[mda-framework]] (loops are dynamics), [[choke-points]] (related regulators), [[level-difficulty]], and [[idle-games]] (which depend heavily on positive loops).

### Index reorganisation
- Added new "Game Systems" section.
- **Moved Sources to the bottom** of the index — sources accumulate with every ingest and were dominating the top of the sidebar nav. Concept pages now lead.
