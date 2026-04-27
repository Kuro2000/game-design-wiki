# MDA Framework

**Summary**: Mechanics → Dynamics → Aesthetics. Hunicke, LeBlanc, & Zubek's three-layer model of how a designer's rules become a player's experience. The most-cited frame for separating the layers of game design; the source of the [[eight-kinds-of-fun]] taxonomy.

**Sources**: `MDA Framework - Hunicke LeBlanc Zubek.md`; `Level Design Saga - Jeremy Kang.md`; `MDA & 8 Kinds of Fun.md`.

**Last updated**: 2026-04-25.

---

## The three layers

| Layer | What it is | Authored by |
|---|---|---|
| **Mechanics** | The components at the level of data representation and algorithms — rules, board geometry, win conditions. | Designer directly. |
| **Dynamics** | Run-time behaviour of mechanics acting on player inputs and each other's outputs over time. | Emerges from play. |
| **Aesthetics** | Desirable emotional responses evoked in the player — see [[eight-kinds-of-fun]]. | Felt by the player. |

Designers can only author mechanics directly. Dynamics and aesthetics are the actual *targets* — but they must be hit by adjusting mechanics, since that's the only authored layer.

## The asymmetry between designer and player

![MDA framework — Mechanics, Dynamics, Aesthetics, with the designer's perspective (M→D→A) and the player's perspective (A→D→M).](assets/mda-framework-paper/page-02.png)

The crucial insight from Hunicke et al.:

- **Designers see M → D → A.** They write mechanics, hope for dynamics, target aesthetics.
- **Players see A → D → M.** They feel aesthetics first, recognise dynamics over time, and may never inspect the mechanics at all.

This asymmetry is why design discussions often go badly — designers debate mechanics; players debate aesthetics; neither side knows the other's vocabulary maps to the same artefact.

## Why "games as artifacts, not media"

Hunicke et al. are emphatic that games differ from books, music, films:

> "The string of events that occur during gameplay and the outcome of those events are unknown at the time the product is finished."
> — *MDA: A Formal Approach…*, p. 2.

The designer ships the *system*; players generate the *experience* by interacting with it. That's why iterative tuning is essential — you can't author the experience directly, only the substrate from which it emerges.

## Aesthetic-driven design

The paper recommends working backwards: pick the aesthetics you want, then design the dynamics that produce them, then the mechanics that implement those dynamics. See [[eight-kinds-of-fun]] for the full aesthetic vocabulary.

Example chains from the paper:

| Aesthetic | Dynamic that produces it | Mechanic that produces the dynamic |
|---|---|---|
| Challenge | Time pressure, opponent play | Timers, AI opponents |
| Fellowship | Shared information; team-only winning conditions | Chat, team objectives |
| Expression | Customisation, emergent behaviour | Cosmetic options, sandbox affordances |

## Where [[level-design]] sits

Per Jeremy Kang at [[king-games]]: "Level design is the bridge from mechanics to dynamics." A mechanic in isolation produces no dynamic — it's the *level* (board shape, blockers, objective composition) that creates the conditions under which the mechanic produces a particular dynamic.

This is why [[level-design]] is a separate discipline from game design even when one person does both.

## Worked examples

- **Monopoly** dynamic problem (rich-get-richer) → mechanic adjustments (taxes on the wealthy, subsidies for losing players, time-pressure mechanics like depleting resources). The paper uses this as an extended example of how mechanics tune dynamics.
- **Charades**: aesthetics = Fellowship + Expression + Challenge. Mechanics support each: turn-taking (Fellowship), open-ended physical performance (Expression), time/silence constraints (Challenge).
- **Quake**: aesthetics = Challenge + Sensation + Competition + Fantasy. Different mechanic stack: weapons, health, level geometry, audio/visual effects.
- **The Legend of Zelda: Breath of the Wild**: see Jenny Wang's [[mda-and-8-kinds-of-fun-jenny-wang|decomposition]].

## Reference

The original paper is Hunicke, LeBlanc, & Zubek, *MDA: A Formal Approach to Game Design and Game Research* — see [[mda-framework-paper]] for the source summary.

## Related pages

- [[mda-framework-paper]]
- [[eight-kinds-of-fun]]
- [[mda-and-8-kinds-of-fun-jenny-wang]]
- [[level-design]]
- [[level-design-saga-jeremy-kang]]
- [[player-motivation-models]]
