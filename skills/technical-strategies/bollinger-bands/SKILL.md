---
name: bollinger-bands
description: Trade Bollinger Band squeezes, breakouts, and mean reversion. Use when measuring volatility, finding overbought/oversold conditions, or anticipating breakout moves.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Bollinger Bands Trading

Bollinger Bands measure volatility and identify potential reversals and breakouts.

## Components

| Band       | Calculation    | Meaning               |
| ---------- | -------------- | --------------------- |
| **Middle** | 20 SMA         | Trend baseline        |
| **Upper**  | SMA + 2 StdDev | Resistance/overbought |
| **Lower**  | SMA - 2 StdDev | Support/oversold      |

**Band Width** = `(Upper - Lower) / Middle * 100`

## Signals

### Mean Reversion (Range Trading)

- Price touches upper band + RSI >70 → look for short toward middle band
- Price touches lower band + RSI <30 → look for long toward middle band
- Requires confirmation candle (engulfing, hammer, pin bar)

### Bollinger Squeeze (Breakout)

- Band Width <2% = low volatility, breakout imminent
- Wait for price to close outside band with volume
- Enter in breakout direction, target extended move

### Band Riding (Trend Trading)

- Uptrend: price hugs upper band, pullbacks to middle band are entries
- Downtrend: price hugs lower band, rallies to middle band are entries

### W-Bottom / M-Top

- W-Bottom at lower band = bullish reversal
- M-Top at upper band = bearish reversal

## Workflow

1. **Get Bollinger Bands**:
   ```
   get_indicator(indicator_code="bbands", symbol=<symbol>, interval=<interval>)
   ```

2. **Calculate Band Width**: `(Upper - Lower) / Middle * 100`
   - Narrow (<2%) → expect breakout
   - Wide (>4%) → expect mean reversion

3. **Confirm with RSI**:
   ```
   get_indicator(indicator_code="rsi", symbol=<symbol>, interval=<interval>)
   ```

4. **Identify setup**: band edge + reversal candle → mean reversion; squeeze + volume → breakout

5. **Mark on chart**:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "highlight",
       "points": [
           {"time": <start_time>, "price": <upper_band>},
           {"time": <end_time>, "price": <lower_band>}
       ],
       "options": {"text": "BB Squeeze (Width: 1.8%)"}
   })
   ```

## Key Rules

- NEVER trade mean reversion when Band Width is expanding (trend in progress)
- NEVER enter on band touch alone; require confirmation candle + RSI extreme
- Band Width <2% signals squeeze; prepare for breakout, not mean reversion
- Default settings: 20 SMA, 2 StdDev. Use 10/1.5 for more signals, 50/2.5 for fewer
- A close outside the band is not a signal by itself; wait for follow-through or reversal

## Related Skills

- **mean-reversion** — adds z-score and RSI frameworks to BB touch signals
- **market-regime-detection** — BB Width is a key volatility input for regime classification
