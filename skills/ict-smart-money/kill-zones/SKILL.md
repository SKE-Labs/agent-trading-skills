---
name: kill-zones
description: Trade during high-volume institutional sessions (London, New York, Asian). Use when timing entries for maximum volatility, avoiding low-volume chop, or aligning trades with session opens.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Kill Zones Trading

Specific session windows when institutional activity peaks, creating the best trading opportunities.

## Kill Zone Schedule (UTC)

| Session    | Kill Zone (UTC) | Characteristics                      |
| ---------- | --------------- | ------------------------------------ |
| **Asian**  | 00:00 - 03:00   | Range formation, accumulation        |
| **London** | 07:00 - 10:00   | Trend initiation, highest volatility |
| **NY AM**  | 12:00 - 15:00   | Continuation or reversal             |
| **NY PM**  | 18:00 - 20:00   | End-of-day positioning               |

## Session Behaviors

- **Asian**: Creates the day's range (high/low boundaries). Builds liquidity at session extremes. Sets up London.
- **London**: Most important session for entries. Often sweeps Asian highs or lows. Creates daily bias direction.
- **NY AM**: Either continues London trend or reverses. Watch for sweep of London extremes. High-impact news window.
- **NY PM**: End-of-day positioning. Lower priority for entries. Potential reversal if overextended.

## Workflow

1. **Pre-session**: Mark Asian session high/low, identify HTF key levels, note scheduled news events
   ```
   get_candles_around_date(symbol=<symbol>, interval="15m", date=<asian_session_date>)
   ```
2. **Session open** (first 15-30 min): Observe manipulation. Wait for sweep of Asian high/low
3. **Entry timing**: Enter after kill zone manipulation (sweeps), typically 30-60 min into the session. Watch for LTF structure shift as confirmation
4. **Session context**:
   - London sweeps Asian low = bullish day
   - London sweeps Asian high = bearish day
   - London takes both = chop/range day

## Key Rules

- NEVER trade the first 15 min of a session -- these are manipulation moves
- NEVER trade outside kill zone windows -- low volume = chop and false signals
- London is the most profitable session for most pairs/instruments
- NY AM can confirm or invalidate London's direction
- Always combine kill zone timing with a structural entry (OB, FVG, or structure shift)

## Related Skills

- **liquidity-zones** — Kill zone opens frequently sweep Asian session liquidity before reversing
- **market-structure-shift** — LTF structure shifts during kill zones time entries after manipulation
