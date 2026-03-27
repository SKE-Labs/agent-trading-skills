---
name: volume-profile-trading
description: Analyze volume at price to identify high-probability support/resistance using POC, Value Area, and volume nodes. Use when finding true S/R levels, identifying breakout zones, or confirming zone strength.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Volume Profile Trading

Volume Profile shows how much trading occurred at each price level, revealing institutional interest beyond simple price bounces.

## Core Concepts

| Concept | Definition | Trading Use |
| --- | --- | --- |
| **POC** | Price with highest traded volume | Magnet — price gravitates toward POC |
| **Value Area (VA)** | Range containing ~70% of total volume | Fair value zone |
| **VAH** | Upper VA boundary | Resistance in ranges, breakout level in trends |
| **VAL** | Lower VA boundary | Support in ranges, breakdown level in trends |
| **HVN** | High volume cluster | Strong S/R — price stalls/consolidates |
| **LVN** | Low volume gap between HVNs | Fast price movement — breakout acceleration zones |

## Entry Strategies

### Value Area Bounce (Range Trading)
- Buy at VAL with bullish rejection candle, target POC
- Sell at VAH with bearish rejection candle, target POC
- Stop beyond VA boundary

### POC Magnet
- Price above VAH or below VAL → look for reversion back to POC
- Combine with RSI divergence at extremes for higher probability

### Value Area Breakout
- Breakout above VAH + volume spike → long, target next HVN above
- Breakdown below VAL + volume spike → short, target next HVN below
- Price must close outside VA (not just wick)

### LVN Breakout Play
- LVN between two HVNs = "air pocket" — price moves through quickly
- Enter when price reaches LVN boundary, expect rapid move to next HVN
- Tight stops since LVN should not hold price

## Workflow

1. **Get price and volume data** (need 50+ candles minimum):
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```

2. **Check volume indicator**:
   ```
   get_indicator(indicator_code="mfi", symbol=<symbol>, interval=<interval>)
   ```

3. **Identify profile levels** from candle data: group by price bins, sum volume per bin. Highest bin = POC. 70% of total volume = Value Area.

4. **Mark levels on chart**:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "support",
       "points": [
           {"time": <start_time>, "price": <poc_price>},
           {"time": <end_time>, "price": <poc_price>}
       ],
       "options": {"text": "POC ($67,250)"}
   })
   ```
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "demand",
       "points": [
           {"time": <start_time>, "price": <vah_price>},
           {"time": <end_time>, "price": <val_price>}
       ],
       "options": {"text": "Value Area (70%)"}
   })
   ```

5. **Confirm with indicators**:
   ```
   get_indicator(indicator_code="rsi", symbol=<symbol>, interval=<interval>)
   get_indicator(indicator_code="ema", symbol=<symbol>, interval=<interval>)
   ```

6. **Report**: POC level, VA boundaries, price position (inside/above/below VA), key LVNs, trade setup

## Key Rules

- NEVER build profile from too few candles; use 50+ for meaningful volume distribution
- NEVER treat LVNs as S/R; they are the opposite — price moves through them quickly
- NEVER use stale profiles; update as new data arrives. A POC from weeks ago may be irrelevant after a major event.
- Volume profile weights by actual traded volume, not by candle count at a level
- Best confluence: POC + Fib 61.8%, VAL + order block, LVN + breakout level

## Related Skills

- **supply-demand-zones** — volume profile HVNs confirm S/D zone strength; LVNs identify breakout acceleration areas
- **fibonacci-trading** — POC or VAL/VAH overlapping with Fib levels creates strong confluence
