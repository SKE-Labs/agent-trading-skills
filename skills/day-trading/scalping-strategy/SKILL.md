---
name: scalping-strategy
description: Execute high-frequency small profit trades for quick gains. Use when trading highly liquid markets, taking advantage of short-term volatility, or building consistent small wins.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Scalping Strategy

Target small, frequent profits from minimal price movements on 1m-5m timeframes.

## Setup Conditions

| Factor | Requirement |
| --- | --- |
| Timeframe | 1m, 5m |
| Profit target | 5-20 pips / 0.1-0.5% |
| Trade duration | Seconds to minutes |
| Win rate target | 60%+ |
| Assets | High liquidity only (BTC, ETH, major forex) |
| Timing | High volume periods (kill zones) only |

## Scalping Techniques

### 1. Momentum Scalping

Enter on strong momentum candles on 1m, ride for small gain, exit immediately on momentum loss.

```
get_indicator(indicator_code="rsi", symbol=<symbol>, interval="1m")
get_indicator(indicator_code="macd", symbol=<symbol>, interval="1m")
```

RSI crossing 50 with expanding MACD histogram on 1m = entry trigger. Exit when histogram shrinks.

### 2. Level Scalping

Quick bounces at key S/R levels with tight stops.

```
get_candles_around_date(symbol=<symbol>, interval="5m", date=<date>)
```

Identify S/R on 5m, enter on rejection candle on 1m. Stop just beyond the level. Target 1:1 to 1:1.5 R:R.

### 3. Range Scalping

Buy support, sell resistance within a defined micro-range. Repeat until range breaks.

```
get_indicator(indicator_code="dmi", symbol=<symbol>, interval="5m")
```

ADX <20 on 5m confirms micro-range. Mark boundaries, trade bounces at edges.

## Workflow

### 1. Confirm Direction on 5m

```
get_indicator(indicator_code="ema", symbol=<symbol>, interval="5m")
get_indicator(indicator_code="dmi", symbol=<symbol>, interval="5m")
```

Establish bias from higher timeframe before scalping on 1m.

### 2. Identify Setup on 1m

```
get_candles_around_date(symbol=<symbol>, interval="1m", date=<date>)
get_indicator(indicator_code="rsi", symbol=<symbol>, interval="1m")
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

Technique selected, entry level, stop (tight -- 5-10 pips max), target, 5m directional bias.

## Key Rules

- NEVER scalp during news events -- unpredictable spikes destroy tight stops
- NEVER scalp low-liquidity assets -- spreads eat the small profits
- NEVER hold a losing scalp hoping for recovery -- exit immediately if wrong
- Stop after 3 consecutive losses -- reassess conditions before continuing
- Always confirm 1m direction aligns with 5m bias before entering
- Factor in fees -- they can consume scalping profits entirely

## Related Skills

- **range-trading** -- range scalping is a micro-timeframe application of range principles
- **momentum-trading** -- momentum scalping borrows directional confirmation logic
