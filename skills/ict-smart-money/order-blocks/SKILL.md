---
name: order-blocks
description: Define and test ICT-style order-block candle zones. Use when labeling the last opposite candle before an objective displacement and structure break, without inferring hidden institutional orders.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Order Blocks Trading

A candle-zone heuristic conventionally defined before a displacement and structure break. OHLC data cannot establish that institutional orders remain there or caused a later reaction.

## Identification

### Bullish Order Block

1. Find the **last bearish candle** before a strong upward move
2. The move must break previous structure (higher high)
3. Zone = open to low of that bearish candle

### Bearish Order Block

1. Find the **last bullish candle** before a strong downward move
2. The move must break previous structure (lower low)
3. Zone = open to high of that bullish candle

### Validation

- **Displacement**: normalize return/range by ATR and elapsed bars
- **Break of Structure**: use an objective pivot and closed-bar buffer
- **Retest count/age**: record continuously and test first versus later returns
- **Context state**: define higher timeframe objectively and test its incremental value

## Workflow

1. **Identify** the zone with fixed timeframe, OHLC boundary, pivot, and displacement rules
2. **Get candle data** around the zone:
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
   ```
3. **Mark the zone** using `draw_chart_analysis` with type `demand` (bullish) or `supply` (bearish)
4. **Wait for price to return** to the order block zone
5. **Confirm entry** with LTF structure shift, rejection wicks, or volume increase
6. **Stop loss** below/above the order block
7. **Target** next opposing order block or liquidity level

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: Treat an order block as a reproducible candle-zone heuristic, not proof of unfilled institutional orders. [Order-flow research](https://arxiv.org/abs/1011.6402) relates price impact to observable imbalance and market depth.

## Key Rules

- Do not describe the zone as unfilled institutional inventory without order-level evidence.
- Test first and later retests with an expiry rule; keep failures in the sample.
- Define context and entry confirmation before evaluation and use closed bars.
- Quantify displacement in normalized units rather than a universal candle count.

## Related Skills

- **fair-value-gaps** — test overlap between two explicitly defined candle-zone conventions
- **market-structure-shift** — BOS/CHoCH confirms the displacement that validates an OB
