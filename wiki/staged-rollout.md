# Staged Rollout

**Summary**: Releasing a game update to a small slice of the player base first, then expanding in stages, to catch bugs and gather feedback before a full release.

**Sources**: `Making a Hit Idle Game – Eight Lessons from Kolibri Games.md`.

**Last updated**: 2026-04-25.

---

## Kolibri's four-day schedule

For each weekly update to [[idle-miner-tycoon]] (source: Making a Hit Idle Game – Eight Lessons from Kolibri Games.md):

| Day | Player base | Goal |
|-----|-------------|------|
| 1   | 1%          | Catch major bugs and any release-blocking issues. |
| 2   | 5%          | Continue bug surveillance. |
| 3   | 20%         | Gather qualitative feedback and store reviews. |
| 4   | 100%        | Full rollout if no red flags. |

## Why it works

- Cost of a bad release scales with the population that sees it; staged rollout caps that population.
- Qualitative feedback at 20% is enough volume to be representative without being catastrophic if the change is wrong.
- It pairs cleanly with high-cadence updates (~1/week) — see [[live-ops-features]] — because the cost of any single update going wrong stays low.

## Related pages

- [[live-ops-features]]
- [[lean-development]]
- [[idle-miner-tycoon]]
