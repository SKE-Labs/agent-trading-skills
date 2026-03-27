---
name: correlation-risk
description: Manage correlated positions to prevent concentrated exposure. Use when holding multiple positions, diversifying portfolio, or assessing total account risk.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
---

# Correlation Risk Management

Managing correlated positions prevents oversized exposure to single market moves.

## Correlation Basics

Correlation coefficient ranges from -1 to +1:

| Correlation | Meaning                           |
| ----------- | --------------------------------- |
| +1.0        | Perfect positive (move together)  |
| +0.5        | Moderate positive                 |
| 0           | No correlation                    |
| -0.5        | Moderate negative                 |
| -1.0        | Perfect negative (move opposite)  |

## Common Correlations

| Asset Pair                | Correlation   |
| ------------------------- | ------------- |
| BTC / ETH                 | +0.85         |
| BTC / Altcoins            | +0.7 to +0.9  |
| EUR/USD vs GBP/USD        | +0.8          |
| USD/JPY vs USD/CHF        | +0.7          |
| Tech stocks (same sector) | +0.7          |
| AUD/USD vs Gold           | +0.6          |
| S&P vs individual stocks  | +0.5          |

## Combined Risk

For two positions with known correlation, combined risk is:

`Combined Risk = sqrt(R1^2 + R2^2 + 2 * R1 * R2 * Correlation)`

Example: BTC 1% risk + ETH 1% risk at 0.85 correlation => sqrt(1 + 1 + 1.7) = ~1.92%. For drawdown purposes, treat as 2%.

## Maximum Exposure Rules

| Correlation | Max Combined Risk        |
| ----------- | ------------------------ |
| >0.7        | Treat as single position -- max 2% total |
| 0.4-0.7     | 1.5x normal combined     |
| <0.4        | Full individual sizing   |

**Practical rule**: 3 positions in BTC-correlated assets => each gets 0.67% risk (2% / 3) instead of 1% each.

## Workflow

1. **List all open positions**
2. **Assess correlations** between them (use common correlations table or recent data)
3. **Sum correlated risk** as single exposure using combined risk formula
4. **Reduce sizing** if combined risk exceeds limits
5. **Monitor** -- correlations shift over time, especially in stress events

## Diversification Strategies

- Spread across uncorrelated asset classes (crypto, forex, equities, commodities)
- Mix long and short when possible to reduce directional exposure
- Use inversely correlated positions as hedges when appropriate
- Different timeframes add some diversification benefit

## Key Rules

- NEVER treat correlated positions as independent -- 5 long tech positions at 1% each is a single 5% sector bet
- NEVER assume correlations are static -- they spike toward +1 during market stress
- NEVER rely on diversification alone -- even "uncorrelated" assets can correlate in a crash
- Max 3% total risk in highly correlated assets (>0.7)
- Multiple positions in correlated assets = one big position, size accordingly

## Related Skills

- **position-sizing** -- correlated positions require reduced per-position sizing
- **drawdown-management** -- correlated positions amplify drawdowns
