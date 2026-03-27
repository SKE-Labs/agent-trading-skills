---
name: dca-strategy
description: Implement Dollar Cost Averaging for systematic long-term accumulation. Use when building positions over time, reducing timing risk, or accumulating during uncertainty.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Dollar Cost Averaging (DCA)

Invest fixed amounts at regular intervals regardless of price, reducing timing risk and emotional decision-making.

## DCA Mechanics

```
Each Purchase = Fixed Amount / Current Price
Average Cost  = Total Spent / Total Units Acquired
```

Example ($100/week):
- Week 1: $100 / $50 = 2.0 units
- Week 2: $100 / $40 = 2.5 units
- Week 3: $100 / $60 = 1.67 units
- Total: 6.17 units for $300 (avg cost: $48.62)

## DCA Variants

| Variant           | Description                                      |
| ----------------- | ------------------------------------------------ |
| Fixed Interval    | Same amount every week/month -- simplest          |
| Value Averaging   | Adjust amount to hit a target portfolio value     |
| Enhanced DCA      | Base amount + bonus when price drops below MA     |
| Lump Sum + DCA    | Deploy 50% immediately, DCA the remaining 50%    |

## Best Assets for DCA

| Suitable         | Less Suitable              |
| ---------------- | -------------------------- |
| BTC, ETH         | Low-cap altcoins           |
| Major indices    | Meme coins                 |
| Blue chip stocks | Highly volatile micro-caps |

## Workflow

1. **Check current price** against historical average:
```
get_latest_candle(symbol="BTCUSDT")
get_indicator(indicator_code="sma", symbol="BTCUSDT", interval="1w")
```

2. **Assess if Enhanced DCA bonus applies** (price below 200-day MA):
```
get_indicator(indicator_code="sma", symbol="BTCUSDT", interval="1d")
```

3. **Evaluate macro conditions** for DCA continuation or pause:
```
get_financial_news(query="BTC macro outlook accumulation")
```

4. **Report recommendation**: current price vs DCA average, whether to buy standard or enhanced amount, and any flags to pause (fundamental deterioration).

## When to Stop DCA

- Target position size reached
- Fundamentals have materially deteriorated
- Better risk/reward opportunity identified elsewhere

## Key Rules

- NEVER skip a scheduled DCA buy based on short-term price action -- consistency is the point
- NEVER DCA into low-cap altcoins or meme tokens -- stick to BTC, ETH, or major assets
- Review quarterly, not daily; over-monitoring defeats the purpose
- Lump sum beats DCA ~67% of the time in rising markets, but DCA reduces regret and improves follow-through

## Related Skills

- **altcoin-rotation** -- DCA into BTC/ETH during accumulation, then rotate when cycle shifts
- **on-chain-analysis** -- MVRV and realized cap identify macro accumulation zones for enhanced DCA
