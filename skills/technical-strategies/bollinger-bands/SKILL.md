---
name: bollinger-bands
description: Trade Bollinger Band squeezes, breakouts, and mean reversion. Use when measuring volatility, finding overbought/oversold conditions, or anticipating breakout moves.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["ranging", "volatile"]
---

# Bollinger Bands Trading

Bollinger Bands measure volatility and identify potential reversals and breakouts.

## Components

| Band       | Calculation    | Meaning               |
| ---------- | -------------- | --------------------- |
| **Middle** | 20 SMA         | Trend baseline        |
| **Upper**  | SMA + 2 StdDev | Resistance/overbought |
| **Lower**  | SMA - 2 StdDev | Support/oversold      |

## Trading Strategies

### 1. Mean Reversion (Range Trading)

Best in sideways markets:

- Price touches upper band → Look for short
- Price touches lower band → Look for long
- Target: Middle band (20 SMA)

### 2. Bollinger Squeeze (Breakout)

Low volatility precedes big moves:

1. Bands contract (narrow squeeze)
2. Wait for price to break out
3. Enter in breakout direction
4. Wide stop, target extended move

### 3. Band Riding (Trend Trading)

In strong trends, price rides a band:

- Uptrend: Price hugs upper band
- Downtrend: Price hugs lower band
- Entry on pullback to middle band

### 4. W-Bottom / M-Top Patterns

Double patterns at bands:

- W-Bottom at lower band = Bullish reversal
- M-Top at upper band = Bearish reversal

## Workflow

1. **Get Bollinger Bands** using `get_indicator(indicator="bbands")`

2. **Calculate band width** (volatility indicator):

```
execute(command='python3 -c "upper=105;lower=95;sma=100;width=(upper-lower)/sma*100;print(f\"Upper: {upper}\\nLower: {lower}\\nBand Width: {width:.2f}%\")"')
```

3. **Assess volatility**:

   - Narrow (<2%) = Low volatility, expect breakout
   - Wide (>4%) = High volatility, expect mean reversion

4. **Identify setup**:

   - At band edge with reversal candle → Mean reversion
   - Squeeze with volume → Breakout

5. **Execute with confirmation**:
   - Candle close outside band isn't enough
   - Wait for follow-through or reversal signal

## Key Rules

| Condition                     | Strategy             |
| ----------------------------- | -------------------- |
| Bands expanding               | Trade breakouts      |
| Bands contracting             | Prepare for squeeze  |
| Price at upper band + RSI >70 | Mean reversion short |
| Price at lower band + RSI <30 | Mean reversion long  |

## Settings

- Default: 20 SMA, 2 standard deviations
- More signals: 10 period, 1.5 StdDev
- Fewer signals: 50 period, 2.5 StdDev

## Related Skills

- **mean-reversion** — Bollinger Band touches are a primary mean reversion entry signal; combine with z-score and RSI
- **market-regime-detection** — BB Width is a key volatility input for regime classification
- **stochastic-trading** — Stochastic overbought/oversold at BB extremes provides strong confluence
