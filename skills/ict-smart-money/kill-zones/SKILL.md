---
name: kill-zones
description: Trade during high-volume institutional sessions (London, New York, Asian). Use when timing entries for maximum volatility, avoiding low-volume chop, or aligning trades with session opens.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Kill Zones Trading

Kill zones are specific times when institutional activity peaks, creating the best trading opportunities.

## Kill Zone Schedule (UTC)

| Session    | Kill Zone (UTC) | Characteristics                      |
| ---------- | --------------- | ------------------------------------ |
| **Asian**  | 00:00 - 03:00   | Range formation, accumulation        |
| **London** | 07:00 - 10:00   | Trend initiation, highest volatility |
| **NY AM**  | 12:00 - 15:00   | Continuation or reversal             |
| **NY PM**  | 18:00 - 20:00   | End-of-day moves                     |

## Session Behaviors

### Asian Session

- Creates the day's range (high/low boundaries)
- Liquidity builds at session highs/lows
- Often "boring" but sets up London

### London Kill Zone

- **Most important session** for entries
- Often sweeps Asian highs OR lows
- Creates daily bias direction
- Best time for trend initiation

### New York AM Kill Zone

- Either continues London trend OR reverses
- Watch for liquidity sweep of London extremes
- High-impact news releases (NFP, CPI, FOMC)

### New York PM

- End-of-day positioning
- Potential reversal if overextended
- Lower priority for entries

## Kill Zone Trading Strategy

### 1. Pre-Session Prep

- Mark Asian session high/low
- Identify key levels from HTF
- Note any news events

### 2. Session Open Analysis

- First 15-30 min: Observe manipulation
- Wait for sweep of Asian high/low
- Watch for structure shift

### 3. Entry Timing

- Enter AFTER kill zone manipulation (sweeps)
- Best entries: 30-60 min into session
- Avoid first 15 min (fake moves)

### 4. Session Context

| Price Action             | Expected Move  |
| ------------------------ | -------------- |
| London sweeps Asian low  | Bullish day    |
| London sweeps Asian high | Bearish day    |
| London takes both        | Chop/range day |

## Key Rules

- Trade only during kill zones for best volatility
- Avoid trading outside these windows
- London is the most profitable session for most pairs
- NY can confirm or invalidate London's direction

## Related Skills

- **liquidity-zones** — Kill zone opens frequently sweep Asian session liquidity before reversing
- **market-structure-shift** — Use LTF structure shifts during kill zones to time entries after manipulation
- **momentum-trading** — Kill zones provide the volume and volatility needed for momentum setups
