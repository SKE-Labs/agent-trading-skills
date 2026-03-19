---
name: dca-strategy
description: Implement Dollar Cost Averaging for systematic long-term accumulation. Use when building positions over time, reducing timing risk, or accumulating during uncertainty.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Dollar Cost Averaging (DCA)

DCA invests fixed amounts at regular intervals regardless of price, reducing timing risk.

## DCA Basics

```
Each Purchase = Fixed Amount / Current Price
```

Example ($100/week):

- Week 1: $100 / $50 = 2.0 units
- Week 2: $100 / $40 = 2.5 units
- Week 3: $100 / $60 = 1.67 units
- Total: 6.17 units for $300 (avg: $48.62)

**Calculate DCA average:**

- Total Spent = sum of all purchase amounts
- Total Units = sum of (amount / price) for each purchase
- Average Cost = Total Spent / Total Units

Use `get_latest_candle` to check current price against your DCA average.

## DCA Benefits

| Benefit              | Description                   |
| -------------------- | ----------------------------- |
| Reduces timing risk  | No need to time perfect entry |
| Emotional discipline | Removes emotional decisions   |
| Lower average cost   | Buy more when price low       |
| Simple execution     | Set and forget                |

## DCA Strategies

### 1. Fixed Interval DCA

- Same amount every week/month
- Most common approach
- Easy to automate

### 2. Value Averaging

- Adjust amount based on goals
- Buy more when below target value
- Buy less or sell when above

### 3. Enhanced DCA

- Base amount + bonus when price drops
- Example: $100 base + $50 if 10%+ below MA
- More aggressive accumulation

### 4. Lump Sum + DCA Hybrid

- Deploy 50% immediately
- DCA remaining 50% over time
- Balances opportunity cost with risk

## Best Assets for DCA

| Suitable         | Less Suitable              |
| ---------------- | -------------------------- |
| BTC, ETH         | Low-cap altcoins           |
| S&P 500 index    | Individual volatile stocks |
| Blue chip stocks | Meme coins                 |

## DCA Parameters

| Parameter   | Suggestion                  |
| ----------- | --------------------------- |
| Frequency   | Weekly or bi-weekly         |
| Amount      | What you can afford to lose |
| Duration    | 6-24+ months                |
| Hold period | 2-5+ years                  |

## When to Stop DCA

- Target position reached
- Fundamentals change (bearish)
- Better opportunity elsewhere
- Personal financial need

## DCA Workflow

1. **Choose asset** (strong fundamentals)
2. **Set budget** (monthly allocation)
3. **Set schedule** (weekly/monthly)
4. **Automate if possible**
5. **Review quarterly** (not daily)
6. **Hold long-term**

## Key Insight

DCA optimizes for psychology and consistency, not maximum returns. Lump sum beats DCA ~67% of the time in rising markets, but DCA reduces regret and improves follow-through.

## Related Skills

- **altcoin-rotation** — DCA into BTC/ETH during accumulation, then rotate to alts when cycle shifts
- **on-chain-analysis** — On-chain metrics help identify macro accumulation zones for enhanced DCA timing
- **position-sizing** — DCA is a position-building approach; combine with position sizing for individual entries
