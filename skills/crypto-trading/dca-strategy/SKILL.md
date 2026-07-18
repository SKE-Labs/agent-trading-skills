---
name: dca-strategy
description: Implement Dollar Cost Averaging for systematic long-term accumulation. Use when building positions over time, reducing timing risk, or accumulating during uncertainty.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Dollar Cost Averaging (DCA)

Invest new cash on a fixed schedule. Distinguish paycheck-style periodic investing from deliberately delaying a lump sum that is already available.

## DCA Mechanics

```
Each Purchase = Fixed Amount / Current Price
Average Cost  = Total Spent / Total Units Acquired
```

Example ($100/week):
- Week 1: $100 / $50 = 2.0 units
- Week 2: $100 / $40 = 2.5 units
- Week 3: $100 / $60 = 1.67 units
- Total: 6.17 units for $300 (avg cost: $48.62)

## DCA Variants

| Variant           | Description                                      |
| ----------------- | ------------------------------------------------ |
| Fixed Interval    | Same amount every week/month -- simplest          |
| Value Averaging   | Adjust amount to hit a target portfolio value     |
| Enhanced DCA      | Base amount + bonus when price drops below MA     |
| Lump Sum + DCA    | Deploy 50% immediately, DCA the remaining 50%    |

## Asset Eligibility

| Candidate         | Reject or escalate              |
| ---------------- | -------------------------- |
| Diversified, liquid exposure | Unclear rights or custody |
| Assets with a documented thesis | Failing liquidity or security |
| Instruments compatible with the horizon | Position already above its risk cap |

## Workflow

1. **Capture the plan**: goal, horizon, target allocation, contribution amount, frequency, funding source, custody, fees, and maximum allocation. Do not change the schedule from short-term price forecasts.

2. **Check allocation drift and current price context**:
```
get_candles(symbol="BTC/USD", exchange="binance", interval="1d", count=1)
get_indicators(indicator_code="sma_50", symbol="BTC/USD", exchange="binance", interval="1w")
```

3. **Apply any enhanced-DCA rule only if it was predeclared and validated**; a 200-day moving-average rule is optional, not inherent to DCA:
```
get_indicators(indicator_code="sma_200", symbol="BTC/USD", exchange="binance", interval="1d")
```

4. **Re-underwrite the asset**, not the next candle:
```
get_financial_news(topic="BTC macro outlook accumulation")
```

5. **Report** scheduled contribution, post-trade allocation, weighted average cost, fees, custody or concentration flags, and whether a written pause condition was triggered.

## When to Stop DCA

- Target position size reached
- Fundamentals have materially deteriorated
- Better risk/reward opportunity identified elsewhere

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Vanguard research](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf) found immediate lump-sum investment historically beat temporary cost averaging about two-thirds of the time; DCA is mainly a cash-flow and behavior plan.

## Key Rules

- Do not skip or enlarge a scheduled purchase from an improvised price forecast
- Do not confuse DCA with averaging down an invalidated speculative thesis
- Review quarterly, not daily; over-monitoring defeats the purpose
- For cash already available, explicitly compare immediate investment with staged deployment; DCA may reduce short-term regret at the cost of expected time in market

## Related Skills

- **altcoin-rotation** -- DCA into BTC/ETH during accumulation, then rotate when cycle shifts
- **on-chain-analysis** -- MVRV and realized cap identify macro accumulation zones for enhanced DCA
