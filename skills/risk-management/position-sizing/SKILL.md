---
name: position-sizing
description: Calculate risk-based position sizes using fixed %, fractional Kelly, ATR-hybrid, or volatility methods. Use when determining trade size, managing account risk, adjusting for correlated positions, or standardizing risk across trades.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Position Sizing

Position sizing determines how much capital to risk per trade. It is the single most important factor in long-term survival — a great strategy with bad sizing will blow up.

## Position Sizing Methods

### 1. Fixed Percentage Risk (Default)

Most common and recommended. Risk a consistent % of account per trade:

```
Position Size = (Account × Risk %) / (Entry - Stop)
```

Example:

- Account: $10,000
- Risk: 1% = $100
- Entry: $100, Stop: $95 (risk $5/share)
- Position: $100 / $5 = 20 shares

### 2. Volatility-Based (ATR)

Automatically adjusts position size to market volatility — smaller positions when volatile, larger when calm:

```
Position Size = (Account × Risk %) / (ATR × Multiplier)
```

| Market Volatility | ATR Multiplier | Effect |
| --- | --- | --- |
| Low (ATR < 50th pctl) | 1.5 | Tighter stop, larger position |
| Normal | 2.0 | Standard |
| High (ATR > 80th pctl) | 2.5-3.0 | Wider stop, smaller position |

**When to use**: Swing trades, crypto, any asset with variable volatility.

### 3. ATR-Hybrid Method (Recommended for Advanced)

Combines fixed % risk with ATR-based stop distance:

```
ATR Stop = Entry ± (ATR × Multiplier)
Risk Amount = Account × Risk %
Position Size = Risk Amount / (ATR × Multiplier)
```

This method:
- Adapts to volatility automatically
- Maintains consistent dollar risk per trade
- Prevents oversizing in volatile markets

### 4. Fractional Kelly Criterion

The Kelly Criterion gives the mathematically optimal bet size for maximum growth:

```
Full Kelly % = W - (1 - W) / R
```

- W = Win rate (decimal)
- R = Average Win / Average Loss

**Critical: Never use full Kelly.** It leads to extreme drawdowns. Use fractional Kelly:

| Kelly Fraction | Risk Level | Who Should Use |
| --- | --- | --- |
| Full Kelly | Extremely aggressive | **Never in practice** |
| Half Kelly (50%) | Aggressive | Experienced with >100 trade sample |
| Quarter Kelly (25%) | Moderate | **Recommended starting point** |
| Tenth Kelly (10%) | Conservative | Learning, small sample size |

Example with 55% win rate, 1.5 R:R:

| Method | Calculation | Risk % |
| --- | --- | --- |
| Full Kelly | 0.55 - (0.45/1.5) = 0.25 | 25% ← would blow up |
| Half Kelly | 0.25 / 2 | 12.5% ← still too aggressive |
| Quarter Kelly | 0.25 / 4 | 6.25% ← aggressive but viable |
| Tenth Kelly | 0.25 / 10 | 2.5% ← reasonable |

**Key insight**: Quarter Kelly achieves ~75% of full Kelly's growth rate with far less volatility and drawdown risk.

### 5. Fixed Dollar Amount

- Risk same dollar amount per trade regardless of account size
- Simple but doesn't scale with account growth/decline
- Best for absolute beginners

## Method Selection Guide

| Your Situation | Recommended Method |
| --- | --- |
| Starting out, <50 tracked trades | Fixed % at 0.5-1% |
| Established win rate (100+ trades) | Quarter Kelly, capped at 2% |
| Trading volatile assets (crypto, small caps) | ATR-Hybrid at 1% risk |
| Swing trading with clear structure stops | Fixed % at 1-2% |
| Scalping / day trading | Fixed % at 0.5% (many trades/day) |
| Multiple correlated positions | Fixed % at reduced rate (see below) |

## Correlated Position Adjustment

Correlated positions multiply risk. Treat them as a single combined position:

| Correlation Level | Examples | Combined Max Risk |
| --- | --- | --- |
| High (>0.7) | BTC/ETH, AAPL/QQQ, EUR/GBP | 2% total across ALL positions |
| Moderate (0.4-0.7) | Gold/Silver, Tech stocks | 3% total |
| Low (<0.4) | BTC/Gold, Stocks/Bonds | Full individual sizing OK |

**Practical rule**: If you have 3 positions in BTC-correlated assets, each gets **0.67% risk** (2% ÷ 3) instead of 1% each.

## Recommended Guidelines

| Account Phase | Risk per Trade | Daily Max | Weekly Max |
| --- | --- | --- | --- |
| Learning | 0.5% | 1.5% | 3% |
| Developing | 1% | 2-3% | 5% |
| Experienced | 1-2% | 3-5% | 8% |
| Maximum ever | 3% | 5% | 10% |

## Tool Integration

Use `calculate_position_size` with:

- Entry price
- Stop loss price
- User profile (contains balance, risk settings)

The tool automatically calculates:

- Position quantity
- Capital allocation
- Recommended leverage

### Quick Calculations

Use the `execute` tool for instant calculations:

**Fixed % Risk:**
```
execute(command='python3 -c "bal=10000;risk_pct=1;e=100;sl=95;risk_amt=bal*risk_pct/100;risk_per_unit=abs(e-sl);size=risk_amt/risk_per_unit;print(f\"Position: {size:.2f} units ({size*e:.2f} value)\")"')
```

**Quarter Kelly:**
```
execute(command='python3 -c "win_rate=0.55;rr=1.5;kelly=(win_rate-(1-win_rate)/rr);quarter=kelly/4;print(f\"Full Kelly: {kelly*100:.1f}%\\nQuarter Kelly: {quarter*100:.2f}% (recommended)\\nHalf Kelly: {kelly/2*100:.2f}%\")"')
```

**ATR-Hybrid:**
```
execute(command='python3 -c "bal=10000;risk_pct=1;atr=3.5;mult=2.0;risk_amt=bal*risk_pct/100;stop_dist=atr*mult;size=risk_amt/stop_dist;print(f\"Position: {size:.2f} units\\nATR stop distance: {stop_dist:.2f}\\nRisk amount: {risk_amt:.2f}\")"')
```

**Correlated Position Sizing:**
```
execute(command='python3 -c "bal=10000;max_corr_risk=2;num_positions=3;per_position=max_corr_risk/num_positions;risk_amt=bal*per_position/100;print(f\"Max combined risk: {max_corr_risk}%\\nPer-position risk: {per_position:.2f}%\\nPer-position amount: ${risk_amt:.2f}\")"')
```

## Position Sizing Workflow

1. **Get entry and stop loss** from the technical analyst's analysis
2. **Check for correlated positions** — are existing positions in correlated assets?
3. **Select sizing method** based on situation (see selection guide)
4. **Calculate position size** using `calculate_position_size` or `execute`
5. **Verify against limits**:
   - Single trade ≤ 2% (3% absolute max)
   - Daily exposure within limit
   - Correlated positions within combined limit
6. **Adjust for events** — reduce 50-75% if high-impact economic event within 24h
7. **Create signal** with the calculated size via `create_trading_signal`

## Risk Rules

| Rule | Guideline |
| --- | --- |
| Single trade max | 2% of account (3% absolute ceiling) |
| Correlated trades | Combined max 2% for high-correlation |
| Daily loss limit | 3-5% of account — stop trading |
| Weekly loss limit | 5-8% — reduce to 50% size, review |
| Monthly loss limit | 10% — 1 week break, resume at 25% size |
| Pre-event reduction | Cut 50-75% before Score ≥8 events |

## Best Practices

| Do | Don't |
| --- | --- |
| Use the same method consistently | Switch methods based on recent results |
| Account for correlation across positions | Size each trade independently |
| Reduce size during drawdowns | Increase size to "make it back" |
| Start with quarter Kelly, not half | Use full Kelly — ever |
| Factor in upcoming economic events | Keep full size into FOMC/NFP/CPI |
| Track every trade for Kelly inputs | Guess your win rate |

## Common Mistakes

- **Sizing based on conviction** — "I'm really sure about this one" is not a position sizing method. Systematic sizing prevents ruin.
- **Ignoring correlation** — 5 long tech positions at 1% each = 5% risk in one sector. That's a single bet.
- **Using full Kelly** — Looks great in theory, catastrophic in practice. Quarter Kelly achieves ~75% of the growth rate.
- **Revenge sizing** — Increasing size after losses to "get it back" is the fastest path to blowing up an account.
- **Forgetting event risk** — Holding full-size into FOMC is gambling, not trading. Always reduce pre-event.

## Related Skills

- **correlation-risk** — Correlated positions must be sized as a combined position; this skill provides the correlation-aware adjustments
- **risk-reward-ratio** — R:R determines whether a setup is worth taking; position sizing determines how much to risk
- **stop-loss-strategies** — Stop distance is a direct input to position size calculation
