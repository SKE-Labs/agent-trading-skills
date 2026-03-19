---
name: vwap-trading
description: Trade using Volume Weighted Average Price for intraday fair value. Use when determining institutional price levels, finding intraday support/resistance, or identifying mean reversion opportunities.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending", "ranging"]
---

# VWAP Trading Strategy

VWAP (Volume Weighted Average Price) represents the average price weighted by volume—institutional benchmark.

## VWAP Basics

**Calculation**: (Cumulative Price × Volume) / Cumulative Volume

Resets daily at market open.

## VWAP Interpretation

| Price Position | Meaning              | Bias    |
| -------------- | -------------------- | ------- |
| Price > VWAP   | Bought above average | Bullish |
| Price < VWAP   | Bought below average | Bearish |
| Price = VWAP   | Fair value           | Neutral |

## Trading Strategies

### 1. VWAP as Support/Resistance

- In uptrend: VWAP acts as support
- In downtrend: VWAP acts as resistance
- Trade bounces from VWAP in trend direction

### 2. VWAP Mean Reversion

- When price extends far from VWAP, expect reversion
- Trade back toward VWAP
- Best in ranging markets

### 3. VWAP Breakout

- Strong move through VWAP = momentum shift
- Entry on breakout with volume
- Target: Standard deviation bands or previous highs/lows

### 4. VWAP Bands

Calculate VWAP deviation:

```
execute(command='python3 -c "price=50200;vwap=50000;dev_pct=(price-vwap)/vwap*100;print(f\"Price: {price}\\nVWAP: {vwap}\\nDeviation: {dev_pct:+.2f}%\")"')
```

Standard deviation bands around VWAP:

- +1/-1 StdDev: Minor targets
- +2/-2 StdDev: Extended targets (often reversal zones)

## Entry Workflow

1. **Identify VWAP** for the session
2. **Determine trend**:

   - Price consistently above VWAP = Buy dips to VWAP
   - Price consistently below VWAP = Sell rallies to VWAP

3. **Entry triggers**:

   - Bounce from VWAP with rejection candle
   - Break of VWAP with volume surge

4. **Stop loss**: Beyond recent swing
5. **Target**: Previous high/low or VWAP bands

## Best Use Cases

| Market Condition | VWAP Strategy                  |
| ---------------- | ------------------------------ |
| Trend day        | Trade with VWAP as dynamic S/R |
| Range day        | Mean reversion to VWAP         |
| Open drive       | Wait for VWAP retest           |

## Key Insights

- Institutions use VWAP to benchmark execution
- Large orders often try to execute at VWAP
- Daily VWAP matters most; weekly/monthly for swing
- VWAP works best on liquid instruments

## Related Skills

- **volume-profile-trading** — VWAP and volume profile POC together define the strongest intraday fair value levels
- **mean-reversion** — VWAP mean reversion setups complement Bollinger Band and RSI mean reversion entries
- **range-trading** — In ranging markets, VWAP acts as a magnet and provides the mean for range-based strategies
