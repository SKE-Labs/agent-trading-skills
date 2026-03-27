---
name: optimal-trade-entry
description: Execute Optimal Trade Entry (OTE) using Fibonacci retracement between 62-79%. Use when entering after structure breaks, timing entries on pullbacks, or finding high-probability retracement levels.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Optimal Trade Entry (OTE)

The sweet spot retracement zone (62%-79% Fib) where smart money typically enters positions.

## OTE Zone Levels

| Fib Level | Significance             |
| --------- | ------------------------ |
| 61.8%     | Start of OTE zone        |
| 70.5%     | Midpoint (CE equivalent) |
| 79%       | End of OTE zone          |

Use after: BOS/CHoCH pullbacks, liquidity sweeps, trending move continuations.

## Workflow

1. **Identify the impulse** -- a strong displacement move with clear swing low to swing high (or vice versa):
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```
2. **Draw Fibonacci** using `draw_chart_analysis` with `fib_retracement`:
   - Bullish: Point 1 = swing low, Point 2 = swing high
   - Bearish: Point 1 = swing high, Point 2 = swing low
3. **Calculate OTE zone** from the swing range:
   - OTE Start: Swing High - Range * 0.618
   - OTE Mid: Swing High - Range * 0.705
   - OTE End: Swing High - Range * 0.79
4. **Mark OTE zone** using `draw_chart_analysis` with `demand` (bullish) or `supply` (bearish)
5. **Enter** at 70.5% midpoint (limit order) or wait for price action confirmation in zone
6. **Stop loss** beyond the 100% level (swing point)
7. **Target** extension levels: -27% (1.27x), -62% (1.62x), or the impulse origin (0%)

### Example Calculation

High=52000, Low=45000, Range=7000:
- OTE Start (61.8%): 47,674
- OTE Mid (70.5%): 47,065
- OTE End (79%): 46,470

## Key Rules

- Best OTE entries have an order block or FVG within the 62-79% zone (confluence)
- NEVER enter an OTE against HTF bias
- NEVER use OTE without a preceding impulsive displacement move
- Entry at 70.5% yields minimum ~2.3 R:R to the impulse origin; extension targets improve this significantly

## Related Skills

- **order-blocks** — Best OTE entries have an OB within the 62-79% zone
- **premium-discount** — OTE in discount for longs, premium for shorts maximizes probability
