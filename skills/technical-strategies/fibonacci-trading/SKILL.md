---
name: fibonacci-trading
description: Use Fibonacci retracement and extension for entries and targets. Use when finding pullback entries, setting profit targets, or identifying key reversal levels.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Fibonacci Trading

Fibonacci ratios identify key retracement and extension levels for entries and targets.

## Levels

### Retracement (Entries)

| Level | Use                      |
| ----- | ------------------------ |
| 23.6% | Shallow pullback         |
| 38.2% | Moderate pullback        |
| 50.0% | Half retracement         |
| 61.8% | Golden ratio (key level) |
| 78.6% | Deep pullback            |

**Formula**: `Retracement = High - Range * Ratio` (where Range = High - Low)

### Extension (Targets)

| Level  | Use                 |
| ------ | ------------------- |
| 127.2% | Conservative target |
| 161.8% | Standard target     |
| 200%   | Extended target     |
| 261.8% | Aggressive target   |

**Formula**: `Extension = High + Range * Ratio` (e.g., 127.2% = High + Range * 0.272)

## Drawing Rules

- **Bullish**: draw from swing low to swing high. Retracements = buy zones, extensions = upside targets.
- **Bearish**: draw from swing high to swing low. Retracements = sell zones, extensions = downside targets.

## Workflow

1. **Get candle data** around the swing:
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<swing_date>)
   ```

2. **Draw Fibonacci retracement** on chart (auto-renders all standard levels):
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "fib_retracement",
       "points": [
           {"time": <swing_low_timestamp>, "price": <swing_low_price>},
           {"time": <swing_high_timestamp>, "price": <swing_high_price>}
       ],
       "options": {"text": "Fib Retracement"}
   })
   ```

3. **Check confluence** with indicators:
   ```
   get_indicator(indicator_code="rsi", symbol=<symbol>, interval=<interval>)
   get_indicator(indicator_code="macd", symbol=<symbol>, interval=<interval>)
   ```

4. **Mark confluence zones** where Fib levels overlap with other structures:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "demand",
       "points": [
           {"time": <zone_start_time>, "price": <zone_top>},
           {"time": <zone_end_time>, "price": <zone_bottom>}
       ],
       "options": {"text": "61.8% + OB"}
   })
   ```

5. **Wait for confirmation**: rejection candle, LTF structure break, or confluence with S/R at the Fib level

## Key Rules

- NEVER draw from unclear or micro swings; use only clear impulsive moves
- NEVER trade Fib levels alone; require confluence (order block, S/R, MA, trendline)
- 61.8% is the primary level; treat it as the strongest retracement zone
- Stop loss beyond 78.6% (conservative) or 100% (aggressive)
- Targets at extension levels: partial at 127.2%, remainder at 161.8%+

## Related Skills

- **supply-demand-zones** — Fib retracements into S/D zones provide high-probability entries
- **multi-timeframe-analysis** — use Fib across timeframes for precise entry and target levels
