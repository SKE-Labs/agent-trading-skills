---
name: macd-trading
description: Trade using MACD crossovers, histogram, and divergence signals. Use when confirming trend direction, timing entries with momentum, or identifying trend strength changes.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending"]
---

# MACD Trading Strategy

MACD (Moving Average Convergence Divergence) combines trend-following and momentum analysis.

## MACD Components

| Component       | Calculation     | Use                |
| --------------- | --------------- | ------------------ |
| **MACD Line**   | 12 EMA - 26 EMA | Trend direction    |
| **Signal Line** | 9 EMA of MACD   | Entry trigger      |
| **Histogram**   | MACD - Signal   | Momentum strength  |
| **Zero Line**   | Centerline      | Bull/bear boundary |

## Trading Signals

### 1. Crossover Signals

- **Bullish**: MACD crosses above Signal line → Buy
- **Bearish**: MACD crosses below Signal line → Sell

### 2. Zero Line Cross

- **MACD above zero**: Bullish trend
- **MACD below zero**: Bearish trend
- Cross of zero = trend change

### 3. Histogram Analysis

- **Growing histogram**: Increasing momentum
- **Shrinking histogram**: Weakening momentum
- Histogram reversal often precedes crossover

### 4. Divergence

- Price makes new high, MACD makes lower high → Bearish
- Price makes new low, MACD makes higher low → Bullish

## Strategy Workflow

1. **Get MACD** using `get_indicator(indicator="macd")`

2. **Determine trend** from zero line:

   - MACD > 0 = Look for longs
   - MACD < 0 = Look for shorts

3. **Wait for crossover** in trend direction:

   - Bullish cross above zero = Strong buy
   - Bearish cross below zero = Strong sell

4. **Confirm with histogram**:

   - Entry confirmed when histogram grows in direction

5. **Exit signals**:
   - Opposite crossover
   - Divergence forming
   - Histogram shrinking significantly

## Best Settings

| Timeframe | Settings  | Use Case      |
| --------- | --------- | ------------- |
| Default   | 12, 26, 9 | All-purpose   |
| Fast      | 8, 17, 9  | Day trading   |
| Slow      | 19, 39, 9 | Swing trading |

## Avoid These Mistakes

- Trading every crossover (many are false)
- Ignoring the zero line context
- Trading against HTF trend

## Related Skills

- **rsi-divergence** — RSI divergence combined with MACD divergence creates high-confidence reversal signals
- **divergence-trading** — Comprehensive multi-indicator divergence framework that includes MACD
- **momentum-trading** — MACD histogram expansion confirms momentum; use together for trend entries
