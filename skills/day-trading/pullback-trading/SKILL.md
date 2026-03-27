---
name: pullback-trading
description: Enter trends on price retracements to key levels. Use when trading with the trend, finding high R:R entries, or timing entries in established trends.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Pullback Trading

Enter established trends during temporary retracements for optimal risk/reward.

## Identification

### Pullback Levels

| Level | Depth | Trend Strength |
| --- | --- | --- |
| 20/50 EMA | Dynamic | Strong (shallow) |
| Fibonacci 38.2% | Shallow | Strong trend |
| Fibonacci 50% | Moderate | Normal trend |
| Fibonacci 61.8% | Deep | Weak but valid |
| Previous S/R flip | Variable | Structure-based |

### Entry Confirmation (require before entering)

- Reversal candlestick pattern (hammer, engulfing)
- Momentum indicator turning in trend direction
- Volume decrease during pullback, increase on resumption

## Workflow

### 1. Confirm Trend on Higher Timeframe

```
get_indicator(indicator_code="dmi", symbol=<symbol>, interval=<interval>)
get_indicator(indicator_code="ema", symbol=<symbol>, interval=<interval>)
```

ADX >25 and price above/below EMA confirms active trend. First pullback in a new trend is the highest-probability entry.

### 2. Get Price Data and Identify Pullback

```
get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
```

Uptrend: HH/HL structure, price pulling back toward support. Downtrend: LH/LL structure, price pulling back toward resistance.

### 3. Check Momentum at Pullback Level

```
get_indicator(indicator_code="rsi", symbol=<symbol>, interval=<interval>)
get_indicator(indicator_code="macd", symbol=<symbol>, interval=<interval>)
```

RSI should be pulling back from extreme toward 50 (not crossing it). MACD histogram shrinking but not flipping sign.

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

## Key Rules

- NEVER trade pullbacks without confirmed trend direction (ADX >25)
- NEVER enter without a reversal confirmation candle -- do not catch falling knives
- Deeper pullbacks (>61.8%) need stronger confirmation -- the trend may be reversing
- Stop goes below pullback low (uptrend) or above pullback high (downtrend)
- First pullback in a new trend has the highest probability of success

## Related Skills

- **momentum-trading** -- pullbacks occur within momentum moves
- **breakout-trading** -- first pullback often retests the breakout level
