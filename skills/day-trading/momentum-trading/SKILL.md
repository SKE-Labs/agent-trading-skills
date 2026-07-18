---
name: momentum-trading
description: Define and test short-horizon directional momentum setups. Use when measuring normalized return, regime, participation, breakout/pullback entry, exhaustion exit, and transaction costs.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Momentum Trading

Enter confirmed directional moves and ride them until momentum decays.

## Setup Conditions

### Regime Features

```
get_indicators(indicator_code="dmi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
```

Use ADX level and slope, normalized return, and relative volume as candidate features. Calibrate thresholds per instrument and timeframe, preferably against rolling percentiles; an ADX number is neither a probability nor a position-size instruction.

### Exit Features

- Volume declining while price advancing
- MACD histogram shrinking
- RSI divergence (price HH, RSI LH)
- Candles smaller with long wicks
- ADX turning down from its recent distribution

These features are correlated transformations of the same price/volume series. Define one exit rule and test it rather than counting two features as independent confirmation.

## Workflow

### 1. Check Regime

```
get_indicators(indicator_code="dmi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
```

Compare current ADX and normalized return with thresholds frozen from training data. If the regime gate fails, report `no trade` rather than substituting another strategy automatically.

### 2. Get Price Data and Confirm Momentum

```
get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
get_indicators(indicator_code="rsi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
get_indicators(indicator_code="macd", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
get_indicators(indicator_code="mfi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
```

Record multi-bar RSI and MACD progressions, time-of-day relative volume, and objectively detected swing structure. Avoid requiring every correlated indicator unless that conjunction improves held-out net expectancy.

### 3. Entry

**Breakout**: enter on a closed-bar break beyond a predeclared buffer. **Pullback**: define retracement depth as a tested interval rather than a fixed Fibonacci band. Invalidate beyond the structural level plus modeled slippage and size from the stop distance.

### 4. Report to Orchestrator

ADX value and trend direction, RSI/MACD/volume readings, entry type, exhaustion signals, stop and target levels.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Moskowitz & Grinblatt](https://onlinelibrary.wiley.com/doi/pdf/10.1111/0022-1082.00146) documented industry momentum, but implementation still requires regime, liquidity, cost, and crash-risk controls.

## Key Rules

- Do not map ADX directly to trade size or use a universal cutoff.
- Normalize extension and participation to the instrument, session, and timeframe.
- Predeclare whether entry is breakout or pullback; do not select retrospectively.
- Define the exit from observable price or feature conditions and test it after costs.
- Cap risk from the portfolio mandate, not from a momentum label.

## Related Skills

- **breakout-trading** -- breakout momentum is a primary entry type
- **pullback-trading** -- retracement entries use pullback principles for timing
