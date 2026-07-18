---
name: pullback-trading
description: Enter trends on price retracements to key levels. Use when trading with the trend, finding high R:R entries, or timing entries in established trends. Trend confirmation via EMA slope (no ADX).
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Pullback Trading

Enter established trends during temporary retracements for optimal risk/reward.

## Identification

### Pullback Levels

| Level | Depth | Trend Strength |
| --- | --- | --- |
| 20/50 EMA | Dynamic | Strong (shallow) |
| Normalized retracement band | Shallow/moderate/deep | Calibrate by instrument and regime |
| Previous S/R flip | Variable | Structure-based |

### Entry Confirmation (require before entering)

- Reversal candlestick pattern (hammer, engulfing)
- Momentum indicator turning in trend direction
- Volume decrease during pullback, increase on resumption

## Workflow

### 1. Confirm Trend on Higher Timeframe

`get_indicators` returns one indicator per call — fetch each separately:
```
get_candles(symbol=<symbol>, exchange=<exchange>, interval=<htf_interval>, count=120)
get_indicators(indicator_code="ema_21", symbol=<symbol>, exchange=<exchange>, interval=<htf_interval>, count=120)
get_indicators(indicator_code="ema_50", symbol=<symbol>, exchange=<exchange>, interval=<htf_interval>, count=120)
```

Then measure a five-bar EMA50 slope and normalize it by price or ATR. Five bars is a modeling choice, not a canonical horizon:
```
execute python3 -c "ema50=[<...>]; s=(ema50[-1]-ema50[-5])/ema50[-5]*100; print(f'htf_ema50_slope_pct={s:.3f}')"
```

Define bullish and bearish stack rules plus slope thresholds from training data, then freeze them. Track bars since the trend trigger as a candidate maturity feature; do not label the first pullback highest probability without held-out evidence.

### 2. Get Price Data and Identify Pullback

```
get_candles(symbol=<symbol>, exchange=<exchange>, interval=<primary_interval>, count=60)
```

Use an objective swing rule for HH/HL or LH/LL structure. Measure retracement as a continuous percentage of the prior impulse and test bands; moving averages, prior swings, and Fibonacci coordinates are candidate reference levels.

### 3. Check Momentum at Pullback Level

```
get_indicators(indicator_code="rsi_21", symbol=<symbol>, exchange=<exchange>, interval=<primary_interval>, count=20)
get_indicators(indicator_code="macd_fast", symbol=<symbol>, exchange=<exchange>, interval=<primary_interval>, count=20)
```

Cite RSI / MACD as a **3-5 value progression** (latest value alone is folklore):
- Uptrend pullback example: `RSI21 47.8 (62.4 → 55.1 → 49.0 → 47.8)`. Define any RSI band and MACD sign rule before testing; neither 50 nor a Fibonacci ratio is a natural boundary.
- Downtrend pullback: mirror — RSI pulling up from low extreme toward 50, MACD histogram shrinking from negative toward zero but NOT crossing into positive.

### 4. Mark Entry Zone

```
draw_chart_analysis(action="create", drawing={
    "type": "demand",
    "points": [
        {"time": <pullback_start>, "price": <fib_38>},
        {"time": <pullback_end>, "price": <fib_62>}
    ],
    "options": {"text": "Pullback Entry Zone (38-62%)"}
})
```

### 5. Report to Orchestrator

Trend direction and strength, pullback depth (which Fib level), confirmation signals, entry level, stop below pullback low, target at previous swing high/low.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: The [technical-analysis evidence review](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID603481_code17745.pdf?abstractid=603481) finds mixed results and recurring data-snooping and transaction-cost problems; calibrate pullback rules rather than treating ratios as natural laws.

## Key Rules

- Require the predeclared trend and retracement conditions before evaluating an entry.
- Define reversal confirmation numerically and use a closed bar.
- Treat deeper retracement as a continuous risk feature, not a law at 61.8%.
- Put invalidation beyond the structural pullback extreme plus a calibrated volatility/tick buffer, then resize the position.
- Test trend age and pullback sequence out of sample rather than assuming the first is best.
- Compute EMA slope via `execute`; do NOT call ADX / DMI / Supertrend (API-billed, not in the free whitelist)

## Related Skills

- **momentum-trading** -- pullbacks occur within momentum moves
- **breakout-trading** -- test pullbacks to an objectively defined breakout level
