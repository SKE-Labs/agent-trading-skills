---
name: flag-pennant
description: Trade bull and bear flags and pennants for trend continuation. Use when riding strong trends, entering on pullbacks, or trading momentum breakouts.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Flag & Pennant Patterns

Continuation patterns that form during pauses in strong trends.

## Pattern Structure

**Components:** Flagpole (strong impulsive move) → Flag/Pennant (consolidation) → Breakout (continuation).

- **Bull Flag** — Strong upward pole, downward-sloping rectangular channel, breaks upward
- **Bear Flag** — Strong downward pole, upward-sloping rectangular channel, breaks downward
- **Pennant** — Strong move (pole), symmetrical triangle consolidation, breaks in pole direction

| Criteria | Flag | Pennant |
|----------|------|---------|
| Shape | Rectangular channel (2 parallel lines) | Symmetrical triangle (2 converging lines) |
| Slope | Against trend | Neutral |
| Volume | Decreasing | Decreasing |

## Workflow

### 1. Get Swing Point Data

Identify the flagpole and consolidation boundaries:

```
get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<flag_date>)
```

### 2. Draw Flag/Pennant Boundaries (2 parallel calls)

**For flags** (2 parallel trend lines sloping against the pole):

```
# Upper flag boundary
draw_chart_analysis(action="create", drawing={
    "type": "trend",
    "points": [
        {"time": <flag_high1_time>, "price": <flag_high1_price>},
        {"time": <flag_high2_time>, "price": <flag_high2_price>}
    ],
    "options": {"text": "Flag R"}
})

# Lower flag boundary (parallel to upper)
draw_chart_analysis(action="create", drawing={
    "type": "trend",
    "points": [
        {"time": <flag_low1_time>, "price": <flag_low1_price>},
        {"time": <flag_low2_time>, "price": <flag_low2_price>}
    ],
    "options": {"text": "Flag S"}
})
```

**For pennants:** same approach but lines converge (like a small symmetrical triangle).

### 3. Confirm and Enter

Confirm declining volume during consolidation via `get_indicator(indicator_code="mfi", symbol=<symbol>, interval=<interval>)`.

**Standard:** Enter on break of flag/pennant boundary with volume spike. Stop beyond opposite side.
**Conservative:** Wait for breakout + retest of boundary. Enter on bounce.
**Target:** Flagpole length projected from breakout point.

## Key Rules
- Pole must be strong and impulsive (3+ candles of directional momentum)
- NEVER trade a flag that retraces more than 50% of the pole — this invalidates the pattern
- NEVER enter without volume decline during formation + spike on breakout
- Quick formations are more reliable than extended consolidations
- Flag duration should be short relative to the pole

## Related Skills
- **triangle-patterns** — Pennants are small symmetrical triangles
- **channel-trading** — Flags are short-duration trending channels
