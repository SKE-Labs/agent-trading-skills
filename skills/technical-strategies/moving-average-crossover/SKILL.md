---
name: moving-average-crossover
description: Trade EMA/SMA crossover systems for trend following. Use when identifying trend changes, timing entries with momentum, or building systematic trading rules.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Moving Average Crossover Trading

MA crossovers provide systematic signals for trend identification and entry timing.

## Candidate Combinations

| Fast MA | Slow MA | Use Case         |
| ------- | ------- | ---------------- |
| 5 EMA | 13 EMA | Fast conventional pair |
| 9 EMA | 21 EMA | Medium-fast conventional pair |
| 20 SMA | 50 SMA | Medium conventional pair |
| 50 SMA | 200 SMA | Slow conventional pair |

These are starting specifications, not style-specific best settings. Record every pair tried and compare against buy-and-hold/cash or an appropriate directional baseline.

## Signals

### Golden Cross (Bullish)

- Fast MA crosses above slow MA
- Record price versus both averages as a candidate filter

### Death Cross (Bearish)

- Fast MA crosses below slow MA
- Record price versus both averages as a candidate filter

## Strategies

### Basic Crossover
- Enter on cross in direction, exit on opposite cross
- Simple but prone to whipsaws in ranges

### Price + MA Confirmation
- Wait for crossover, then wait for pullback to fast MA
- Enter on an objectively defined pullback trigger; test whether it changes whipsaw rate and net expectancy

### Triple MA System (5-8-13)
- All 3 aligned = ordered-average state; not independent confirmation
- Entry: 5 crosses 8, both above 13
- Exit: 5 crosses below 8

### MA as Dynamic S/R
- In uptrend: MA acts as support (buy bounces)
- In downtrend: MA acts as resistance (sell rallies)

## Workflow

1. **Get each chosen average explicitly**:
   ```
   get_indicators(indicator_code="ema_<fast>", symbol=<symbol>, exchange=<exchange>, interval=<interval>, count=<enough>)
   get_indicators(indicator_code="ema_<slow>", symbol=<symbol>, exchange=<exchange>, interval=<interval>, count=<enough>)
   ```

2. **Identify cross** direction and confirm with price position relative to MAs

3. **Get candle data** for entry timing:
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
   ```

4. **Enter on pullback** to fast MA (conservative) or on cross (aggressive)

5. **Stop loss** beyond recent swing or slow MA. Exit on opposite cross or target.

6. **Mark on chart**:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "trend",
       "points": [
           {"time": <cross_time>, "price": <cross_price>},
           {"time": <current_time>, "price": <current_ma>}
       ],
       "options": {"text": "Golden Cross (9/21 EMA)"}
   })
   ```

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: The [technical-analysis evidence review](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID603481_code17745.pdf?abstractid=603481) finds mixed market- and era-dependent profitability and highlights transaction costs and data snooping.

## Key Rules

- Use a regime filter only if it adds held-out net value; ADX does not confirm trend by itself.
- A crossover rule must specify closed-bar timing, order timing, stop, exit, and warm-up.
- Faster averages react sooner and trade more often; reliability is empirical after costs.
- EMA weights recent data more heavily; SMA weights its window equally.
- Test additional features incrementally and control parameter/data-snooping risk.

## Related Skills

- **market-regime-detection** — MA crossovers only work in trending regimes; check ADX before trading
- **macd-trading** — MACD is derived from EMAs and provides complementary momentum confirmation
