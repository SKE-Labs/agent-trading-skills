---
name: flag-pennant
description: Define and test flag or pennant continuation shapes. Use when measuring an impulse, consolidation, closed-bar break, invalidation, and measured-move hypothesis.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
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
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<flag_date>)
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

Confirm declining volume during consolidation via `get_indicators(indicator_code="mfi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)`.

**Standard:** Enter on break of flag/pennant boundary with volume spike. Stop beyond opposite side.
**Conservative:** Wait for breakout + retest of boundary. Enter on bounce.
**Target:** Flagpole length projected from breakout point.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Lo, Mamaysky & Wang](https://www.nber.org/papers/w7613) supports objective pattern definitions and conditional testing rather than visual labels alone.

## Key Rules
- Quantify the pole with return divided by ATR and a maximum bar count; “looks impulsive” is not reproducible
- Define and calibrate the maximum retracement rather than assuming 50% is universal
- Treat volume contraction and breakout expansion as candidate filters; report their measured values
- Quick formations are more reliable than extended consolidations
- Flag duration should be short relative to the pole

## Related Skills
- **triangle-patterns** — Pennants are small symmetrical triangles
- **channel-trading** — Flags are short-duration trending channels
