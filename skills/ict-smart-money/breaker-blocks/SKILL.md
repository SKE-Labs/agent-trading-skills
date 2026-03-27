---
name: breaker-blocks
description: Trade failed order blocks that flip into breaker patterns. Use when a previous support becomes resistance (or vice versa), identifying high-probability reversal zones after structure breaks.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Breaker Blocks Trading

Failed order blocks that flip polarity -- bullish OB becomes bearish resistance, bearish OB becomes bullish support.

## Identification

### Bullish Breaker (Failed Bearish OB)
1. Bearish order block forms
2. Price returns and breaks **through** the OB aggressively (displacement)
3. The broken OB flips to support (bullish breaker)
4. Trade longs when price returns to this zone

### Bearish Breaker (Failed Bullish OB)
1. Bullish order block forms
2. Price returns and breaks **through** the OB aggressively (displacement)
3. The broken OB flips to resistance (bearish breaker)
4. Trade shorts when price returns to this zone

### Quality Criteria

- **Break strength**: Impulsive, 3+ candles (not slow grinding)
- **FVG created**: Yes, on the break = strong; no FVG = weak
- **HTF alignment**: Must match HTF direction
- **Freshness**: First retest only; multiple tests weaken the zone

## Workflow

1. **Find a failed order block** using candle data:
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```
2. **Confirm the break** with CHoCH or BOS through the original OB
3. **Mark the breaker zone** using `draw_chart_analysis` with `demand` (bullish) or `supply` (bearish)
4. **Wait for price to return** to the zone from the opposite side
5. **Enter with LTF confirmation** (structure shift or rejection)
6. **Stop loss** beyond the breaker zone
7. **Target** next liquidity level or POI

## Key Rules

- Breakers work because traders trapped at the original OB provide fuel for the new direction
- NEVER trade a breaker without an impulsive break through the original OB
- NEVER trade a breaker that has already been retested
- The break must create displacement; a slow grind through the OB is not a valid breaker

## Related Skills

- **order-blocks** — Breakers are failed OBs; understanding OBs is prerequisite
- **fair-value-gaps** — FVGs created during the break add confluence to breaker zones
