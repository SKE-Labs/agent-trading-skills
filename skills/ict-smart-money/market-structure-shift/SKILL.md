---
name: market-structure-shift
description: Detect Break of Structure (BOS) and Change of Character (CHoCH) for trend analysis. Use when identifying trend reversals, confirming entry signals, or determining market bias direction.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Market Structure Shift

Market structure analysis identifies trend direction and potential reversals through swing point analysis.

## Core Concepts

### Swing Points

- **Higher High (HH)**: High above previous high → Bullish
- **Higher Low (HL)**: Low above previous low → Bullish
- **Lower Low (LL)**: Low below previous low → Bearish
- **Lower High (LH)**: High below previous high → Bearish

### Break of Structure (BOS)

- Continuation signal confirming trend
- **Bullish BOS**: Price breaks above swing high (HH)
- **Bearish BOS**: Price breaks below swing low (LL)

### Change of Character (CHoCH)

- Reversal signal indicating potential trend change
- **Bullish CHoCH**: In downtrend, price breaks above LH
- **Bearish CHoCH**: In uptrend, price breaks below HL

## Structure Analysis Workflow

1. **Identify current trend** using HTF (4H/Daily)

   - HH + HL = Uptrend
   - LH + LL = Downtrend

2. **Mark swing points** using `draw_chart_analysis` with `highlight` type

3. **Watch for structure breaks**:

   - BOS = Trade continuation
   - CHoCH = Look for reversal entry

4. **Confirm with LTF**:
   - Wait for LTF CHoCH in reversal direction
   - Enter after LTF structure confirms

## Multi-Timeframe Structure

| Timeframe | Purpose                 |
| --------- | ----------------------- |
| Daily/4H  | Overall trend direction |
| 1H/30m    | Intermediate structure  |
| 15m/5m    | Entry timing            |

## Entry Strategies

### Trend Continuation (BOS)

1. Wait for BOS confirmation
2. Enter on pullback to FVG or order block
3. Stop below recent swing low (bull) or high (bear)

### Trend Reversal (CHoCH)

1. Wait for CHoCH confirmation
2. Wait for LTF BOS in new direction
3. Enter on retracement to CHoCH level
4. Stop beyond the CHoCH swing point

## Chart Marking

Use `draw_chart_analysis` with `highlight` type:

- Mark HH, HL, LH, LL labels at swing points
- This visualizes the market structure clearly

## Related Skills

- **multi-timeframe-analysis** — Structure on HTF defines bias; LTF structure shifts provide entry timing
- **order-blocks** — After a BOS/CHoCH, order blocks at the break point become high-probability entry zones
- **liquidity-zones** — Structure breaks often occur after liquidity sweeps of swing points
