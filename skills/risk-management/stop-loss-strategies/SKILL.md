---
name: stop-loss-strategies
description: Place strategic stop losses using structure, ATR, or volatility methods. Use when protecting capital, defining trade invalidation, or managing downside risk.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Stop Loss Strategies

Proper stop placement protects capital while giving trades room to work.

## Stop Loss Methods

### 1. Structure-Based (Recommended)

- Place below swing low (long) or above swing high (short)
- Respects market structure
- Invalidation point is clear

### 2. ATR-Based

```
Stop = Entry - (ATR × Multiplier)
```

- Typical multiplier: 1.5-2x
- Adjusts to volatility
- More mechanical

### 3. Percentage-Based

- Fixed % below entry
- Simple but ignores structure
- Use only for position sizing limits

### 4. Support/Resistance Based

- Below support zone (long)
- Above resistance zone (short)
- Beyond the level, not at it

### 5. Moving Average Based

- Below key MA (20, 50, or 200)
- Dynamic stop level
- Good for trend following

## Stop Placement Guidelines

| Do                          | Don't                            |
| --------------------------- | -------------------------------- |
| Place beyond structure      | Place at obvious levels          |
| Account for volatility      | Use too tight stops              |
| Give "wiggle room"          | Stop hunt yourself               |
| Pre-calculate position size | Move stop to breakeven too early |

## Buffer Rules

Add buffer to avoid stop hunts:

- Below support: 0.5-1% buffer
- Based on ATR: Add 0.3x ATR
- Round numbers: Avoid exact round #

## Stop Loss by Trade Type

| Trade Type | Stop Placement        |
| ---------- | --------------------- |
| Scalp      | Very tight (0.3-0.5%) |
| Day trade  | Below minor structure |
| Swing      | Below major structure |
| Position   | Below trend structure |

## Stop Management

### Initial Stop

- Set at entry based on analysis
- Never move to widen loss
- Based on invalidation point

### Breakeven Stop

- Move to breakeven after 1R profit
- Locks in risk-free trade
- Not too early (avoid noise)

### Trailing Stop (see trailing-stop skill)

- Locks in profits as trade progresses
- Multiple methods available

## Mental Stops

**Never use mental stops.** Always:

- Set actual stop order
- Define before entering
- Accept the loss level

## Related Skills

- **trailing-stop** — After initial stop is set, trailing stop strategies lock in profits as the trade progresses
- **position-sizing** — Stop distance is a direct input to position size; tighter stops allow larger positions
- **risk-reward-ratio** — Stop placement determines the risk side of the R:R equation
