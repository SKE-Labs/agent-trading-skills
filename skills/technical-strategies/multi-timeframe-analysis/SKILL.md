---
name: multi-timeframe-analysis
description: Analyze markets using 3 timeframes with signal priority scoring and conflict resolution. Use when determining trend direction, timing entries with precision, or validating trade setups across timeframes. Uses only free indicators (EMA slope, RSI, MACD) — avoids API-billed ADX/DMI.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "3.0"
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

1. **Higher TF — establish bias** via EMA stack + slope (no ADX — use the canonical slope computation). `get_indicators` returns one indicator per call — fetch each separately:
   ```
   get_candles(symbol=<symbol>, exchange=<exchange>, interval=<htf_interval>, count=120)
   get_indicators(indicator_code="ema_21", symbol=<symbol>, exchange=<exchange>, interval=<htf_interval>, count=120)
   get_indicators(indicator_code="ema_50", symbol=<symbol>, exchange=<exchange>, interval=<htf_interval>, count=120)
   get_indicators(indicator_code="atr_14", symbol=<symbol>, exchange=<exchange>, interval=<htf_interval>, count=120)
   get_indicators(indicator_code="donchian_20", symbol=<symbol>, exchange=<exchange>, interval=<htf_interval>, count=120)
   ```
   Then compute trend strength via slope %:
   ```
   execute python3 -c "ema50=[<...>]; s=(ema50[-1]-ema50[-5])/ema50[-5]*100; print(f'htf_ema50_slope_pct={s:.3f}')"
   ```
   - `slope > +0.5%` and `ema_21 > ema_50` → HTF bullish
   - `slope < −0.5%` and `ema_21 < ema_50` → HTF bearish
   - `|slope| ≤ 0.15%` → HTF ranging (skip directional entries; range-trading playbook only)

   Mark major HTF S/R: prior swing pivots, donchian_20 boundaries, Fibonacci extensions, weekly open / prior week high-low.

2. **Primary TF — find setup** aligned with HTF bias:
   ```
   get_candles(symbol=<symbol>, exchange=<exchange>, interval=<primary_interval>, count=60)
   get_indicators(indicator_code="ema_9",   symbol=<symbol>, exchange=<exchange>, interval=<primary_interval>, count=60)
   get_indicators(indicator_code="ema_21",  symbol=<symbol>, exchange=<exchange>, interval=<primary_interval>, count=60)
   get_indicators(indicator_code="ema_50",  symbol=<symbol>, exchange=<exchange>, interval=<primary_interval>, count=60)
   get_indicators(indicator_code="rsi_21",  symbol=<symbol>, exchange=<exchange>, interval=<primary_interval>, count=60)
   get_indicators(indicator_code="macd_fast", symbol=<symbol>, exchange=<exchange>, interval=<primary_interval>, count=60)
   get_indicators(indicator_code="atr_14",  symbol=<symbol>, exchange=<exchange>, interval=<primary_interval>, count=60)
   ```
   If HTF bullish → look for bullish setups (pullbacks to ema_21 / ema_50 / 50-61.8% Fib, demand zones, order blocks). Mark setup zones.

   Cite the RSI / MACD slope as a 3–5 value progression (latest value alone is folklore):
   - `RSI21 53.2 (49.8 → 51.4 → 52.9 → 53.2) rising` ← evidence of momentum continuation
   - `MACD hist +8.4 (−1.2 → +3.6 → +8.4) accelerating bull` ← evidence of impulse

3. **Lower TF — time the entry**:
   ```
   get_candles(symbol=<symbol>, exchange=<exchange>, interval=<ltf_interval>, count=20)
   get_indicators(indicator_code="rsi_21",    symbol=<symbol>, exchange=<exchange>, interval=<ltf_interval>, count=20)
   get_indicators(indicator_code="macd_fast", symbol=<symbol>, exchange=<exchange>, interval=<ltf_interval>, count=20)
   get_indicators(indicator_code="atr_14",    symbol=<symbol>, exchange=<exchange>, interval=<ltf_interval>, count=20)
   ```
   Entry triggers (any ONE confirmed at LTF candle close):
   - **BOS in HTF direction** — break of structure on LTF (HH for long, LL for short)
   - **Rejection candle at setup zone** — engulfing, hammer, pin
   - **RSI hook back toward midline** from extreme (e.g. RSI 36 → 42 in 2 bars after a pullback)
   - **MACD histogram flip** in HTF direction after a reset

   The LTF candle must be **closed** (not forming) before counting it as a trigger.

4. **Score and report**: calculate signal priority score, report HTF bias (with slope %) + primary setup + LTF confirmation + score + recommended action + key levels marked.

## Key Rules

- NEVER trade LTF signals against HTF trend; a 15m bullish signal means nothing if the daily is bearish
- NEVER skip HTF analysis; the extra time checking HTF prevents chasing bad trades
- NEVER use more than 3 timeframes; a 4th or 5th adds confusion, not clarity
- NEVER force trades in ranging HTF; when HTF has no clear trend, wait for directional bias
- Use the EMA slope % (computed via `execute`) as the HTF bias gate; do NOT call ADX / DMI / Supertrend (API-billed, not in the free whitelist)
- Use **market-regime-detection** skill to classify the regime before applying MTF weights; regime determines which timeframe dominates

## Related Skills

- **market-regime-detection** — classify regime before applying MTF; regime determines which TF dominates
- **fibonacci-trading** — use Fib across timeframes for precise entry and target levels
