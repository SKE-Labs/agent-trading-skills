---
name: trailing-stop
description: Lock in profits with dynamic trailing stop strategies. Use when riding winner trends, protecting open profits, or managing exits systematically.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending"]
---

# Trailing Stop Strategies

Trailing stops lock in profits while allowing trades to run.

## Trailing Methods

### 1. Fixed Distance Trail

- Move stop by fixed amount (pips/%)
- Example: Trail by 20 pips behind price
- Simple but can be too static

### 2. ATR Trail (Recommended)

```
Trailing Stop = Highest High - (ATR × 2)
```

- Adjusts to volatility
- Tighter in calm markets
- Wider in volatile markets

### 3. Structure Trail

- Move stop below each new swing low (long)
- Move stop above each new swing high (short)
- Lets trade breathe but locks in structure

### 4. Moving Average Trail

- Use MA as trailing stop
- Common: 10 EMA, 20 EMA
- Exit when price closes below MA

### 5. Chandelier Exit

- Trail from highest high by ATR multiple
- Classic exit strategy
- Good for trending markets

## When to Start Trailing

| Trigger             | Strategy     |
| ------------------- | ------------ |
| After 1R profit     | Conservative |
| After 2R profit     | Moderate     |
| New structure break | Dynamic      |
| Immediately         | Aggressive   |

## Trail Management

### Do

- Pre-define trailing rules
- Trail only in profit direction
- Consider volatility
- Allow some drawdown

### Don't

- Trail too tightly (noise exit)
- Trail against trend structure
- Override during trade
- Manually exit before stop

## Hybrid Approach

Combine methods:

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

## Example Workflow

**Long trade at $100, stop at $95:**

1. Price hits $108 (1.5R) → Move stop to $100 (breakeven)
2. Price hits $115 (3R) → Trail to $110 (below last swing)
3. Price hits $120 → Trail to $115
4. Price pulls back → Stop hit at $115 (3R locked)

## Related Skills

- **stop-loss-strategies** — Initial stop placement determines when trailing begins; this skill manages exits after entry
- **partial-profit-taking** — Combine trailing stops with partial exits for optimal profit capture
- **momentum-trading** — Trailing stops are essential for riding momentum moves without giving back profits
