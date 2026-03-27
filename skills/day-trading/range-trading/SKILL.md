---
name: range-trading
description: Buy support and sell resistance within ranging markets. Use when markets lack trend direction, trading consolidation, or identifying accumulation/distribution.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Range Trading

Profit from price oscillating between clear support and resistance in non-trending markets.

## Identification

### Range Characteristics

- Price bouncing between two levels with 2+ touches each side
- No clear HH/HL or LH/LL structure
- Volume decreasing during range
- Width at least 3% (narrower ranges are not worth trading)

### Range Quality

| Factor | Strong | Weak |
| --- | --- | --- |
| Bounces | Clean, multiple (3+) | Sloppy, few |
| Width | >3% | <3% |
| Duration | Multi-day/week | Few hours |
| Volume | Low, stable | Erratic |

## Workflow

### 1. Confirm Ranging Regime

```
get_indicator(indicator_code="dmi", symbol=<symbol>, interval=<interval>)
```

ADX <20 confirms ranging market. If ADX >25, this is a trend -- use momentum-trading or pullback-trading instead.

### 2. Identify Range Boundaries

```
get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
```

Find flat support/resistance with 2+ touches each side.

### 3. Mark Range Levels

```
draw_chart_analysis(action="create", drawing={
    "type": "support",
    "points": [
        {"time": <first_touch>, "price": <support_level>},
        {"time": <current>, "price": <support_level>}
    ],
    "options": {"text": "Range Support"}
})
draw_chart_analysis(action="create", drawing={
    "type": "resistance",
    "points": [
        {"time": <first_touch>, "price": <resistance_level>},
        {"time": <current>, "price": <resistance_level>}
    ],
    "options": {"text": "Range Resistance"}
})
```

### 4. Trade at Boundaries

- **Buy at support**: Wait for rejection candle (hammer, engulfing), stop below support, target resistance
- **Sell at resistance**: Wait for rejection candle (shooting star, engulfing), stop above resistance, target support
- Only enter in the outer 20% of range -- never trade the middle
- Target 70-80% of range width (not the full range)

### 5. Report to Orchestrator

Range boundaries, width, number of touches, entry recommendation, stop level, target level. Flag if breakout appears imminent.

## Key Rules

- NEVER trade the middle of a range -- only enter at support/resistance boundaries
- NEVER enter without a rejection candle confirmation
- If price closes beyond the range boundary, stop trading the range -- a breakout is underway
- Volume surge at a boundary signals potential breakout, not a range trade
- Watch for failed bounces (weak rejection) as a sign the range is ending

## Related Skills

- **breakout-trading** -- when the range breaks, switch to breakout strategy
- **momentum-trading** -- ADX rising above 25 signals transition from range to trend
