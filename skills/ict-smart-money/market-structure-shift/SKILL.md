---
name: market-structure-shift
description: Detect Break of Structure (BOS) and Change of Character (CHoCH) for trend analysis. Use when identifying trend reversals, confirming entry signals, or determining market bias direction.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Market Structure Shift

Identify trend direction and potential reversals through swing point analysis.

## Structure

### Swing Points
- **Higher High (HH)** + **Higher Low (HL)** = Uptrend
- **Lower Low (LL)** + **Lower High (LH)** = Downtrend

### Break of Structure (BOS)
- Continuation signal confirming current trend
- **Bullish BOS**: Price breaks above swing high (HH)
- **Bearish BOS**: Price breaks below swing low (LL)

### Change of Character (CHoCH)
- Reversal signal indicating potential trend change
- **Bullish CHoCH**: In downtrend, price breaks above LH
- **Bearish CHoCH**: In uptrend, price breaks below HL

## Workflow

1. **Identify current trend** on HTF (4H/Daily):
   ```
   get_candles_around_date(symbol=<symbol>, interval="4h", date=<date>)
   ```
2. **Mark swing points** using `draw_chart_analysis` with `highlight` type (label HH, HL, LH, LL)
3. **Watch for structure breaks**:
   - BOS = trade continuation (enter on pullback to FVG or order block)
   - CHoCH = look for reversal entry
4. **Confirm with LTF** (15m/5m): Wait for LTF CHoCH in reversal direction, then enter

### Trend Continuation Entry (BOS)
1. Wait for BOS confirmation
2. Enter on pullback to FVG or order block
3. Stop below recent swing low (bull) or above swing high (bear)

### Trend Reversal Entry (CHoCH)
1. Wait for CHoCH confirmation on HTF
2. Wait for LTF BOS in the new direction
3. Enter on retracement to CHoCH level
4. Stop beyond the CHoCH swing point

## Key Rules

- HTF structure determines bias; LTF structure provides entry timing
- NEVER counter-trade HTF structure without a confirmed CHoCH
- A single break is not enough — wait for the follow-through (LTF confirmation)
- Use Daily/4H for direction, 1H/30m for intermediate structure, 15m/5m for entry timing

## Related Skills

- **order-blocks** — After BOS/CHoCH, order blocks at the break point become high-probability entries
- **liquidity-zones** — Structure breaks often occur after liquidity sweeps of swing points
