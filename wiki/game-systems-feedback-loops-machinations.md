# Game Systems: Feedback Loops (Machinations)

**Summary**: Article from Machinations.io (2021) introducing positive and negative [[feedback-loops]] with examples from Call of Duty, Hades, XCOM, Mario Kart, and Cultist Simulator. Frames feedback loops as the designer's primary tool for *dynamic* (not statically-set) difficulty control.

**Sources**: `Game systems Feedback loops and how they help craft player experiences.md` (machinations.io, 2021-09-16).

**Last updated**: 2026-04-26.

---

## Distinctive framing

Where the [[feedback-loops-akshat-sultania|Sultania article]] focuses on the "rich get richer" dynamic and how to dampen it, Machinations frames feedback loops as the answer to a structural problem: **you set difficulty at the start of the game, when the player is least experienced.** Static difficulty settings can't adapt; feedback loops can.

> "Positive and negative feedback loops are in-game elements that allow the game designers to dynamically control the game difficulty. They act as sliders that prevent the game from becoming too easy or too hard."
> — Source: Game systems Feedback loops…

## The biology analogy it draws

| | Biology example | Game example |
|---|---|---|
| **Positive loop** | Cut → platelets activate → release more clotting chemicals → more platelets | Killstreak → airstrike → more kills → bigger streak |
| **Negative loop** | Body heats up → sweat → evaporative cooling → temperature drops | Player wins → catch-up items go to opponents → balance restored |

Useful framing: positive loops *amplify* the system's current state; negative loops *regulate* it back toward a target.

## Examples it uses

| Game | Positive loop | Negative loop |
|---|---|---|
| Call of Duty | Killstreaks (eventually phased out — too snowbally) | — |
| Hades | Each room rewards skills/perks → easier next run | Death = lose all progress (but story advances on death) |
| XCOM | XP-based soldier progression | — (the brutal flip side: permadeath means lost soldiers stay lost) |
| Mario Kart | — | Catch-up items (blue shell etc.) |
| Cultist Simulator | — | Notoriety mechanic — the more you progress, the more do-gooders try to stop you |

The Hades double-loop (positive metaprogression *and* negative per-run reset) is the article's headline case for why **balanced** loops produce the most engaging structures.

## On hidden vs. visible loops

Like Sultania, Machinations highlights Resident Evil 4's hidden [[dynamic-difficulty]] as a case where the loop *must* stay invisible — telling players "we adapt to your skill" creates perverse incentives.

## The Machinations pitch

The article ends with a sales pitch for Machinations.io diagrams as a tool for modelling and simulating feedback loops without writing code. Worth knowing the source's commercial interest, but doesn't undermine the conceptual content.

## Related pages

- [[feedback-loops]]
- [[dynamic-difficulty]]
- [[feedback-loops-akshat-sultania]]
