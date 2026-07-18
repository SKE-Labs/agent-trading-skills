---
name: drawdown-management
description: Manage account drawdowns with limits and recovery protocols. Use when protecting capital during losing streaks, implementing loss limits, or developing recovery plans.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Drawdown Management

Drawdown management protects capital and ensures trading longevity through loss limits and recovery protocols.

## Drawdown Types

| Type             | Definition                     |
| ---------------- | ------------------------------ |
| Max Drawdown     | Largest peak-to-trough decline |
| Daily Drawdown   | Loss in single trading day     |
| Weekly Drawdown  | Loss in single week            |
| Open Drawdown    | Unrealized loss on open trades |

## Drawdown Policy

Obtain daily, weekly, strategy, and maximum-drawdown limits from the portfolio mandate. Define the equity series (realized plus marked-to-market P&L, fees, funding, deposits/withdrawals), peak reset rule, timezone, and whether open-position stress is added. If no limits exist, propose examples for approval rather than enforcing invented percentages.

## Loss Response Protocol

At a limit, block new risk as specified by the mandate and alert the owner. Do not automatically liquidate positions: compare orderly reduction with gap, spread, tax, and hedge consequences. Resume only after the documented cause, data/execution health, model validity, and revised risk budget pass an authorized review—not after an arbitrary pause or number of winning days.

## Recovery Math

Larger drawdowns require exponentially larger gains to recover:

| Drawdown | Return Needed to Recover |
| -------- | ------------------------ |
| 10%      | 11%                      |
| 20%      | 25%                      |
| 30%      | 43%                      |
| 50%      | 100%                     |

Formula: `Recovery % = Drawdown / (1 - Drawdown) x 100`

This is why preventing large drawdowns matters more than maximizing gains.

## Prevention Strategies

1. **Size to mandate** -- include gap and correlated exposure
2. **Enforce approved limits** -- block new risk and escalate exactly as documented
3. **Manage correlations** -- avoid stacking similar positions (see correlation-risk)
4. **Reduce in losing streaks** -- cut size early, don't wait for the limit
5. **Diversify strategies** -- single-strategy risk is concentrated risk

## Monitoring

Track these metrics continuously:

- Current drawdown from equity peak
- Number of consecutive losing days
- Deviation from the strategy's confidence interval for return and loss distribution
- Equity curve slope (flattening = warning)

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Risk-constrained Kelly research](https://web.stanford.edu/~boyd/papers/kelly.html) explicitly trades expected growth against drawdown probability; loss limits should be chosen from mandate and tested distributions, not copied as universal percentages.

## Key Rules

- Never add risk to recover a loss unless a preapproved sizing policy independently calls for it.
- Preserve realized/unrealized P&L, cash flows, peak, limit, and response in an immutable audit record.
- Distinguish strategy deterioration, expected variance, concentration, data faults, and execution faults.
- Do not label a drawdown percentage normal without strategy-specific simulations and mandate approval.
- Use forward-looking stress and remaining risk budget, not winning/losing streak folklore, to set size.

## Related Skills

- **position-sizing** -- proper sizing is the primary drawdown prevention tool
- **correlation-risk** -- correlated positions amplify drawdowns
