---
name: optimal-trade-entry
description: Define and test the ICT Optimal Trade Entry retracement convention. Use when measuring whether a 62–79% pullback region adds value after an objectively defined impulse.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Optimal Trade Entry (OTE)

The ICT convention labels a 62–79% retracement region as OTE. Treat it as a candidate coordinate band; candles do not reveal where "smart money" entered, and empirical evidence does not support special standalone Fibonacci power.

## OTE Zone Levels

| Fib Level | Convention |
| --------- | ------------------------ |
| 61.8%     | Start of OTE zone        |
| 70.5%     | Arithmetic midpoint of 61.8% and 79% |
| 79%       | End of OTE zone          |

Use after: BOS/CHoCH pullbacks, liquidity sweeps, trending move continuations.

## Workflow

1. **Identify the impulse** -- a strong displacement move with clear swing low to swing high (or vice versa):
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
   ```
2. **Draw Fibonacci** using `draw_chart_analysis` with `fib_retracement`:
   - Bullish: Point 1 = swing low, Point 2 = swing high
   - Bearish: Point 1 = swing high, Point 2 = swing low
3. **Calculate OTE zone** from the swing range:
   - OTE Start: Swing High - Range * 0.618
   - OTE Mid: Swing High - Range * 0.705
   - OTE End: Swing High - Range * 0.79
4. **Mark OTE zone** using `draw_chart_analysis` with `demand` (bullish) or `supply` (bearish)
5. **Test entry choices** at the boundary, midpoint, full traversal, or an objective confirmation; do not privilege 70.5% without evidence
6. **Stop loss** beyond the 100% level (swing point)
7. **Set target** from objective structure/time logic; extensions are candidate coordinates only

### Example Calculation

High=52000, Low=45000, Range=7000:
- OTE Start (61.8%): 47,674
- OTE Mid (70.5%): 47,065
- OTE End (79%): 46,470

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: Empirical [Fibonacci research](https://www.sciencedirect.com/science/article/abs/pii/S0957417421012495) found Fibonacci zones did not outperform non-Fibonacci zones as standalone rules; treat 62–79% as a candidate region only.

## Key Rules

- Define the impulse endpoints without hindsight and normalize displacement by ATR/bars.
- Test higher-timeframe state, order-block, and FVG overlap as correlated candidate features.
- Compare the 62–79% region with equal-width non-Fibonacci and continuous-retracement baselines.
- Compute R:R from the actual entry, stop, target, side, and costs; no coordinate guarantees a minimum R:R.

## Related Skills

- **order-blocks** — test whether a separately defined candle zone adds information to the OTE band
- **premium-discount** — OTE in discount for longs, premium for shorts maximizes probability
