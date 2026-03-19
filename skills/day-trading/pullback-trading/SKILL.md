---
name: pullback-trading
description: Enter trends on price retracements to key levels. Use when trading with the trend, finding high R:R entries, or timing entries in established trends.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending"]
---

# Pullback Trading

Pullback trading enters established trends during temporary retracements for optimal risk/reward.

## Pullback Concept

In an uptrend:

- Price makes higher highs, higher lows
- Pullbacks retrace to support before continuing
- Enter the pullback, ride the next impulse

In a downtrend:

- Price makes lower lows, lower highs
- Pullbacks retrace to resistance before continuing
- Enter the pullback, ride the next impulse

## Pullback Levels

| Level              | Depth    | Strength         |
| ------------------ | -------- | ---------------- |
| Moving Average     | Dynamic  | 20/50 EMA common |
| Fibonacci 38.2%    | Shallow  | Strong trend     |
| Fibonacci 50%      | Moderate | Normal pullback  |
| Fibonacci 61.8%    | Deep     | Weak but valid   |
| Previous structure | Variable | S/R flip         |

## Entry Strategies

### 1. MA Pullback

1. Confirm trend direction
2. Wait for price to pull back to MA (20/50 EMA)
3. Enter on rejection candle
4. Stop below MA

### 2. Fibonacci Pullback

1. Draw Fib from swing low to high (uptrend)
2. Wait for pullback to 38-62% zone
3. Enter on confirmation
4. Stop below 78.6%

### 3. Structure Pullback

1. Identify previous resistance now support
2. Wait for pullback to flip level
3. Enter on bounce
4. Stop below structure

## Entry Confirmation

Wait for these before entering:

- Reversal candlestick pattern
- Lower TF structure shift
- Momentum indicator turning
- Volume decrease then increase

## Workflow

1. **Confirm trend** on HTF
2. **Wait for pullback** to key level
3. **Mark entry zone** using `draw_chart_analysis`
4. **Enter with confirmation**
5. **Stop** below pullback low
6. **Target** previous high/low or extension

## Best Practices

- Only trade pullbacks in clear trends
- Deeper pullbacks need more confirmation
- First pullback in new trend is best
- Don't catch falling knives (wait for confirmation)

## Related Skills

- **fibonacci-trading** — Fibonacci retracement levels (38.2%, 50%, 61.8%) define the pullback entry zones
- **momentum-trading** — Pullbacks occur within momentum moves; enter pullbacks to ride the next impulse leg
- **multi-timeframe-analysis** — Confirm the trend on HTF before entering pullbacks on LTF
