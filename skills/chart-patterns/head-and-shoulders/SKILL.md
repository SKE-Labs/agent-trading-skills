---
name: head-and-shoulders
description: Define and test head-and-shoulders or inverse patterns. Use when measuring objective pivots, neckline breaks/retests, symmetry, invalidation, and measured-move outcomes.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Head and Shoulders Pattern

A conventional reversal shape following a prior trend. The neckline break and target remain hypotheses whose conditional outcomes must be measured.

## Pattern Structure

### H&S (Bearish Reversal)
1. **Left Shoulder** — Rally to new high, pullback
2. **Head** — Higher high than left shoulder, pullback
3. **Right Shoulder** — Lower high than head, starts to drop
4. **Neckline** — Connect the two pullback lows

### Inverse H&S (Bullish Reversal)
1. **Left Shoulder** — Drop to new low, bounce
2. **Head** — Lower low, bounce
3. **Right Shoulder** — Higher low, starts to rise
4. **Neckline** — Connect the two bounce highs

| Criteria | Requirement |
|----------|-------------|
| Activity | Compare right-shoulder volume with the left using a predeclared statistic |
| Symmetry | Shoulders roughly equal height |
| Prior trend | Must have existing trend to reverse |

## Workflow

### 1. Get Exact Data

```
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<head_date>)
```

### 2. Mark Structure Points (3 parallel highlight calls)

```
draw_chart_analysis(action="create", drawing={
    "type": "highlight",
    "points": [{"time": <ls_time>, "price": <ls_price>}],
    "options": {"text": "LS"}
})

draw_chart_analysis(action="create", drawing={
    "type": "highlight",
    "points": [{"time": <head_time>, "price": <head_price>}],
    "options": {"text": "Head"}
})

draw_chart_analysis(action="create", drawing={
    "type": "highlight",
    "points": [{"time": <rs_time>, "price": <rs_price>}],
    "options": {"text": "RS"}
})
```

### 3. Draw Neckline

```
draw_chart_analysis(action="create", drawing={
    "type": "support",
    "points": [
        {"time": <neckline_left_time>, "price": <neckline_left_price>},
        {"time": <neckline_right_time>, "price": <neckline_right_price>}
    ],
    "options": {"text": "Neckline"}
})
```

For inverse H&S, use `"resistance"` instead of `"support"`.

### 4. Enter

**Standard:** Enter on neckline break + close with volume. Stop above right shoulder.
**Preferred:** Wait for neckline break, then retest. Enter on rejection. Tighter stop.
**Target:** Head-to-neckline distance projected from break point.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Lo, Mamaysky & Wang](https://www.nber.org/papers/w7613) studied algorithmic head-and-shoulders recognition and found conditional information in some samples, not a guaranteed reversal.

## Key Rules
- NEVER trade before neckline break — pattern incomplete until confirmed
- Volume differences are contextual and do not validate the pattern without a neckline break
- Must have a prior trend to reverse; H&S in a range is invalid
- Record shoulder-height asymmetry rather than assuming a lower right shoulder always increases expectancy

## Related Skills
- **double-top-bottom** — Similar reversal family
- **multi-timeframe-analysis** — HTF H&S signals major reversals
