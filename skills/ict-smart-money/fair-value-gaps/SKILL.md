---
name: fair-value-gaps
description: Trade fair value gaps (FVG) and imbalances where price moved too fast, leaving unfilled zones. Use when identifying retracement targets, finding high-probability entry points, or analyzing institutional order flow imbalances.
---

# Fair Value Gaps (FVG) Trading

FVGs are 3-candle patterns where price moved so fast it left a "gap" between wicks, indicating market inefficiency.

## Identification

### Bullish FVG

1. Strong bullish middle candle
2. Gap between: **Candle 1 high** and **Candle 3 low**
3. Zone = the unfilled gap area

### Bearish FVG

1. Strong bearish middle candle
2. Gap between: **Candle 1 low** and **Candle 3 high**
3. Zone = the unfilled gap area

## FVG Quality Factors

| Factor  | High Quality                      | Low Quality     |
| ------- | --------------------------------- | --------------- |
| Size    | Large gap (>50% of middle candle) | Small gap       |
| Context | After liquidity sweep             | Random location |
| Volume  | High volume on creation           | Low volume      |
| HTF     | Aligns with HTF bias              | Against HTF     |

## Trading Strategies

### 1. Fill & React (Most Common)

- Wait for price to return and fill the FVG
- Enter when price reaches 50% of FVG
- Stop beyond the full FVG

### 2. Consequent Encroachment (CE)

- Enter at the 50% level (midpoint) of the FVG
- Most precise entry point
- Higher win rate, tighter stops

### 3. FVG + Order Block Confluence

- Best setups: FVG overlaps with order block
- Treat as single high-probability zone

## Entry Workflow

1. **Identify FVG** after impulsive move
2. **Mark the zone** using `draw_chart_analysis` with type `demand` or `supply`
3. **Wait for retracement** into the gap
4. **Enter at 50%** (CE) or wait for reaction
5. **Stop loss** beyond the FVG
6. **Target** the high/low of the impulse move

## Key Rules

- FVGs act as magnets—price tends to return
- Unfilled FVGs on HTF are powerful future targets
- Multiple FVGs stacked = strong directional bias
