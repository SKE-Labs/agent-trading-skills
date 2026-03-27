---
name: double-top-bottom
description: Trade double and triple top/bottom reversal patterns. Use when identifying trend exhaustion, finding reversal entries at key resistance/support, or confirming failed breakouts.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Double Top & Bottom Patterns

Reversal patterns that form when price fails to break a level twice.

## Pattern Structure

### Double Top (Bearish)
1. Rally to resistance (Peak 1) → pullback to neckline → rally back to same resistance (Peak 2, within 3%) → failure → reversal

### Double Bottom (Bullish)
1. Drop to support (Trough 1) → bounce to neckline → drop back to same support (Trough 2, within 3%) → failure → reversal

| Factor | Strong | Weak |
|--------|--------|------|
| Time between tests | 2-4 weeks | Very close or far apart |
| Volume | Declining on 2nd test | Higher on 2nd test |
| Peak/trough alignment | Within 3% | Widely different |

## Workflow

### 1. Get Exact Data

```
get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<peak_date>)
```

### 2. Mark Peaks/Troughs (2 parallel highlight calls)

```
draw_chart_analysis(action="create", drawing={
    "type": "highlight",
    "points": [{"time": <peak1_time>, "price": <peak1_price>}],
    "options": {"text": "Peak 1"}
})

draw_chart_analysis(action="create", drawing={
    "type": "highlight",
    "points": [{"time": <peak2_time>, "price": <peak2_price>}],
    "options": {"text": "Peak 2"}
})
```

### 3. Draw Neckline

```
draw_chart_analysis(action="create", drawing={
    "type": "support",
    "points": [
        {"time": <neckline_start>, "price": <neckline_price>},
        {"time": <neckline_end>, "price": <neckline_price>}
    ],
    "options": {"text": "Neckline"}
})
```

For double top use `"support"` (neckline is below). For double bottom use `"resistance"` (neckline is above).

### 4. Enter

**Standard:** Enter on neckline break + close with volume. Stop beyond peaks/troughs.
**Preferred:** Wait for break + neckline retest. Enter on rejection.
**Aggressive:** Enter at second peak/trough with LTF reversal confirmation.
**Target:** Neckline ± (Peak - Neckline). Example: Peak $100, Neckline $90 → Target $80.

## Key Rules
- NEVER trade before neckline confirmation — pattern incomplete until it breaks
- NEVER ignore volume: declining volume on 2nd test validates the pattern
- Peaks/troughs must be within 3% to qualify
- Failed double tops/bottoms lead to strong continuation moves

## Related Skills
- **head-and-shoulders** — Similar reversal family
- **cup-and-handle** — Failed double bottoms can morph into cup patterns
