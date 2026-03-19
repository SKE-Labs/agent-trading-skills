---
name: drawdown-management
description: Manage account drawdowns with limits and recovery protocols. Use when protecting capital during losing streaks, implementing loss limits, or developing recovery plans.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Drawdown Management

Drawdown management protects capital and ensures trading longevity through loss limits.

## Drawdown Types

| Type                | Definition                     |
| ------------------- | ------------------------------ |
| **Max Drawdown**    | Largest peak-to-trough decline |
| **Daily Drawdown**  | Loss in single trading day     |
| **Weekly Drawdown** | Loss in single week            |
| **Open Drawdown**   | Unrealized loss on open trades |

## Drawdown Limits

| Limit        | Threshold | Action               |
| ------------ | --------- | -------------------- |
| Daily loss   | 2-3%      | Stop trading for day |
| Weekly loss  | 5-6%      | Reduce size, review  |
| Monthly loss | 10%       | Stop, full review    |
| Max drawdown | 20%       | Major intervention   |

## Loss Response Protocol

### After Daily Limit Hit (2-3%)

1. Stop trading immediately
2. Close all positions
3. Review losing trades
4. Resume next day with full size

### After Weekly Limit Hit (5-6%)

1. Stop trading for 24-48 hours
2. Review week's trades
3. Resume with 50% position size
4. Return to full size after 3 winning days

### After Monthly Limit (10%)

1. Stop for 1 week minimum
2. Full journal review
3. Paper trade for 1 week
4. Resume at 25% size
5. Slowly increase

## Drawdown Recovery

### Psychology

- Accept drawdowns are normal
- Don't revenge trade
- Stick to system
- Reduce size, not increase

### Mathematics

Calculate recovery requirements:

```
execute(command='python3 -c "dd=0.20;recovery=dd/(1-dd)*100;print(f\"Drawdown: {dd*100:.0f}%\\nRecovery Needed: {recovery:.1f}%\")"')
```

| Drawdown | Return Needed |
| -------- | ------------- |
| 10%      | 11%           |
| 20%      | 25%           |
| 30%      | 43%           |
| 50%      | 100%          |

Larger drawdowns require exponentially larger gains.

## Prevention Strategies

1. **Size properly**: Never risk more than 2%
2. **Daily limits**: Stop at 2-3% daily loss
3. **Correlations**: Avoid similar positions
4. **Diversify**: Multiple strategies
5. **Reduce in losing streaks**: Cut size early

## Monitoring

Track these metrics:

- Current drawdown from peak
- Number of consecutive losing days
- Deviation from expected win rate
- Equity curve slope

## Related Skills

- **position-sizing** — Proper position sizing is the primary drawdown prevention tool; reduce size during losing streaks
- **correlation-risk** — Correlated positions amplify drawdowns; managing correlation prevents concentrated losses
- **market-regime-detection** — Drawdowns often occur when trading strategies mismatched to the current regime
