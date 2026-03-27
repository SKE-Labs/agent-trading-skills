---
name: cup-and-handle
description: Trade cup and handle breakout patterns for bullish continuation. Use when identifying accumulation patterns, finding breakout setups, or timing entries on established stocks/crypto.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Cup and Handle Pattern

Bullish continuation pattern indicating accumulation before a breakout.

## Pattern Structure

### The Cup
- Price rounds down from resistance, forms a "U" shaped bottom (not "V"), rises back to resistance
- Duration: 7-65 weeks (classic), or scaled for crypto/lower timeframes

### The Handle
- Small pullback from resistance into a declining flag/pennant
- Should retrace 10-15% of cup depth (up to 33% acceptable)
- Must stay in upper half of cup

| Factor | Ideal | Acceptable |
|--------|-------|------------|
| Cup shape | Rounded "U" | Slightly V-shaped |
| Handle depth | 10-15% of cup | Up to 33% |
| Volume | Decreasing in handle | Stable |

## Workflow

### 1. Get Exact Data

```
get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<cup_bottom_date>)
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

## Key Rules
- NEVER enter before the handle forms — cup alone is incomplete
- NEVER trust a handle that drops below 50% of cup depth — invalidates pattern
- Volume must decline in handle and spike on breakout
- Failure at lip on second attempt = potential double top, not cup and handle

## Related Skills
- **flag-pennant** — The handle is essentially a small flag
- **double-top-bottom** — Failed cup breakouts can become double tops
