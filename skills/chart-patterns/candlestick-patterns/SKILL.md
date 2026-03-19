---
name: candlestick-patterns
description: Identify key reversal and continuation candlestick patterns. Use when timing entries/exits, confirming price action signals, or finding reversal confirmation at key levels.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Candlestick Pattern Trading

Candlestick patterns provide visual entry/exit signals based on price action psychology.

## Reversal Patterns (Single Candle)

### Hammer / Hanging Man

- Small body, long lower wick (2x+ body)
- Hammer at support = Bullish
- Hanging Man at resistance = Bearish

### Inverted Hammer / Shooting Star

- Small body, long upper wick (2x+ body)
- Inverted Hammer at support = Bullish
- Shooting Star at resistance = Bearish

### Doji

- Open = Close (tiny body)
- Shows indecision
- Reversal when at extremes

## Reversal Patterns (Multi-Candle)

### Engulfing

- **Bullish Engulfing**: Green candle completely engulfs prior red
- **Bearish Engulfing**: Red candle completely engulfs prior green
- Strongest reversal pattern

### Piercing Line / Dark Cloud Cover

- Second candle opens gap, closes 50%+ into prior candle
- Piercing (bullish) at support
- Dark Cloud (bearish) at resistance

### Morning Star / Evening Star

- 3-candle pattern
- Morning Star: Red, small/doji, green (bullish)
- Evening Star: Green, small/doji, red (bearish)

## Continuation Patterns

### Three White Soldiers / Three Black Crows

- Three consecutive strong candles
- Same direction, each closing higher/lower
- Strong trend continuation

### Rising/Falling Three Methods

- 5-candle pause-and-continue pattern
- Strong candle → 3 small opposite → Strong candle
- Trend continuation after pause

## Entry Workflow

1. **Identify key level** (S/R, supply/demand)
2. **Wait for pattern** to form at level
3. **Confirm direction** matches HTF bias
4. **Enter on next candle** open or on break
5. **Stop loss** beyond pattern's extreme
6. **Target** next key level

## Pattern Strength Ranking

| Strength | Patterns                        |
| -------- | ------------------------------- |
| High     | Engulfing, Morning/Evening Star |
| Medium   | Hammer, Shooting Star           |
| Lower    | Doji, Piercing/Dark Cloud       |

## Best Practices

- Patterns at key levels are most reliable
- Combine with other confluence
- Higher timeframe patterns are stronger
- Confirmation (next candle) reduces false signals

## Reference

See [references/PATTERNS.md](references/PATTERNS.md) for visual pattern diagrams.

## Related Skills

- **multi-timeframe-analysis** — HTF candlestick patterns are far more reliable; always confirm with higher timeframe context
- **supply-demand-zones** — Candlestick reversal patterns at supply/demand zones create the highest-probability entries
- **position-sizing** — Use risk management to size trades based on the pattern's stop distance
