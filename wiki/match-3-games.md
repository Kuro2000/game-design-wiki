# Match-3 Games

**Summary**: A puzzle genre where the player swaps adjacent tiles to form lines of 3+ matching tiles. The genre's depth comes from objectives layered on top of matching, and from [[blockers]] that constrain how players can match.

**Sources**: `GDC2020 Blockers - Lucien Chen.md`; `Level Design Saga - Jeremy Kang.md`.

**Last updated**: 2026-04-25.

---

## Core mechanics

- Swap adjacent tiles to make a line of ≥3 same-coloured candies (or equivalent).
- Matches of 4+ create power-ups (striped, wrapped, colour bomb, etc.).
- Each level has an objective: clear jelly, collect ingredients, hit a score, etc.

## What makes match-3 distinctive

- It looks simple but the gameplay possibility space at each board is enormous.
- Difficulty is driven by [[four-ways-of-raising-difficulty|four levers]]: blockers, spawn rate, [[match-3-design-styles|design styles]], and level layout.
- Cousin observation to [[idle-games]]' "spreadsheet with an interface": match-3 is roughly a constraint-satisfaction puzzle disguised as a candy game.

## Building blocks of a level

Per [[level-design-saga-jeremy-kang]] (using Candy Crush Soda Saga as the example):

- **Game mechanics** — swapping, power-up creation, power-up combos, helper abilities.
- **Game modes** — Pop the Bottles, Find the Bears, Clear the Chocolate, Clear the Bubblegum, Spread the Jam.
- **[[blockers]]** — frosting, liquorice locks, cupcakes, jelly cake, honey, liquorice swirl.
- **Gameplay elements** — candies, power-ups, walls, holes.
- **Modifiers** — soda physics, gravity direction, multiple screens, scrolling levels.

A level is a *composition* of items from each category.

## Related pages

- [[blockers]]
- [[blocker-framework]]
- [[four-ways-of-raising-difficulty]]
- [[match-3-design-styles]]
- [[saga-games]]
- [[candy-crush-franchise]]
