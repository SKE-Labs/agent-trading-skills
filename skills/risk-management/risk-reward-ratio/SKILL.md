---
name: risk-reward-ratio
description: Calculate long/short planned R-multiples and net expectancy. Use when evaluating executable entry, stop, target, win/loss distribution, costs, gaps, and uncertainty without treating R:R as trade quality by itself.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Risk-Reward Ratio (R:R)

R:R compares potential profit to potential loss, helping filter high-quality trades.

## Calculation

For a long: `R:R = (Target - Entry) / (Entry - Stop)`. For a short: `R:R = (Entry - Target) / (Stop - Entry)`. Require positive denominators and use executable prices plus expected slippage/fees.

Example: Entry $100, Stop $95, Target $115 => R:R = $15 / $5 = 3:1.

The zero-cost binary breakeven R:R is `(1 - Win Rate) / Win Rate`. Actual breakeven is higher after costs, gaps, partial fills, and non-binary exits.

| Win Rate | Minimum R:R | Breakeven R:R |
| -------- | ----------- | ------------- |
| 40%      | 1.5:1       | 1.5:1         |
| 50%      | 1:1         | 1:1           |
| 60%      | 0.7:1       | 0.67:1        |
| 70%      | 0.5:1       | 0.43:1        |

## Expectancy

Use realized net payoff distributions: `E = p × average_win - (1-p) × average_loss - average_costs`. Report uncertainty, tail loss, sample period, and regime stability. Planned R:R alone does not establish win probability or trade quality.

## Optimizing R:R

**Improve Entry**: Enter at better levels (OTE, pullbacks), wait for confirmation at S/R, use limit orders at key levels.

**Define Stop**: use thesis invalidation plus a validated tick/volatility buffer, then size from the resulting risk.

**Define Target**: use observable structure, time exit, or a tested rule; moving a target farther away improves displayed R:R but can reduce hit probability.

Filter on conservative net expectancy, tail risk, liquidity, and mandate fit. Do not label a trade good or excellent from its planned R:R.

## Workflow

1. **Identify entry** from technical analysis
2. **Set stop loss** based on structure or ATR (see stop-loss-strategies)
3. **Calculate R:R** using the formula above
4. **Filter** -- require positive conservative net expectancy and mandate compliance
5. **Set targets** at R:R milestones (1R, 2R, 3R) for partial exits

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: R-multiples describe a planned payoff but do not establish expectancy. Include win probability, costs, gaps, and partial fills; [FINRA](https://www.finra.org/investors/investing/investing-basics/fees-commissions) notes that trading costs persist even with zero commissions.

## Key Rules

- Evaluate win probability and payoff jointly; neither high R:R nor high win rate is sufficient.
- Use executable, predeclared targets and stops rather than decorative ratios.
- Avoid selection bias from waiting only for entries that make the displayed ratio attractive.
- Return `no trade` when net expectancy, uncertainty, liquidity, or risk limits fail.

## Related Skills

- **position-sizing** -- R:R determines trade quality; position sizing determines trade quantity
- **stop-loss-strategies** -- stop placement defines the risk side of the R:R equation
