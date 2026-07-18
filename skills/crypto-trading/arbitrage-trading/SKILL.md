---
name: arbitrage-trading
description: Screen execution-sensitive price differences across exchanges, pairs, spot, and derivatives. Use when evaluating synchronized spreads, triangular conversion paths, or basis trades after fees, depth, settlement, counterparty, and inventory risk.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Arbitrage Trading

Identify executable price differences while assuming that every apparent spread may compensate for latency, liquidity, settlement, or venue risk.

> **Note:** Agent can identify arbitrage opportunities via price comparison but cannot execute cross-exchange trades directly. Use this skill to detect and report opportunities.

## Arbitrage Types

| Type             | Mechanism                                  | Key Cost Factor   |
| ---------------- | ------------------------------------------ | ----------------- |
| Cross-Exchange   | Same asset priced differently on two venues | Transfer fees     |
| Triangular       | Three-pair cycle (BTC->ETH->USDT->BTC)    | Trading fees x3   |
| Futures-Spot     | Premium between spot and perp/futures      | Funding rate      |
| DEX-CEX          | Price gap between decentralized and centralized | Gas fees     |

## Profitability Check

**Cross-Exchange:**
- Gross P&L = executable sell proceeds − executable buy cost for the same quantity
- Net P&L = Gross P&L − fees − slippage − funding/borrow − transfer/gas − hedge and rebalancing costs

**Triangular:**
- Expected cross rate = Price_A / Price_B
- Actual cross rate = observed market rate
- Spread % = (Actual - Expected) / Expected x 100

Require a positive buffer above estimated costs and model error; `Net Profit > 0` on stale top-of-book quotes is not sufficient.

## Workflow

1. **Fetch synchronized executable quotes** from every leg. Candle closes are a coarse screening proxy only; do not call the result actionable without bid/ask, depth, size, timestamp, and venue status.
```
get_candles(symbol="BTC/USD", exchange="binance", interval="5m", count=1)
get_candles(symbol="ETH/USD", exchange="binance", interval="5m", count=1)
get_candles(symbol="ETH/BTC", exchange="binance", interval="5m", count=1)
```

2. **Simulate the exact path** using the correct bid or ask at each leg, lot/tick rules, rounding, and available depth.

3. **Check carry and convergence terms** from the venue's contract specification, funding history, margin rules, and settlement index—not a news summary alone:
```
get_financial_news(topic="BTC funding rate perpetual futures premium")
```

4. **Stress all costs and failures**: one-leg fill, reject, latency, transfer halt, depeg, funding flip, liquidation, borrow recall, and exchange default.

5. **Report opportunity** with: pair(s), spread %, estimated fees, net profit, and time sensitivity.

## Triangular Arbitrage Example

```
BTC/USDT: 50,000 | ETH/USDT: 2,000 | ETH/BTC: 0.041
Expected ETH/BTC: 2000/50000 = 0.040
Actual: 0.041 → ~2.5% spread (before fees)
Path: USDT → BTC → ETH → USDT
```

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [John, Li & Liu](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4816710) and [Vidal-Tomás](https://www.sciencedirect.com/science/article/pii/S154461232401393X) show that observed crypto spreads reflect liquidity, settlement, fees, and exchange-default risk—not risk-free profit.

## Key Rules

- NEVER report an opportunity without deducting all fees (trading, transfer, gas, slippage)
- NEVER assume execution is instant -- note that cross-exchange opportunities decay in seconds
- Pre-funded accounts on both sides are required for cross-exchange arb; transfers kill the edge
- Use a venue-, size-, and latency-specific minimum edge; no universal spread floor is valid
- Check order book depth: thin liquidity means slippage will eat the spread

## Related Skills

- **funding-rate-trading** -- funding rate arb (spot + perp) is a specific delta-neutral strategy
- **altcoin-rotation** -- cross-pair price analysis overlaps with rotation screening
