---
name: moving-average-crossover
description: Trade EMA/SMA crossover systems for trend following. Use when identifying trend changes, timing entries with momentum, or building systematic trading rules.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending"]
---

# Moving Average Crossover Trading

MA crossovers provide simple, systematic signals for trend identification and entry timing.

## Common MA Combinations

| Fast MA | Slow MA | Use Case         |
| ------- | ------- | ---------------- |
| 5 EMA   | 13 EMA  | Scalping         |
| 9 EMA   | 21 EMA  | Day trading      |
| 20 SMA  | 50 SMA  | Swing trading    |
| 50 SMA  | 200 SMA | Position trading |

## Classic Signals

### Golden Cross (Bullish)

- Fast MA crosses ABOVE slow MA
- Indicates uptrend beginning
- Best when price is above both MAs

### Death Cross (Bearish)

- Fast MA crosses BELOW slow MA
- Indicates downtrend beginning
- Best when price is below both MAs

## Trading Strategies

### 1. Basic Crossover

- Enter on cross in direction
- Exit on opposite cross
- Simple but can have whipsaws

### 2. Price + MA Confirmation

- Wait for crossover
- THEN wait for price to pullback to fast MA
- Enter on bounce from MA
- Reduces whipsaws

### 3. Triple MA System (5-8-13)

Popular Investopedia strategy:

- All 3 aligned = Strong trend
- Entry: 5 crosses 8, both above 13
- Exit: 5 crosses below 8

### 4. MA as Dynamic S/R

- In uptrend: MA acts as support
- In downtrend: MA acts as resistance
- Trade bounces from MA in trend direction

## Workflow

1. **Get MAs** using `get_indicator(indicator_code="ema")`
2. **Identify cross** direction
3. **Confirm with price** position relative to MAs
4. **Enter on pullback** to MA or aggressive on cross
5. **Stop loss** beyond recent swing or far MA
6. **Exit** on opposite cross or target

## EMA vs SMA

| Type | Pros            | Cons           |
| ---- | --------------- | -------------- |
| EMA  | Faster response | More whipsaws  |
| SMA  | Smoother        | Slower signals |

## Best Practices

- Use in trending markets (avoid ranges)
- Combine with other confluence
- Faster MAs = more signals, more false signals
- Slower MAs = fewer signals, more reliable

## Related Skills

- **multi-timeframe-analysis** — Use HTF MA alignment to confirm LTF crossover signals
- **market-regime-detection** — MA crossovers only work in trending regimes; check ADX before trading
- **macd-trading** — MACD is derived from EMAs and provides complementary momentum confirmation
