---
name: macd-trading
description: Trade using MACD crossovers, histogram, and divergence signals. Use when confirming trend direction, timing entries with momentum, or identifying trend strength changes.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
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
- Bullish cross above zero = strongest buy; bearish cross below zero = strongest sell

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
   get_indicator(indicator_code="macd", symbol=<symbol>, interval=<interval>)
   ```

2. **Determine trend** from zero line: MACD > 0 → look for longs; MACD < 0 → look for shorts

3. **Wait for crossover** in trend direction. Confirm with histogram growing in direction.

4. **Check for divergence** between price and MACD line/histogram

5. **Get candles for context**:
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```

6. **Exit signals**: opposite crossover, divergence forming, or histogram shrinking significantly

## Key Rules

- NEVER trade every crossover; most are false signals in ranging markets
- NEVER ignore zero line context; a bullish cross below zero is weaker than one above zero
- NEVER trade MACD against HTF trend direction
- Default settings: 12, 26, 9. Use 8, 17, 9 for day trading; 19, 39, 9 for swing trading.
- Histogram reversal is an early warning; crossover is the confirmation

## Related Skills

- **divergence-trading** — multi-indicator divergence framework that includes MACD
- **moving-average-crossover** — MACD is derived from EMAs; combine for confirmation
