---
name: triangle-patterns
description: Trade ascending, descending, and symmetrical triangle patterns. Use when anticipating breakouts from consolidation, measuring potential move targets, or timing entries on compression breakouts.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Triangle Pattern Trading

Triangles form during consolidation and typically break in the direction of the prevailing trend.

## Pattern Structure

### Ascending Triangle (Bullish Bias)
- Flat horizontal resistance + rising lows — usually breaks upward

### Descending Triangle (Bearish Bias)
- Flat horizontal support + lower highs — usually breaks downward

### Symmetrical Triangle (Neutral)
- Lower highs + higher lows, converging — breaks with prevailing trend

## Workflow

### 1. Get Swing Point Data

Identify at least 2 swing highs and 2 swing lows (4+ total touch points):

```
get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<swing_date>)
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

Check volume declining during formation via `get_indicator(indicator_code="mfi", symbol=<symbol>, interval=<interval>)`.

**Standard:** Enter on break + candle close outside triangle with volume spike. Stop inside triangle on opposite side.
**Preferred:** Wait for breakout, then retest of broken trendline. Enter on rejection.
**Target:** Triangle height at widest point, projected from breakout.

| Phase | Expected Volume |
|-------|----------------|
| Formation | Declining |
| Breakout | Spike |
| Continuation | Sustained |

## Key Rules
- Minimum 4 touch points (2 per trendline) to validate
- NEVER enter on a wick breakout alone — wait for candle close outside
- NEVER trade symmetrical triangles against the prevailing trend
- Breakouts in the final third (near apex) are more likely false
- Wider triangles produce stronger moves

## Related Skills
- **wedge-patterns** — Similar converging lines, both slope same direction
- **flag-pennant** — Pennants are small symmetrical triangles
