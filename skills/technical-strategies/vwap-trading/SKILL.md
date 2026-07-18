---
name: vwap-trading
description: Calculate and test session or anchored VWAP setups. Use when benchmarking execution or evaluating price distance from a volume-weighted average with explicit session and volume-data rules.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# VWAP Trading Strategy

VWAP is an execution benchmark: `sum(price_i × volume_i) / sum(volume_i)` over a declared interval. Session VWAP resets at the chosen session boundary; anchored VWAP uses an explicitly chosen event. Neither is fundamental fair value.

## Interpretation

| Price Position | Meaning              | Bias    |
| -------------- | -------------------- | ------- |
| Price > VWAP | Current price above the interval's volume-weighted average | Context only |
| Price < VWAP | Current price below the interval's volume-weighted average | Context only |
| Price = VWAP | Current price near benchmark | Context only |

**Deviation %** = `(Price - VWAP) / VWAP * 100`

## Strategies

### VWAP as Dynamic S/R
- Test VWAP reaction as a dynamic-coordinate hypothesis using objective trend and rejection rules

### VWAP Mean Reversion
- Define extension by rolling session-conditioned standard deviation/percentile and verify a reversion model; no universal 1% threshold applies

### VWAP Breakout
- Strong move through VWAP with volume = momentum shift
- Enter on breakout, target deviation bands or previous highs/lows

### VWAP Deviation Bands
- +1/-1 StdDev: minor targets
- +2/-2 StdDev: extended targets (often reversal zones)

## Workflow

1. **Get timestamped trade/volume data** for the declared venue and session. If only candles exist, state the price proxy (typical price/close) and whether volume is actual or tick volume:
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
   ```

2. **Get EMA** for trend context:
   ```
   get_indicators(indicator_code="ema", symbol=<symbol>, exchange=<exchange>, interval=<interval>)
   ```

3. **Calculate VWAP and deviation** without future session volume; also report standardized/percentile distance from comparable time-of-day history

4. **Determine strategy**:
   - Price consistently above VWAP → buy dips to VWAP
   - Price consistently below VWAP → sell rallies to VWAP
   - Price far from VWAP in range → mean reversion

5. **Mark on chart**:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "support",
       "points": [
           {"time": <session_start>, "price": <vwap_price>},
           {"time": <current_time>, "price": <vwap_price>}
       ],
       "options": {"text": "VWAP ($50,000)"}
   })
   ```

6. **Entry triggers**: bounce from VWAP with rejection candle, or break of VWAP with volume surge. Stop beyond recent swing.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: Academic [VWAP research](https://web.stanford.edu/~boyd/papers/pdf/vwap_opt_exec.pdf) treats VWAP as an execution benchmark under volume uncertainty and costs—not as proof that price must revert to it.

## Key Rules

- Use VWAP when it is relevant to the benchmark or validated strategy; never make it mandatory.
- State venue, timezone, session/anchor, price proxy, volume source, and reset rule.
- Do not mix daily, weekly, monthly, or event-anchored VWAPs without separate hypotheses.
- Reject unreliable volume, sparse liquidity, or noncomparable fragmented-venue data.
- Do not infer institutional orders or expected clustering from VWAP alone.

## Related Skills

- **volume-profile-trading** — compare two volume-derived descriptive coordinates without calling either fair value
- **mean-reversion** — VWAP mean reversion complements BB and RSI mean reversion setups
