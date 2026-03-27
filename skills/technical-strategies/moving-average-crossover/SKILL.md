---
name: moving-average-crossover
description: Trade EMA/SMA crossover systems for trend following. Use when identifying trend changes, timing entries with momentum, or building systematic trading rules.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Moving Average Crossover Trading

MA crossovers provide systematic signals for trend identification and entry timing.

## Common Combinations

| Fast MA | Slow MA | Use Case         |
| ------- | ------- | ---------------- |
| 5 EMA   | 13 EMA  | Scalping         |
| 9 EMA   | 21 EMA  | Day trading      |
| 20 SMA  | 50 SMA  | Swing trading    |
| 50 SMA  | 200 SMA | Position trading |

## Signals

### Golden Cross (Bullish)

- Fast MA crosses above slow MA
- Strongest when price is above both MAs

### Death Cross (Bearish)

- Fast MA crosses below slow MA
- Strongest when price is below both MAs

## Strategies

### Basic Crossover
- Enter on cross in direction, exit on opposite cross
- Simple but prone to whipsaws in ranges

### Price + MA Confirmation
- Wait for crossover, then wait for pullback to fast MA
- Enter on bounce from MA — reduces whipsaws significantly

### Triple MA System (5-8-13)
- All 3 aligned = strong trend
- Entry: 5 crosses 8, both above 13
- Exit: 5 crosses below 8

### MA as Dynamic S/R
- In uptrend: MA acts as support (buy bounces)
- In downtrend: MA acts as resistance (sell rallies)

## Workflow

1. **Get EMAs**:
   ```
   get_indicator(indicator_code="ema", symbol=<symbol>, interval=<interval>)
   ```

2. **Identify cross** direction and confirm with price position relative to MAs

3. **Get candle data** for entry timing:
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
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

## Key Rules

- NEVER use MA crossovers in ranging markets; check ADX >25 first to confirm trend
- NEVER trade every crossover; most are false in choppy conditions
- Faster MAs = more signals + more false signals; slower MAs = fewer but more reliable
- EMA reacts faster (more whipsaws); SMA is smoother (slower signals)
- Combine with other confluence; crossover alone is a weak signal

## Related Skills

- **market-regime-detection** — MA crossovers only work in trending regimes; check ADX before trading
- **macd-trading** — MACD is derived from EMAs and provides complementary momentum confirmation
