---
name: partial-profit-taking
description: Scale out of positions at multiple targets to lock in gains. Use when managing winning trades, reducing risk, or optimizing exit strategy.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
---

# Partial Profit Taking

Scaling out locks in profits while leaving room for extended moves.

## Scaling Strategies

### 1. Fixed Thirds

- 1/3 at Target 1, 1/3 at Target 2, 1/3 runner (trailing stop)

### 2. Half-and-Half

- 50% at Target 1, 50% runner (trailing stop)

### 3. Pyramiding Out

- 25% at 1R, 25% at 2R, 25% at 3R, 25% runner

### 4. All Or Nothing

- Full position to single target. Higher variance but potentially higher reward. For high conviction trades only.

## Target Setting

| Exit     | Level                    |
| -------- | ------------------------ |
| Target 1 | 1:1 R:R (cover risk)     |
| Target 2 | 2:1 R:R                  |
| Target 3 | 3:1 R:R or Fib extension |
| Runner   | Trail until stopped      |

## Stop Management After Partials

After each partial exit:

1. Move stop to protect remaining position
2. After 1st partial: typically move to breakeven
3. After 2nd partial: trail below structure

## Workflow

**Example -- Long entry at $100, stop at $95 (risk $5):**

| Action            | Price | Position | Profit    |
| ----------------- | ----- | -------- | --------- |
| Entry             | $100  | 100%     | $0        |
| Exit 1/3          | $105  | 67%      | +$170     |
| Move stop to $100 | --    | --       | --        |
| Exit 1/3          | $110  | 33%      | +$170     |
| Move stop to $105 | --    | --       | --        |
| Runner stopped    | $108  | 0%       | +$90      |
| **Total**         | --    | --       | **+$430** |

## Tradeoffs

**Pros**: Reduces psychological pressure, locks in partial profit, allows runners without stress.

**Cons**: Reduces total profit if the move continues, more complex execution, must pre-plan levels.

## Key Rules

- NEVER decide scale-out levels during a trade -- pre-define them before entry
- NEVER skip adjusting the stop after a partial exit -- the remaining position must be protected
- Use limit orders at targets for clean execution
- Let the runner ride with a wide trail -- that is where outsized gains come from
- Adjust remaining stop after every partial, not just the first

## Related Skills

- **trailing-stop** -- manages the runner position after partial exits
- **risk-reward-ratio** -- partial targets are set at R:R milestones (1R, 2R, 3R)
