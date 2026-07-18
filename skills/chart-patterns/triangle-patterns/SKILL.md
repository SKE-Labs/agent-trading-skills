---
name: triangle-patterns
description: Trade ascending, descending, and symmetrical triangle patterns. Use when anticipating breakouts from consolidation, measuring potential move targets, or timing entries on compression breakouts.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Triangle Pattern Trading

Triangles describe converging swing boundaries. Treat breakout direction as unknown until price closes beyond a boundary.

## Pattern Structure

### Ascending Triangle (Bullish Bias)
- Flat horizontal resistance + rising lows — bullish bias is a hypothesis

### Descending Triangle (Bearish Bias)
- Flat horizontal support + lower highs — bearish bias is a hypothesis

### Symmetrical Triangle (Neutral)
- Lower highs + higher lows, converging — condition results on trend rather than assuming direction

## Workflow

### 1. Get Swing Point Data

Identify at least 2 swing highs and 2 swing lows (4+ total touch points):

```
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<swing_date>)
```

### 2. Draw Converging Trendlines (2 parallel calls)

```
# Upper trendline (connecting swing highs)
draw_chart_analysis(action="create", drawing={
    "type": "trend",
    "points": [
        {"time": <high1_time>, "price": <high1_price>},
        {"time": <high2_time>, "price": <high2_price>}
    ],
    "options": {"text": "Triangle R"}
})

# Lower trendline (connecting swing lows)
draw_chart_analysis(action="create", drawing={
    "type": "trend",
    "points": [
        {"time": <low1_time>, "price": <low1_price>},
        {"time": <low2_time>, "price": <low2_price>}
    ],
    "options": {"text": "Triangle S"}
})
```

For ascending: upper line is flat (`resistance` type instead of `trend`). For descending: lower line is flat (`support` type).

### 3. Confirm and Enter

Check volume declining during formation via `get_indicators(indicator_code="mfi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)`.

**Standard:** Enter on break + candle close outside triangle with volume spike. Stop inside triangle on opposite side.
**Preferred:** Wait for breakout, then retest of broken trendline. Enter on rejection.
**Target:** Triangle height at widest point, projected from breakout.

| Phase | Expected Volume |
|-------|----------------|
| Formation | Declining |
| Breakout | Spike |
| Continuation | Sustained |

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Lo, Mamaysky & Wang](https://www.nber.org/papers/w7613) supports systematic pattern recognition; direction, breakout buffer, and target rules still require out-of-sample calibration.

## Key Rules
- Minimum 4 touch points (2 per trendline) to validate
- NEVER enter on a wick breakout alone — wait for candle close outside
- If using trend direction or apex timing as filters, freeze their definitions and verify their incremental net expectancy
- Report width in ATR units and breakout location as a fraction of time-to-apex; do not infer strength from width alone

## Related Skills
- **wedge-patterns** — Similar converging lines, both slope same direction
- **flag-pennant** — Pennants are small symmetrical triangles
