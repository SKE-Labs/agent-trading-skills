---
name: double-top-bottom
description: Trade double and triple top/bottom reversal patterns. Use when identifying trend exhaustion, finding reversal entries at key resistance/support, or confirming failed breakouts.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Double Top & Bottom Patterns

Reversal patterns that form when price fails to break a level twice.

## Pattern Structure

### Double Top (Bearish)
1. Rally to resistance (Peak 1) → pullback to neckline → retest the resistance within a predeclared price or ATR tolerance → failure

### Double Bottom (Bullish)
1. Drop to support (Trough 1) → bounce to neckline → retest the support within the same frozen tolerance → failure

| Factor | Strong | Weak |
|--------|--------|------|
| Time between tests | Within a predeclared bar window | Selected after seeing outcome |
| Volume | Declining on 2nd test | Higher on 2nd test |
| Peak/trough alignment | Within a volatility-normalized tolerance | Arbitrary visual match |

## Workflow

### 1. Get Exact Data

```
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<peak_date>)
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

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Lo, Mamaysky & Wang](https://www.nber.org/papers/w7613) found incremental information in some algorithmically defined patterns, including double bottoms, but did not establish universal thresholds or profits.

## Key Rules
- NEVER trade before neckline confirmation — pattern incomplete until it breaks
- Treat declining activity on the second test as context, not validation by itself
- Freeze the peak/trough tolerance and bar window before evaluating returns
- Failed double tops/bottoms lead to strong continuation moves

## Related Skills
- **head-and-shoulders** — Similar reversal family
- **cup-and-handle** — Failed double bottoms can morph into cup patterns
