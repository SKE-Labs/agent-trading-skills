---
name: pullback-trading
description: Enter trends on price retracements to key levels. Use when trading with the trend, finding high R:R entries, or timing entries in established trends. Trend confirmation via EMA slope (no ADX).
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
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

`get_indicators` returns one indicator per call — fetch each separately:
```
get_candles(symbol=<symbol>, exchange=<exchange>, interval=<htf_interval>, count=120)
get_indicators(indicator_code="ema_21", symbol=<symbol>, exchange=<exchange>, interval=<htf_interval>, count=120)
get_indicators(indicator_code="ema_50", symbol=<symbol>, exchange=<exchange>, interval=<htf_interval>, count=120)
```

Then verify trend strength via the canonical 5-bar slope of EMA50:
```
execute python3 -c "ema50=[<...>]; s=(ema50[-1]-ema50[-5])/ema50[-5]*100; print(f'htf_ema50_slope_pct={s:.3f}')"
```

Active trend requires BOTH:
- `slope > +0.5%` AND `ema_21 > ema_50` AND price above ema_50 (bull), OR
- `slope < −0.5%` AND `ema_21 < ema_50` AND price below ema_50 (bear)

The first pullback in a new trend is the highest-probability entry — a fresh trend has more runway than a mature one. Track bars-since-EMA-cross; <30 bars old = fresh.

### 2. Get Price Data and Identify Pullback

```
get_candles(symbol=<symbol>, exchange=<exchange>, interval=<primary_interval>, count=60)
```

Uptrend: HH/HL structure, price pulling back toward support (ema_21, ema_50, prior swing low, Fib 38.2/50/61.8). Downtrend: LH/LL structure, price pulling back toward resistance (mirror).

### 3. Check Momentum at Pullback Level

```
get_indicators(indicator_code="rsi_21", symbol=<symbol>, exchange=<exchange>, interval=<primary_interval>, count=20)
get_indicators(indicator_code="macd_fast", symbol=<symbol>, exchange=<exchange>, interval=<primary_interval>, count=20)
```

Cite RSI / MACD as a **3-5 value progression** (latest value alone is folklore):
- Uptrend pullback: `RSI21 47.8 (62.4 → 55.1 → 49.0 → 47.8)` — pulling back from extreme toward 50, NOT crossing 50 (40-50 is the pullback sweet spot). MACD histogram shrinking toward zero but NOT flipping sign.
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

## Key Rules

- NEVER trade pullbacks without confirmed trend direction (EMA50 5-bar slope >+0.5% bull / <−0.5% bear AND ema_21 / ema_50 stack agrees)
- NEVER enter without a reversal confirmation candle -- do not catch falling knives
- Deeper pullbacks (>61.8%) need stronger confirmation -- the trend may be reversing
- Stop goes below pullback low (uptrend) or above pullback high (downtrend), with an ATR buffer (0.3× ATR(1H) for BTC/ETH, 0.5× for alts) to avoid stop hunts
- First pullback in a new trend has the highest probability of success — older trends mean less remaining runway
- Compute EMA slope via `execute`; do NOT call ADX / DMI / Supertrend (API-billed, not in the free whitelist)

## Related Skills

- **momentum-trading** -- pullbacks occur within momentum moves
- **breakout-trading** -- first pullback often retests the breakout level
