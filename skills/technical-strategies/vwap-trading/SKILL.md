---
name: vwap-trading
description: Trade using Volume Weighted Average Price for intraday fair value. Use when determining institutional price levels, finding intraday support/resistance, or identifying mean reversion opportunities.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# VWAP Trading Strategy

VWAP (Volume Weighted Average Price) is the institutional benchmark for intraday fair value. Resets daily at market open.

## Interpretation

| Price Position | Meaning              | Bias    |
| -------------- | -------------------- | ------- |
| Price > VWAP   | Bought above average | Bullish |
| Price < VWAP   | Bought below average | Bearish |
| Price = VWAP   | Fair value           | Neutral |

**Deviation %** = `(Price - VWAP) / VWAP * 100`

## Strategies

### VWAP as Dynamic S/R
- Uptrend: VWAP acts as support — buy bounces from VWAP with rejection candle
- Downtrend: VWAP acts as resistance — sell rallies to VWAP with rejection candle

### VWAP Mean Reversion
- When price extends far from VWAP (Deviation >1%), expect reversion
- Trade back toward VWAP; best in ranging markets

### VWAP Breakout
- Strong move through VWAP with volume = momentum shift
- Enter on breakout, target deviation bands or previous highs/lows

### VWAP Deviation Bands
- +1/-1 StdDev: minor targets
- +2/-2 StdDev: extended targets (often reversal zones)

## Workflow

1. **Get VWAP/price data** for the session:
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```

2. **Get EMA** for trend context:
   ```
   get_indicator(indicator_code="ema", symbol=<symbol>, interval=<interval>)
   ```

3. **Calculate deviation**: `(Price - VWAP) / VWAP * 100`

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

## Key Rules

- NEVER ignore VWAP on intraday charts; institutions use it to benchmark execution
- NEVER treat VWAP as meaningful on daily+ charts; it resets each session
- Daily VWAP matters most; weekly/monthly VWAP is useful for swing context
- VWAP works best on liquid instruments; thin markets produce unreliable VWAP
- Large institutional orders often try to execute at VWAP — expect clusters there

## Related Skills

- **volume-profile-trading** — VWAP and volume profile POC together define strongest intraday fair value
- **mean-reversion** — VWAP mean reversion complements BB and RSI mean reversion setups
