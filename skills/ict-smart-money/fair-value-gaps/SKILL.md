---
name: fair-value-gaps
description: Trade fair value gaps (FVG) and imbalances where price moved too fast, leaving unfilled zones. Use when identifying retracement targets, finding high-probability entry points, or analyzing institutional order flow imbalances.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Fair Value Gaps (FVG) Trading

3-candle patterns where price left an unfilled gap between wicks, indicating market inefficiency.

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

- **Size**: Large gap (>50% of middle candle) is high quality; small gaps are weak
- **Context**: After a liquidity sweep is ideal; random location is weak
- **Volume**: High volume on creation; low volume = unreliable
- **HTF**: Must align with HTF bias

## Workflow

1. **Identify FVG** after impulsive move using candle data:
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```
2. **Mark the zone** using `draw_chart_analysis` with type `demand` (bullish) or `supply` (bearish)
3. **Wait for retracement** into the gap
4. **Enter at Consequent Encroachment (CE)** — the 50% midpoint of the FVG for the most precise entry
5. **Stop loss** beyond the full FVG boundary
6. **Target** the high/low of the impulse move

### FVG + Order Block Confluence

When an FVG overlaps with an order block, treat as a single high-probability zone. These are the best setups.

## Key Rules

- FVGs act as magnets — price tends to return to fill them
- Unfilled FVGs on HTF are powerful future targets
- Multiple stacked FVGs in one direction = strong directional bias
- NEVER trade an FVG against the HTF trend direction
- CE (50% midpoint) offers the best entry; waiting for full fill risks missing the move

## Related Skills

- **order-blocks** — FVG + OB confluence creates highest-probability zones
- **premium-discount** — Enter FVGs in discount for longs, premium for shorts
