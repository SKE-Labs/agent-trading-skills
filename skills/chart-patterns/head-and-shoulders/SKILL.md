---
name: head-and-shoulders
description: Identify and trade head and shoulders reversal patterns. Use when spotting major trend reversals, validating bearish/bullish structure changes, or finding high R:R reversal setups.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Head and Shoulders Pattern

Reliable reversal pattern signaling the end of an uptrend (or downtrend for inverse).

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
| Volume | Decreasing on right shoulder |
| Symmetry | Shoulders roughly equal height |
| Prior trend | Must have existing trend to reverse |

## Workflow

### 1. Get Exact Data

```
get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<head_date>)
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

## Key Rules
- NEVER trade before neckline break — pattern incomplete until confirmed
- NEVER ignore volume: declining volume on right shoulder validates weakness
- Must have a prior trend to reverse; H&S in a range is invalid
- Right shoulder failure (doesn't reach LS height) strengthens bearish case

## Related Skills
- **double-top-bottom** — Similar reversal family
- **multi-timeframe-analysis** — HTF H&S signals major reversals
