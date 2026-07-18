---
name: ichimoku-cloud
description: Calculate and test correctly shifted Ichimoku components. Use when evaluating price/cloud, TK-cross, Chikou, and cloud-state features without future leakage or confirmation-count scoring.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Ichimoku Cloud Trading

Ichimoku Kinko Hyo provides trend, momentum, and S/R in one indicator system.

## Components

| Component       | Formula                        | Use              |
| --------------- | ------------------------------ | ---------------- |
| **Tenkan-sen**  | (9H + 9L) / 2                 | Fast signal line |
| **Kijun-sen**   | (26H + 26L) / 2               | Slow signal line |
| **Senkou A**    | (Tenkan + Kijun) / 2, plotted 26 ahead | Cloud boundary |
| **Senkou B**    | (52H + 52L) / 2, plotted 26 ahead | Cloud boundary |
| **Chikou Span** | Close plotted 26 periods back  | Confirmation     |

## Cloud (Kumo) Analysis

| Cloud Color   | Meaning                   |
| ------------- | ------------------------- |
| Green (A > B) | Senkou A above Senkou B; bullish-context feature |
| Red (A < B) | Senkou A below Senkou B; bearish-context feature |
| Thin/thick cloud | Relative spread between Senkou spans; test any S/R interpretation |

## Signals

### TK Cross (Tenkan/Kijun)

- **Bullish feature**: Tenkan crosses above Kijun; record cloud location as context
- **Bearish feature**: Tenkan crosses below Kijun; record cloud location as context

### Price vs Cloud

- Above cloud = bullish bias
- Below cloud = bearish bias
- Inside cloud = overlap state; apply the calibrated policy

### Chikou Span Confirmation

- Chikou above price (26 bars ago) = bullish
- Chikou below price (26 bars ago) = bearish

### Component State Checklist

| Condition      | Bullish     | Bearish     |
| -------------- | ----------- | ----------- |
| Price position | Above cloud | Below cloud |
| TK cross       | Bullish     | Bearish     |
| Chikou span    | Above price | Below price |
| Cloud ahead    | Green       | Red         |

These components share the same price history and are not independent votes. Preserve the four states but assign strength only if a calibrated model supports it.

## Workflow

1. **Get at least 120 closed candles** to calculate components and their plotted shifts:
   ```
   get_candles(symbol=<symbol>, exchange=<exchange>, interval=<interval>, count=120)
   ```
   Compute rolling highest-high/lowest-low midpoints. Plot Senkou spans 26 bars ahead and Chikou 26 bars back. When backtesting, compare each decision timestamp only with values computable then; never use the future plotted location as future information.

2. **Assess price versus the correctly aligned current cloud**, not the unshifted calculations

3. **Record TK cross and Chikou relation** as correlated features

4. **Apply the predeclared closed-bar entry and structural invalidation**; a line touch is not enough.

5. **Mark on chart**:
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

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: The [technical-analysis evidence review](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID603481_code17745.pdf?abstractid=603481) finds results vary by market and testing design; Ichimoku settings and confirmation rules require the same out-of-sample scrutiny.

## Key Rules

- Treat inside-cloud status as a testable filter, not a universal prohibition.
- Test 9/26/52 and chosen timeframes on the intended session; no 4H minimum is universal.
- Use cloud edges as candidate coordinates and stop only at thesis invalidation.
- Do not convert component agreement directly into confidence or size.

## Related Skills

- **multi-timeframe-analysis** — Ichimoku across timeframes for alignment
- **moving-average-crossover** — TK cross is analogous to MA crossovers; combine for confirmation
