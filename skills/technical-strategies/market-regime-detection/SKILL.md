---
name: market-regime-detection
description: Identify current market regime (trending, ranging, squeeze, or volatile) to select appropriate trading strategies. Uses only no-cost indicators (EMA slope, BB Width, ATR Ratio, Donchian) — avoids API-billed indicators like ADX/DMI/Supertrend.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
---

# Market Regime Detection

Markets cycle between distinct regimes. Detect the regime first before applying any other skill — the same setup means different things in trend vs range.

## Regime Types

| Regime       | EMA Slope (50, 5-bar) | BB Width  | Price Action                              |
| ------------ | --------------------- | --------- | ----------------------------------------- |
| **Trending Up**   | > +0.5% on 1H / 4H    | Expanding | HH + HL, strong directional candles       |
| **Trending Down** | < −0.5% on 1H / 4H    | Expanding | LH + LL, strong directional candles       |
| **Ranging**       | \|slope\| ≤ 0.15%     | Mid       | Oscillates around MAs, dojis at boundaries |
| **Squeeze**       | \|slope\| ≤ 0.15%     | <20th pctl, BB inside KC | Compression; breakout coming |
| **Volatile / Chop** | Slope flipping run-to-run | Very wide | Whipsaws both directions |

## Detection Inputs (all in the free indicator whitelist)

**EMA Slope (primary trend gate)** — compute the % slope of EMA50 over the last 5 closes:
```
ema50_slope_pct = (ema50[-1] - ema50[-5]) / ema50[-5] * 100
```
- `> +0.5%` → bullish trend
- `< −0.5%` → bearish trend
- `|slope| ≤ 0.15%` → flat (ranging / squeeze)
- between 0.15% and 0.5% → transitional, classify by other inputs

**BB Width** = `(bb_upper - bb_lower) / bb_middle * 100` — rolling-100-period percentile:
- `> 80th pctl` → expansion, supports a trend read
- `< 20th pctl` → squeeze, breakout imminent
- mid-band → ranging

**ATR Ratio** = `atr_14 / rolling_median(atr_14, 20)`:
- `> 1.2x` → elevated vol, trend or volatile
- `0.8–1.2x` → normal
- `< 0.8x` → compressed, squeeze
- `> 1.8x` → volatile / chop (large swings either way)

**BB Inside KC** — if `bb_lower > kc_lower AND bb_upper < kc_upper`, the Bollinger band is inside the Keltner channel → compression. Pair with low BB Width to confirm squeeze.

**Donchian Position** — `(close - donchian_lower) / (donchian_upper - donchian_lower)`:
- near 0 or 1 with EMA slope agreeing → confirmed trend continuation
- mid-band (0.4–0.6) with flat slope → ranging

## Composite Classification

| EMA Slope        | BB Width | ATR Ratio | BB-in-KC | Regime               |
| ---------------- | -------- | --------- | -------- | -------------------- |
| > +0.5% / < −0.5% | Expanding | ≥ 1.0x   | No       | **Trending**         |
| flat (\|slope\| ≤ 0.15%) | < 20th pctl | < 0.8x | Yes | **Squeeze**          |
| flat             | mid-band | 0.8–1.2x  | No       | **Ranging**          |
| flipping run-to-run | very wide | > 1.8x | No   | **Volatile / Chop**  |
| > 0.15% but < 0.5% | mixed  | mixed     | mixed    | **Transitional** (downgrade size) |

- 3/4 inputs agree → **high confidence**. 2/4 → **medium**, reduce size ×0.75. Split → **no trade, re-check next bar**.

## Regime Change Signals

| Signal                                          | Meaning                                |
| ----------------------------------------------- | -------------------------------------- |
| EMA50 5-bar slope crosses through ±0.15%        | Range → trend or trend → range pivot  |
| BB Width expands >50% in 5 bars                 | Breakout / vol spike                   |
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
| **Transitional** | apply trend playbook at ×0.75 size                 | direct A-tier entries                   |

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

3. **Classify** using the composite table. Report regime label + confidence (high/med/low) + the four numeric inputs + recommended/avoid skills.

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

## Key Rules

- NEVER skip regime detection before applying any other strategy
- NEVER force trades in the transitional zone (0.15% < |slope| < 0.5%); wait for clarity or apply trend playbook at ×0.75 size
- Combine all four inputs; no single indicator is sufficient. The composite reduces false regime calls
- Re-check regime on the higher timeframe; HTF regime overrides LTF
- Compute EMA slope via `execute`; do NOT call ADX / DMI / Supertrend (API-billed, not in the free whitelist)

## Related Skills

- **multi-timeframe-analysis** — regime on HTF sets context; MTF refines entries within the regime
- **bollinger-bands** — BB Width is a key detection input; BB strategies adapt to detected regime
- **trailing-stop** — trail method per regime (TRENDING: Donchian/chandelier; RANGING: structural; SQUEEZE: don't enter)
