---
name: mean-reversion
description: Trade price extremes back toward the statistical mean using z-scores, Bollinger Bands, and RSI. Use when price is overextended from its average in ranging markets, or when identifying exhaustion at extremes.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Mean Reversion

Price tends to revert to its statistical mean after moving to extremes. Mean reversion profits from buying oversold and selling overbought in ranging markets.

## Detection Methods

### Z-Score

`Z-Score = (Price - SMA) / Standard Deviation`. Enter at |Z| > 2.0, target Z = 0 (the mean).

| Z-Score | Signal |
| --- | --- |
| > +2.0 | Strongly overbought → sell/short |
| -1.0 to +1.0 | Normal → no signal |
| < -2.0 | Strongly oversold → buy/long |

### Bollinger Band Method

- Band touch/pierce + reversal candle → trade toward middle band
- Confirmation: band touch + RSI extreme + reversal candle = high probability

### RSI Extreme Method

Use 25/75 thresholds (not 30/70): RSI <25 = deeply oversold (buy), RSI >75 = deeply overbought (sell).

## Regime Filter (Critical)

| ADX | Mean Reversion? |
| --- | --- |
| < 20 | **Yes** — ideal |
| 20-25 | **Caution** — reduced size |
| > 25 | **No** — trending, skip |

## Workflow

1. **Check regime** (must pass first):
   ```
   get_indicator(indicator_code="dmi", symbol=<symbol>, interval=<interval>)
   ```
   ADX > 25 → stop. Mean reversion not applicable.

2. **Get BB and RSI**:
   ```
   get_indicator(indicator_code="bbands", symbol=<symbol>, interval=<interval>)
   get_indicator(indicator_code="rsi", symbol=<symbol>, interval=<interval>)
   get_indicator(indicator_code="ema", symbol=<symbol>, interval=<interval>)
   ```

3. **Get candles** for confirmation:
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```

4. **Mark setup**:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "demand",
       "points": [
           {"time": <extreme_time>, "price": <lower_bb>},
           {"time": <current_time>, "price": <entry_zone>}
       ],
       "options": {"text": "Mean Reversion Buy (RSI: 22, Z: -2.3)"}
   })
   ```

5. **Targets**: conservative = middle band (~65% WR), standard = 75% to middle (~55%), aggressive = opposite band (~35%)

## Key Rules

- NEVER use mean reversion in trending markets (ADX > 25); "oversold" in a downtrend gets more oversold
- NEVER enter on BB touch alone; require confirmation candle (engulfing, hammer, doji)
- NEVER hold for opposite band as the plan; middle band (SMA) is the realistic target
- NEVER ignore BB Width squeeze (<20th pctl); a breakout is coming and mean reversion will fail
- Require 2+ confirming signals (BB + RSI + Z-Score) for entry
- If price is at lower BB due to fundamental repricing (earnings, news), it is not "oversold"

## Related Skills

- **bollinger-bands** — BB touches are the primary visual mean reversion signal
- **market-regime-detection** — ADX must confirm ranging market before any mean reversion trade
