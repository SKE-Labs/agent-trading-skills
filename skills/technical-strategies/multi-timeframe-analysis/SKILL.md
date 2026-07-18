---
name: multi-timeframe-analysis
description: Map context, setup, and execution states across fixed timeframes. Use when measuring normalized EMA slope, objective structure, closed-bar triggers, and aligned or conflicting states without hand-built confidence scores.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Multi-Timeframe Analysis (MTF)

Map context, setup, and execution states across fixed timeframes. Higher-timeframe information may help, but it does not automatically dominate; validate aligned and conflicting states separately.

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

## State Output

Report each timeframe as bullish, bearish, ranging, or uncertain under its objective rule. Combine them as `aligned`, `mixed`, `counter-context`, or `incomplete`. Do not turn a hand-built score into confidence or position size; size comes from portfolio risk.

## Conflict Resolution

| Conflict | Resolution |
| --- | --- |
| HTF bullish, Primary bearish | Label mixed; evaluate the predeclared mixed-state policy. |
| HTF bearish, LTF bullish | Label counter-context; trade only if that state is validated. |
| HTF ranging, Primary trending | Label mixed; do not map to arbitrary size. |
| All timeframes conflicting | **No trade.** Clarity is a prerequisite. |

When evidence is incomplete or a state was not validated, return `no trade`.

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
   Calibrate price/ATR-normalized slope bands in training data, then combine with the EMA stack. Absolute percentage thresholds are not portable across timeframes/assets.

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

4. **Report states**: show timestamps, normalized slope, context/setup/execution states, conflict label, closed-bar trigger, invalidation, and `valid`, `watch`, or `no trade`.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Lo, Mamaysky & Wang](https://www.nber.org/papers/w7613) supports objective conditional price-pattern analysis; timeframe weights and scores are heuristics that must be frozen before testing.

## Key Rules

- Test counter-context and aligned states rather than declaring one meaningless.
- Use higher-timeframe context only when it adds held-out value.
- Fix the number and ratios of timeframes before testing; more timeframes increase multiple-testing risk.
- Apply a predeclared policy to ranging/uncertain context.
- Use the EMA slope % (computed via `execute`) as the HTF bias gate; do NOT call ADX / DMI / Supertrend (API-billed, not in the free whitelist)
- Use **market-regime-detection** skill to classify the regime before applying MTF weights; regime determines which timeframe dominates

## Related Skills

- **market-regime-detection** — classify regime before applying MTF; regime determines which TF dominates
- **fibonacci-trading** — use Fib across timeframes for precise entry and target levels
