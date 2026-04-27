# Candy Crush Franchise

**Summary**: King's flagship line of [[match-3-games]], built on the [[saga-games]] format. The franchise spans multiple titles that share the Candy Crush brand but vary mechanically — making it a useful controlled comparison for [[blocker-framework|blocker design]].

**Sources**: `GDC2020 Blockers - Lucien Chen.md`.

**Last updated**: 2026-04-25.

---

## Titles in the franchise (referenced in the source)

- **Candy Crush Saga (CCS)** — the original (2012). Standard match-3 with gravity falling top-to-bottom.
- **Candy Crush Soda Saga** — variant gravity rules ("soda physics"); some boards have candies floating upward.
- **Candy Crush Jelly Saga** — adds character-vs-player jelly-spreading mode; tilts blocker mix toward MatchOn.
- **Candy Crush Friends Saga** — emphasises social/character mechanics.

## What the [[blocker-framework]] reveals

Plotting each title on the 16-characteristic radar chart (source: GDC2020 Blockers - Lucien Chen.md):

![Comparison radar charts across the four Candy Crush titles — Saga (top-left), Jelly (top-right), Soda (bottom-left), Friends (bottom-right).](assets/gdc2020-blockers-lucien-chen/page-29.png)

- **Shared common traits**: Stationary, Layered, Colorless, Removable, MatchBeside — across all four titles. See [[blockers]] for why these dominate.
- **CCS distinctives**: more Dynamic, Single, and Movable blockers than the rest.
- **Jelly distinctives**: MatchOn > MatchBeside (uniquely; the others lean MatchBeside).
- **Less Hiding** across the franchise generally — an unexploited design space.

## Why the franchise matters as a case study

It's a controlled comparison: same studio, same brand, similar economic constraints — but four different blocker philosophies. The differences expose what's a *match-3 universal* vs. what's a *design choice*.

## Related pages

- [[king-games]]
- [[match-3-games]]
- [[saga-games]]
- [[blocker-framework]]
- [[blockers]]
