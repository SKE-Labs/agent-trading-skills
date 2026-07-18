---
name: premium-discount
description: Measure price location within a chosen swing range using ICT premium/discount terminology. Use when testing whether above/below-midpoint location adds value to an existing directional setup.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Premium & Discount Trading

This convention labels price above a selected range midpoint "premium" and below it "discount." It describes relative location, not fundamental value, equilibrium, or an obligation to oscillate.

## Core Concept

**Equilibrium** = (Swing High + Swing Low) / 2

| Zone            | Location  | Action                 |
| --------------- | --------- | ---------------------- |
| **Premium** | Above 50% | Upper half of selected range |
| **Midpoint** | At 50% | Arithmetic midpoint |
| **Discount** | Below 50% | Lower half of selected range |

### Trading Zones
- Test long and short filters separately; below/above 50% is not an entry by itself.
- If evaluating OTE, compare the Fibonacci band with continuous location and equal-width control bands.

## Workflow

1. **Identify the swing range** using a fixed pivot/timeframe algorithm and only information available at the timestamp:
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval="1d", date=<date>)
   ```
2. **Draw Fibonacci** using `draw_chart_analysis` with `fib_retracement` (0% = Swing High, 100% = Swing Low)
3. **Determine current position**: Above 50% = Premium, Below 50% = Discount
4. **Mark levels** using `draw_chart_analysis`: equilibrium with `support`/`resistance`, OTE zone with `demand`/`supply`
5. **Combine with a separately defined direction hypothesis** and report conflicts.
6. **Apply a predeclared entry trigger**; range location alone is `watch`, not a trade.
7. **Use a fixed execution timeframe** and closed bars; avoid hindsight swing changes.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: Empirical [Fibonacci research](https://www.sciencedirect.com/science/article/abs/pii/S0957417421012495) does not support special standalone bounce power for retracement ratios; the 50% split is a descriptive range location, not fundamental value.

## Key Rules

- Do not infer institutional accumulation/distribution or a "retail trap" from range location.
- Permit both directions in either half when a separately validated strategy does; test the filter incrementally.
- State range endpoints, confirmation status, timeframe, and midpoint explicitly.
- Treat 50% as arithmetic, not an empirical decision boundary or fair value.

## Related Skills

- **optimal-trade-entry** — OTE provides the precise entry within premium/discount zones
- **market-structure-shift** — Structure determines whether to look for entries in premium or discount
