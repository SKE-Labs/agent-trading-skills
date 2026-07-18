---
name: divergence-trading
description: Define and test regular or hidden divergence at objective pivots. Use when aligning RSI, MACD, Stochastic, MFI, or volume features to exact price-pivot timestamps without counting correlated indicators as independent votes.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Divergence Trading

Divergence occurs when price and an indicator move in opposite directions, signaling potential trend change or continuation.

## Divergence Types

### Regular Divergence (Reversal)

| Type | Price | Indicator | Signal |
| --- | --- | --- | --- |
| **Bullish Regular** | Lower Low | Higher Low | Momentum weakening, potential reversal up |
| **Bearish Regular** | Higher High | Lower High | Momentum weakening, potential reversal down |

### Hidden Divergence (Continuation)

| Type | Price | Indicator | Signal |
| --- | --- | --- | --- |
| **Bullish Hidden** | Higher Low | Lower Low | Uptrend pullback ending, continuation up |
| **Bearish Hidden** | Lower High | Higher High | Downtrend rally ending, continuation down |

## Multi-Indicator Detection

| Indicator | Best For | Extreme Zone |
| --- | --- | --- |
| RSI | OB/OS exhaustion | <30 or >70 for regular div |
| MACD histogram | Momentum shifts | Compare histogram peaks/troughs with price |
| Stochastic | Ranging markets | <20 or >80 (skip mid-range div) |
| MFI (price/volume transform) | Volume-aware momentum | Define pivots and compare slopes |

RSI, MACD, and Stochastic are correlated transforms of price, while MFI also uses volume. Do not count them as independent votes or map the count to probability; compare each feature and any combination with a price-only baseline.

## Validation Rules

- Use an objective pivot algorithm with fixed left/right bars or ATR reversal and exclude the unconfirmed right-edge pivot.
- Calibrate minimum/maximum spacing and optional oscillator zones by instrument/timeframe.
- Match indicator values at the exact price-pivot timestamps; use closed data and specify equality tolerance.

## Workflow

1. **Get indicator data**:
   ```
   get_indicators(indicator_code="rsi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   get_indicators(indicator_code="macd", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   get_indicators(indicator_code="stoch", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   ```

2. **Compare swings**: For each indicator, identify last two significant peaks/troughs and compare direction vs price direction

3. **Evaluate**: report each divergence and contextual feature separately; use a numeric score only if calibrated on held-out labels.

4. **Get candles for chart drawing**:
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
   ```

5. **Mark divergence on chart**:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "trend",
       "points": [
           {"time": <first_low_time>, "price": <first_low_price>},
           {"time": <second_low_time>, "price": <second_low_price>}
       ],
       "options": {"text": "Bullish Divergence (RSI + MACD)"}
   })
   ```

6. **Wait for confirmation candle** (engulfing, hammer, pin bar) at the divergence zone before entry

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: The [technical-analysis evidence review](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID603481_code17745.pdf?abstractid=603481) finds mixed performance and common data-snooping problems; multiple correlated oscillators do not create independent confirmation.

## Key Rules

- Do not treat multiple price-derived oscillators as independent confirmation.
- Calibrate oscillator zones rather than declaring mid-range values meaningless.
- Define an objective closed-bar entry and invalidate beyond the second pivot plus buffer.
- Test timeframe and regime interactions; no timeframe is universally more reliable.
- Keep unresolved divergences and failures in the evaluation sample.
- Entry on confirmation candle close; stop beyond the second divergence swing point

## Related Skills

- **rsi-divergence** — focused RSI divergence framework; this skill extends it to multiple indicators
- **macd-trading** — MACD histogram divergence is one of the four indicators in multi-indicator scoring
