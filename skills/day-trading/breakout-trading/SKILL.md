---
name: breakout-trading
description: Define and test closed-bar consolidation breakouts. Use when measuring boundaries, normalized break buffers, relative participation, retests, invalidation, and net execution costs.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Breakout Trading

Captures explosive moves when price breaks out of consolidation zones or key support/resistance levels.

## Identification

Types: **Horizontal** (flat S/R, 3+ touches), **Pattern** (triangle/wedge/flag completion), **Trendline** (trend change signal).

### Participation Confirmation

Measure breakout-bar volume against the same instrument's time-of-day baseline or a predeclared rolling median. Treat relative volume, RSI, and MACD as candidate filters to validate, not confidence grades or independent votes. Require a closed bar beyond the level by a volatility- or tick-normalized buffer; do not use future follow-through to label the original entry.

## Workflow

### 1. Identify Consolidation

```
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
```

Look for tight range with 3+ touches on support/resistance.

### 2. Mark the Level

```
draw_chart_analysis(action="create", drawing={
    "type": "resistance",
    "points": [
        {"time": <first_touch_time>, "price": <level_price>},
        {"time": <current_time>, "price": <level_price>}
    ],
    "options": {"text": "Breakout Level (<price>)"}
})
```

### 3. Check Volume and Momentum

```
get_indicators(indicator_code="mfi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
get_indicators(indicator_code="rsi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
get_indicators(indicator_code="macd", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
```

Record the close-to-level distance in ATR or ticks, relative volume, spread, and momentum progression. Apply only filter thresholds fixed before the evaluation sample.

### 4. Entry and Target

Use the consolidation-height projection as a scenario, not a forecast. Choose and test one entry rule: closed-bar break or first retest within a predeclared bar window. Put invalidation back inside the range plus the tested buffer; size from that distance and modeled slippage.

### 5. Report to Orchestrator

Breakout type, volume multiple, entry recommendation, measured move target, stop level, false breakout risk assessment.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Opening-range breakout research](https://www.sciencedirect.com/science/article/pii/S1544612312000438) finds conditional evidence for a specified rule, while the broader [technical-analysis review](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID603481_code17745.pdf?abstractid=603481) warns about data snooping and costs.

## Key Rules

- Require a closed-bar trigger; a wick alone is not an entry under this rule.
- Freeze the participation, buffer, retest-window, and invalidation definitions before testing.
- A close back inside the range invalidates the setup only if that exact rule was specified in advance.
- Do not move a stop to breakeven merely because volume declines; compare that management rule out of sample.
- Report `valid`, `watch`, or `no trade` when the trigger, liquidity, or cost gate is missing.

## Related Skills

- **momentum-trading** -- ride the continuation after consolidation breaks
- **pullback-trading** -- time the retest entry after breakout
