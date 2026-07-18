---
name: partial-profit-taking
description: Design and test partial-exit schedules against a single-exit baseline. Use when calculating weighted R outcomes, residual risk, target/stop order mechanics, fees, and partial-fill behavior.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Partial Profit Taking

Scaling out changes the payoff distribution. It can reduce variance and regret, but may lower expectancy and adds orders, fees, and partial-fill risk. Select it only against an identical-signal single-exit baseline.

## Scaling Strategies

### 1. Fixed Thirds

- 1/3 at Target 1, 1/3 at Target 2, 1/3 runner (trailing stop)

### 2. Half-and-Half

- 50% at Target 1, 50% runner (trailing stop)

### 3. Pyramiding Out

- 25% at 1R, 25% at 2R, 25% at 3R, 25% runner

### 4. Single Exit Baseline

- Exit the full position using one predeclared target, time stop, or trailing rule. Treat it as the baseline, not a conviction choice.

## Target Setting

| Exit     | Level                    |
| -------- | ------------------------ |
| Target 1..n | Predeclared structural, time, or R-multiple exits |
| Runner | Precisely defined trailing or time exit |

Weights must sum to the executable quantity after lot-size rounding. Compute net R for every branch, including fees/slippage; taking 1R on part of a position does not "cover risk" on the remainder automatically.

## Stop Management After Partials

After each partial exit:

1. Recalculate remaining quantity, open risk, and portfolio risk after each fill.
2. Move the stop only according to the pretested schedule; breakeven is not risk-free after gaps, spread, and fees.
3. Handle rejected/partial target orders, stop quantity replacement, and overfill/race conditions explicitly.

## Workflow

**Example -- Long entry at $100, stop at $95 (risk $5):**

Assume 99 shares to make exact thirds and ignore costs only for this arithmetic example:

| Action | Price | Shares exited | Realized profit |
| --- | --- | --- | --- |
| Exit first third | $105 | 33 | $165 |
| Exit second third | $110 | 33 | $330 |
| Runner stopped | $108 | 33 | $264 |
| **Total** | -- | **99** | **$759 = 1.53R** |

Initial risk was `99 × $5 = $495`. Real implementation must subtract costs and model stop slippage.

## Tradeoffs

**Pros**: Reduces psychological pressure, locks in partial profit, allows runners without stress.

**Cons**: Reduces total profit if the move continues, more complex execution, must pre-plan levels.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: Partial exits change the payoff distribution; compare them with a single-exit baseline on identical signals. [Backtest-overfitting research](https://escholarship.org/uc/item/9tq3327h) explains why choosing the best scale-out schedule after many trials creates false discoveries.

## Key Rules

- NEVER decide scale-out levels during a trade -- pre-define them before entry
- Do not change stops merely because a partial filled; follow the tested schedule.
- Choose limit versus marketable orders from the fill/price tradeoff; limits are not guaranteed.
- Define runner exit, time limit, and stop quantity before entry.
- Compare net expectancy, drawdown, tail loss, turnover, and capacity with a single-exit baseline.

## Related Skills

- **trailing-stop** -- manages the runner position after partial exits
- **risk-reward-ratio** -- partial targets are set at R:R milestones (1R, 2R, 3R)
