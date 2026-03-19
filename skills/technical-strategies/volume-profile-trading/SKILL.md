---
name: volume-profile-trading
description: Analyze volume at price to identify high-probability support/resistance using POC, Value Area, and volume nodes. Use when finding true S/R levels, identifying breakout zones, or confirming zone strength.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending", "ranging"]
---

# Volume Profile Trading

Volume Profile shows how much trading occurred at each price level, revealing where real institutional interest exists — not just where price bounced.

## Core Concepts

| Concept | Definition | Trading Use |
| --- | --- | --- |
| **POC** (Point of Control) | Price level with highest traded volume | Acts as magnet — price gravitates toward POC |
| **Value Area (VA)** | Range containing ~70% of total volume | Fair value zone — price spends most time here |
| **VAH** (Value Area High) | Upper boundary of Value Area | Resistance in ranges, breakout level in trends |
| **VAL** (Value Area Low) | Lower boundary of Value Area | Support in ranges, breakdown level in trends |
| **HVN** (High Volume Node) | Cluster of high volume at a price | Strong S/R — price tends to stall or consolidate |
| **LVN** (Low Volume Node) | Area of thin volume between HVNs | Fast price movement through — breakout zones |

## Identification

### Building a Volume Profile

Use `get_candles_around_date` to retrieve price + volume data for the analysis period:

```
get_candles_around_date(symbol="BTCUSD", interval="1h", date="2026-03-15")
```

Analyze volume distribution across price levels:
1. Group candles by price range (bins)
2. Sum volume in each bin
3. Identify the bin with highest volume → **POC**
4. Find the range containing 70% of total volume → **Value Area**

### Key Levels to Mark

Use `draw_chart_analysis` to mark profile levels:

**POC (strongest level):**
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

**Value Area boundaries:**
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

**Low Volume Nodes (breakout zones):**
```
draw_chart_analysis(action="create", drawing={
    "type": "highlight",
    "points": [
        {"time": <start_time>, "price": <lvn_top>},
        {"time": <end_time>, "price": <lvn_bottom>}
    ],
    "options": {"text": "LVN - Fast Move Zone"}
})
```

## Entry Strategies

### 1. Value Area Bounce (Range Trading)

In ranging markets, price oscillates within the Value Area:

- **Buy at VAL** with bullish rejection candle
- **Sell at VAH** with bearish rejection candle
- **Target**: POC (middle of range)
- **Stop**: Beyond VA boundary (VAL - buffer for longs, VAH + buffer for shorts)

### 2. POC Magnet

Price tends to return to POC after deviating:

- If price moves above VAH, look for **reversion back to POC**
- If price moves below VAL, look for **reversion back to POC**
- Use with RSI divergence at extremes for higher probability

### 3. Value Area Breakout

When price breaks out of the Value Area with volume:

- **Breakout above VAH** + volume spike → Long, target next HVN above
- **Breakdown below VAL** + volume spike → Short, target next HVN below
- **Confirmation**: Price must close outside VA (not just wick)
- LVN zones above/below VA are where price moves fastest — expect acceleration

### 4. LVN Breakout Play

Low Volume Nodes are "air pockets" — price moves quickly through them:

- Identify LVN between two HVNs
- Enter when price reaches LVN boundary
- Expect rapid move to next HVN
- Tight stops since LVN should not hold price

## Volume Profile + Confluence

Best trades combine volume profile with other tools:

| Confluence | Signal Strength |
| --- | --- |
| POC + Fibonacci 61.8% | Very strong S/R |
| VAL + Order block | High probability demand |
| VAH + Supply zone | High probability supply |
| LVN + Breakout level | Acceleration zone |
| HVN + Moving average | Trend continuation support |

## Workflow

### 1. Get Price and Volume Data

```
get_candles_around_date(symbol="BTCUSD", interval="4h", date="2026-03-15")
```

### 2. Check Volume Indicator

```
get_indicator(indicator_code="mfi")
```

Compare current volume to average — is volume confirming the move?

### 3. Identify Profile Levels

From the candle data, identify:
- Where most volume traded (POC)
- The 70% value area (VAH/VAL)
- Gaps in volume (LVNs)
- Volume clusters (HVNs)

### 4. Mark Levels on Chart

Use `draw_chart_analysis` to mark POC, VAH, VAL, HVNs, and LVNs (see examples above).

### 5. Confirm with Indicators

```
get_indicator(indicator_code="rsi")
get_indicator(indicator_code="ema")
```

Check if indicators align with volume profile signal.

### 6. Report to Orchestrator

- **POC level** and current price relative to it
- **Value Area** boundaries (VAH/VAL)
- **Current position**: Price inside VA (range), above (bullish), below (bearish)
- **Key LVNs**: Where to expect fast moves
- **Trade setup**: Entry zone, rationale, and key levels

## Best Practices

| Do | Don't |
| --- | --- |
| Use sufficient data (50+ candles minimum) | Build profile from too few candles |
| Mark POC, VAH, VAL on every analysis | Ignore volume and only use price S/R |
| Treat LVNs as acceleration zones | Expect price to hold at LVNs |
| Combine with other S/R methods | Trade volume profile in isolation |
| Update profile as new data arrives | Use stale profiles from weeks ago |

## Common Mistakes

- **Too narrow a timeframe** — Building profile from 10 candles gives unreliable levels. Use at least 50 candles for meaningful volume distribution.
- **Ignoring context** — A POC from last week may not matter if a major event changed the market structure. Always use recent, relevant data.
- **Trading LVNs as S/R** — LVNs are the opposite of S/R. Price moves through them quickly. Don't expect bounces at LVNs.
- **Confusing volume with candle count** — Volume profile weights by actual traded volume, not by number of candles at a level.

## Related Skills

- **supply-demand-zones** — Volume profile HVNs confirm supply/demand zone strength; LVNs identify breakout acceleration areas
- **breakout-trading** — LVN zones above/below value areas are where breakout moves accelerate
- **fibonacci-trading** — POC or VAL/VAH overlapping with Fibonacci levels creates strong confluence
