---
name: bollinger-bands
description: Define and test Bollinger bandwidth, percent-b, squeeze, continuation, and mean-reversion rules. Use when measuring relative volatility and evaluating closed-band triggers without treating tags as signals.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Bollinger Bands Trading

Bollinger Bands measure volatility and identify potential reversals and breakouts.

## Components

| Band       | Calculation    | Meaning               |
| ---------- | -------------- | --------------------- |
| **Middle** | 20 SMA         | Trend baseline        |
| **Upper**  | SMA + k StdDev | Upper volatility envelope |
| **Lower**  | SMA - k StdDev | Lower volatility envelope |

**Band Width** = `(Upper - Lower) / Middle * 100`

## Signals

### Mean Reversion (Range Trading)

- A band tag is descriptive, not a reversal signal.
- Define regime, `%b`/distance, objective reversal trigger, invalidation, and middle-band target before testing.
- Calibrate any RSI or candlestick filter; both are derived from the same price history.

### Bollinger Squeeze (Breakout)

- Define a squeeze by rolling bandwidth percentile within the same instrument/session.
- A squeeze indicates low relative volatility, not that a breakout is imminent or directional.
- Test closed-band exit, retest, and volume rules with a fixed horizon.

### Band Riding (Trend Trading)

- Uptrend: price hugs upper band, pullbacks to middle band are entries
- Downtrend: price hugs lower band, rallies to middle band are entries

### W-Bottom / M-Top

- W-Bottom at lower band = bullish reversal
- M-Top at upper band = bearish reversal

## Workflow

1. **Get Bollinger Bands**:
   ```
   get_indicators(indicator_code="bbands", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   ```

2. **Calculate Band Width**: `(Upper - Lower) / Middle * 100`
   - Report rolling percentile and historical sample; do not use universal percentage cutoffs.

3. **Confirm with RSI**:
   ```
   get_indicators(indicator_code="rsi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   ```

4. **Identify setup**: band edge + reversal candle → mean reversion; squeeze + volume → breakout

5. **Mark on chart**:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "highlight",
       "points": [
           {"time": <start_time>, "price": <upper_band>},
           {"time": <end_time>, "price": <lower_band>}
       ],
       "options": {"text": "BB Squeeze (Width: 1.8%)"}
   })
   ```

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: John Bollinger's [22 rules](https://cmtassociation.org/technically_speaking/technically-speaking-march-2013/) state that band tags are not signals and outside closes are initially continuation—not reversal—signals.

## Key Rules

- Treat band expansion as a regime feature and test mean reversion/continuation separately.
- Never enter on a band tag alone; apply the predeclared price trigger.
- Define squeezes by an instrument-specific rolling percentile.
- Treat 20/2 as a conventional starting specification; record every lookback/multiplier tried.
- Per Bollinger's rules, an outside close is initially continuation information, not automatic reversal.

## Related Skills

- **mean-reversion** — adds z-score and RSI frameworks to BB touch signals
- **market-regime-detection** — BB Width is a key volatility input for regime classification
