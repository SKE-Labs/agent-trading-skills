---
name: partial-profit-taking
description: Scale out of positions at multiple targets to lock in gains. Use when managing winning trades, reducing risk, or optimizing exit strategy.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Partial Profit Taking

Scaling out locks in profits while leaving room for extended moves.

## Scaling Strategies

### 1. Fixed Thirds

- 1/3 at Target 1
- 1/3 at Target 2
- 1/3 runner (trailing stop)

### 2. Half-and-Half

- 50% at Target 1
- 50% runner (trailing stop)

### 3. Pyramiding Out

- 25% at 1R
- 25% at 2R
- 25% at 3R
- 25% runner

### 4. All Or Nothing

- Full position to single target
- Higher variance, potentially higher reward
- For high conviction trades

## Target Setting

| Exit     | Level                    |
| -------- | ------------------------ |
| Target 1 | 1:1 R:R (cover risk)     |
| Target 2 | 2:1 R:R                  |
| Target 3 | 3:1 R:R or Fib extension |
| Runner   | Trail until stopped      |

## Stop Management After Partials

After each partial:

1. Move stop to protect remaining position
2. Typically to breakeven after 1st partial
3. Or trail below structure

## Workflow Example

**Long entry at $100, stop at $95 (risk $5):**

| Action            | Price | Position | Profit    |
| ----------------- | ----- | -------- | --------- |
| Entry             | $100  | 100%     | $0        |
| Exit 1/3          | $105  | 67%      | +$170     |
| Move stop to $100 | —     | —        | —         |
| Exit 1/3          | $110  | 33%      | +$170     |
| Move stop to $105 | —     | —        | —         |
| Runner stopped    | $108  | 0%       | +$90      |
| **Total**         | —     | —        | **+$430** |

## Pros and Cons

### Pros

- Reduces psychological pressure
- Locks in partial profit
- Allows runners without stress
- Better risk management

### Cons

- Reduces total profit if move continues
- More complex execution
- Must pre-plan levels

## Best Practices

- Pre-define scale out levels before entry
- Use limit orders at targets
- Adjust remaining stop after each partial
- Let runner ride with wide trail

## Related Skills

- **trailing-stop** — After partial profits are taken, trailing stops manage the remaining runner position
- **risk-reward-ratio** — Partial profit targets are typically set at R:R milestones (1R, 2R, 3R)
- **stop-loss-strategies** — Stop management must be updated after each partial exit to protect remaining position
