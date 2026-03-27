---
name: breakout-trading
description: Trade consolidation breakouts with volume confirmation. Use when anticipating trend continuation, catching early moves, or trading pattern completions.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Breakout Trading

Captures explosive moves when price breaks out of consolidation zones or key support/resistance levels.

## Identification

Types: **Horizontal** (flat S/R, 3+ touches), **Pattern** (triangle/wedge/flag completion), **Trendline** (trend change signal).

### Volume Confirmation

| Volume vs 20-period Average | Signal |
| --- | --- |
| >2.0x | Strong -- high confidence |
| 1.5-2.0x | Valid -- normal confidence |
| 1.0-1.5x | Weak -- wait for confirmation |
| <1.0x | Likely false breakout -- skip |

Also require: candle **closes** beyond level (not just wick), follow-through for 3+ candles, RSI trending in breakout direction.

## Workflow

### 1. Identify Consolidation

```
get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
```

Look for tight range with 3+ touches on support/resistance.

### 2. Mark the Level

```
draw_chart_analysis(action="create", drawing={
    "type": "resistance",
    "points": [
        {"time": <first_touch_time>, "price": <level_price>},
        {"time": <current_time>, "price": <level_price>}
    ],
    "options": {"text": "Breakout Level (<price>)"}
})
```

### 3. Check Volume and Momentum

```
get_indicator(indicator_code="mfi", symbol=<symbol>, interval=<interval>)
get_indicator(indicator_code="rsi", symbol=<symbol>, interval=<interval>)
get_indicator(indicator_code="macd", symbol=<symbol>, interval=<interval>)
```

Breakout candle volume must be >1.5x 20-period average. RSI trending in breakout direction. MACD histogram expanding.

### 4. Entry and Target

Target = breakout level + consolidation height (measured move). **Aggressive**: enter on breakout candle close. **Conservative**: wait for retest (~65% retest within 5-10 candles). Stop below breakout level.

### 5. Report to Orchestrator

Breakout type, volume multiple, entry recommendation, measured move target, stop level, false breakout risk assessment.

## Key Rules

- NEVER enter without volume confirmation (>1.5x average) -- ~60% of breakouts fail
- NEVER trust a wick-only break -- require a candle close beyond the level
- If price returns inside range within 3 candles, exit immediately -- thesis invalidated
- If volume declines after breakout candle, tighten stop to breakeven
- Multiple failed breakouts at the same level means the level may be exhausted -- look elsewhere

## Related Skills

- **momentum-trading** -- ride the continuation after consolidation breaks
- **pullback-trading** -- time the retest entry after breakout
