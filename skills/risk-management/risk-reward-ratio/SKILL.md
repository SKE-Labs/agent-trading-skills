---
name: risk-reward-ratio
description: Calculate and optimize risk-reward ratios for trade setups. Use when evaluating trade quality, setting targets, or filtering low-quality setups.
---

# Risk-Reward Ratio (R:R)

R:R compares potential profit to potential loss, helping filter high-quality trades.

## Calculation

```
Risk-Reward Ratio = Potential Profit / Potential Loss
```

Or expressed as ratio:

```
R:R = (Target - Entry) / (Entry - Stop)
```

Example:

- Entry: $100
- Stop: $95 (Risk: $5)
- Target: $115 (Reward: $15)
- R:R = $15 / $5 = 3:1

## Minimum R:R Guidelines

| Win Rate | Minimum R:R | Breakeven R:R |
| -------- | ----------- | ------------- |
| 40%      | 1.5:1       | 1.5:1         |
| 50%      | 1:1         | 1:1           |
| 60%      | 0.7:1       | 0.67:1        |
| 70%      | 0.5:1       | 0.43:1        |

Formula: Breakeven R:R = (1 - Win Rate) / Win Rate

**Quick calculation:**
```
execute(command='python3 -c "e=100;sl=95;tp=115;rr=(tp-e)/(e-sl);print(f\"Entry: {e}\\nStop: {sl}\\nTarget: {tp}\\nR:R = 1:{rr:.2f}\")"')
```

**Breakeven R:R for win rate:**
```
execute(command='python3 -c "wr=0.50;be_rr=(1-wr)/wr;print(f\"Win Rate: {wr*100:.0f}%\\nBreakeven R:R: 1:{be_rr:.2f}\")"')
```

## R:R Targets by Style

| Trading Style    | Target R:R   |
| ---------------- | ------------ |
| Scalping         | 1:1 to 1.5:1 |
| Day Trading      | 1.5:1 to 2:1 |
| Swing Trading    | 2:1 to 3:1   |
| Position Trading | 3:1+         |

## Optimizing R:R

### Improve Entry

- Enter at better levels (OTE, pullbacks)
- Wait for confirmation at support/resistance
- Use limit orders at key levels

### Optimize Stop Loss

- Structure-based stops (below swing low)
- ATR-based stops (1.5-2x ATR)
- Avoid arbitrary stops

### Extend Target

- Use Fibonacci extensions
- Target next key level
- Allow runners with trailing stop

## Trade Filtering

Use R:R as quality filter:

| R:R       | Action                      |
| --------- | --------------------------- |
| <1:1      | Skip (unless 70%+ win rate) |
| 1:1 - 2:1 | Trade with caution          |
| 2:1 - 3:1 | Good trade                  |
| 3:1+      | Excellent trade             |

## Key Insights

- High R:R allows lower win rate profitability
- Don't sacrifice R:R for win rate
- Better entries = Better R:R
- Realistic targets based on structure
