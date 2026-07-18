---
name: volume-profile-trading
description: Build and test volume-at-price profiles using POC, value area, and nodes. Use when the user has trade/tick data or needs a clearly disclosed OHLCV approximation.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Volume Profile Trading

Volume profile describes volume assigned to price bins over a declared session/range. It does not reveal trader identity, fair value, or a guaranteed reaction.

## Core Concepts

| Concept | Definition | Trading Use |
| --- | --- | --- |
| **POC** | Bin with highest assigned volume | Descriptive mode of the profile |
| **Value Area (VA)** | Contiguous region containing a chosen volume share | Conventional descriptive region |
| **VAH** | Upper VA boundary | Resistance in ranges, breakout level in trends |
| **VAL** | Lower VA boundary | Support in ranges, breakdown level in trends |
| **HVN** | Locally high assigned-volume bin | Candidate consolidation/reaction feature |
| **LVN** | Locally low assigned-volume bin | Candidate traversal/reaction feature |

## Entry Strategies

### Value Area Bounce (Range Trading)
- Buy at VAL with bullish rejection candle, target POC
- Sell at VAH with bearish rejection candle, target POC
- Stop beyond VA boundary

### POC Magnet
- Test reversion to POC with a fixed horizon; price position alone is not an entry
- Combine with RSI divergence at extremes for higher probability

### Value Area Breakout
- Breakout above VAH + volume spike → long, target next HVN above
- Breakdown below VAL + volume spike → short, target next HVN below
- Price must close outside VA (not just wick)

### LVN Breakout Play
- Define LVN relative to neighboring bins and test traversal time versus matched control bins
- Use an objective trigger and structural invalidation; do not assume rapid movement

## Workflow

1. **Get trade/tick data when available**, including venue, session, price, size, and corrections. If only OHLCV exists, disclose that volume-at-price is approximated because candle volume has no exact price allocation:
   ```
   get_candles(symbol=<symbol>, exchange=<exchange>, interval=<interval>, count=200)
   ```

2. **Check volume indicator**:
   ```
   get_indicators(indicator_code="mfi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   ```

3. **Freeze the profile specification**: session/range anchor, tick/bin size, trade corrections, allocation method, value-area share (70% is conventional), expansion algorithm, and tie handling. Compute POC/VAH/VAL without using future observations.

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
   get_indicators(indicator_code="rsi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   get_indicators(indicator_code="ema", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   ```

6. **Report**: POC level, VA boundaries, price position (inside/above/below VA), key LVNs, trade setup

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: Volume profile is a descriptive distribution. Published trading-rule evidence is limited; a recent [value-area breakout test](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6350238) found the unfiltered signal was not economically significant.

## Key Rules

- Require enough observations for stable bins and show sensitivity to bin width; no candle count is universal.
- Treat HVN/LVN reactions as hypotheses, not magnets, barriers, or air pockets.
- Anchor and update profiles according to the predeclared session/event rule.
- State whether volume is actual venue trades, consolidated, tick volume, or OHLCV-allocated approximation.
- Test overlaps incrementally; multiple price-derived labels are not independent confluence.

## Related Skills

- **supply-demand-zones** — volume profile HVNs confirm S/D zone strength; LVNs identify breakout acceleration areas
- **fibonacci-trading** — POC or VAL/VAH overlapping with Fib levels creates strong confluence
