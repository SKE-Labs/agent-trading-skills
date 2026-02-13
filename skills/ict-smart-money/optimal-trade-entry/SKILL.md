---
name: optimal-trade-entry
description: Execute Optimal Trade Entry (OTE) using Fibonacci retracement between 62-79%. Use when entering after structure breaks, timing entries on pullbacks, or finding high-probability retracement levels.
---

# Optimal Trade Entry (OTE)

OTE is the sweet spot retracement zone (62%-79% Fib) where smart money typically enters positions.

## The OTE Zone

| Fib Level | Significance             |
| --------- | ------------------------ |
| 61.8%     | Start of OTE zone        |
| 70.5%     | Midpoint (CE equivalent) |
| 79%       | End of OTE zone          |

The 62-79% zone balances:

- Deep enough for good R:R
- Not so deep that you're caught in reversal

## When to Use OTE

1. **After BOS/CHoCH** - Pullback entry in new direction
2. **After liquidity sweep** - Retracement entry
3. **During trending moves** - Continuation entries

## Entry Workflow

### Step 1: Identify the Impulse

- Find a strong impulsive move (displacement)
- Must have clear swing low to swing high (or vice versa)

### Step 2: Draw Fibonacci

Use `get_candles_around_date` to get exact swing points, then use `draw_chart_analysis` with `fib_retracement`:

- **Bullish**: Point 1 = swing low, Point 2 = swing high
- **Bearish**: Point 1 = swing high, Point 2 = swing low

### Step 3: Calculate OTE Zone

Use the `execute` tool to calculate exact OTE levels:

```
execute(command='python3 -c "h=52000;l=45000;r=h-l;ote_start=h-r*0.618;ote_mid=h-r*0.705;ote_end=h-r*0.79;print(f\"OTE Start (61.8%): {ote_start:.2f}\\nOTE Mid (70.5%): {ote_mid:.2f}\\nOTE End (79%): {ote_end:.2f}\")"')
```

Calculate R:R for entry at 70.5%:

```
execute(command='python3 -c "h=52000;l=45000;r=h-l;e=h-r*0.705;risk=e-l;t1=h;t2=h+r*0.272;t3=h+r*0.618;print(f\"Entry: {e:.2f}\\nRisk: {risk:.2f}\\nR:R to {t1:.2f}: {(t1-e)/risk:.2f}:1\\nR:R to {t2:.2f}: {(t2-e)/risk:.2f}:1\\nR:R to {t3:.2f}: {(t3-e)/risk:.2f}:1\")"')
```

### Step 4: Mark OTE Zone

- Zone between 61.8% and 79%
- Use `draw_chart_analysis` with `demand`/`supply` type

### Step 5: Enter at OTE

- Set limit order at 70.5% (midpoint) OR
- Wait for price action confirmation in zone

### Step 6: Stop & Target

- **Stop loss**: Beyond the 100% (swing point)
- **Target**: Extension levels (1.27, 1.618, 2.0)

## OTE + Confluence

Best entries combine OTE with:

- Order block in the zone
- Fair value gap in the zone
- Previous structure level

## Example R:R Calculation

Entry at 70% retracement:

- Stop at 100% = 30% of move risked
- Target at 0% = 70% profit
- **R:R = 2.33:1** minimum

Targeting extensions:

- -27% extension = 97% profit = **3.23 R:R**
- -62% extension = 132% profit = **4.4 R:R**
