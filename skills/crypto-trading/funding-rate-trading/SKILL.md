---
name: funding-rate-trading
description: Evaluate venue-specific perpetual funding, basis, and delta-neutral carry. Use when normalizing funding history, stress-testing hedge/margin/exchange risks, or testing contrarian funding features.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Funding Rate Trading

Perpetual futures use venue-specific funding mechanisms to influence alignment with spot. Funding and basis can support carry or directional hypotheses, but neither is an arbitrage guarantee or standalone signal.

## Funding Rate Basics

- **Positive funding**: Longs pay shorts (market is bullish/overleveraged long)
- **Negative funding**: Shorts pay longs (market is bearish/overleveraged short)
- Interval, formula, caps, and settlement are venue-specific. Read the current contract specification before annualizing.

## Funding Rate Signals

| Observation | What it establishes | What it does not establish |
| --- | --- | --- |
| Positive funding | Longs pay shorts for that interval | Imminent reversal |
| Negative funding | Shorts pay longs for that interval | Market bottom |
| Persistent extreme percentile | Crowded carry relative to venue history | Safe contrarian entry |
| Wide perp/spot basis | Hedge and funding demand | Guaranteed convergence |

## Strategies

**1. Funding Rate Arbitrage (Delta Neutral)**
- Long spot + short perp when funding is highly positive
- Collect funding payments while market-neutral
- Annualized simple rate = interval rate × actual intervals per year; also report compounded and realized rates separately
- Enter only when stressed net carry remains positive after fees, basis moves, rebalancing, margin, and custody costs

**2. Extreme Funding Reversal Hypothesis**
- Define extremes by the same venue/contract's historical percentile and test positive/negative tails separately.
- Require an objective price trigger and stress continued crowding; do not wait for or assume a liquidation cascade.

**3. Funding as Confirmation**
- Use funding direction to confirm or reject a technical setup
- Test whether funding adds information beyond price-derived features such as RSI

## Workflow

1. **Get current funding rate data**:
```
get_financial_news(topic="BTC perpetual funding rate Binance Bybit")
```

2. **Check spot price and momentum**:
```
get_candles(symbol="BTC/USD", exchange="binance", interval="4h", count=1)
get_indicators(indicator_code="rsi", symbol="BTC/USD", exchange="binance", interval="4h")
```

3. **Assess futures-spot premium**:
```
get_financial_news(topic="BTC futures premium spot basis")
```

4. **Calculate net carry** from the venue's actual interval and historical realized rates. Stress a funding flip, spot/perp basis widening, hedge mismatch, and liquidation on either leg.

5. **Report**: funding regime (extreme/normal), sentiment implication, arb APR if applicable, and any contrarian trade setup with technical confirmation.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Coinbase's funding documentation](https://help.coinbase.com/en/coinbase/derivatives/funding-rate) shows that interval, annualization, caps, and settlement are venue-specific; [perpetual-futures research](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4301150) documents basis and trading-cost bounds.

## Key Rules

- Use a predeclared persistence window and the contract's actual interval; never assume an 8-hour schedule.
- Monitor funding, basis, hedge error, collateral, and liquidation state throughout the position.
- Extreme funding can persist or flip; estimate conditional outcomes rather than predicting a cascade.
- Same-venue legs reduce transfer latency but concentrate exchange and collateral risk; cross-venue legs introduce transfer and basis risk

## Related Skills

- **arbitrage-trading** -- funding arb is a specific delta-neutral arbitrage strategy
- **on-chain-analysis** -- exchange flow data confirms leverage buildup behind funding extremes
