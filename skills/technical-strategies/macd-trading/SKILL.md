---
name: macd-trading
description: Define and test MACD line, signal, histogram, zero-line, and divergence features. Use when evaluating closed-bar momentum/trend rules with explicit parameters, exits, regime context, and costs.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# MACD Trading Strategy

MACD (Moving Average Convergence Divergence) combines trend-following and momentum analysis.

## Components

| Component       | Calculation     | Use                |
| --------------- | --------------- | ------------------ |
| **MACD Line**   | 12 EMA - 26 EMA | Trend direction    |
| **Signal Line** | 9 EMA of MACD   | Entry trigger      |
| **Histogram**   | MACD - Signal   | Momentum strength  |
| **Zero Line**   | Centerline      | Bull/bear boundary |

## Signals

### Crossover

- **Bullish**: MACD crosses above Signal line → buy
- **Bearish**: MACD crosses below Signal line → sell
- Record whether a cross occurs above or below zero as context; do not assign strength without validation

### Zero Line Cross

- MACD above zero = bullish trend
- MACD below zero = bearish trend
- Cross of zero = trend change confirmation

### Histogram

- Growing histogram = increasing momentum
- Shrinking histogram = weakening momentum (often precedes crossover)

### Divergence

- Price new high + MACD lower high → bearish divergence
- Price new low + MACD higher low → bullish divergence

## Workflow

1. **Get MACD**:
   ```
   get_indicators(indicator_code="macd", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   ```

2. **Record zero-line state** as one feature; it does not determine direction by itself

3. **Wait for crossover** in trend direction. Confirm with histogram growing in direction.

4. **Check for divergence** between price and MACD line/histogram

5. **Get candles for context**:
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
   ```

6. **Exit**: choose one objective crossover, histogram, price, target, or time rule before entry and test it separately

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: Cross-market studies summarized in the [technical-rule evidence](https://pmc.ncbi.nlm.nih.gov/articles/PMC4583561/) show MACD performance varies by market and costs; a crossover is a feature, not an edge by itself.

## Key Rules

- A crossover is a lagged price-derived feature; require a separately validated decision rule.
- Test zero-line and higher-timeframe filters for incremental held-out value.
- Treat 12/26/9 as the conventional baseline and record all parameter variants tried.
- Define histogram expansion/shrinkage over a fixed number of closed bars.
- Do not label a crossover confirmation unless its conditional outcome distribution supports that use.

## Related Skills

- **divergence-trading** — multi-indicator divergence framework that includes MACD
- **moving-average-crossover** — MACD is derived from EMAs; combine for confirmation
