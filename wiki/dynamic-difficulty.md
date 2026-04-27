# Dynamic Difficulty

**Summary**: A system that adjusts game difficulty in response to how well the player is doing — almost always implemented as a [[feedback-loops|negative feedback loop]]. Often deliberately hidden from the player, because surfacing it creates perverse incentives.

**Sources**: `Feedback Loops in Games.md`; `Game systems Feedback loops and how they help craft player experiences.md`.

**Last updated**: 2026-04-26.

---

## What it solves

Static difficulty (Easy/Medium/Hard) has to be picked at the start of the game, when the player has the least information about how the game plays. Once chosen, it can't track the player's growing skill. Two failure modes:

- **Pick too easy** — game becomes trivial as you learn it; stops being engaging.
- **Pick too hard** — bounce off and never come back.

Dynamic difficulty replaces the static dial with a system that *responds* to the player's actual performance.

## The Resident Evil 4 case

The most-cited example, mentioned in both source articles. RE4 has a **hidden** Difficulty Adjustment system that scales enemy aggression, ammo drops, and health spawns based on how the player is doing. Capcom deliberately never publicised the system.

Why hide it? Per [[feedback-loops-akshat-sultania|Sultania]]:

> "Telling players that the game will get harder if they're doing well, or easier if they're struggling, is effectively telling good players to make mistakes."

A surfaced negative loop becomes a perverse incentive. If skilled players know dying lowers difficulty, they'll die strategically. If struggling players know good play makes the game harder, they'll resent every win. The loop only works if it's invisible.

## When dynamic difficulty is OK to surface

Negative loops that are framed as part of the *fiction* rather than as adaptive systems can be surfaced freely:

- **Mario Kart** — the blue shell is *clearly* a catch-up mechanic, but it's framed as a chaotic party game item, not a difficulty correction. Players don't underperform to avoid it.
- **Cultist Simulator** — the notoriety mechanic is named, visible, and clearly tied to your in-game progress. It's diegetic, so it doesn't feel like a system manipulating you.
- **Hades** — meta-progression is openly described. Each death visibly improves your next run.

The pattern: **surface diegetic negative loops, hide non-diegetic ones.**

## Why design negative loops at all

Three reasons (synthesised from both sources):

1. **Player retention.** Players who bounce off difficulty don't come back. Negative loops cap the bounce rate.
2. **Multiplayer balance.** Without catch-up mechanics, online matches devolve into stomps after the first lead.
3. **Pacing.** A 40-hour campaign needs sustained tension. Static difficulty can't deliver that.

## Risk: punishing the skilled player

The flip side of dynamic difficulty is that *every win is partially deflated*. Skilled players know — even if the system is hidden — that the game is "going easy" on the struggling players around them. This is why competitive games (League of Legends, Counter-Strike, fighting games) generally avoid dynamic difficulty entirely and use **matchmaking** instead. Match the skilled player against another skilled player; let static rules apply equally.

## Related pages

- [[feedback-loops]]
- [[level-difficulty]]
- [[flow-theory]]
- [[feedback-loops-akshat-sultania]]
- [[game-systems-feedback-loops-machinations]]
