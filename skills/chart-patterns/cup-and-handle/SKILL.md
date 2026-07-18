---
name: cup-and-handle
description: Define and test cup-and-handle breakout shapes. Use when measuring a rounded base, handle depth, lip break, retest, invalidation, and measured-move hypothesis without inferring accumulation.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Cup and Handle Pattern

A conventionally bullish continuation shape. Treat its geometry, breakout direction, and measured move as testable hypotheses rather than evidence of accumulation.

## Pattern Structure

### The Cup
- Price rounds down from resistance, forms a "U" shaped bottom (not "V"), rises back to resistance
- Duration and symmetry are market- and timeframe-specific; define minimum and maximum bars before scanning

### The Handle
- Small pullback from resistance into a declining flag/pennant
- Define handle depth as `(lip - handle_low) / (lip - cup_low)` and reject only at a pretested threshold
- Require the handle to remain above the cup midpoint only if that rule is part of the frozen specification

| Factor | Preferred seed definition | Alternative to test |
|--------|-------|------------|
| Cup shape | Rounded "U" | Slightly V-shaped |
| Handle depth | Shallow relative to cup | Predeclare a tested maximum |
| Volume | Decreasing in handle | Stable |

## Workflow

### 1. Get Exact Data

```
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<cup_bottom_date>)
```

### 2. Mark Key Structure

**Cup lip** (resistance level where both sides of the cup meet):

```
draw_chart_analysis(action="create", drawing={
    "type": "resistance",
    "points": [
        {"time": <left_lip_time>, "price": <lip_price>},
        {"time": <right_lip_time>, "price": <lip_price>}
    ],
    "options": {"text": "Lip"}
})
```

**Cup bottom:**

```
draw_chart_analysis(action="create", drawing={
    "type": "highlight",
    "points": [{"time": <bottom_time>, "price": <bottom_price>}],
    "options": {"text": "Cup Low"}
})
```

**Handle boundaries** (2 converging or parallel trend lines):

```
draw_chart_analysis(action="create", drawing={
    "type": "trend",
    "points": [
        {"time": <handle_high1_time>, "price": <handle_high1>},
        {"time": <handle_high2_time>, "price": <handle_high2>}
    ],
    "options": {"text": "Handle R"}
})

draw_chart_analysis(action="create", drawing={
    "type": "trend",
    "points": [
        {"time": <handle_low1_time>, "price": <handle_low1>},
        {"time": <handle_low2_time>, "price": <handle_low2>}
    ],
    "options": {"text": "Handle S"}
})
```

### 3. Enter

**Standard:** Enter on break above cup lip with volume spike. Stop below handle low.
**Aggressive:** Enter as handle finds support. Tighter stop, higher risk.
**Conservative:** Wait for breakout + retest of lip (now support).
**Target:** Breakout level + cup depth (lip to bottom distance).

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Lo, Mamaysky & Wang](https://www.nber.org/papers/w7613) supports testing objectively defined chart patterns, not assuming that a named shape has a universal measured-move edge.

## Key Rules
- NEVER enter before the handle forms — cup alone is incomplete
- Treat a break below the cup midpoint as structural invalidation only when the chosen specification says so
- Measure relative volume during the handle and breakout; do not require an untested universal multiple
- Failure at lip on second attempt = potential double top, not cup and handle

## Related Skills
- **flag-pennant** — The handle is essentially a small flag
- **double-top-bottom** — Failed cup breakouts can become double tops
