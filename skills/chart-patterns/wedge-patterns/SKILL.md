---
name: wedge-patterns
description: Define and test rising or falling wedge resolutions. Use when fitting same-direction converging boundaries and evaluating breakout, retest, invalidation, and measured-move rules.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Wedge Pattern Trading

Converging boundaries sloping in the same direction. Reversal versus continuation behavior depends on the specification, context, market, and sample.

## Pattern Structure

### Rising Wedge (Conventionally Bearish)
- Both lines slope **upward**, HH + HL but compressing
- In uptrend = reversal; in downtrend = continuation
- Treat downside resolution as a hypothesis and wait for confirmation

### Falling Wedge (Conventionally Bullish)
- Both lines slope **downward**, LH + LL but compressing
- In downtrend = reversal; in uptrend = continuation
- Treat upside resolution as a hypothesis and wait for confirmation

| Feature | Wedge | Triangle |
|---------|-------|----------|
| Slopes | Both lines slope **same** direction | Lines converge from **opposite** directions |

## Workflow

### 1. Get Swing Point Data

```
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<swing_date>)
```

### 2. Draw Wedge Boundaries (2 parallel calls)

Both trendlines slope in the same direction (this is what distinguishes a wedge from a triangle):

```
# Upper boundary (connecting highs — both slope upward for rising wedge)
draw_chart_analysis(action="create", drawing={
    "type": "trend",
    "points": [
        {"time": <high1_time>, "price": <high1_price>},
        {"time": <high2_time>, "price": <high2_price>}
    ],
    "options": {"text": "Wedge R"}
})

# Lower boundary (connecting lows — also slopes upward for rising wedge)
draw_chart_analysis(action="create", drawing={
    "type": "trend",
    "points": [
        {"time": <low1_time>, "price": <low1_price>},
        {"time": <low2_time>, "price": <low2_price>}
    ],
    "options": {"text": "Wedge S"}
})
```

### 3. Confirm and Enter

Confirm declining volume with `get_indicators(indicator_code="mfi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)`.

**Standard:** Rising wedge → short on downside break. Falling wedge → long on upside break. Volume spike confirms. Stop beyond opposite boundary.
**Preferred:** Wait for breakout + retest of broken trendline. Enter on rejection.
**Target:** Height at widest part of wedge, projected from breakout.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Lo, Mamaysky & Wang](https://www.nber.org/papers/w7613) supports making visual patterns algorithmic and testing them conditionally; it does not support a fixed breakout probability.

## Key Rules
- Minimum 4 touch points (2 per line) to validate
- Both trendlines MUST slope in the same direction — otherwise it's a triangle
- Record preceding direction and test reversal/continuation outcomes separately; context does not determine the result.
- Define “extended trend” and volume contraction quantitatively if they are used as filters

## Related Skills
- **triangle-patterns** — Similar converging lines but different slope behavior
- **multi-timeframe-analysis** — HTF wedges signal major reversals
