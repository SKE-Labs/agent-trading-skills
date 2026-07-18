---
name: supply-demand-zones
description: Define and test supply/demand-style base-and-departure candle zones. Use when planning support/resistance hypotheses without inferring unfilled institutional inventory.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Supply & Demand Zone Trading

Supply/demand zones are candle-range heuristics around a base before a directional departure. OHLC data alone does not reveal institutional accumulation, distribution, or resting inventory.

## Zone Identification

### Demand Zone (Buy Area)
- Price dropped, formed a base under a predeclared bar/range rule, then rallied by a normalized departure threshold
- Zone = the consolidation base before the rally (draw from base low to base high)

### Supply Zone (Sell Area)
- Price rallied, formed a base under the same rule, then dropped by a normalized threshold
- Zone = the consolidation base before the drop (draw from base high to base low)

## Zone Quality

| Factor           | Strong Zone         | Weak Zone          |
| ---------------- | ------------------- | ------------------ |
| **Departure** | Large/small ATR-normalized move over fixed bars |
| **Time at base** | Bar count and range/ATR |
| **Retests** | Count, depth, and age |
| **Context** | Objective higher-timeframe state |

Treat retest count as a feature. Estimate first and later retest outcomes with a fixed expiry; do not assume monotonic weakening.

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
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
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
   get_indicators(indicator_code="rsi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   ```
   Check for oversold/overbought at zone.

4. **Wait for price** to return to zone. Enter with confirmation or limit order. Stop beyond zone. Target: next opposing zone.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: Empirical [limit-order clustering research](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=966454) supports price barriers at clustered levels, but candle zones do not reveal unfilled institutional inventory.

## Key Rules

- Define base, departure, zone bounds, retest, expiry, and invalidation without hindsight.
- Normalize departure by ATR, ticks, and bars; do not call it order imbalance without order-flow evidence.
- Treat the construct as a support/resistance zone, not unfilled institutional orders.
- Test retest age/count and lower-timeframe refinement for incremental net value.
- Keep broken, never-retested, and expired zones in the denominator.

## Related Skills

- **volume-profile-trading** — volume profile HVNs confirm S/D zone strength
- **fibonacci-trading** — Fib retracements into S/D zones provide high-confluence entries
