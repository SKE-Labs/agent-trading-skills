---
name: scalping-strategy
description: Evaluate and plan very short-horizon trades in highly liquid markets. Use when the user needs an executable scalp with latency, spread, fee, slippage, and capacity controls.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Scalping Strategy

Target small, frequent profits from minimal price movements on 1m-5m timeframes.

## Setup Conditions

| Factor | Requirement |
| --- | --- |
| Data | Timestamped quotes/trades plus closed bars |
| Cost gate | Expected gross edge exceeds spread, fees, slippage, and adverse selection |
| Liquidity | Tested depth, order size, fill rate, and cancellation behavior |
| Risk | Hard per-trade and session loss limits from the portfolio mandate |
| Deployment | Positive held-out expectancy in the intended venue and session |

## Scalping Techniques

### 1. Momentum Scalping

Enter on strong momentum candles on 1m, ride for small gain, exit immediately on momentum loss.

```
get_indicators(indicator_code="rsi", symbol=<symbol>, exchange=<exchange>, interval="1m")
get_indicators(indicator_code="macd", symbol=<symbol>, exchange=<exchange>, interval="1m")
```

Define an objective closed-bar momentum trigger and exit. RSI/MACD are correlated price transforms; retain them only if they improve held-out net results over a price-only baseline.

### 2. Level Scalping

Quick bounces at key S/R levels with tight stops.

```
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval="5m", date=<date>)
```

Identify levels on the context timeframe, define a numerical rejection on the execution timeframe, and place invalidation beyond the level plus expected stop slippage. Require the planned payoff to remain positive after costs.

### 3. Range Scalping

Buy support, sell resistance within a defined micro-range. Repeat until range breaks.

```
get_indicators(indicator_code="dmi", symbol=<symbol>, exchange=<exchange>, interval="5m")
```

Use a calibrated range classifier; ADX alone does not confirm a micro-range. Stop applying the rule when the closed-bar invalidation or liquidity gate fails.

## Workflow

### 1. Confirm Direction on 5m

```
get_indicators(indicator_code="ema", symbol=<symbol>, exchange=<exchange>, interval="5m")
get_indicators(indicator_code="dmi", symbol=<symbol>, exchange=<exchange>, interval="5m")
```

Establish bias from higher timeframe before scalping on 1m.

### 2. Identify Setup on 1m

```
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval="1m", date=<date>)
get_indicators(indicator_code="rsi", symbol=<symbol>, exchange=<exchange>, interval="1m")
```

Pick one technique (momentum, level, or range) based on current conditions.

### 3. Mark Key Levels

```
draw_chart_analysis(action="create", drawing={
    "type": "support",
    "points": [
        {"time": <touch_1>, "price": <level>},
        {"time": <touch_2>, "price": <level>}
    ],
    "options": {"text": "Scalp Level"}
})
```

### 4. Report to Orchestrator

Technique selected, timestamped quote, order type, expected fill, entry, invalidation, target, total cost estimate, capacity, and context-timeframe bias.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Barber et al.](https://academic.oup.com/raps/article-pdf/10/1/61/31788119/raz006.pdf) found aggregate day-trader performance was negative and persistent profitability rare, making net-of-cost evidence and strict loss limits essential.

## Key Rules

- Exclude scheduled event windows unless a separately tested event strategy and mandate apply.
- Reject markets and order sizes that fail the spread, depth, fill-rate, latency, or cost gate.
- Exit on the predeclared invalidation; do not widen risk after entry.
- Enforce the mandate's session loss and order-rate limits; pause on feed, clock, or execution anomalies.
- Compare context-aligned and context-agnostic variants rather than assuming alignment adds edge.
- Do not deploy from win rate alone; require positive net expectancy and stable tail losses.

## Related Skills

- **range-trading** -- range scalping is a micro-timeframe application of range principles
- **momentum-trading** -- momentum scalping borrows directional confirmation logic
