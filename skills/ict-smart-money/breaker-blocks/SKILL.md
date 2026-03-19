---
name: breaker-blocks
description: Trade failed order blocks that flip into breaker patterns. Use when a previous support becomes resistance (or vice versa), identifying high-probability reversal zones after structure breaks.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending"]
---

# Breaker Blocks Trading

Breaker blocks are failed order blocks that flip polarity—bullish becomes bearish resistance, bearish becomes bullish support.

## How Breakers Form

### Bullish Breaker (Failed Bearish OB)

1. Bearish order block forms
2. Price returns and breaks THROUGH the OB
3. The broken OB becomes support (bullish breaker)
4. Trade longs when price returns to this zone

### Bearish Breaker (Failed Bullish OB)

1. Bullish order block forms
2. Price returns and breaks THROUGH the OB
3. The broken OB becomes resistance (bearish breaker)
4. Trade shorts when price returns to this zone

## Identification Steps

1. **Find a failed order block**:

   - OB that was broken through aggressively
   - Must have displacement (strong move)

2. **Mark the breaker zone**:

   - The original OB range becomes the breaker
   - Draw using `demand` (bullish) or `supply` (bearish)

3. **Wait for retest**:
   - Price returns to breaker from the opposite side
   - Previous resistance now acts as support (vice versa)

## Quality Criteria

| Factor         | Strong Breaker        | Weak Breaker   |
| -------------- | --------------------- | -------------- |
| Break strength | Impulsive, 3+ candles | Slow, grinding |
| FVG created    | Yes, on the break     | No FVG         |
| HTF alignment  | Matches HTF direction | Against HTF    |
| First retest   | Untested              | Multiple tests |

## Entry Workflow

1. **Identify original order block**
2. **Confirm break** with CHoCH or BOS
3. **Mark the breaker zone**
4. **Wait for price to return** to the zone
5. **Enter with confirmation** (LTF structure, rejection)
6. **Stop loss** beyond the breaker zone
7. **Target** next liquidity or POI

## Key Insight

Breaker blocks work because:

- Traders who bought/sold at the OB are now trapped
- Their stop losses provide fuel for the new direction
- Smart money flips the level, using trapped traders

## Related Skills

- **order-blocks** — Breaker blocks are failed order blocks; understanding OBs is prerequisite to identifying breakers
- **fair-value-gaps** — FVGs created during the break through the original OB add confluence to breaker zones
- **market-structure-shift** — CHoCH/BOS confirms the break that creates the breaker block
