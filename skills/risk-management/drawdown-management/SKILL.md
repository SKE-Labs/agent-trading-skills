---
name: drawdown-management
description: Manage account drawdowns with limits and recovery protocols. Use when protecting capital during losing streaks, implementing loss limits, or developing recovery plans.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
---

# Drawdown Management

Drawdown management protects capital and ensures trading longevity through loss limits and recovery protocols.

## Drawdown Types

| Type             | Definition                     |
| ---------------- | ------------------------------ |
| Max Drawdown     | Largest peak-to-trough decline |
| Daily Drawdown   | Loss in single trading day     |
| Weekly Drawdown  | Loss in single week            |
| Open Drawdown    | Unrealized loss on open trades |

## Drawdown Limits

| Limit        | Threshold | Action               |
| ------------ | --------- | -------------------- |
| Daily loss   | 2-3%      | Stop trading for day |
| Weekly loss  | 5-6%      | Reduce size, review  |
| Monthly loss | 10%       | Stop, full review    |
| Max drawdown | 20%       | Major intervention   |

## Loss Response Protocol

**After Daily Limit (2-3%)**: Stop trading immediately. Close all positions. Review losing trades. Resume next day with full size.

**After Weekly Limit (5-6%)**: Stop trading for 24-48 hours. Review week's trades. Resume with 50% position size. Return to full size after 3 winning days.

**After Monthly Limit (10%)**: Stop for 1 week minimum. Full journal review. Paper trade for 1 week. Resume at 25% size and slowly increase.

## Recovery Math

Larger drawdowns require exponentially larger gains to recover:

| Drawdown | Return Needed to Recover |
| -------- | ------------------------ |
| 10%      | 11%                      |
| 20%      | 25%                      |
| 30%      | 43%                      |
| 50%      | 100%                     |

Formula: `Recovery % = Drawdown / (1 - Drawdown) x 100`

This is why preventing large drawdowns matters more than maximizing gains.

## Prevention Strategies

1. **Size properly** -- never risk more than 2% per trade
2. **Enforce daily limits** -- stop at 2-3% daily loss, no exceptions
3. **Manage correlations** -- avoid stacking similar positions (see correlation-risk)
4. **Reduce in losing streaks** -- cut size early, don't wait for the limit
5. **Diversify strategies** -- single-strategy risk is concentrated risk

## Monitoring

Track these metrics continuously:

- Current drawdown from equity peak
- Number of consecutive losing days
- Deviation from expected win rate
- Equity curve slope (flattening = warning)

## Key Rules

- NEVER revenge trade after hitting a loss limit -- the protocol exists for a reason
- NEVER increase size during a drawdown to "make it back" -- reduce size, not increase
- NEVER skip the mandatory pause after hitting weekly or monthly limits
- Accept that drawdowns are normal -- 10-15% max drawdown is typical for good systems
- Reduce position size at the first sign of a losing streak, before limits are hit
- The goal is survival first, profits second

## Related Skills

- **position-sizing** -- proper sizing is the primary drawdown prevention tool
- **correlation-risk** -- correlated positions amplify drawdowns
