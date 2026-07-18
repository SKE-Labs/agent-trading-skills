---
name: gap-trading
description: Identify and test opening-gap continuation or fade setups. Use when price opens away from the prior session and the user needs a normalized gap definition, catalyst context, entry, invalidation, and cost-aware plan.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Gap Trading

Trade price gaps by classifying gap type first -- different types require opposite strategies.

## Identification

Distinguish a **full gap** (open above the prior high or below the prior low) from a **body gap** (open away from the prior close). State the exchange session, corporate-action adjustment, and overnight-trading treatment.

```
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval="1D", date=<date>)
```

Compute both percentage gap and `abs(Open - Previous Close) / prior ATR`. Set the minimum from tick size, spread, and the instrument's historical gap distribution; do not use a universal percentage cutoff.

## Gap Classification

Classify observable context rather than assigning universal fill rates:

| Context | Evidence to record | Candidate hypothesis |
| --- | --- | --- |
| Range / no catalyst | Gap remains inside an established range | Fade after a defined reversal trigger |
| Level break / catalyst | Gap clears a predeclared level with unusual participation | Continuation after an opening range |
| Extended move | Gap follows an objectively extended trend | Test fade and continuation separately |

## Workflow

### 1. Detect and Classify

```
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval="1D", date=<date>)
get_indicators(indicator_code="mfi", symbol=<symbol>, exchange=<exchange>, interval="1D")
```

Calculate both normalized gap measures. Compare volume with the same time-of-day baseline and document the catalyst from a primary source when available.

### 2. Check Trend Context

```
get_indicators(indicator_code="dmi", symbol=<symbol>, exchange=<exchange>, interval="1D")
get_indicators(indicator_code="ema", symbol=<symbol>, exchange=<exchange>, interval="1D")
```

Determine if ranging, starting trend, mid-trend, or extended trend to confirm classification.

### 3. Mark Gap Zone

```
draw_chart_analysis(action="create", drawing={
    "type": "highlight",
    "points": [
        {"time": <previous_close_time>, "price": <previous_close>},
        {"time": <gap_open_time>, "price": <gap_open>}
    ],
    "options": {"text": "<Gap Type> Gap (+/-X.X%)"}
})
```

### 4. Apply Strategy

- **Fade**: enter only after the predeclared reversal or failed-break trigger; use the prior close as a scenario target, not an assumed fill.
- **Continuation**: define an opening-range length in bars, enter on its closed-bar break, and invalidate on a tested return through the range or gap level.
- Compare several opening-range lengths in training data only and retain a rule only when it survives held-out costs.

### 5. Report to Orchestrator

Gap type and rationale, gap size, volume confirmation, strategy recommendation, gap boundaries, fill target, stop level.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Research on overnight versus intraday price formation](https://www.sciencedirect.com/science/article/pii/S1059056024006610) supports treating the open as a distinct information period, not assigning universal fill rates to named gap types.

## Key Rules

- Do not assume the open is noise or that a named gap type has a fixed fill probability.
- Use a time-stamped session definition and adjusted prior prices.
- Treat event-driven gaps separately and model opening-auction spread, slippage, and halt risk.
- A wider stop must reduce position size; never widen it solely to avoid an exit.
- Return `no trade` when the gap is too small relative to total execution cost.

## Related Skills

- **breakout-trading** -- gap-and-go follows breakout principles
- **momentum-trading** -- breakaway gaps create momentum moves
