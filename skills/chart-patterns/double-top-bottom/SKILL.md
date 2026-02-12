---
name: double-top-bottom
description: Trade double and triple top/bottom reversal patterns. Use when identifying trend exhaustion, finding reversal entries at key resistance/support, or confirming failed breakouts.
---

# Double Top & Bottom Patterns

Double tops/bottoms signal reversal when price fails to break a level twice.

## Pattern Structure

### Double Top (Bearish)

1. Price rallies to resistance (Peak 1)
2. Pullback to support (Neckline)
3. Rally back to same resistance (Peak 2)
4. Failure to break → Reversal

### Double Bottom (Bullish)

1. Price drops to support (Trough 1)
2. Bounce to resistance (Neckline)
3. Drop back to same support (Trough 2)
4. Failure to break → Reversal

### Triple Top/Bottom

Same concept with 3 tests of the level.

- More confirmations = Stronger pattern
- But also means level may finally break

## Validation Criteria

| Factor                     | Strong Pattern        | Weak Pattern            |
| -------------------------- | --------------------- | ----------------------- |
| Time between peaks/troughs | 2-4 weeks             | Very close or far apart |
| Volume                     | Declining on 2nd test | Higher on 2nd test      |
| Peak/trough alignment      | Within 3%             | Widely different        |
| Neckline break             | With volume           | Weak close              |

## Entry Strategies

### 1. Neckline Break

- Enter when price breaks neckline
- Confirmation: Candle close beyond neckline
- Stop: Beyond the peaks/troughs

### 2. Neckline Retest

- Wait for break and then retest of neckline
- Enter on rejection (former support = resistance)
- Better R:R, may miss some moves

### 3. Early Entry (Aggressive)

- Enter at second peak/trough
- Requires additional confirmation (LTF reversal)
- Tightest stop, highest risk

## Target Calculation

**Measured Move**:

```
Target = Neckline ± (Peak/Trough - Neckline)
```

Example (Double Top):

- Peak at $100, Neckline at $90
- Target = $90 - ($100 - $90) = $80

## Chart Marking

Use `draw_chart_analysis`:

1. Mark the two peaks/troughs with `highlight`
2. Draw neckline with `support` or `resistance`
3. Pattern becomes clear visually

## Trading Tips

- The more obvious the pattern, the more it gets front-run
- Wait for confirmation (neckline break)
- Volume should confirm the reversal
- Failed double tops/bottoms can lead to strong continuation
