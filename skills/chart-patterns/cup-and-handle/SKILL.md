---
name: cup-and-handle
description: Trade cup and handle breakout patterns for bullish continuation. Use when identifying accumulation patterns, finding breakout setups, or timing entries on established stocks/crypto.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending"]
---

# Cup and Handle Pattern

Cup and handle is a bullish continuation pattern indicating accumulation before a breakout.

## Pattern Structure

### The Cup

1. Price rounds down from resistance
2. Forms a "U" shaped bottom (not "V")
3. Rises back to the resistance level
4. Duration: 7-65 weeks (classic) or scaled for crypto

### The Handle

1. Price pulls back from resistance
2. Forms small flag or pennant (declining)
3. Should retrace 10-15% of cup depth
4. Duration: 1-4 weeks

### The Breakout

1. Price breaks above resistance (cup lip)
2. Confirmation with volume
3. Target based on cup depth

## Validation Criteria

| Factor          | Ideal                | Acceptable        |
| --------------- | -------------------- | ----------------- |
| Cup shape       | Rounded "U"          | Slightly V-shaped |
| Handle depth    | 10-15% of cup        | Up to 33% of cup  |
| Volume          | Decreasing in handle | Stable            |
| Handle position | Upper half of cup    | Not below 50%     |
| Prior uptrend   | Yes                  | At least flat     |

## Entry Strategies

### 1. Breakout Entry

- Enter on break above cup resistance (lip)
- Volume should spike
- Stop: Below handle low

### 2. Handle Entry (Aggressive)

- Enter as handle forms support
- Tighter stop, better R:R
- Risk: May break down

### 3. Confirmation Entry

- Wait for breakout
- Wait for retest of resistance (now support)
- Enter on bounce

## Target Calculation

**Measured Move**:

```
Target = Breakout level + Cup depth
```

Measure from cup lip to cup bottom, add to breakout.

## Chart Marking

Use `draw_chart_analysis`:

- Mark cup lip with `resistance`
- Mark cup bottom with `support`
- Mark handle with `trend` lines

## Key Points

- Pattern works on all timeframes
- Volume pattern is crucial (high at breakout)
- Handle should not drop below 50% of cup
- Failure at lip = Potential double top instead

## Related Skills

- **multi-timeframe-analysis** — Cup and handle patterns on HTF carry more significance; confirm with LTF entry timing
- **breakout-trading** — The cup lip breakout follows breakout trading principles for volume confirmation and entry
- **position-sizing** — Size the trade based on stop distance below the handle low
