---
name: head-and-shoulders
description: Identify and trade head and shoulders reversal patterns. Use when spotting major trend reversals, validating bearish/bullish structure changes, or finding high R:R reversal setups.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending"]
---

# Head and Shoulders Pattern

H&S is a reliable reversal pattern signaling the end of an uptrend (or downtrend for inverse).

## Pattern Structure

### Head & Shoulders (Bearish Reversal)

1. **Left Shoulder**: Rally to new high, pullback
2. **Head**: Higher high than left shoulder, pullback
3. **Right Shoulder**: Lower high than head, starts to drop
4. **Neckline**: Connect the two lows (support)

### Inverse H&S (Bullish Reversal)

1. **Left Shoulder**: Drop to new low, bounce
2. **Head**: Lower low than left shoulder, bounce
3. **Right Shoulder**: Higher low than head, starts to rise
4. **Neckline**: Connect the two highs (resistance)

## Validation Criteria

| Criteria    | Requirement                         |
| ----------- | ----------------------------------- |
| Volume      | Decreasing on right shoulder        |
| Symmetry    | Shoulders roughly equal height      |
| Neckline    | Clear, identifiable line            |
| Prior Trend | Must have existing trend to reverse |

## Entry Strategies

### 1. Neckline Break (Conservative)

- Wait for price to break and close below/above neckline
- Enter on the break with volume confirmation
- Stop: Above right shoulder

### 2. Retest Entry (Preferred)

- Wait for neckline break
- Wait for price to retest neckline
- Enter on rejection from neckline
- Tighter stop, better R:R

## Target Calculation

**Measured Move**:

- Measure distance from head to neckline
- Project that distance from neckline break point
- Example: Head at 100, Neckline at 90 → Target = 80

## Chart Marking

Use `draw_chart_analysis`:

1. Mark left shoulder, head, right shoulder with `highlight` (LL, Head, LH labels)
2. Draw neckline with `support` type
3. Visualize the pattern clearly

## Common Mistakes

- Trading before neckline break
- Ignoring volume profile
- Pattern too small (noise, not structure)
- Missing the prior trend requirement

## Related Skills

- **multi-timeframe-analysis** — H&S on HTF signals major trend reversals; confirm with LTF structure shifts
- **double-top-bottom** — Similar reversal pattern family; right shoulder failure resembles a double top
- **position-sizing** — Measured move from head to neckline provides clear target for position sizing
