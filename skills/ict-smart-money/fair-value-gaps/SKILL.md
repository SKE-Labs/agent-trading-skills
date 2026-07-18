---
name: fair-value-gaps
description: Detect and test three-candle fair-value-gap zones. Use when the user wants an objective wick-gap definition, retracement statistics, entry, invalidation, and cost-aware validation.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Fair Value Gaps (FVG) Trading

A three-candle wick-gap convention. The pattern is observable in OHLC data; calling it inefficiency or institutional imbalance requires separate order-book/trade evidence.

## Identification

### Bullish FVG

1. Strong bullish middle candle
2. Gap between **Candle 1 high** and **Candle 3 low**
3. Zone = the unfilled gap area

### Bearish FVG

1. Strong bearish middle candle
2. Gap between **Candle 1 low** and **Candle 3 high**
3. Zone = the unfilled gap area

### Quality Factors

- Normalize gap size by ATR, spread, and middle-candle range.
- Record preceding swing/sweep, time-of-day relative volume, and higher-timeframe state as features.
- Calibrate thresholds and interactions; do not convert them into untested quality labels.

## Workflow

1. **Identify FVG** after impulsive move using candle data:
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
   ```
2. **Mark the zone** using `draw_chart_analysis` with type `demand` (bullish) or `supply` (bearish)
3. **Wait for retracement** into the gap
4. **Choose an entry rule** — near boundary, midpoint, full traversal, or price confirmation; select in training data only
5. **Stop loss** beyond the full FVG boundary
6. **Target** the high/low of the impulse move

### FVG + Order Block Confluence

Record overlap with a separately defined order-block zone and test whether it adds value over FVG alone; the labels are correlated price-derived features.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: The three-candle definition follows the [ICT convention](https://www.theinnercircletraders.com/fair-value-gaps-vs-order-blocks/), but independent market-microstructure research links price changes to observable order-flow imbalance and depth—not to guaranteed gap fills.

## Key Rules

- Estimate touch and fill rates with a fixed horizon and competing-risk rule; do not call gaps magnets.
- Expire zones after a predeclared time and retain unfilled zones in the denominator.
- Test stacked gaps and higher-timeframe alignment rather than assuming directional strength.
- The midpoint is a coordinate, not an empirically privileged entry.

## Related Skills

- **order-blocks** — test overlap between two explicitly defined candle-zone conventions
- **premium-discount** — Enter FVGs in discount for longs, premium for shorts
