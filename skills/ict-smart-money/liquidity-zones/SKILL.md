---
name: liquidity-zones
description: Identify liquidity pools and stop-hunt levels where retail stops cluster. Use when predicting price manipulation, understanding smart money targets, or timing entries after liquidity sweeps.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Liquidity Zones Trading

Clustered stop losses that institutions target for order fills before reversing price.

## Identification

### Buy-Side Liquidity (BSL)
- **Location**: Above swing highs, equal highs, resistance
- **Contains**: Stop losses from short positions
- **Action**: Smart money drives price up to trigger stops, then sells

### Sell-Side Liquidity (SSL)
- **Location**: Below swing lows, equal lows, support
- **Contains**: Stop losses from long positions
- **Action**: Smart money drives price down to trigger stops, then buys

### Formation Strength

| Formation     | Liquidity Type | Strength  |
| ------------- | -------------- | --------- |
| Equal highs   | BSL            | Very High |
| Equal lows    | SSL            | Very High |
| Swing highs   | BSL            | High      |
| Swing lows    | SSL            | High      |
| Round numbers | Both           | Medium    |

## Workflow

1. **Identify liquidity pool** (equal highs/lows, obvious swing points):
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```
2. **Mark levels** using `draw_chart_analysis`: `resistance` for BSL, `support` for SSL, `highlight` for sweep points
3. **Wait for sweep** — price takes out the level
4. **Confirm reversal**: LTF structure shift, strong rejection candle, return into previous range (within 1-3 candles)
5. **Enter after confirmation**
6. **Stop loss** beyond the sweep wick
7. **Target** opposite liquidity pool

## Key Rules

- NEVER trade before the sweep — anticipation leads to losses
- Sweeps must be followed by quick reversal (1-3 candles) to be valid
- Volume spike on the sweep adds confirmation
- Not all sweeps reverse immediately; require LTF structure shift
- Equal highs/lows are the strongest liquidity magnets

## Related Skills

- **kill-zones** — Liquidity sweeps most commonly occur during London and NY AM sessions
- **market-structure-shift** — CHoCH after a sweep confirms the reversal direction
