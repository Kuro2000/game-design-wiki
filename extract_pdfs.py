#!/usr/bin/env python3
"""Extract text + key page images from PDFs in raw/ for ingestion.

For each registered PDF in `SOURCES`:
  - Extract full text into raw/<name>.md (one section per slide).
  - Render the listed `image_pages` to PNG under wiki/assets/<asset_slug>/page-NN.png.

Wiki pages then reference these images via `![caption](assets/<slug>/page-NN.png)`.
The build script (build_site.py) copies wiki/assets/ → site/assets/ so the same
relative paths work in HTML.
"""

from __future__ import annotations

import re
from pathlib import Path

import pymupdf
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw"
ASSETS = ROOT / "wiki" / "assets"

# Patterns to strip from each page of extracted text.
NOISE = [
    re.compile(r"©\s*King\.com\s*Ltd[^\n]*", re.IGNORECASE),
    re.compile(r"Commercially Confidential", re.IGNORECASE),
    re.compile(r"^\s*Page\s+\d+\s*$", re.MULTILINE),
]

# Each source PDF gets:
#   md_name: text-extract output filename in raw/
#   title: H1 for the extracted markdown
#   source_note: byline/credit line
#   asset_slug: folder name under wiki/assets/ for rendered images
#   image_pages: {page_number_1_indexed: short_caption}
SOURCES: dict = {
    "GDC2020 Final PPT.pdf": {
        "md_name": "GDC2020 Blockers - Lucien Chen.md",
        "title": "GDC 2020 — Blockers: Analyzing Difficulty Drivers in Candy Crush Games",
        "source_note": "Lucien Chen, Senior Level Designer at King, GDC 2020.",
        "asset_slug": "gdc2020-blockers-lucien-chen",
        "image_pages": {
            6: "Five match-3 design styles — Explosive, Snipey, Journey, Puzzly, Grindy.",
            7: "Match-3 design styles plotted on the Easy↔Hard axis.",
            20: "The 16 blocker characteristics organized into 4 categories (Nature, Movement, Discovery, Destruction).",
            21: "Nature characteristics defined — Colorless, Colored, Layered, Single, Space.",
            22: "Destruction characteristics defined — Removable, Irremovable, MatchOn, MatchBeside, Impenetrable.",
            23: "Movement characteristics defined — Stationary, Locked, Movable.",
            24: "Discovery characteristics defined — Chained, Hiding, Dynamic.",
            26: "16-characteristic table for Candy Crush Soda Saga blockers.",
            27: "Radar chart — Candy Crush Saga blockers.",
            29: "Comparison radar charts across the four Candy Crush titles (Saga, Soda, Jelly, Friends).",
            49: "Accessibility comparison — MatchOn (44 ways to break) vs MatchBeside (104 ways).",
            50: "The five dominant blocker characteristics and the three forces behind them.",
            66: "Production timeline with vs without the blocker customization tool.",
        },
    },
    "MDA Framework.pdf": {
        "md_name": "MDA Framework - Hunicke LeBlanc Zubek.md",
        "title": "MDA: A Formal Approach to Game Design and Game Research",
        "source_note": "Robin Hunicke, Marc LeBlanc, Robert Zubek. GDC Workshop paper, 2004.",
        "asset_slug": "mda-framework-paper",
        "image_pages": {
            2: "MDA framework — Mechanics, Dynamics, Aesthetics, with the designer's perspective (M→D→A) and the player's perspective (A→D→M).",
        },
    },
    "Gamer-Motivation-Model-Reference.pdf": {
        "md_name": "Gamer Motivation Model - Quantic Foundry.md",
        "title": "Gamer Motivation Model — Reference Guide",
        "source_note": "Nick Yee & Nic Ducheneaut, Quantic Foundry. Based on 1.25M+ gamer survey responses.",
        "asset_slug": "gamer-motivation-model-quantic-foundry",
        "image_pages": {
            3: "The 12 gamer motivations grouped into 6 clusters (Action, Social, Mastery, Achievement, Immersion, Creativity).",
            4: "The three meta-clusters — Action+Social = BRIGHT, Mastery+Achievement = TALL, Immersion+Creativity = WIDE.",
            5: "Percentile-rank interpretation of the Motivation Chart.",
            15: "Motivation spectra (1 of 3) — Independence/Community, Non-Adversarial/Competition, Calm/Excitement, Enduring/Destruction.",
            16: "Motivation spectra (2 of 3) — Self-Driven/Completion, Flat-Progression/Power, Spontaneous/Strategy, Easy-Fun/Challenge.",
            17: "Motivation spectra (3 of 3) — Generic/Fantasy, Open-Ended/Story, Practical/Discovery, Curated/Design.",
        },
    },
    "KANG_Jeremy_LevelDesignSaga.pdf": {
        "md_name": "Level Design Saga - Jeremy Kang.md",
        "title": "Level Design Saga: Creating Levels for Casual Games",
        "source_note": "Jeremy Kang, Principal Game Designer at King Berlin, GDC 2016.",
        "asset_slug": "level-design-saga-jeremy-kang",
        "image_pages": {
            8: "Level design as the composite intersection of Art, Code, and Design.",
            11: "MDA Framework — Mechanics → Dynamics → Aesthetics.",
            22: "The five-stage level design process — Concept → Layout → Creation → Balancing → Testing.",
            25: "The four level design principles — Hooks, Difficulty, Flow, Rhythm.",
            28: "Level hooks across core games (Super Mario 3D World, Shadow of the Colossus, Half-Life 2, Bayonetta 2).",
            34: "Level Creation micro-process — Layout → Objectives → Game Objects → Blockers → Test.",
            46: "Rhythm — pattern, frequency, and intensity of events in a level.",
            49: "Ki-Shō-Ten-Ketsu — 4-part Japanese narrative structure applied to level pacing.",
            56: "Five level-balancing knobs — objectives, moves, mastery stars, colours, blockers.",
            57: "Flow Theory (Csíkszentmihályi via Jenova Chen) — the engagement channel between anxiety and boredom.",
            61: "Four-stage level testing pipeline — Self → Internal → Qualitative → Playtest releases.",
            63: "Level KPIs — Difficulty, Retention, Progression, Monetization.",
        },
    },
}


def clean_page_text(text: str) -> str:
    for pat in NOISE:
        text = pat.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_text(pdf_path: Path, md_path: Path, title: str, source_note: str):
    reader = PdfReader(str(pdf_path))
    parts = [
        f"# {title}",
        "",
        f"**Source**: `{pdf_path.name}` — {source_note}",
        f"**Pages**: {len(reader.pages)}",
        "",
        "Text extracted from PDF; layout artifacts may remain. Each `## Page N` "
        "corresponds to one slide. Selected pages are also rendered to "
        "`wiki/assets/<slug>/page-NN.png` for visual reference.",
        "",
        "---",
        "",
    ]
    for i, page in enumerate(reader.pages, start=1):
        text = clean_page_text(page.extract_text() or "")
        parts.append(f"## Page {i}")
        parts.append("")
        parts.append(
            text if text else "*(no extractable text — likely an image-only slide)*"
        )
        parts.append("")
    md_path.write_text("\n".join(parts), encoding="utf-8")


def render_pages(pdf_path: Path, asset_dir: Path, image_pages: dict, dpi: int = 140):
    asset_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(str(pdf_path))
    for page_num, _caption in sorted(image_pages.items()):
        if not (1 <= page_num <= len(doc)):
            print(f"  ! page {page_num} out of range (1..{len(doc)}) in {pdf_path.name}")
            continue
        page = doc[page_num - 1]
        pix = page.get_pixmap(dpi=dpi)
        out_path = asset_dir / f"page-{page_num:02d}.png"
        pix.save(str(out_path))
    doc.close()


def write_caption_index(asset_dir: Path, image_pages: dict, source_md: str):
    """Write a small README so the asset folder self-documents."""
    lines = [
        f"# Image references — {asset_dir.name}",
        "",
        f"Rendered slides from `{source_md}`. Captions describe what's on each slide.",
        "",
    ]
    for page_num, caption in sorted(image_pages.items()):
        lines.append(f"- **page-{page_num:02d}.png** — {caption}")
    (asset_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    for pdf_name, cfg in SOURCES.items():
        pdf_path = RAW / pdf_name
        if not pdf_path.exists():
            print(f"! missing {pdf_path}")
            continue
        md_path = RAW / cfg["md_name"]
        asset_dir = ASSETS / cfg["asset_slug"]

        extract_text(pdf_path, md_path, cfg["title"], cfg["source_note"])
        render_pages(pdf_path, asset_dir, cfg["image_pages"])
        write_caption_index(asset_dir, cfg["image_pages"], pdf_name)

        print(
            f"{pdf_name}: text → {md_path.name}; "
            f"{len(cfg['image_pages'])} images → {asset_dir.relative_to(ROOT)}/"
        )


if __name__ == "__main__":
    main()
