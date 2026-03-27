---
name: stop-loss-strategies
description: Place strategic stop losses using structure, ATR, or volatility methods. Use when protecting capital, defining trade invalidation, or managing downside risk.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
---

# Stop Loss Strategies

Proper stop placement protects capital while giving trades room to work.

## Stop Loss Methods

### 1. Structure-Based (Recommended)

Place below swing low (long) or above swing high (short). Respects market structure with a clear invalidation point.

### 2. ATR-Based

`Stop = Entry - (ATR x Multiplier)` (typical multiplier: 1.5-2x). Adjusts to volatility automatically.

### 3. Support/Resistance Based

Place beyond (not at) key S/R zones. Below support for longs, above resistance for shorts.

### 4. Moving Average Based

Place below key MA (20, 50, or 200). Dynamic stop level, good for trend following.

### 5. Percentage-Based

Fixed % below entry. Simple but ignores structure -- use only as a position sizing limit.

## Stop Placement by Trade Type

| Trade Type | Stop Placement        |
| ---------- | --------------------- |
| Scalp      | Very tight (0.3-0.5%) |
| Day trade  | Below minor structure  |
| Swing      | Below major structure  |
| Position   | Below trend structure  |

## Buffer Rules

Add buffer to avoid stop hunts:

- Below support: 0.5-1% buffer
- Based on ATR: add 0.3x ATR
- Round numbers: avoid exact round levels

## Stop Management

**Initial Stop**: Set at entry based on analysis. Based on the invalidation point for the trade thesis.

**Breakeven Stop**: Move to breakeven after 1R profit. Locks in a risk-free trade. Not too early -- avoid getting stopped by noise.

**Trailing Stop**: Locks in profits as the trade progresses (see trailing-stop skill).

## Workflow

1. **Identify invalidation** -- the price level where the trade thesis is wrong
2. **Choose method** -- structure-based for most setups, ATR-based for volatile assets
3. **Add buffer** -- 0.5-1% or 0.3x ATR beyond the level
4. **Set the order** -- always place an actual stop order, never a mental stop
5. **Manage** -- move to breakeven at 1R, then trail (see trailing-stop)

## Key Rules

- NEVER use mental stops -- always set an actual stop order before entering
- NEVER move a stop to widen a loss -- only move stops in the profit direction
- NEVER place stops at obvious round numbers or exact S/R levels -- add a buffer
- NEVER move to breakeven too early -- give the trade room to work past noise
- Define stop before entry and accept the loss level
- Tighter stops allow larger positions; wider stops require smaller positions

## Related Skills

- **trailing-stop** -- manages exits after initial stop is set
- **position-sizing** -- stop distance is a direct input to position size calculation
