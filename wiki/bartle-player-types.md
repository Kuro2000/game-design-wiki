# Bartle Player Types

**Summary**: Richard Bartle's classic four-category typology of game players: Achievers, Explorers, Socializers, Killers. Originally derived from observing MUD (multi-user dungeon) communities; widely applied to gamification.

**Sources**: `Bartle's Player Types for Gamification.md`.

**Last updated**: 2026-04-25.

---

## The four types

| Type | What they want | What they enjoy |
|---|---|---|
| **Achiever** | Status. Visible progress. | Points, badges, rankings, completion. |
| **Explorer** | Discovery. Surprise. | Hidden areas, Easter eggs, unknown mechanics. |
| **Socializer** | Connection. Collaboration. | Group play, in-game friendships, social rituals. |
| **Killer** | Domination. Beating others. | PvP, competitive ranking, *visible* defeat of opponents. |

(Source: Bartle's Player Types for Gamification.md.)

## The two axes Bartle's types come from

Bartle derives the four types from a 2×2 grid:

|  | Acting on | Interacting with |
|---|---|---|
| **Players** | Killers | Socializers |
| **World** | Achievers | Explorers |

A Killer *acts on* other players. A Socializer *interacts with* other players. An Achiever *acts on* the world (gaining mastery over it). An Explorer *interacts with* the world (probing it for what it does).

## Population fractions (with caveat)

The article cites Bartle's claimed split:

- ~10% Achievers
- ~10% Explorers
- ~80% Socializers
- <1% Killers

⚠️ **Treat with caution.** These come from MUD-era observation, not modern empirical surveys. [[gamer-motivation-model|Quantic Foundry's]] 1.25M-player factor analysis paints a more even distribution across motivation clusters. Use Bartle's *types* freely; cite his *percentages* with hedging. See [[player-motivation-models]] for cross-comparison.

## Don't stereotype

Per [[bartles-player-types-article|the article]]: most players display some traits in more than one type — but most have a *dominant* type. The right design move is:

- Identify the dominant type for your audience.
- Build features that serve it.
- Add a small number of features that serve each of the other three.
- **Survey/observe** to confirm — don't assume.

## What features serve which type

| Feature | Achiever | Explorer | Socializer | Killer |
|---|:---:|:---:|:---:|:---:|
| Leaderboards | ✓ | | | ✓ |
| Achievements/badges | ✓ | | | |
| Hidden content / Easter eggs | | ✓ | | |
| Co-op modes | | | ✓ | |
| Asynchronous social (gift / help) | | | ✓ | |
| PvP arenas | | | | ✓ |
| World maps with unknowns | | ✓ | | |
| Progression bars | ✓ | | | |

(Synthesised from the article's discussion.)

## Limits of the model

- **Built for MUDs.** Single-player and casual mobile contexts may distort the categories.
- **No mention of Submission/comfort play** (the [[eight-kinds-of-fun|MDA aesthetic of Submission]]) — a substantial slice of mobile audiences fits there but doesn't fit Bartle's four.
- **No spectrum.** Bartle's types are categorical; [[gamer-motivation-model|Quantic Foundry]] treats motivations as continuous spectra, which is more flexible.

Despite the limits, the typology persists because it gives a fast vocabulary for the *kinds of player* a designer is making for.

## Related pages

- [[bartles-player-types-article]]
- [[gamer-motivation-model]]
- [[eight-kinds-of-fun]]
- [[player-motivation-models]]
