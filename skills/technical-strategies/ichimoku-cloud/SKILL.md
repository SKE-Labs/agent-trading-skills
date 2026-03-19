---
name: ichimoku-cloud
description: Trade using Ichimoku Cloud for trend, momentum, and support/resistance. Use when identifying trend direction at a glance, finding support/resistance zones, or timing entries with multiple confirmations.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending"]
---

# Ichimoku Cloud Trading

Ichimoku Kinko Hyo ("one glance equilibrium chart") provides comprehensive market analysis in one indicator.

## Components

| Component       | Calculation                   | Use              |
| --------------- | ----------------------------- | ---------------- |
| **Tenkan-sen**  | (9-high + 9-low) / 2          | Fast signal line |
| **Kijun-sen**   | (26-high + 26-low) / 2        | Slow signal line |
| **Senkou A**    | (Tenkan + Kijun) / 2          | Cloud boundary   |
| **Senkou B**    | (52-high + 52-low) / 2        | Cloud boundary   |
| **Chikou Span** | Close plotted 26 periods back | Confirmation     |

**Quick calculation:**
```
execute(command='python3 -c "h9=50500;l9=49500;h26=51000;l26=48000;h52=52000;l52=46000;tenkan=(h9+l9)/2;kijun=(h26+l26)/2;senkou_a=(tenkan+kijun)/2;senkou_b=(h52+l52)/2;print(f\"Tenkan: {tenkan:.2f}\\nKijun: {kijun:.2f}\\nSenkou A: {senkou_a:.2f}\\nSenkou B: {senkou_b:.2f}\")"')
```

## Cloud (Kumo) Analysis

| Cloud Color   | Meaning                   |
| ------------- | ------------------------- |
| Green (A > B) | Bullish trend             |
| Red (A < B)   | Bearish trend             |
| Thin cloud    | Weak support/resistance   |
| Thick cloud   | Strong support/resistance |

## Trading Signals

### 1. TK Cross (Tenkan/Kijun)

- **Bullish**: Tenkan crosses above Kijun
- **Bearish**: Tenkan crosses below Kijun
- Strongest when above/below cloud

### 2. Price vs Cloud

- Price above cloud = Bullish
- Price below cloud = Bearish
- Price inside cloud = Consolidation/indecision

### 3. Chikou Span Confirmation

- Chikou above price (26 bars ago) = Bullish
- Chikou below price (26 bars ago) = Bearish

### 4. Cloud Breakout

- Price breaks above cloud = Strong buy
- Price breaks below cloud = Strong sell
- Use cloud as stop loss zone

## Strong Signal Checklist

| Condition      | Bullish     | Bearish     |
| -------------- | ----------- | ----------- |
| Price position | Above cloud | Below cloud |
| TK cross       | Bullish     | Bearish     |
| Chikou span    | Above price | Below price |
| Cloud ahead    | Green       | Red         |

All 4 = Strong signal. 3/4 = Moderate. <3 = Weak.

## Entry Workflow

1. **Identify cloud color** for trend direction
2. **Wait for price position** relative to cloud
3. **Confirm with TK cross** in trend direction
4. **Check Chikou span** for final confirmation
5. **Enter on pullback** to Tenkan or Kijun
6. **Stop loss** below/above cloud or Kijun

## Time Frame Consideration

- Default settings (9, 26, 52) designed for daily charts
- For lower TFs, some traders adjust settings
- Cloud works best on 4H and above

## Related Skills

- **multi-timeframe-analysis** — Ichimoku provides trend, momentum, and S/R in one view; use across timeframes for alignment
- **moving-average-crossover** — TK cross is analogous to MA crossovers; combine for confirmation
