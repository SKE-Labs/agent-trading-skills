---
name: rsi-divergence
description: Define and test RSI divergence at confirmed price pivots. Use when aligning exact pivot timestamps, spacing, equality tolerances, oscillator zones, closed-bar entry, and invalidation.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# RSI Divergence Trading

RSI divergence is a geometric relationship between confirmed price pivots and RSI values at the same timestamps. It is a candidate feature, not a reversal signal by itself.

## Divergence Types

### Regular (Reversal)

| Type        | Price Action | RSI Action | Signal      |
| ----------- | ------------ | ---------- | ----------- |
| **Bullish** | Lower Low | Higher Low | Candidate bullish regular divergence |
| **Bearish** | Higher High | Lower High | Candidate bearish regular divergence |

### Hidden (Continuation)

| Type        | Price Action | RSI Action  | Signal               |
| ----------- | ------------ | ----------- | -------------------- |
| **Bullish** | Higher Low   | Lower Low   | Trend continues up   |
| **Bearish** | Lower High   | Higher High | Trend continues down |

## RSI Zones

| Level | Interpretation |
| ----- | -------------- |
| High percentile/band | Context for bearish candidates; calibrate |
| Low percentile/band | Context for bullish candidates; calibrate |
| Mid-range | Descriptive only; test rather than discard universally |

## Workflow

1. **Get RSI**:
   ```
   get_indicators(indicator_code="rsi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   ```

2. **Identify confirmed pivots** with fixed left/right bars or an ATR-reversal rule; exclude the unconfirmed right edge

3. **Compare exact timestamps**: sample RSI at the two price pivots and apply predeclared price/RSI equality tolerances and pivot-spacing limits.

4. **Get candles** for chart marking:
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
   ```

5. **Mark divergence**:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "trend",
       "points": [
           {"time": <first_swing_time>, "price": <first_swing_price>},
           {"time": <second_swing_time>, "price": <second_swing_price>}
       ],
       "options": {"text": "Bullish RSI Divergence"}
   })
   ```

6. **Wait for confirmation candle** (engulfing, hammer, pin bar) at divergence zone before entry

### Entry

- **Bullish**: enter above confirmation candle at support; stop below swing low; target previous resistance
- **Bearish**: enter below confirmation candle at resistance; stop above swing high; target previous support

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: The [technical-rule evidence](https://pmc.ncbi.nlm.nih.gov/articles/PMC4583561/) shows oscillator results vary materially across markets and often weaken after costs; RSI extremes and divergence spacing require calibration.

## Key Rules

- Define any support/resistance and entry trigger objectively before evaluation.
- Enter only from the specified closed-bar trigger; divergence alone is `watch`.
- Test timeframe interactions; no 1H minimum is universally reliable.
- Calibrate optional RSI zones and pivot spacing by instrument/regime.
- Do not convert correlated price/structure features into a high-probability claim without calibration.

## Related Skills

- **divergence-trading** — extends RSI divergence with multi-indicator scoring (MACD, Stochastic, OBV)
- **macd-trading** — MACD divergence combined with RSI divergence strengthens reversal signals
