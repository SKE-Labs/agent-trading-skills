---
name: trailing-stop
description: Lock in profits with dynamic trailing stop strategies. Use when riding winner trends, protecting open profits, or managing exits systematically.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
---

# Trailing Stop Strategies

Trailing stops lock in profits while allowing trades to run.

## Trailing Methods

### 1. ATR Trail (Recommended)

`Trailing Stop = Highest High - (ATR x 2)`. Adjusts to volatility -- tighter in calm markets, wider in volatile markets.

### 2. Structure Trail

Move stop below each new swing low (long) or above each new swing high (short). Lets the trade breathe while locking in structure.

### 3. Moving Average Trail

Use MA as trailing stop (common: 10 EMA, 20 EMA). Exit when price closes below MA.

### 4. Chandelier Exit

Trail from highest high by ATR multiple. Classic exit strategy, good for trending markets.

### 5. Fixed Distance Trail

Move stop by fixed amount (pips/%). Simple but can be too static -- prefer ATR or structure.

## When to Start Trailing

| Trigger             | Strategy     |
| ------------------- | ------------ |
| After 1R profit     | Conservative |
| After 2R profit     | Moderate     |
| New structure break | Dynamic      |
| Immediately         | Aggressive   |

## Hybrid Approach

Combine methods for staged exit management:

1. Fixed initial stop
2. Move to breakeven at 1R
3. Trail by structure after 2R
4. Tight ATR trail near target

## Exit Scenarios

| Price Action    | Trailing Action   |
| --------------- | ----------------- |
| New high/low    | Move stop up/down |
| Consolidation   | Keep stop same    |
| Reversal candle | Tighten trail     |
| Structure break | Consider exiting  |

## Workflow

**Example -- Long trade at $100, stop at $95:**

1. Price hits $108 (1.5R) -> Move stop to $100 (breakeven)
2. Price hits $115 (3R) -> Trail to $110 (below last swing)
3. Price hits $120 -> Trail to $115
4. Price pulls back -> Stop hit at $115 (3R locked)

## Key Rules

- NEVER trail too tightly -- noise will stop you out prematurely
- NEVER trail against trend structure -- only move stops in the profit direction
- NEVER override your trailing rules during a trade -- define them before entry
- NEVER manually exit before your trailing stop is hit unless structure clearly breaks
- Pre-define trailing rules before entering the trade
- Allow some drawdown from highs -- that is the cost of catching extended moves

## Related Skills

- **stop-loss-strategies** -- initial stop placement determines when trailing begins
- **partial-profit-taking** -- combine trailing stops with partial exits for optimal capture
