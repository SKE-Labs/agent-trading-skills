---
name: correlation-risk
description: Manage correlated positions to prevent concentrated exposure. Use when holding multiple positions, diversifying portfolio, or assessing total account risk.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Correlation Risk Management

Managing correlated positions prevents oversized exposure to single market moves.

## Correlation Basics

**Correlation coefficient** ranges from -1 to +1:
| Correlation | Meaning |
|-------------|---------|
| +1.0 | Perfect positive (move together) |
| +0.5 | Moderate positive |
| 0 | No correlation |
| -0.5 | Moderate negative |
| -1.0 | Perfect negative (move opposite) |

## Common Correlations

### Crypto

| Pair         | Correlation  |
| ------------ | ------------ |
| BTC/Altcoins | +0.7 to +0.9 |
| BTC/ETH      | +0.85        |
| ETH/Altcoins | +0.8         |

### Forex

| Pair               | Correlation |
| ------------------ | ----------- |
| EUR/USD vs GBP/USD | +0.8        |
| USD/JPY vs USD/CHF | +0.7        |
| AUD/USD vs Gold    | +0.6        |

### Stocks

| Pair                     | Correlation |
| ------------------------ | ----------- |
| Tech stocks              | +0.7        |
| Same sector              | +0.6        |
| S&P vs individual stocks | +0.5        |

## Risk Rules

### Treat Correlated Trades as One Position

Calculate combined risk for correlated positions:

```
execute(command='python3 -c "r1=1;r2=1;corr=0.85;combined_risk=(r1**2+r2**2+2*r1*r2*corr)**0.5;print(f\"Position 1: {r1}%\\nPosition 2: {r2}%\\nCorrelation: {corr}\\nCombined Risk: {combined_risk:.2f}%\")"')
```

If BTC and ETH correlate +0.85:

- Long BTC 1% risk + Long ETH 1% risk
- Effective risk ≈ 1.85% (not 2%)
- But for drawdown: treat as 2%

### Maximum Exposure Rules

| Correlation | Max Position             |
| ----------- | ------------------------ |
| >0.7        | Treat as single position |
| 0.4-0.7     | 1.5x normal combined     |
| <0.4        | Full individual sizing   |

## Managing Correlation Risk

### 1. Limit Correlated Exposure

- Max 3% total in highly correlated assets
- Spread across uncorrelated markets
- Mix long and short when possible

### 2. Diversify Effectively

- Different asset classes
- Different sectors
- Different timeframes
- Long and short positions

### 3. Hedge When Needed

- Use inversely correlated positions
- Reduce directional exposure
- Accept reduced profit for protection

## Workflow

1. **List all open positions**
2. **Assess correlations** between them
3. **Sum correlated risk** as single exposure
4. **Reduce** if exceeds limits
5. **Monitor** correlations (they change)

## Key Insight

Diversification only works with uncorrelated assets. Multiple positions in correlated assets = One big position.

## Related Skills

- **position-sizing** — Correlated positions require adjusted sizing; this skill identifies correlation, position-sizing applies the reduction
- **market-correlation-trading** — Provides the macro correlation analysis that feeds into portfolio-level risk assessment
- **drawdown-management** — Correlated positions amplify drawdowns; managing correlation is a key drawdown prevention tool
