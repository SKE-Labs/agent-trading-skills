---
name: market-structure-shift
description: Detect Break of Structure (BOS) and Change of Character (CHoCH) for trend analysis. Use when identifying trend reversals, confirming entry signals, or determining market bias direction.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Market Structure Shift

Identify trend direction and potential reversals through swing point analysis.

## Structure

### Swing Points
- **Higher High (HH)** + **Higher Low (HL)** = Uptrend
- **Lower Low (LL)** + **Lower High (LH)** = Downtrend

Choose an objective swing algorithm before analysis—for example, a pivot with fixed left/right bars or an ATR-reversal rule. State how equal highs/lows, nested swings, and the unconfirmed final pivot are handled.

### Break of Structure (BOS)
- Descriptive continuation label under the chosen swing rule
- **Bullish BOS**: Price breaks above swing high (HH)
- **Bearish BOS**: Price breaks below swing low (LL)

### Change of Character (CHoCH)
- Descriptive possible-change label, not confirmation of reversal
- **Bullish CHoCH**: In downtrend, price breaks above LH
- **Bearish CHoCH**: In uptrend, price breaks below HL

## Workflow

1. **Identify current trend** on a predeclared context timeframe:
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval="4h", date=<date>)
   ```
2. **Mark swing points** using `draw_chart_analysis` with `highlight` type (label HH, HL, LH, LL)
3. **Detect structure breaks** only after a closed bar exceeds the pivot by a calibrated tick/ATR buffer.
4. **Map nested timeframes** with exact ratios and timestamps. If context and execution structure conflict, return `watch` or `no trade`; do not force alignment.

### Trend Continuation Entry (BOS)
1. Wait for the closed-bar BOS trigger
2. Enter on pullback to FVG or order block
3. Stop below recent swing low (bull) or above swing high (bear)

### Trend Reversal Entry (CHoCH)
1. Treat HTF CHoCH as a candidate reversal condition
2. Wait for LTF BOS in the new direction
3. Enter on retracement to CHoCH level
4. Stop beyond the CHoCH swing point

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: Use BOS/CHoCH as explicit swing-labeling rules. [Lo, Mamaysky & Wang](https://www.nber.org/papers/w7613) shows why visual price patterns must be algorithmically defined and tested.

## Key Rules

- The context timeframe supplies a feature, not an immutable direction.
- Never use an unconfirmed right-edge pivot or intrabar break.
- Predeclare whether a single close, retest, or second-timeframe event is required; avoid future leakage.
- Select timeframes for the instrument/session and test nested conflicts explicitly.

## Related Skills

- **order-blocks** — define and test candle zones around objective structure events
- **liquidity-zones** — Structure breaks often occur after liquidity sweeps of swing points
