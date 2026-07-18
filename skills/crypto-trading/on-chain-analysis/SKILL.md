---
name: on-chain-analysis
description: Analyze on-chain metrics with provider, entity-adjustment, revision, and normalization controls. Use when evaluating holder behavior, exchange flows, valuation ratios, or network activity as contextual trading features.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# On-Chain Analysis

Interpret blockchain data to understand market participant behavior and identify macro accumulation/distribution phases.

> **Note:** Agent does not have direct on-chain API access. Use this framework to interpret on-chain data found via `get_financial_news`.

## Exchange Flows

| Metric            | Accumulation hypothesis | Distribution hypothesis |
| ----------------- | ------------------- | -------------- |
| Exchange net flow | Persistent outflow | Persistent inflow |
| Exchange reserves | Decreasing          | Increasing     |
| Stablecoin flows | Dry-powder hypothesis | Redemption or risk-off hypothesis |

## Wallet Activity

| Metric                  | Growth hypothesis | Weakness hypothesis |
| ----------------------- | ---------- | ---------- |
| Whale accumulation      | High       | Low        |
| Long-term holder supply | Increasing | Decreasing |
| Active addresses        | Growing    | Declining  |

## Normalization

Do not reuse absolute BTC thresholds across eras or networks. For every metric, record provider, definition, unit, entity-adjustment status, timestamp, revision policy, and a trailing percentile or robust z-score. Multiple metrics derived from the same transaction graph are correlated and do not count as independent votes.

## MVRV Ratio

| MVRV Range | Interpretation                        | Action                 |
| ---------- | ------------------------------------- | ---------------------- |
| High relative to its own history | Large aggregate unrealized profit | Distribution risk, not an automatic sale |
| Near 1 | Market value near realized value | Cost-basis context, not fair value |
| Below 1 | Aggregate unrealized loss | Stress context, not an automatic buy |

For NVT and activity metrics, match the numerator and denominator frequency and account for batching, L2 migration, exchange-internal transfers, spam, and changes in address clustering. “Active address” is not the same as a user.

## Workflow

1. **Gather on-chain intelligence** from news sources:
```
get_financial_news(topic="BTC on-chain exchange outflow whale accumulation")
get_financial_news(topic="BTC MVRV NVT realized cap ratio")
```

2. **Check current price and momentum** for technical confirmation:
```
get_candles(symbol="BTC/USD", exchange="binance", interval="1d", count=1)
get_indicators(indicator_code="rsi", symbol="BTC/USD", exchange="binance", interval="1d")
get_indicators(indicator_code="macd", symbol="BTC/USD", exchange="binance", interval="1d")
```

3. **Classify evidence**: separate observed metric changes from provider interpretation and from the trading hypothesis. Reconcile contradictory metrics instead of counting votes.

4. **Report macro thesis**: on-chain regime, metric alignment count, technical confirmation status, key levels, and confidence level.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Glassnode's MVRV methodology](https://docs.glassnode.com/guides-and-tutorials/metric-guides/mvrv/mvrv-ratio) defines the metric, while [entity-adjustment notes](https://docs.glassnode.com/guides-and-tutorials/on-chain-concepts/entity-adjusted-metrics) explain clustering and revision risk; neither supports universal cutoffs.

## Key Rules

- Match each on-chain metric's timestamp, revision latency, and tested forecast horizon; do not assume one universal horizon.
- NEVER convert a count of correlated metrics into “high confidence” without testing incremental information
- Large transfers may be internal exchange movements -- context matters
- On-chain data is lagging; it confirms trends rather than predicting them
- LTH selling = distribution phase warning; LTH accumulating = bullish macro signal

## Related Skills

- **altcoin-rotation** -- on-chain metrics confirm cycle phases driving rotation decisions
- **dca-strategy** -- MVRV and realized cap identify macro accumulation zones for enhanced DCA
