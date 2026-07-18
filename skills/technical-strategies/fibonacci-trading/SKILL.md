---
name: fibonacci-trading
description: Measure Fibonacci retracement and extension coordinates over objective swings. Use when testing candidate pullback/target bands against non-Fibonacci controls rather than assuming special bounce levels.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Fibonacci Trading

Fibonacci ratios provide a reproducible coordinate grid over a chosen swing. Empirical evidence does not support special standalone bounce power; use them only as candidate features or chart labels.

## Levels

### Retracement (Entries)

| Level | Use                      |
| ----- | ------------------------ |
| 23.6% | Shallow pullback         |
| 38.2% | Moderate pullback        |
| 50.0% | Half retracement         |
| 61.8% | Fibonacci-derived coordinate |
| 78.6% | Deep pullback            |

**Formula**: `Retracement = High - Range * Ratio` (where Range = High - Low)

### Extension (Targets)

| Level  | Use                 |
| ------ | ------------------- |
| 127.2% | Candidate extension coordinate |
| 161.8% | Candidate extension coordinate |
| 200%   | Range multiple coordinate |
| 261.8% | Candidate extension coordinate |

**Formula**: `Extension = High + Range * Ratio` (e.g., 127.2% = High + Range * 0.272)

## Drawing Rules

- **Bullish measurement**: draw from an objectively confirmed swing low to high.
- **Bearish measurement**: draw from an objectively confirmed swing high to low.
- A coordinate is not an entry/target until a separately specified rule selects it.

## Workflow

1. **Get candle data** around the swing:
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<swing_date>)
   ```

2. **Draw Fibonacci retracement** on chart (auto-renders all standard levels):
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "fib_retracement",
       "points": [
           {"time": <swing_low_timestamp>, "price": <swing_low_price>},
           {"time": <swing_high_timestamp>, "price": <swing_high_price>}
       ],
       "options": {"text": "Fib Retracement"}
   })
   ```

3. **Check confluence** with indicators:
   ```
   get_indicators(indicator_code="rsi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   get_indicators(indicator_code="macd", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   ```

4. **Mark confluence zones** where Fib levels overlap with other structures:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "demand",
       "points": [
           {"time": <zone_start_time>, "price": <zone_top>},
           {"time": <zone_end_time>, "price": <zone_bottom>}
       ],
       "options": {"text": "61.8% + OB"}
   })
   ```

5. **Apply a testable trigger**: define rejection/structure numerically and compare Fibonacci overlap with equal-width non-Fibonacci controls

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: A multi-market [empirical study](https://www.sciencedirect.com/science/article/abs/pii/S0957417421012495) found bounce rates at Fibonacci zones statistically indistinguishable from non-Fibonacci zones and no standalone outperformance.

## Key Rules

- Define swing pivots, confirmation delay, and range before viewing the outcome.
- Do not trade a Fibonacci coordinate alone or assume confluence creates independent evidence.
- Never privilege 61.8% without held-out incremental results.
- Place invalidation where the underlying price thesis fails, then size accordingly.
- Set exits from tested structure/time rules; extensions are chart coordinates only.

## Related Skills

- **supply-demand-zones** — test whether retracement coordinates overlap with objectively defined candle zones
- **multi-timeframe-analysis** — use Fib across timeframes for precise entry and target levels
