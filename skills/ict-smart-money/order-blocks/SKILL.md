---
name: order-blocks
description: Identify bullish and bearish order blocks where institutional orders were executed. Use when analyzing price action for high-probability entry zones, detecting smart money accumulation/distribution, or finding areas where price may react on retest.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Order Blocks Trading

Institutional buy/sell zones that leave footprints for future price reactions.

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

- **Displacement**: Strong impulsive move away (3+ candles)
- **Break of Structure**: Must break previous swing high/low
- **Freshness**: Untested (first return has highest probability)
- **HTF Alignment**: Should align with higher timeframe bias

## Workflow

1. **Identify** the order block on HTF (4H/Daily) for bias, LTF (15m/5m) for entry
2. **Get candle data** around the zone:
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```
3. **Mark the zone** using `draw_chart_analysis` with type `demand` (bullish) or `supply` (bearish)
4. **Wait for price to return** to the order block zone
5. **Confirm entry** with LTF structure shift, rejection wicks, or volume increase
6. **Stop loss** below/above the order block
7. **Target** next opposing order block or liquidity level

## Key Rules

- Only trade the **first retest** of an order block; mitigated OBs lose their edge
- NEVER enter without HTF alignment confirming direction
- NEVER enter without LTF confirmation (structure shift or rejection)
- Displacement must be impulsive (3+ candles); slow grinds are not valid OBs

## Related Skills

- **fair-value-gaps** — FVG + OB confluence creates highest-probability zones
- **market-structure-shift** — BOS/CHoCH confirms the displacement that validates an OB
