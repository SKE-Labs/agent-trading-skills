---
name: multi-timeframe-analysis
description: Analyze markets using 3 timeframes with signal priority scoring and conflict resolution. Use when determining trend direction, timing entries with precision, or validating trade setups across timeframes.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.1"
---

# Multi-Timeframe Analysis (MTF)

Analyze 3 timeframes to align trend, structure, and entry. Never trade a lower timeframe signal that contradicts the higher timeframe bias.

## Timeframe Selection

| Primary TF | Higher TF | Lower TF | Use Case         |
| ---------- | --------- | -------- | ---------------- |
| 1D         | Weekly    | 4H       | Position trading |
| 4H         | 1D        | 1H       | Swing trading    |
| 1H         | 4H        | 15m      | Intraday swing   |
| 15m        | 1H        | 5m       | Day trading      |

Each timeframe should be 4-6x the one below it. Pick one combination and use consistently.

## Timeframe Roles

| Role        | Purpose         | Focus                                    |
| ----------- | --------------- | ---------------------------------------- |
| **Higher**  | Trend direction | Major S/R, overall bias, regime          |
| **Primary** | Trade structure | Patterns, setups, key levels             |
| **Lower**   | Entry timing    | Precise entries, confirmation, tight stops |

## Signal Priority

| HTF Bias | Primary Setup | LTF Entry | Score | Action |
| --- | --- | --- | --- | --- |
| Bullish | Bullish setup | Bullish confirmation | **10/10** | Full size, high confidence |
| Bullish | Bullish setup | No LTF signal yet | **7/10** | Wait for LTF, don't force |
| Bullish | Ranging | — | **4/10** | Wait for primary setup |
| Bullish | Bearish setup | Bearish confirmation | **2/10** | Skip — counter-trend |
| Ranging | Bullish setup | Bullish confirmation | **6/10** | Reduced size (no HTF support) |
| Ranging | Ranging | — | **1/10** | No trade — wait |
| Bearish | Bullish setup | Bullish confirmation | **3/10** | Skip — against HTF |

**Minimum score**: 6/10 for standard entries, 8/10 for full-size positions.

## Conflict Resolution

| Conflict | Resolution |
| --- | --- |
| HTF bullish, Primary bearish | **Wait.** Primary is likely a pullback in HTF trend. |
| HTF bearish, LTF bullish | **Skip.** LTF bullish in HTF downtrend = counter-trend trap. |
| HTF ranging, Primary trending | **Reduce size.** 50% normal — no HTF confirmation. |
| All timeframes conflicting | **No trade.** Clarity is a prerequisite. |

**When in doubt, the higher timeframe wins. Period.**

## Workflow

1. **Higher TF — establish bias**:
   ```
   generate_chart(symbol=<symbol>, interval=<htf_interval>)
   get_indicator(indicator_code="ema", symbol=<symbol>, interval=<htf_interval>)
   get_indicator(indicator_code="dmi", symbol=<symbol>, interval=<htf_interval>)
   ```
   Determine trend direction (HH/HL, LH/LL, or ranging), strength (ADX), and mark major S/R.

2. **Primary TF — find setup** aligned with HTF bias:
   ```
   generate_chart(symbol=<symbol>, interval=<primary_interval>)
   get_indicator(indicator_code="rsi", symbol=<symbol>, interval=<primary_interval>)
   get_indicator(indicator_code="macd", symbol=<symbol>, interval=<primary_interval>)
   ```
   If HTF bullish → look for bullish setups (pullbacks, OBs, demand zones). Mark setup zones.

3. **Lower TF — time the entry**:
   ```
   generate_chart(symbol=<symbol>, interval=<ltf_interval>)
   get_indicator(indicator_code="rsi", symbol=<symbol>, interval=<ltf_interval>)
   get_indicator(indicator_code="ema", symbol=<symbol>, interval=<ltf_interval>)
   ```
   Entry triggers: BOS in HTF direction, rejection candle at setup zone, RSI divergence, volume spike.

4. **Score and report**: calculate signal priority score, report HTF bias + primary setup + LTF confirmation + score + recommended action + key levels marked on chart.

## Key Rules

- NEVER trade LTF signals against HTF trend; a 15m bullish signal means nothing if the daily is bearish
- NEVER skip HTF analysis; the extra time checking HTF prevents chasing bad trades
- NEVER use more than 3 timeframes; a 4th or 5th adds confusion, not clarity
- NEVER force trades in ranging HTF; when HTF has no clear trend, wait for directional bias
- Use **market-regime-detection** skill to classify the regime before applying MTF weights; regime determines which timeframe dominates

## Related Skills

- **market-regime-detection** — classify regime before applying MTF; regime determines which TF dominates
- **fibonacci-trading** — use Fib across timeframes for precise entry and target levels
