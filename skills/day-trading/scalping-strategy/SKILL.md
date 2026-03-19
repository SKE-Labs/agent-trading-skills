---
name: scalping-strategy
description: Execute high-frequency small profit trades for quick gains. Use when trading highly liquid markets, taking advantage of short-term volatility, or building consistent small wins.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Scalping Strategy

Scalping targets small, frequent profits from minimal price movements within seconds to minutes.

## Scalping Essentials

| Factor          | Requirement        |
| --------------- | ------------------ |
| Timeframe       | 1m, 5m             |
| Trades per day  | 10-100+            |
| Profit target   | 5-20 pips/0.1-0.5% |
| Trade duration  | Seconds to minutes |
| Win rate target | 60%+               |

## Best Conditions

- High liquidity assets (BTC, ETH, major forex)
- High volatility periods (kill zones)
- Tight spreads
- Fast execution

## Scalping Techniques

### 1. Spread Scalping

- Profit from bid-ask spread
- Market make around VWAP
- Requires very low fees

### 2. Momentum Scalping

- Enter on strong momentum candles
- Ride momentum for small gain
- Exit quickly on momentum loss

### 3. Level Scalping

- Trade bounces at S/R
- Quick in-and-out at key levels
- Tight stops required

### 4. Range Scalping

- Trade within defined range
- Buy support, sell resistance
- Repeat until range breaks

## Entry Rules

1. **Confirm direction** on 5m (higher TF)
2. **Enter on 1m** in direction of 5m
3. **Tight stop** (5-10 pips max)
4. **Quick target** (1:1 to 1:1.5 R:R)
5. **Exit immediately** if wrong

## Risk Management

| Rule             | Guideline               |
| ---------------- | ----------------------- |
| Position size    | Small (0.5-1% risk max) |
| Stop loss        | Tight, non-negotiable   |
| Daily loss limit | 2-3% of capital         |
| Trading hours    | Only during high volume |

## Best Practices

- Use limit orders when possible
- Factor in fees (can eat profits)
- Avoid news events (unpredictable)
- Take breaks regularly
- Stop after 3 consecutive losses

## Related Skills

- **range-trading** — Range scalping buys support and sells resistance within defined ranges
- **bollinger-bands** — BB band touches on 1m/5m charts provide scalping reversal signals
- **stochastic-trading** — Stochastic overbought/oversold on fast timeframes times scalp entries
