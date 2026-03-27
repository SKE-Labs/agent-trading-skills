---
name: on-chain-analysis
description: Analyze blockchain data for trading signals (whale movements, exchange flows). Use when understanding smart money, detecting accumulation/distribution, or confirming macro trends.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# On-Chain Analysis

Interpret blockchain data to understand market participant behavior and identify macro accumulation/distribution phases.

> **Note:** Agent does not have direct on-chain API access. Use this framework to interpret on-chain data found via `get_financial_news`.

## Exchange Flows

| Metric            | Bullish             | Bearish        |
| ----------------- | ------------------- | -------------- |
| Exchange inflow   | Low                 | High (selling) |
| Exchange outflow  | High (accumulation) | Low            |
| Exchange reserves | Decreasing          | Increasing     |

## Wallet Activity

| Metric                  | Bullish    | Bearish    |
| ----------------------- | ---------- | ---------- |
| Whale accumulation      | High       | Low        |
| Long-term holder supply | Increasing | Decreasing |
| Active addresses        | Growing    | Declining  |

## Key Metric Thresholds

| Metric                       | Bullish             | Bearish              | Neutral      |
| ---------------------------- | ------------------- | -------------------- | ------------ |
| Exchange Net Flow            | <-10K BTC/day out   | >+10K BTC/day in     | +/-10K       |
| Whale Txns (>1000 BTC)      | Majority to cold    | Majority to exchange | Mixed        |
| LTH Supply Change (30d)     | >+50K BTC           | <-50K BTC            | +/-50K       |
| Active Addresses (vs 30d avg)| >120% of average   | <80% of average      | 80-120%      |

When 3+ metrics align in the same direction, the signal is high-confidence.

## MVRV Ratio

| MVRV Range | Interpretation                        | Action                 |
| ---------- | ------------------------------------- | ---------------------- |
| > 3.5      | Market overvalued -- distribution zone | Reduce exposure        |
| 1.0 - 3.5  | Normal range                          | Standard positioning   |
| < 1.0      | Below aggregate cost basis            | Historically best buys |

## NVT Signal

| NVT Range | Interpretation                         | Signal  |
| --------- | -------------------------------------- | ------- |
| > 95      | Network overvalued relative to usage   | Bearish |
| 45 - 95   | Normal range                           | Neutral |
| < 45      | Network undervalued relative to usage  | Bullish |

NVT works best as a macro indicator; use multi-day averages to filter noise.

## Workflow

1. **Gather on-chain intelligence** from news sources:
```
get_financial_news(query="BTC on-chain exchange outflow whale accumulation")
get_financial_news(query="BTC MVRV NVT realized cap ratio")
```

2. **Check current price and momentum** for technical confirmation:
```
get_latest_candle(symbol="BTCUSDT")
get_indicator(indicator_code="rsi", symbol="BTCUSDT", interval="1d")
get_indicator(indicator_code="macd", symbol="BTCUSDT", interval="1d")
```

3. **Classify regime**: Map news findings to the tables above -- accumulation, distribution, or neutral.

4. **Report macro thesis**: on-chain regime, metric alignment count, technical confirmation status, key levels, and confidence level.

## Key Rules

- NEVER use on-chain metrics for day trading or short-term timing -- they are macro indicators
- NEVER treat a single metric in isolation; require 3+ aligned metrics for high-confidence signals
- Large transfers may be internal exchange movements -- context matters
- On-chain data is lagging; it confirms trends rather than predicting them
- LTH selling = distribution phase warning; LTH accumulating = bullish macro signal

## Related Skills

- **altcoin-rotation** -- on-chain metrics confirm cycle phases driving rotation decisions
- **dca-strategy** -- MVRV and realized cap identify macro accumulation zones for enhanced DCA
