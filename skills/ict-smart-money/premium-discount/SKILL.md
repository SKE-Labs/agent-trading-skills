---
name: premium-discount
description: Enter positions in discount zones (below equilibrium) and exit in premium zones (above). Use when determining optimal entry areas, understanding value-based trading, or timing buy/sell decisions.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending", "ranging"]
---

# Premium & Discount Trading

The market oscillates between premium (expensive) and discount (cheap) zones around an equilibrium point.

## Core Concept

**Equilibrium** = 50% of any price range

| Zone            | Location  | Action                 |
| --------------- | --------- | ---------------------- |
| **Premium**     | Above 50% | Look for shorts/exits  |
| **Equilibrium** | At 50%    | Decision point         |
| **Discount**    | Below 50% | Look for longs/entries |

## Calculation

For any swing (high to low):

```
Equilibrium = (Swing High + Swing Low) / 2
```

Or use Fibonacci tool:

- 0% = Swing High
- 50% = Equilibrium
- 100% = Swing Low

## Trading Rules

### For Longs (Bullish Bias)

- **Enter**: Only in discount zone (below 50%)
- **Avoid**: Entries in premium zone
- **Best entries**: 61.8% - 79% (OTE in discount)

### For Shorts (Bearish Bias)

- **Enter**: Only in premium zone (above 50%)
- **Avoid**: Entries in discount zone
- **Best entries**: 61.8% - 79% (OTE in premium)

## Workflow

1. **Identify the swing range**

   - Use HTF to find major swing high/low
   - Draw Fibonacci retracement

2. **Determine current position**

   - Above 50% = Premium
   - Below 50% = Discount

3. **Align with bias**

   - Bullish bias → Wait for discount entries
   - Bearish bias → Wait for premium entries

4. **Enter at OTE within correct zone**
   - OTE (62-79%) in discount for longs
   - OTE (62-79%) in premium for shorts

## Multi-Timeframe Application

| Timeframe    | Purpose                      |
| ------------ | ---------------------------- |
| Weekly/Daily | Determine overall P/D zone   |
| 4H           | Find swing range for trading |
| 1H/15m       | Refine entry within zone     |

## Key Insight

Why this works:

- Institutions buy at discount (accumulation)
- Institutions sell at premium (distribution)
- Retail buys premium "breakouts" → bad entries
- Retail sells discount "breakdowns" → bad entries

**Think like institutions**: Buy cheap, sell expensive.

## Chart Marking

Use `draw_chart_analysis`:

- Mark equilibrium with `support`/`resistance`
- Mark OTE zone with `demand`/`supply`
- Visualize the range boundaries

## Related Skills

- **optimal-trade-entry** — OTE provides the precise entry zone within premium/discount areas
- **fibonacci-trading** — Fibonacci levels define the premium/discount boundaries and extension targets
- **market-structure-shift** — Structure determines whether to look for entries in premium (shorts) or discount (longs)
