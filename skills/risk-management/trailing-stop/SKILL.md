---
name: trailing-stop
description: Lock in profits with dynamic trailing stop strategies. Use when riding winner trends, protecting open profits, or managing exits systematically.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Trailing Stop Strategies

Trailing stops lock in profits while allowing trades to run.

## Trailing Methods

### 1. ATR Trail (Recommended)

Long example: `Trailing Stop = Highest High - (ATR × multiplier)`; mirror for shorts. Declare ATR lookback, multiplier, update frequency, and whether intrabar or closed-bar highs apply.

### 2. Structure Trail

Move stop below each new swing low (long) or above each new swing high (short). Lets the trade breathe while locking in structure.

### 3. Moving Average Trail

Use a predeclared moving average and exit condition. Treat any period as a candidate parameter and prevent look-ahead by updating from available bars only.

### 4. Chandelier Exit

Trail from highest high by ATR multiple. Classic exit strategy, good for trending markets.

### 5. Fixed Distance Trail

Move stop by fixed amount (pips/%). Simple but can be too static -- prefer ATR or structure.

## When to Start Trailing

Test start conditions such as immediate, an R-multiple, elapsed bars, or a new objective swing. These labels do not imply conservative/aggressive risk without the resulting payoff distribution.

## Hybrid Approach

Combine methods for staged exit management:

1. Fixed initial stop
2. Optional, tested transition rule
3. One precisely defined trailing method
4. Time or terminal exit for any remaining quantity

## Exit Scenarios

| Price Action    | Trailing Action   |
| --------------- | ----------------- |
| New high/low    | Move stop up/down |
| Consolidation   | Keep stop same    |
| Predefined reversal trigger | Apply the specified update |
| Objective structure break | Exit or update as predeclared |

## Workflow

For each bar or tick, update the high-water mark and stop exactly once under the chosen rule; never lower a long trail or raise a short trail. Record trigger price versus fill price and handle gaps, partial fills, halts, and venue-specific trailing-order semantics.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: The [SEC stop-order bulletin](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15) explains trailing-stop mechanics and warns that short-term fluctuations can trigger an order and execution can differ from the stop.

## Key Rules

- Freeze lookbacks, multipliers, start condition, update clock, and terminal exit before entry.
- Never loosen the authorized trailing stop; account for order replacement races.
- Compare the trail against fixed-target, time-exit, and unchanged-stop baselines.
- Model trigger/fill gaps, fees, stop-limit nonexecution, and partial fills.
- Do not override the rule using hindsight; an emergency risk-off action must be logged separately.

## Related Skills

- **stop-loss-strategies** -- initial stop placement determines when trailing begins
- **partial-profit-taking** -- combine trailing stops with partial exits for optimal capture
