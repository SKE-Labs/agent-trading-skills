---
name: market-regime-detection
description: Identify current market regime (trending, ranging, squeeze, or volatile) to select appropriate trading strategies. Uses only no-cost indicators (EMA slope, BB Width, ATR Ratio, Donchian) — avoids API-billed indicators like ADX/DMI/Supertrend.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Market Regime Detection

Regime labels summarize observable trend and volatility states. They are model outputs with uncertainty, not natural market categories; measure whether they add held-out value to the downstream strategy.

## Regime Types

| Regime       | EMA Slope (50, 5-bar) | BB Width  | Price Action                              |
| ------------ | --------------------- | --------- | ----------------------------------------- |
| **Trending Up** | Positive normalized slope | Expanding/steady | Objective HH/HL or directional-return state |
| **Trending Down** | Negative normalized slope | Expanding/steady | Objective LH/LL or directional-return state |
| **Ranging** | Near-zero normalized slope | Middle distribution | Oscillation under predeclared rule |
| **Squeeze** | Near-zero normalized slope | Low percentile, optional BB inside KC | Relative compression; direction unknown |
| **Volatile / Chop** | Slope flipping run-to-run | Very wide | Whipsaws both directions |

## Detection Inputs (all in the free indicator whitelist)

**EMA slope candidate** — compute over a predeclared horizon and normalize by price or ATR:
```
ema50_slope_pct = (ema50[-1] - ema50[-5]) / ema50[-5] * 100
```
Derive positive, negative, and near-zero bands from training data or rolling historical percentiles for the instrument/timeframe; freeze them before evaluation.

**BB Width** = `(bb_upper - bb_lower) / bb_middle * 100` — rolling-100-period percentile:
- `> 80th pctl` → expansion, supports a trend read
- `< 20th pctl` → squeeze candidate; no direction or imminent break is implied
- mid-band → ranging

**ATR Ratio** = `atr_14 / rolling_median(atr_14, 20)`:
Use rolling percentiles or training-set thresholds; ATR ratio measures volatility, not whether price is trending or choppy.

**BB Inside KC** — if `bb_lower > kc_lower AND bb_upper < kc_upper`, the Bollinger band is inside the Keltner channel → compression. Pair with low BB Width to confirm squeeze.

**Donchian Position** — `(close - donchian_lower) / (donchian_upper - donchian_lower)`:
- near 0 or 1 with EMA slope agreeing → confirmed trend continuation
- mid-band (0.4–0.6) with flat slope → ranging

## Composite Classification

| EMA Slope        | BB Width | ATR Ratio | BB-in-KC | Regime               |
| ---------------- | -------- | --------- | -------- | -------------------- |
| Outside trained near-zero band | Expanding | Elevated percentile | No | **Trending candidate** |
| Inside trained near-zero band | Low percentile | Low percentile | Yes | **Squeeze candidate** |
| Inside trained near-zero band | Middle percentile | Middle percentile | No | **Range candidate** |
| Unstable sign | Very high percentile | Very high percentile | No | **Volatile candidate** |
| Mixed | Mixed | Mixed | Mixed | **Transitional/uncertain** |

The table is a seed specification only. Do not count correlated inputs as independent agreement or map them directly to confidence/size. Calibrate a classifier, report posterior/calibration if available, otherwise report features plus `classified`, `uncertain`, or `no trade`.

## Regime Change Signals

| Signal                                          | Meaning                                |
| ----------------------------------------------- | -------------------------------------- |
| EMA50 5-bar slope crosses through ±0.15%        | Range → trend or trend → range pivot  |
| BB Width expansion exceeds trained percentile/rate | Volatility expansion; direction unknown |
| BB Width contracts to <20th pctl + BB inside KC | Squeeze forming                        |
| ATR Ratio jumps above 1.5x off a low base       | Vol expansion, expect direction reveal |
| Price closes outside Donchian-20 boundary       | Breakout from prior range              |

## Strategy Selection Matrix

| Regime          | Use These Skills                                    | Avoid                                   |
| --------------- | --------------------------------------------------- | --------------------------------------- |
| **Trending**    | moving-average-crossover, pullback-trading, fibonacci-trading, trailing-stop | mean-reversion, range-trading |
| **Ranging**     | mean-reversion, bollinger-bands, supply-demand-zones | momentum-trading, MA crossover         |
| **Squeeze**     | breakout-trading (arm BOTH directions, wait for break) | range-trading (about to break)         |
| **Volatile / Chop** | wider stops, smaller size, prefer to sit out    | all trend-following, all mean-reversion |
| **Transitional** | use only strategies validated in this state or wait | untested regime substitution |

## Workflow

1. **Pull indicators** (`get_indicators` returns one indicator per call — fetch each separately):
   ```
   get_indicators(indicator_code="ema_50",      symbol=<symbol>, exchange=<exchange>, interval=<interval>, count=120)
   get_indicators(indicator_code="bbands",      symbol=<symbol>, exchange=<exchange>, interval=<interval>, count=120)
   get_indicators(indicator_code="atr_14",      symbol=<symbol>, exchange=<exchange>, interval=<interval>, count=120)
   get_indicators(indicator_code="keltner_20",  symbol=<symbol>, exchange=<exchange>, interval=<interval>, count=120)
   get_indicators(indicator_code="donchian_20", symbol=<symbol>, exchange=<exchange>, interval=<interval>, count=120)
   ```

2. **Compute the four inputs** in one execute block:
   ```
   execute python3 -c "
   import numpy as np
   ema50 = [<ema50 array>]
   bb_lower, bb_upper, bb_middle = [<...>], [<...>], [<...>]
   kc_lower, kc_upper = [<...>], [<...>]
   atr = [<atr_14 array>]
   don_lo, don_hi = [<...>], [<...>]
   close = [<...>]

   slope_pct = (ema50[-1] - ema50[-5]) / ema50[-5] * 100
   bb_width  = [(u - l) / m * 100 for u, l, m in zip(bb_upper, bb_lower, bb_middle)]
   bb_width_pctl = sum(1 for w in bb_width if w <= bb_width[-1]) / len(bb_width) * 100
   atr_ratio = atr[-1] / np.median(atr[-20:])
   bb_in_kc  = bb_lower[-1] > kc_lower[-1] and bb_upper[-1] < kc_upper[-1]
   don_pos   = (close[-1] - don_lo[-1]) / (don_hi[-1] - don_lo[-1])

   print(f'slope_pct={slope_pct:.3f} bb_width_pctl={bb_width_pctl:.1f} atr_ratio={atr_ratio:.2f} bb_in_kc={bb_in_kc} don_pos={don_pos:.2f}')
   "
   ```

3. **Classify** using thresholds frozen from training data. Report label, uncertainty, numeric inputs, data window, and which downstream strategies have validated conditional results.

4. **Visualize** (optional, only if user-facing report needs it):
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "highlight",
       "points": [
           {"time": <regime_start>, "price": <candle_high>},
           {"time": <current_time>, "price": <candle_low>}
       ],
       "options": {"text": "TRENDING bullish (EMA50 slope +0.84%)"}
   })
   ```

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Ang & Bekaert](https://www.nber.org/papers/w7056) supports regime-dependent volatility and correlation, while [backtest-overfitting research](https://escholarship.org/uc/item/9tq3327h) cautions against selecting thresholds after repeated trials.

## Key Rules

- Use regime detection only when it improves the downstream strategy versus a no-regime baseline.
- Treat transitional/uncertain states according to predeclared policy; never map them to arbitrary size.
- The inputs are correlated; feature count does not prove accuracy or reduce false calls.
- Model higher/lower-timeframe conflicts explicitly; the higher timeframe does not automatically override.
- Compute EMA slope via `execute`; do NOT call ADX / DMI / Supertrend (API-billed, not in the free whitelist)

## Related Skills

- **multi-timeframe-analysis** — regime on HTF sets context; MTF refines entries within the regime
- **bollinger-bands** — BB Width is a key detection input; BB strategies adapt to detected regime
- **trailing-stop** — trail method per regime (TRENDING: Donchian/chandelier; RANGING: structural; SQUEEZE: don't enter)
