---
name: supply-demand-zones
description: Identify institutional supply and demand zones for reversal entries. Use when finding high-probability bounce areas, understanding institutional order flow, or planning entries at key zones.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Supply & Demand Zone Trading

Supply and demand zones mark areas of institutional accumulation (demand) and distribution (supply).

## Zone Identification

### Demand Zone (Buy Area)
- Price dropped, consolidated briefly (1-5 candles), then rallied explosively
- Zone = the consolidation base before the rally (draw from base low to base high)

### Supply Zone (Sell Area)
- Price rallied, consolidated briefly (1-5 candles), then dropped explosively
- Zone = the consolidation base before the drop (draw from base high to base low)

## Zone Quality

| Factor           | Strong Zone         | Weak Zone          |
| ---------------- | ------------------- | ------------------ |
| **Departure**    | Explosive move out  | Slow grind         |
| **Time at base** | Short (1-5 candles) | Long consolidation |
| **Freshness**    | Untested            | Multiple tests     |
| **HTF context**  | Aligned with trend  | Counter-trend      |

**Zone weakening**: 1st test = strongest reaction. 2nd test = moderate. 3rd+ = zone likely breaks.

## Entry Strategies

### Set & Forget
- Limit order at zone edge, stop beyond opposite edge

### Confirmation Entry
- Wait for price to enter zone, look for rejection candle (pin bar, engulfing), enter on confirmation

### Refined Zone Entry
- Use LTF to find order block or FVG within the zone for tighter stop

## Workflow

1. **Get candle data** on HTF (4H/Daily) to identify zones:
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```

2. **Mark zones** on chart:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "demand",
       "points": [
           {"time": <zone_start_time>, "price": <zone_top>},
           {"time": <zone_end_time>, "price": <zone_bottom>}
       ],
       "options": {"text": "Fresh Demand Zone"}
   })
   ```

3. **Confirm with indicators**:
   ```
   get_indicator(indicator_code="rsi", symbol=<symbol>, interval=<interval>)
   ```
   Check for oversold/overbought at zone.

4. **Wait for price** to return to zone. Enter with confirmation or limit order. Stop beyond zone. Target: next opposing zone.

## Key Rules

- NEVER trade zones that have been tested 3+ times; they are likely to break
- NEVER draw zones from slow grinds; only from explosive departures (strong imbalance)
- S/D zones differ from S/R: S/R is a single level, S/D is a price range representing unfilled institutional orders
- Freshness matters most; an untested zone is far higher probability than a retested one
- Use LTF for refined entries within HTF zones for better risk/reward

## Related Skills

- **volume-profile-trading** — volume profile HVNs confirm S/D zone strength
- **fibonacci-trading** — Fib retracements into S/D zones provide high-confluence entries
