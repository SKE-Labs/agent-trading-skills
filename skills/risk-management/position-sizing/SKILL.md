---
name: position-sizing
description: Calculate risk-based position sizes using fixed %, fractional Kelly, ATR-hybrid, or volatility methods. Use when determining trade size, managing account risk, adjusting for correlated positions, or standardizing risk across trades.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "3.0"
---

# Position Sizing

Position sizing determines how much capital to risk per trade -- the single most important factor in long-term survival.

## Sizing Methods

### 1. Fixed Percentage Risk (Default)

`Position Size = (Account x Risk%) / (Entry - Stop)`

Example: $10,000 account, 1% risk, entry $100, stop $95 => $100 / $5 = 20 shares.

### 2. Volatility-Based (ATR)

`Position Size = (Account x Risk%) / (ATR x Multiplier)`

| Market Volatility       | ATR Multiplier | Effect                       |
| ----------------------- | -------------- | ---------------------------- |
| Low (ATR < 50th pctl)   | 1.5            | Tighter stop, larger position |
| Normal                  | 2.0            | Standard                     |
| High (ATR > 80th pctl)  | 2.5-3.0        | Wider stop, smaller position |

### 3. ATR-Hybrid (Recommended for Advanced)

Combines fixed % risk with ATR-based stop distance: `Position Size = (Account x Risk%) / (ATR x Multiplier)`. Adapts to volatility while maintaining consistent dollar risk per trade.

### 4. Fractional Kelly Criterion

`Full Kelly % = W - (1 - W) / R` where W = win rate, R = avg win / avg loss.

**Never use full Kelly.** Use a fraction:

| Kelly Fraction   | Risk Level          | Who Should Use                       |
| ---------------- | ------------------- | ------------------------------------ |
| Half Kelly (50%) | Aggressive          | Experienced with >100 trade sample   |
| Quarter Kelly    | Moderate            | **Recommended starting point**       |
| Tenth Kelly      | Conservative        | Learning, small sample size          |

Quarter Kelly achieves ~75% of full Kelly's growth rate with far less drawdown risk.

## Method Selection

| Situation                             | Method                         |
| ------------------------------------- | ------------------------------ |
| Starting out, <50 tracked trades      | Fixed % at 0.5-1%             |
| Established win rate (100+ trades)    | Quarter Kelly, capped at 2%   |
| Volatile assets (crypto, small caps)  | ATR-Hybrid at 1% risk         |
| Swing trading with structure stops    | Fixed % at 1-2%               |
| Scalping / day trading                | Fixed % at 0.5%               |
| Multiple correlated positions         | Fixed % at reduced rate        |

## Risk Limits

| Limit              | Threshold                                    |
| ------------------ | -------------------------------------------- |
| Single trade max   | 2% of account (3% absolute ceiling)          |
| Correlated trades  | Combined max 2% for high-correlation (>0.7)  |
| Daily loss limit   | 3-5% of account -- stop trading              |
| Weekly loss limit  | 5-8% -- reduce to 50% size, review           |
| Monthly loss limit | 10% -- 1 week break, resume at 25% size      |
| Pre-event          | Cut 50-75% before Score >= 8 events          |

## Workflow

1. **Get entry and stop loss** from the technical analyst's analysis
2. **Check for correlated positions** -- are existing positions in correlated assets?
3. **Select sizing method** based on situation (see table above)
4. **Calculate position size** using `calculate_position_size` (pass entry, stop loss, user profile with balance/risk settings)
5. **Verify against limits** -- single trade <= 2%, daily exposure within limit, correlated positions within combined limit
6. **Adjust for events** -- reduce 50-75% if high-impact economic event within 24h
7. **Create signal** with the calculated size via `create_trading_signal`

## Key Rules

- NEVER use full Kelly -- quarter Kelly achieves ~75% of the growth with survivable drawdowns
- NEVER size based on conviction -- "I'm really sure" is not a sizing method
- NEVER increase size after losses to "make it back" -- revenge sizing is the fastest path to ruin
- NEVER hold full size into FOMC/NFP/CPI -- reduce pre-event, always
- Correlated positions (>0.7) are a single bet -- 5 long tech positions at 1% each = 5% in one sector
- Use the same method consistently; do not switch based on recent results
- Start with quarter Kelly, not half; track every trade for Kelly inputs

## Related Skills

- **correlation-risk** -- correlated positions must be sized as combined exposure
- **stop-loss-strategies** -- stop distance is a direct input to position size calculation
