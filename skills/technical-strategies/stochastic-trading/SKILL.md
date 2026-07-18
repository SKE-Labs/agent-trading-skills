---
name: stochastic-trading
description: Define and test Stochastic percent-K/percent-D states, crosses, and divergence. Use when calibrating oscillator bands, trend interactions, closed-bar entries, exits, and turnover.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Stochastic Oscillator Trading

Stochastic measures momentum by comparing closing price to the price range over a period.

## Components

| Line | Description               | Use            |
| ---- | ------------------------- | -------------- |
| %K   | Main line (fast)          | Primary signal |
| %D   | Signal line (3-SMA of %K) | Confirmation   |

## Signals

### Overbought/Oversold Reversals

- Define low/high bands from training data or use 20/80 only as conventional seeds; a cross creates a candidate trigger, not an automatic trade

### %K/%D Crossover

- %K crosses above %D → bullish feature; test interaction with oscillator zone
- %K crosses below %D → bearish

### Divergence

- Price new high + Stochastic lower high → bearish
- Price new low + Stochastic higher low → bullish

### Momentum

- %K above 50 and rising → bullish momentum
- %K below 50 and falling → bearish momentum

## Market-Specific Strategies

### Ranging Markets
- Apply calibrated low/high exit-cross rules
- Target: opposite zone

### Trending Markets
- Define trend objectively and test trend-direction filters; persistent extremes are possible

## Workflow

1. **Get Stochastic**:
   ```
   get_indicators(indicator_code="stoch", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   ```

2. **Determine market type** (trending vs ranging) to select strategy

3. **Check for %K/%D cross** in OB/OS zone

4. **Confirm with candle data**:
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
   ```

5. **Enter with confirmation** candle; stop beyond recent swing

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: The [technical-rule evidence](https://pmc.ncbi.nlm.nih.gov/articles/PMC4583561/) finds stochastic-rule performance differs across markets and is not reliably positive after transaction costs.

## Key Rules

- Never trade from an extreme label alone; require the predeclared closed-bar rule.
- Calibrate divergence pivots, spacing, and oscillator bands.
- Test with/against-trend variants rather than assuming the filter adds edge.
- Treat 14/3/3 as a conventional baseline; record all parameter variants and turnover.

## Related Skills

- **rsi-divergence** — Stochastic divergence + RSI divergence together strengthens reversal signals
- **bollinger-bands** — test stochastic state at volatility-envelope extremes as a combined feature
