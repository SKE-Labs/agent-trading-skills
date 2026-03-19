---
name: stochastic-trading
description: Trade using Stochastic oscillator for overbought/oversold and momentum. Use when finding reversal points in ranges, confirming trend entries, or timing exits.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending", "ranging"]
---

# Stochastic Oscillator Trading

Stochastic measures momentum by comparing closing price to price range over a period.

## Components

| Line | Description               | Use            |
| ---- | ------------------------- | -------------- |
| %K   | Main line (fast)          | Primary signal |
| %D   | Signal line (3-SMA of %K) | Confirmation   |

## Key Levels

| Level | Meaning                     |
| ----- | --------------------------- |
| 80+   | Overbought (potential sell) |
| 20-   | Oversold (potential buy)    |
| 50    | Equilibrium                 |

## Trading Signals

### 1. Overbought/Oversold Reversals

- %K enters oversold (<20) then crosses above → Buy
- %K enters overbought (>80) then crosses below → Sell

### 2. %K/%D Crossover

- %K crosses above %D → Bullish
- %K crosses below %D → Bearish
- Most reliable in OB/OS zones

### 3. Divergence

- Price makes new high, stochastic makes lower high → Bearish
- Price makes new low, stochastic makes higher low → Bullish

### 4. Bull/Bear Setup

- **Bull**: %K above 50, rising → Bullish momentum
- **Bear**: %K below 50, falling → Bearish momentum

## Strategies by Market Type

### Ranging Markets

- Buy when stochastic exits oversold (<20 to >20)
- Sell when stochastic exits overbought (>80 to <80)
- Target opposite zone

### Trending Markets

- In uptrend: Buy on oversold (ignore overbought)
- In downtrend: Sell on overbought (ignore oversold)
- Stochastic can stay OB/OS in strong trends

## Settings

| Setting   | Fast | Slow |
| --------- | ---- | ---- |
| %K period | 5    | 14   |
| %D period | 3    | 3    |
| Smoothing | 3    | 3    |

- Fast: More signals, more noise
- Slow (14,3,3): Standard, smoother

## Workflow

1. **Get Stochastic** using `get_indicator(indicator="stoch")`
2. **Identify market** type (trending vs ranging)
3. **Apply appropriate strategy**
4. **Wait for confirmation** (%K/%D cross)
5. **Enter with stop** beyond recent swing

## Avoid These Mistakes

- Selling just because stochastic is overbought (can stay OB)
- Trading against strong trends
- Ignoring divergences

## Related Skills

- **rsi-divergence** — Stochastic divergence combined with RSI divergence strengthens reversal signals
- **bollinger-bands** — Stochastic overbought/oversold at BB extremes provides high-probability mean reversion entries
- **range-trading** — Stochastic is most reliable in ranging markets for timing boundary entries
