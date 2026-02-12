---
name: liquidity-zones
description: Identify liquidity pools and stop-hunt levels where retail stops cluster. Use when predicting price manipulation, understanding smart money targets, or timing entries after liquidity sweeps.
---

# Liquidity Zones Trading

Liquidity represents clustered stop losses that institutions target for order fills before reversing price.

## Types of Liquidity

### Buy-Side Liquidity (BSL)

- **Location**: Above swing highs, equal highs, resistance
- **Contains**: Stop losses from short positions
- **Smart Money Action**: Drive price up to trigger stops, then sell

### Sell-Side Liquidity (SSL)

- **Location**: Below swing lows, equal lows, support
- **Contains**: Stop losses from long positions
- **Smart Money Action**: Drive price down to trigger stops, then buy

## Liquidity Identification

| Formation         | Liquidity Type | Strength  |
| ----------------- | -------------- | --------- |
| Equal highs       | BSL            | Very High |
| Equal lows        | SSL            | Very High |
| Swing highs       | BSL            | High      |
| Swing lows        | SSL            | High      |
| Trendline touches | Both           | Medium    |
| Round numbers     | Both           | Medium    |

## Trading the Sweep

### Entry Workflow

1. **Identify liquidity pool** (equal highs/lows, obvious levels)
2. **Wait for sweep** (price takes out the level)
3. **Look for reversal signs**:
   - Market structure shift on LTF
   - Strong rejection candle
   - Return into previous range
4. **Enter after confirmation**
5. **Target** opposite liquidity pool

### Sweep Confirmation Checklist

- [ ] Liquidity level taken out
- [ ] Quick reversal (within 1-3 candles)
- [ ] Volume spike on sweep
- [ ] Lower TF structure shift
- [ ] Return inside previous range

## Chart Marking

Use `draw_chart_analysis` to mark:

- `resistance` for BSL levels
- `support` for SSL levels
- `highlight` for sweep points (HH/LL markers)

## Risk Management

- **Never trade BEFORE the sweep** (anticipation = losses)
- Stop loss: Beyond the sweep wick
- Target: Opposite liquidity or order block
- Accept that not all sweeps reverse immediately
