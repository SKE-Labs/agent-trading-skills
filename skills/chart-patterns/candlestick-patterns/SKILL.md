---
name: candlestick-patterns
description: Identify key reversal and continuation candlestick patterns. Use when timing entries/exits, confirming price action signals, or finding reversal confirmation at key levels.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Candlestick Pattern Trading

Candlestick patterns provide visual entry/exit signals based on price action psychology.

## Pattern Identification

### Single-Candle Reversals
- **Hammer / Hanging Man** — Small body, long lower wick (2x+ body). Hammer at support = bullish; Hanging Man at resistance = bearish.
- **Inverted Hammer / Shooting Star** — Small body, long upper wick (2x+ body). Inverted Hammer at support = bullish; Shooting Star at resistance = bearish.
- **Doji** — Open ≈ Close (tiny body). Indecision; reversal signal at extremes.

### Multi-Candle Reversals
- **Engulfing** — Bullish: green engulfs prior red. Bearish: red engulfs prior green. Strongest single reversal signal.
- **Piercing Line / Dark Cloud Cover** — Second candle opens gap, closes 50%+ into prior candle.
- **Morning Star / Evening Star** — 3-candle: large, small/doji, large opposite direction.

### Continuation
- **Three White Soldiers / Three Black Crows** — Three consecutive strong candles closing progressively higher/lower.

| Strength | Patterns |
|----------|----------|
| High | Engulfing, Morning/Evening Star |
| Medium | Hammer, Shooting Star |
| Lower | Doji, Piercing/Dark Cloud |

## Workflow

### 1. Identify Key Level

Use `get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)` to find S/R levels from price action (swing highs/lows, prior rejection zones).

### 2. Confirm Pattern at Level

Wait for a candlestick pattern to form at the key level. Confirm:
- Direction matches HTF bias
- Volume context via `get_indicator(indicator_code="mfi", symbol=<symbol>, interval=<interval>)`

### 3. Mark Key Candles

```
draw_chart_analysis(action="create", drawing={
    "type": "highlight",
    "points": [{"time": <pattern_candle_time>, "price": <pattern_candle_high>}],
    "options": {"text": "Engulfing"}
})
```

### 4. Enter

Enter on next candle open or break of pattern extreme. Stop beyond pattern's extreme wick. Target the next key S/R level.

## Key Rules
- NEVER trade a pattern in isolation — require a key level (S/R, supply/demand zone) as confluence
- NEVER trust a pattern without HTF directional alignment
- NEVER rely on doji alone — requires adjacent candle confirmation
- HTF patterns carry far more weight than LTF
- Engulfing is strongest when body exceeds prior candle's full range (wicks included)
- Morning/Evening Stars require 3rd candle to close beyond midpoint of 1st candle

## Related Skills
- **multi-timeframe-analysis** — HTF patterns far more reliable
- **supply-demand-zones** — Best confluence for reversal patterns
