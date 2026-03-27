---
name: stochastic-trading
description: Trade using Stochastic oscillator for overbought/oversold and momentum. Use when finding reversal points in ranges, confirming trend entries, or timing exits.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
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

- %K enters oversold (<20) then crosses above → buy
- %K enters overbought (>80) then crosses below → sell

### %K/%D Crossover

- %K crosses above %D → bullish (most reliable in OB/OS zones)
- %K crosses below %D → bearish

### Divergence

- Price new high + Stochastic lower high → bearish
- Price new low + Stochastic higher low → bullish

### Momentum

- %K above 50 and rising → bullish momentum
- %K below 50 and falling → bearish momentum

## Market-Specific Strategies

### Ranging Markets
- Buy when Stochastic exits oversold (<20 → >20)
- Sell when Stochastic exits overbought (>80 → <80)
- Target: opposite zone

### Trending Markets
- Uptrend: buy on oversold only (ignore overbought — Stochastic can stay OB in strong trends)
- Downtrend: sell on overbought only (ignore oversold)

## Workflow

1. **Get Stochastic**:
   ```
   get_indicator(indicator_code="stoch", symbol=<symbol>, interval=<interval>)
   ```

2. **Determine market type** (trending vs ranging) to select strategy

3. **Check for %K/%D cross** in OB/OS zone

4. **Confirm with candle data**:
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```

5. **Enter with confirmation** candle; stop beyond recent swing

## Key Rules

- NEVER sell just because Stochastic is overbought; in strong trends it stays OB for extended periods
- NEVER trade Stochastic divergence in mid-range (20-80); only valid at extremes
- NEVER trade against strong trends; use Stochastic only for pullback entries in trend direction
- Settings: slow (14,3,3) is standard; fast (5,3,3) gives more signals but more noise

## Related Skills

- **rsi-divergence** — Stochastic divergence + RSI divergence together strengthens reversal signals
- **bollinger-bands** — Stochastic OB/OS at BB extremes provides high-probability mean reversion entries
