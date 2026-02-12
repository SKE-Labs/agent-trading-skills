---
name: order-blocks
description: Identify bullish and bearish order blocks where institutional orders were executed. Use when analyzing price action for high-probability entry zones, detecting smart money accumulation/distribution, or finding areas where price may react on retest.
---

# Order Blocks Trading

Order blocks are price zones where significant institutional buy/sell orders executed, leaving "footprints" for future price reactions.

## Identification

### Bullish Order Block

1. Find the **last bearish candle** before a strong upward move
2. The move must break previous structure (higher high)
3. Zone = open to low of that bearish candle

### Bearish Order Block

1. Find the **last bullish candle** before a strong downward move
2. The move must break previous structure (lower low)
3. Zone = open to high of that bullish candle

## Validation Criteria

| Criteria           | Requirement                                     |
| ------------------ | ----------------------------------------------- |
| Displacement       | Strong impulsive move away (3+ candles)         |
| Break of Structure | Must break previous swing high/low              |
| Freshness          | Untested (first return has highest probability) |
| HTF Alignment      | Should align with higher timeframe bias         |

## Entry Workflow

1. **Mark the zone** on chart using `draw_chart_analysis` with type `demand` (bullish) or `supply` (bearish)
2. **Wait for price to return** to the order block zone
3. **Confirm entry** with:
   - Lower timeframe structure shift
   - Rejection wicks
   - Volume increase
4. **Set stop loss** below/above the order block
5. **Target** next opposing order block or liquidity level

## Risk Management

- Stop loss: 5-10 pips beyond the order block
- Risk per trade: 1-2% max
- Target: Minimum 1:2 R:R

## Common Mistakes

- Trading mitigated (already tested) order blocks
- Ignoring higher timeframe context
- No confirmation before entry
