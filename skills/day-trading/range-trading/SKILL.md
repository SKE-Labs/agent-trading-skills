---
name: range-trading
description: Define and test trades near objective range boundaries. Use when measuring range width versus ATR/costs, rejection triggers, breakout invalidation, and target logic without inferring accumulation.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Range Trading

Profit from price oscillating between clear support and resistance in non-trending markets.

## Identification

### Range Characteristics

- Price bouncing between two levels with 2+ touches each side
- No clear HH/HL or LH/LL structure
- Volume decreasing during range
- Width large enough that the planned payoff exceeds round-trip costs and slippage

### Range Quality

| Factor | Strong | Weak |
| --- | --- | --- |
| Bounces | Clean, multiple (3+) | Sloppy, few |
| Width | Wide relative to ATR and costs | Too narrow after costs |
| Duration | Multi-day/week | Few hours |
| Volume | Low, stable | Erratic |

## Workflow

### 1. Confirm Ranging Regime

```
get_indicators(indicator_code="dmi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
```

Use ADX level/slope as one contextual feature, calibrated to the instrument and timeframe. It does not by itself confirm a range or authorize another strategy.

### 2. Identify Range Boundaries

```
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
```

Find flat support/resistance with 2+ touches each side.

### 3. Mark Range Levels

```
draw_chart_analysis(action="create", drawing={
    "type": "support",
    "points": [
        {"time": <first_touch>, "price": <support_level>},
        {"time": <current>, "price": <support_level>}
    ],
    "options": {"text": "Range Support"}
})
draw_chart_analysis(action="create", drawing={
    "type": "resistance",
    "points": [
        {"time": <first_touch>, "price": <resistance_level>},
        {"time": <current>, "price": <resistance_level>}
    ],
    "options": {"text": "Range Resistance"}
})
```

### 4. Trade at Boundaries

- **Buy at support**: Wait for rejection candle (hammer, engulfing), stop below support, target resistance
- **Sell at resistance**: Wait for rejection candle (shooting star, engulfing), stop above resistance, target support
- Define the boundary band as an ATR- or range-normalized interval fixed before testing
- Set the target from tested exit logic and require positive payoff after costs; the opposite boundary is a scenario, not a promised destination

### 5. Report to Orchestrator

Range boundaries, width, number of touches, entry recommendation, stop level, target level. Flag if breakout appears imminent.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: The [technical-analysis evidence review](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID603481_code17745.pdf?abstractid=603481) supports market-specific testing and warns that rule selection and costs can erase apparent profits.

## Key Rules

- Trade only inside the predeclared boundary band; report `no trade` in the middle.
- Define the rejection trigger numerically and use closed bars.
- Invalidate on the tested close-plus-buffer rule beyond the range, not on a wick.
- Treat relative-volume expansion as breakout risk to evaluate, not proof of direction.
- Reject a range whose available width cannot cover costs and the required payoff.

## Related Skills

- **breakout-trading** -- when the range breaks, switch to breakout strategy
- **momentum-trading** -- ADX rising above 25 signals transition from range to trend
