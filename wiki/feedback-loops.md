# Feedback Loops

**Summary**: A game system where an output is fed back as input — a player's success or failure changes the likelihood of future successes or failures. Two flavours: **positive** (amplifying) and **negative** (regulating). One of the most reusable design tools for shaping the difficulty curve and the player's emotional arc.

**Sources**: `Feedback Loops in Games.md`; `Game systems Feedback loops and how they help craft player experiences.md`.

**Last updated**: 2026-04-26.

---

## The two types

### Positive (amplifying) feedback loops

Success makes more success more likely. The "rich get richer." Used to:

- **Translate skill into momentum** — players who play well feel powerful and rewarded.
- **Drive snowballing endings** — once a winning condition is in reach, accelerate it so the game closes out instead of dragging.
- **Reinforce learning** — the player gets feedback that "this strategy works."

Canonical example: **Call of Duty killstreaks** (Modern Warfare era). Kills → airstrike → more kills → AC-130 → more kills → tactical nuke. A textbook positive loop, eventually rebalanced because it broke matches for everyone except the leader.

Side note from [[feedback-loops-akshat-sultania]]: positive loops cut both ways. Losing a key piece in **chess** is a negative-for-the-player positive loop — the loss compresses your future options, increasing the chance of more losses.

### Negative (regulating) feedback loops

Success makes the next success harder. Pushes back against snowballing. Used to:

- **Keep games competitive** — give back-of-pack players a chance.
- **Prevent over-easy endgames** — RPG level-up cost rises so you can't grind to level 99 in 20 minutes.
- **Slow expansion** — Civilization's unhappiness + empire-management cost punishes uncontrolled conquest.

Canonical example: **Mario Kart's blue shell** (and the wider catch-up item distribution). First place gets bananas; last place gets bullet bills.

(Sources: Feedback Loops in Games.md; Game systems Feedback loops and how they help craft player experiences.md.)

## The deeper purpose: dynamic difficulty

The most articulate framing comes from the Machinations article (source: Game systems Feedback loops…):

> "Positive and negative feedback loops are in-game elements that allow the game designers to dynamically control the game difficulty. They act as sliders that prevent the game from becoming too easy or too hard."

Static difficulty settings have to be picked at the start of the game, when the player is least experienced. Feedback loops let difficulty *track* what the player is actually doing.

See [[dynamic-difficulty]] for the special case of explicitly hidden adaptive systems (e.g., Resident Evil 4).

## Combining positive and negative

The most engaging systems use **both**. Hades is the canonical example:

- **Positive** — meta-progression. Each escape attempt earns persistent upgrades that make future runs easier.
- **Negative** — every death wipes per-run progress; you start over.

The negative loop creates the challenge; the positive loop ensures the challenge is overcomeable. Without the positive loop, dying would feel pointless. Without the negative loop, escape would feel cheap. Together they make every death feel like progress (source: Game systems Feedback loops…).

Civilization is another mixed-loop case: conquest → bigger empire (positive) → unhappiness + management cost (negative). The two loops keep expansion bounded.

## Dampening: when a loop is too strong

A positive loop that's "working too well" needs intervention. Two patterns:

1. **Break the recursion.** Black Ops removed killstreak-bonuses-counting-toward-killstreaks. You can still earn streaks, but each one needs your own kills.
2. **Add a counter-item.** Mario Kart 8's Super Horn lets the leader defend against the blue shell. Doesn't remove the negative loop — gives the dominant player a tool against it.

(Source: Feedback Loops in Games.md.)

## When loops go wrong

A few cautionary cases worth remembering:

- **XCOM** — XP-based soldier progression is a positive loop. With permadeath + no grinding, fallen comrades stay fallen and new recruits can't catch up. Experienced troops become juggernauts; lost ones cripple the team. Single-player feedback loops can be just as destabilising as multiplayer ones (source: Feedback Loops in Games.md).
- **Devil May Cry** — high-score → orbs → better gear is a positive loop that gives the *best* players the most help. Struggling players end up perpetually under-equipped.
- **Call of Duty (early)** — killstreak-on-killstreak chaining was the textbook example of a positive loop that had to be redesigned out.

## Connections to other concepts

- **[[mda-framework|MDA]]** — feedback loops are *dynamics*, emerging from mechanics. A designer authors the loop's mechanics; the loop's effect on play is the dynamic; the resulting tension/relief is the aesthetic.
- **[[choke-points]]** — both regulate progression flow; choke points are static gates, feedback loops are responsive ones.
- **[[level-difficulty]]** — feedback loops are one of the tools for keeping difficulty in the [[flow-theory|flow channel]] over the course of a single play session.
- **[[idle-games]]** — virtually all idle games are built on stacked positive feedback loops (currency → upgrade → faster currency → more upgrades). [[choke-points]] act as the regulator.

## Designer's checklist

When building or auditing a system:

1. **What loops exist?** Trace each output → input pathway.
2. **Are they intentional?** Some emerge accidentally and break balance.
3. **Is each one bounded?** Unbounded positive loops lead to runaway. Unbounded negative loops lead to stalemate.
4. **Does the strong player have a way to fight a negative loop?** (Super Horn pattern.)
5. **Does the struggling player have a way to escape a negative-for-them positive loop?** (Catch-up items, mercy invincibility, soft restarts.)
6. **Should the loop be visible or hidden?** Most loops should be legible. [[dynamic-difficulty|Adaptive systems]] are the exception.

## Related pages

- [[feedback-loops-akshat-sultania]]
- [[game-systems-feedback-loops-machinations]]
- [[dynamic-difficulty]]
- [[mda-framework]]
- [[choke-points]]
- [[level-difficulty]]
- [[idle-games]]
