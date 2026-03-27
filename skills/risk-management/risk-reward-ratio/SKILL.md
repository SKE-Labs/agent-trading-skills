---
name: risk-reward-ratio
description: Calculate and optimize risk-reward ratios for trade setups. Use when evaluating trade quality, setting targets, or filtering low-quality setups.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
---

# Risk-Reward Ratio (R:R)

R:R compares potential profit to potential loss, helping filter high-quality trades.

## Calculation

`R:R = (Target - Entry) / (Entry - Stop)`

Example: Entry $100, Stop $95, Target $115 => R:R = $15 / $5 = 3:1.

Breakeven R:R formula: `(1 - Win Rate) / Win Rate`

| Win Rate | Minimum R:R | Breakeven R:R |
| -------- | ----------- | ------------- |
| 40%      | 1.5:1       | 1.5:1         |
| 50%      | 1:1         | 1:1           |
| 60%      | 0.7:1       | 0.67:1        |
| 70%      | 0.5:1       | 0.43:1        |

## R:R Targets by Style

| Trading Style    | Target R:R    |
| ---------------- | ------------- |
| Scalping         | 1:1 to 1.5:1  |
| Day Trading      | 1.5:1 to 2:1  |
| Swing Trading    | 2:1 to 3:1    |
| Position Trading | 3:1+          |

## Optimizing R:R

**Improve Entry**: Enter at better levels (OTE, pullbacks), wait for confirmation at S/R, use limit orders at key levels.

**Optimize Stop**: Structure-based stops (below swing low), ATR-based stops (1.5-2x ATR). Avoid arbitrary stops.

**Extend Target**: Use Fibonacci extensions, target next key level, allow runners with trailing stop.

## Trade Filtering

| R:R       | Action                      |
| --------- | --------------------------- |
| <1:1      | Skip (unless 70%+ win rate) |
| 1:1 - 2:1 | Trade with caution          |
| 2:1 - 3:1 | Good trade                  |
| 3:1+      | Excellent trade             |

## Workflow

1. **Identify entry** from technical analysis
2. **Set stop loss** based on structure or ATR (see stop-loss-strategies)
3. **Calculate R:R** using the formula above
4. **Filter** -- skip if R:R is below minimum for your win rate
5. **Set targets** at R:R milestones (1R, 2R, 3R) for partial exits

## Key Rules

- NEVER sacrifice R:R for win rate -- high R:R allows profitability even with lower win rates
- NEVER use arbitrary targets -- base them on structure, Fibonacci, or key levels
- Better entries = better R:R; be patient for optimal levels
- Always calculate R:R before entering; if the math doesn't work, skip the trade

## Related Skills

- **position-sizing** -- R:R determines trade quality; position sizing determines trade quantity
- **stop-loss-strategies** -- stop placement defines the risk side of the R:R equation
