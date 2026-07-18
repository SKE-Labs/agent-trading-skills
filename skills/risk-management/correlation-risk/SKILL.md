---
name: correlation-risk
description: Manage correlated positions to prevent concentrated exposure. Use when holding multiple positions, diversifying portfolio, or assessing total account risk.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
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

Estimate correlation from aligned, same-currency returns over predeclared horizons. Report sample length, frequency, confidence interval, and current versus stress estimates; never use a permanent pair table.

## Combined Risk

Use covariance to estimate portfolio **return volatility**: `sigma_p = sqrt(w' Sigma w)`. Do not insert stop-loss dollars into that formula: stop losses are nonlinear, can gap, and are not standard deviations. For loss control, aggregate factor exposures and run joint gap, correlation-to-one, volatility-spike, and liquidity scenarios.

## Exposure Limits

Apply portfolio-mandated limits by issuer, sector, country, currency, duration, beta, and common factor. Reduce or hedge positions until both normal covariance risk and stress loss fit the remaining risk budget. State the hedge basis and residual risk; a long and short are not diversified merely because signs differ.

## Workflow

1. **List all open positions**
2. **Align returns and estimate covariance/beta** with uncertainty
3. **Map factor and scenario losses**, including gaps past stops
4. **Reduce or hedge** until mandate limits pass under normal and stress assumptions
5. **Monitor** -- correlations shift over time, especially in stress events

## Diversification Strategies

- Spread across uncorrelated asset classes (crypto, forex, equities, commodities)
- Mix long and short when possible to reduce directional exposure
- Use inversely correlated positions as hedges when appropriate
- Different timeframes diversify only if their realized return streams and stress losses demonstrate it

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Ang & Bekaert](https://www.nber.org/papers/w7056) documents time-varying correlations and higher-correlation stress regimes; estimate recent covariance and run stress scenarios instead of using permanent pair values.

## Key Rules

- Aggregate shared factor, collateral, venue, liquidity, and gap risk across positions.
- Do not assume correlations are static; show rolling estimates and adverse stress matrices.
- Never rely on one covariance estimate—use scenarios and concentration limits too.
- Take limits from the portfolio mandate rather than universal percentages.
- Report assumptions, missing exposures, and the largest normal and stressed risk contributors.

## Related Skills

- **position-sizing** -- correlated positions require reduced per-position sizing
- **drawdown-management** -- correlated positions amplify drawdowns
