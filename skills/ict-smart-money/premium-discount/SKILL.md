---
name: premium-discount
description: Enter positions in discount zones (below equilibrium) and exit in premium zones (above). Use when determining optimal entry areas, understanding value-based trading, or timing buy/sell decisions.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Premium & Discount Trading

The market oscillates between premium (expensive) and discount (cheap) zones around an equilibrium point.

## Core Concept

**Equilibrium** = (Swing High + Swing Low) / 2

| Zone            | Location  | Action                 |
| --------------- | --------- | ---------------------- |
| **Premium**     | Above 50% | Look for shorts/exits  |
| **Equilibrium** | At 50%    | Decision point         |
| **Discount**    | Below 50% | Look for longs/entries |

### Trading Zones
- **Longs**: Enter only in discount (below 50%). Best entries at 61.8%-79% (OTE in discount)
- **Shorts**: Enter only in premium (above 50%). Best entries at 61.8%-79% (OTE in premium)

## Workflow

1. **Identify the swing range** on HTF (Weekly/Daily for zone, 4H for swing range):
   ```
   get_candles_around_date(symbol=<symbol>, interval="1d", date=<date>)
   ```
2. **Draw Fibonacci** using `draw_chart_analysis` with `fib_retracement` (0% = Swing High, 100% = Swing Low)
3. **Determine current position**: Above 50% = Premium, Below 50% = Discount
4. **Mark levels** using `draw_chart_analysis`: equilibrium with `support`/`resistance`, OTE zone with `demand`/`supply`
5. **Align with bias**:
   - Bullish bias: wait for discount entries
   - Bearish bias: wait for premium entries
6. **Enter at OTE** (62-79%) within the correct zone
7. **Refine entry** on LTF (1H/15m) for precision

## Key Rules

- Institutions buy at discount (accumulation) and sell at premium (distribution)
- NEVER buy in premium or sell in discount -- this is the retail trap
- HTF determines the overall P/D zone; LTF refines the entry within it
- Equilibrium (50%) is the decision point -- price above favors shorts, below favors longs

## Related Skills

- **optimal-trade-entry** — OTE provides the precise entry within premium/discount zones
- **market-structure-shift** — Structure determines whether to look for entries in premium or discount
