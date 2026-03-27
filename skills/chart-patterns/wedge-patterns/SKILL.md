---
name: wedge-patterns
description: Trade rising and falling wedge patterns for reversals and continuations. Use when spotting weakening trends, anticipating reversal moves, or identifying continuation patterns.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Wedge Pattern Trading

Converging trendlines sloping in the same direction, typically signaling reversals.

## Pattern Structure

### Rising Wedge (Mostly Bearish)
- Both lines slope **upward**, HH + HL but compressing
- In uptrend = reversal; in downtrend = continuation
- Breaks down ~68% of the time

### Falling Wedge (Mostly Bullish)
- Both lines slope **downward**, LH + LL but compressing
- In downtrend = reversal; in uptrend = continuation
- Breaks up ~68% of the time

| Feature | Wedge | Triangle |
|---------|-------|----------|
| Slopes | Both lines slope **same** direction | Lines converge from **opposite** directions |

## Workflow

### 1. Get Swing Point Data

```
get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<swing_date>)
```

### 2. Draw Wedge Boundaries (2 parallel calls)

Both trendlines slope in the same direction (this is what distinguishes a wedge from a triangle):

```
# Upper boundary (connecting highs — both slope upward for rising wedge)
draw_chart_analysis(action="create", drawing={
    "type": "trend",
    "points": [
        {"time": <high1_time>, "price": <high1_price>},
        {"time": <high2_time>, "price": <high2_price>}
    ],
    "options": {"text": "Wedge R"}
})

# Lower boundary (connecting lows — also slopes upward for rising wedge)
draw_chart_analysis(action="create", drawing={
    "type": "trend",
    "points": [
        {"time": <low1_time>, "price": <low1_price>},
        {"time": <low2_time>, "price": <low2_price>}
    ],
    "options": {"text": "Wedge S"}
})
```

### 3. Confirm and Enter

Confirm declining volume with `get_indicator(indicator_code="mfi", symbol=<symbol>, interval=<interval>)`.

**Standard:** Rising wedge → short on downside break. Falling wedge → long on upside break. Volume spike confirms. Stop beyond opposite boundary.
**Preferred:** Wait for breakout + retest of broken trendline. Enter on rejection.
**Target:** Height at widest part of wedge, projected from breakout.

## Key Rules
- Minimum 4 touch points (2 per line) to validate
- Both trendlines MUST slope in the same direction — otherwise it's a triangle
- NEVER ignore context: rising wedge in uptrend = reversal, in downtrend = continuation
- Wedges near the end of extended trends produce higher-probability reversals
- Decreasing volume during formation is essential for validity

## Related Skills
- **triangle-patterns** — Similar converging lines but different slope behavior
- **multi-timeframe-analysis** — HTF wedges signal major reversals
