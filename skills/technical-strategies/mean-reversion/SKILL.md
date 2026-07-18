---
name: mean-reversion
description: Test whether a price or spread reverts toward a modeled center. Use when evaluating stationarity, half-life, z-score bands, regime breaks, time stops, and net execution costs.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Mean Reversion

Mean reversion is a hypothesis that a specified price/spread process returns toward a modeled center fast enough to overcome costs. Verify stationarity or stable conditional behavior before trading; an individual price level may trend indefinitely.

## Detection Methods

### Z-Score

`Z-Score = (Series - rolling mean) / rolling standard deviation`. Select the series, lookback, entry/exit bands, and time stop in training data. A z-score is descriptive and is not normally distributed by assumption.

| Z-Score | Signal |
| --- | --- |
| Positive extreme | Candidate short only if reversion model passes |
| Near center | No new extreme under the chosen rule |
| Negative extreme | Candidate long only if reversion model passes |

### Bollinger Band Method

- Band touch/pierce + reversal candle → trade toward middle band
- Test band, RSI, and reversal features for incremental value; they are correlated price transforms

### RSI Extreme Method

Calibrate RSI percentiles/bands to the instrument and regime; no fixed threshold creates a buy or sell.

## Regime and Stationarity Gate

Use an objective, calibrated regime/stationarity gate. ADX can be one feature but does not establish mean reversion or set size.

## Workflow

1. **Check regime** (must pass first):
   ```
   get_indicators(indicator_code="dmi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   ```
   Apply the frozen regime and stationarity gates; return `no trade` when either fails.

2. **Get BB and RSI**:
   ```
   get_indicators(indicator_code="bbands", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   get_indicators(indicator_code="rsi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   get_indicators(indicator_code="ema", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   ```

3. **Get candles** for confirmation:
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
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

5. **Exits**: predeclare center, partial-center, opposite-band, stop, and maximum-holding-time variants; retain only net-positive held-out logic without universal win rates.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: Mean reversion is a model assumption, not a universal property. [Optimal mean-reversion research](https://arxiv.org/abs/2003.10502) derives thresholds under an Ornstein–Uhlenbeck process; verify that the spread is stationary before applying them.

## Key Rules

- Never assume a series mean reverts; verify the process and monitor parameter/stationarity breaks.
- NEVER enter on BB touch alone; require confirmation candle (engulfing, hammer, doji)
- Compare center and opposite-band exits rather than assigning realism beforehand.
- A squeeze is compression, not proof that a breakout is coming.
- Do not count BB, RSI, and z-score as independent confirmation.
- Use a time stop tied to estimated half-life and exit on a stationarity/regime break.
- If price is at lower BB due to fundamental repricing (earnings, news), it is not "oversold"

## Related Skills

- **bollinger-bands** — BB touches are the primary visual mean reversion signal
- **market-regime-detection** — supply a calibrated regime feature and uncertainty state
