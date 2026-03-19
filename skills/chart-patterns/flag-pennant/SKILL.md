---
name: flag-pennant
description: Trade bull and bear flags and pennants for trend continuation. Use when riding strong trends, entering on pullbacks, or trading momentum breakouts.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending"]
---

# Flag & Pennant Patterns

Flags and pennants are continuation patterns that form during pauses in strong trends.

## Pattern Components

1. **Flagpole**: The strong impulsive move before the pattern
2. **Flag/Pennant**: The consolidation (the pattern itself)
3. **Breakout**: Continuation in direction of flagpole

## Pattern Types

### Bull Flag

- Strong upward move (pole)
- Downward sloping channel (flag)
- Breaks upward to continue

### Bear Flag

- Strong downward move (pole)
- Upward sloping channel (flag)
- Breaks downward to continue

### Pennant (Bull or Bear)

- Strong move (pole)
- Symmetrical triangle consolidation
- Breaks in direction of pole

## Identification Criteria

| Criteria | Flag                | Pennant           |
| -------- | ------------------- | ----------------- |
| Shape    | Rectangular channel | Triangle          |
| Duration | Short (1-3 weeks)   | Short (1-3 weeks) |
| Volume   | Decreasing          | Decreasing        |
| Slope    | Against trend       | Neutral           |

## Entry Strategies

### 1. Breakout Entry

- Enter on break of flag/pennant boundary
- Confirm with volume increase
- Stop: Below/above flag structure

### 2. Conservative Entry

- Wait for breakout
- Wait for brief retest
- Enter on bounce from pattern boundary

## Target Calculation

**Flagpole Projection**:

```
Target = Breakout point + Flagpole length
```

Measure the pole, add to breakout level.

## Chart Drawing

Use `draw_chart_analysis`:

- For flags: Draw 2 parallel `trend` lines (channel)
- For pennants: Draw 2 converging `trend` lines

## Best Practices

- Pole should be strong and impulsive (3+ candles)
- Flag should retrace 38-50% of pole max
- Volume should decline during flag formation
- Breakout should have increased volume
- Quick formations are more reliable

## Related Skills

- **multi-timeframe-analysis** — Flags/pennants on primary TF within an HTF trend are the highest-probability continuation setups
- **momentum-trading** — Flags form during momentum pauses; the breakout resumes the momentum move
- **position-sizing** — Flagpole projection provides clear targets for R:R-based position sizing
