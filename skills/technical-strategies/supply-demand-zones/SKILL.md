---
name: supply-demand-zones
description: Identify institutional supply and demand zones for reversal entries. Use when finding high-probability bounce areas, understanding institutional order flow, or planning entries at key zones.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending", "ranging"]
---

# Supply & Demand Zone Trading

Supply and demand zones mark areas of institutional accumulation (demand) and distribution (supply).

## Zone Identification

### Demand Zone (Buy Area)

1. Find area where price dropped, consolidated, then shot up
2. Zone = the consolidation (base) before the rally
3. Draw from base low to base high

### Supply Zone (Sell Area)

1. Find area where price rallied, consolidated, then dropped
2. Zone = the consolidation (base) before the drop
3. Draw from base high to base low

## Zone Quality Factors

| Factor           | Strong Zone         | Weak Zone          |
| ---------------- | ------------------- | ------------------ |
| **Departure**    | Explosive move out  | Slow grind         |
| **Time at base** | Short (1-5 candles) | Long consolidation |
| **Freshness**    | Untested            | Multiple tests     |
| **HTF context**  | Aligned with trend  | Counter-trend      |

## Entry Strategies

### 1. Set & Forget

- Place limit order at zone edge
- Stop beyond opposite edge
- Fire and forget

### 2. Confirmation Entry

- Wait for price to enter zone
- Look for rejection candle (pin bar, engulfing)
- Enter on confirmation

### 3. Refined Zone Entry

- Use LTF to find OB or FVG within zone
- More precise entry, tighter stop

## Workflow

1. **Identify zones** on HTF (4H/Daily) using `get_candles_around_date`
2. **Mark zones** using `draw_chart_analysis` with `demand` or `supply` type
3. **Confirm with indicators**: `get_indicator(indicator_code="rsi")` for oversold/overbought at zone
4. **Wait for price** to return to zone
5. **Enter with confirmation** or limit order
6. **Stop loss** beyond the zone
7. **Target** next opposing zone

## Zone Weakening

Zones weaken with each test:

- 1st test: Strongest reaction expected
- 2nd test: Moderate reaction
- 3rd+ test: Zone likely to break

## Key Insight

Supply/demand differs from S/R:

- S/R = single price level
- S/D = zone (range of prices)
- S/D represents unfilled institutional orders

## Related Skills

- **order-blocks** — Order blocks are ICT-specific supply/demand zones; similar concept with different identification criteria
- **volume-profile-trading** — Volume profile HVNs and VAH/VAL confirm supply/demand zone strength
- **fibonacci-trading** — Fibonacci levels overlapping with supply/demand zones create high-confluence entries
