---
name: ichimoku-cloud
description: Trade using Ichimoku Cloud for trend, momentum, and support/resistance. Use when identifying trend direction at a glance, finding support/resistance zones, or timing entries with multiple confirmations.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Ichimoku Cloud Trading

Ichimoku Kinko Hyo provides trend, momentum, and S/R in one indicator system.

## Components

| Component       | Formula                        | Use              |
| --------------- | ------------------------------ | ---------------- |
| **Tenkan-sen**  | (9H + 9L) / 2                 | Fast signal line |
| **Kijun-sen**   | (26H + 26L) / 2               | Slow signal line |
| **Senkou A**    | (Tenkan + Kijun) / 2          | Cloud boundary   |
| **Senkou B**    | (52H + 52L) / 2               | Cloud boundary   |
| **Chikou Span** | Close plotted 26 periods back  | Confirmation     |

## Cloud (Kumo) Analysis

| Cloud Color   | Meaning                   |
| ------------- | ------------------------- |
| Green (A > B) | Bullish trend             |
| Red (A < B)   | Bearish trend             |
| Thin cloud    | Weak support/resistance   |
| Thick cloud   | Strong support/resistance |

## Signals

### TK Cross (Tenkan/Kijun)

- **Bullish**: Tenkan crosses above Kijun (strongest when above cloud)
- **Bearish**: Tenkan crosses below Kijun (strongest when below cloud)

### Price vs Cloud

- Above cloud = bullish bias
- Below cloud = bearish bias
- Inside cloud = consolidation, no trade

### Chikou Span Confirmation

- Chikou above price (26 bars ago) = bullish
- Chikou below price (26 bars ago) = bearish

### Strong Signal Checklist

| Condition      | Bullish     | Bearish     |
| -------------- | ----------- | ----------- |
| Price position | Above cloud | Below cloud |
| TK cross       | Bullish     | Bearish     |
| Chikou span    | Above price | Below price |
| Cloud ahead    | Green       | Red         |

All 4 = strong signal. 3/4 = moderate. <3 = weak/skip.

## Workflow

1. **Get Ichimoku components**:
   ```
   get_indicator(indicator_code="ema", symbol=<symbol>, interval=<interval>)
   get_indicator(indicator_code="dmi", symbol=<symbol>, interval=<interval>)
   ```

2. **Get candle data** to calculate Ichimoku manually:
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```
   Compute: `Tenkan = (9H + 9L) / 2`, `Kijun = (26H + 26L) / 2`, `Senkou A = (Tenkan + Kijun) / 2`, `Senkou B = (52H + 52L) / 2`

3. **Assess cloud color** for trend direction, price position relative to cloud

4. **Check TK cross** and Chikou span for confirmation

5. **Enter on pullback** to Tenkan or Kijun in trend direction. Stop below/above cloud or Kijun.

6. **Mark on chart**:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "support",
       "points": [
           {"time": <start_time>, "price": <kijun_price>},
           {"time": <end_time>, "price": <kijun_price>}
       ],
       "options": {"text": "Kijun Support"}
   })
   ```

## Key Rules

- NEVER trade when price is inside the cloud (indecision zone)
- NEVER use Ichimoku on timeframes below 4H; default settings (9, 26, 52) are designed for daily charts
- Cloud acts as dynamic S/R; use cloud edge as stop loss zone
- All 4 conditions aligned = high confidence; fewer than 3 = skip

## Related Skills

- **multi-timeframe-analysis** — Ichimoku across timeframes for alignment
- **moving-average-crossover** — TK cross is analogous to MA crossovers; combine for confirmation
