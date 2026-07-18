---
name: liquidity-zones
description: Mark candidate liquidity levels and test sweep/reversal behavior. Use when analyzing equal highs/lows, swing levels, round-number clustering, or stop-loss cascade risk without inferring hidden intent.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Liquidity Zones Trading

Observable price levels where stop or limit orders may cluster. Clustering can contribute to cascades, but candles alone cannot identify the orders, their owners, institutional targeting, or a guaranteed reversal.

## Identification

### Buy-Side Liquidity (BSL)
- **Location**: Above swing highs, equal highs, resistance
- **Hypothesis**: Some buy stops may rest above the level; verify with available order/trade data

### Sell-Side Liquidity (SSL)
- **Location**: Below swing lows, equal lows, support
- **Hypothesis**: Some sell stops may rest below the level; verify with available order/trade data

### Level Features

Record formation type, number of touches, equality tolerance in ATR/ticks, age, visible depth if available, distance, and time of day. Calibrate these features rather than assigning ordinal strength.

## Workflow

1. **Identify liquidity pool** (equal highs/lows, obvious swing points):
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
   ```
2. **Mark levels** using `draw_chart_analysis`: `resistance` for BSL, `support` for SSL, `highlight` for sweep points
3. **Wait for sweep** — price takes out the level
4. **Confirm reversal**: use an objective swing/rejection rule and a predeclared return window
5. **Enter after confirmation**
6. **Stop loss** beyond the sweep wick
7. **Target** opposite liquidity pool

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Osler](https://www.newyorkfed.org/research/staff_reports/sr150.html) found clustered FX stop-loss orders can contribute to price cascades. This supports conditional liquidity hypotheses, not certainty that institutions target a visible level.

## Key Rules

- Define sweep distance, close condition, reversal window, and expiry before evaluation.
- Compare anticipation, reversal, and continuation hypotheses on identical samples.
- Use time-of-day relative volume; it is contextual, not proof of stop orders.
- Equal highs/lows are candidate clustering coordinates, not known liquidity or magnets.
- Return `no trade` when the level or trigger cannot be defined without hindsight.

## Related Skills

- **kill-zones** — Liquidity sweeps most commonly occur during London and NY AM sessions
- **market-structure-shift** — CHoCH after a sweep confirms the reversal direction
