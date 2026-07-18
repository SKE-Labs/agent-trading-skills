---
name: channel-trading
description: Trade within ascending, descending, and horizontal channels. Use when range trading, riding trends with defined boundaries, or finding breakout setups.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Channel Trading

Channels define parallel price boundaries for trading bounces or anticipating breakouts.

## Pattern Structure

### Ascending Channel (Bullish)
- Both lines slope upward — buy at lower line, sell at upper
- Break below = reversal signal

### Descending Channel (Bearish)
- Both lines slope downward — sell at upper line, cover at lower
- Break above = reversal signal

### Horizontal Channel (Range)
- Parallel horizontal lines — classic range trading
- Break either direction = new trend

## Workflow

### 1. Get Swing Point Data

Fetch exact timestamps and prices for swing highs/lows (need 2+ per line):

```
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<swing_date>)
```

### 2. Draw the Channel (2 parallel trend lines)

Draw both channel boundaries as separate `trend` lines in parallel calls:

```
# Upper channel boundary (connecting swing highs)
draw_chart_analysis(action="create", drawing={
    "type": "trend",
    "points": [
        {"time": <high1_time>, "price": <high1_price>},
        {"time": <high2_time>, "price": <high2_price>}
    ],
    "options": {"text": "Channel R"}
})

# Lower channel boundary (connecting swing lows)
draw_chart_analysis(action="create", drawing={
    "type": "trend",
    "points": [
        {"time": <low1_time>, "price": <low1_price>},
        {"time": <low2_time>, "price": <low2_price>}
    ],
    "options": {"text": "Channel S"}
})
```

### 3. Confirm and Enter

**Channel Bounce:** Wait for price at boundary + reversal candle + RSI divergence via `get_indicators(indicator_code="rsi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)`. Stop beyond boundary.

**Channel Breakout:** Wait for candle close outside channel. Confirm with `get_indicators(indicator_code="mfi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)` for volume. Target = channel width projected from breakout. Mark breakout level:

```
draw_chart_analysis(action="create", drawing={
    "type": "breakout",
    "points": [
        {"time": <break_time>, "price": <break_price>},
        {"time": <target_time>, "price": <break_price>}
    ],
    "options": {"text": "Breakout"}
})
```

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Lo, Mamaysky & Wang](https://www.nber.org/papers/w7613) found that some objectively defined chart patterns contain incremental information, while emphasizing that visual pattern recognition is subjective.

## Key Rules
- Minimum 4 total touch points (2 per line) to validate a channel
- Trade WITH channel direction: buy support in ascending, sell resistance in descending
- Channel midline acts as interim S/R — price rejecting at midline signals weakening momentum
- Stop applying the fade rule after its predeclared closed-bar breakout invalidation.
- Record incomplete boundary traversals as a feature; do not declare weakening without tested evidence.

## Related Skills
- **multi-timeframe-analysis** — HTF channels define trend; LTF channels refine entries
- **triangle-patterns** — Converging channels become triangles
