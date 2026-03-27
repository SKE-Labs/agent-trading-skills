---
name: funding-rate-trading
description: Trade based on perpetual futures funding rate signals. Use when funding is extreme, finding market sentiment, or earning funding payments.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Funding Rate Trading

Perpetual futures use funding rates to keep price aligned with spot -- creating trading signals and arbitrage opportunities.

## Funding Rate Basics

- **Positive funding**: Longs pay shorts (market is bullish/overleveraged long)
- **Negative funding**: Shorts pay longs (market is bearish/overleveraged short)
- Paid every 8 hours; 0.01% per 8h ~ 10.95% APR

## Funding Rate Signals

| Funding Rate            | Market Sentiment     | Trade Idea       |
| ----------------------- | -------------------- | ---------------- |
| Very Positive (>0.05%)  | Overleveraged longs  | Contrarian short |
| Positive (0.01-0.05%)   | Bullish              | No signal        |
| Neutral (~0.01%)        | Balanced             | No signal        |
| Negative (<0%)          | Bearish              | Potential bottom |
| Very Negative (<-0.05%) | Overleveraged shorts | Contrarian long  |

## Strategies

**1. Funding Rate Arbitrage (Delta Neutral)**
- Long spot + short perp when funding is highly positive
- Collect funding payments while market-neutral
- APR = Funding Rate (%) x 3 x 365
- Only enter if APR > 20%; close when rate normalizes

**2. Extreme Funding Reversal**
- Very high positive funding + resistance = strong short signal
- Very negative funding + support = strong long signal
- Wait for liquidation cascade to confirm

**3. Funding as Confirmation**
- Use funding direction to confirm or reject a technical setup
- High funding aligning with overbought RSI strengthens reversal case

## Workflow

1. **Get current funding rate data**:
```
get_financial_news(query="BTC perpetual funding rate Binance Bybit")
```

2. **Check spot price and momentum**:
```
get_latest_candle(symbol="BTCUSDT")
get_indicator(indicator_code="rsi", symbol="BTCUSDT", interval="4h")
```

3. **Assess futures-spot premium**:
```
get_financial_news(query="BTC futures premium spot basis")
```

4. **Calculate arb APR** if funding is extreme: APR = rate x 3 x 365.

5. **Report**: funding regime (extreme/normal), sentiment implication, arb APR if applicable, and any contrarian trade setup with technical confirmation.

## Key Rules

- NEVER enter funding arb without confirming the rate has been sustained (check multi-day average, not a single 8h print)
- NEVER ignore that funding can flip direction -- monitor continuously after entry
- Extreme funding often precedes reversals; when "everyone is long," liquidation cascades follow
- Funding arb requires positions on the same exchange to avoid transfer/timing risk

## Related Skills

- **arbitrage-trading** -- funding arb is a specific delta-neutral arbitrage strategy
- **on-chain-analysis** -- exchange flow data confirms leverage buildup behind funding extremes
