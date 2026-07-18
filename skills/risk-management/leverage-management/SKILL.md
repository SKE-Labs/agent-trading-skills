---
name: leverage-management
description: Calculate effective leverage, margin, stress loss, and venue-specific liquidation state. Use when sizing derivatives or managing collateral, cross/isolated margin, funding, fees, and forced-liquidation risk.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Leverage Management

Leverage amplifies both gains and losses -- use it responsibly.

## Leverage Basics

| Leverage | $1,000 Controls | Exposure |
| -------- | ---------------- | -------- |
| 1x       | $1,000           | None     |
| 5x       | $5,000           | 5x       |
| 10x      | $10,000          | 10x      |
| 100x     | $100,000         | 100x     |

There is no universally safe leverage by asset label or trading style. Faster intended exits do not remove gap, latency, liquidation, or venue risk. Derive exposure from maximum stress loss, maintenance margin, liquidity, and the portfolio mandate.

## Key Formulas

**Effective Leverage**: `Position Size / Account Equity`

Example: $50,000 position on $10,000 equity = 5x effective leverage.

**Position sizing with leverage**: `Position Size = (Account x Risk%) / Stop Distance%`. Leverage does not change how much you risk -- it changes how much capital you tie up.

For a linear position before costs, account return is approximately `effective leverage × asset return`. Add contract multiplier, inverse/quanto payoff, fees, funding/interest, FX, collateral haircuts, and nonlinear option exposure as applicable.

## Liquidation Awareness

Obtain the venue's actual calculator and rules: initial/maintenance tiers, mark or index price, liquidation fees, isolated versus cross margin, collateral valuation, open orders, and other positions. Record the estimated liquidation price and a stressed value after fee/funding/volatility changes. A stop can gap or fail before liquidation.

## Workflow

1. **Assess volatility** of the asset being traded
2. **Set exposure** from mandate loss limits and shocked volatility/liquidity
3. **Calculate effective leverage** -- position size / equity
4. **Verify liquidation state** with the venue-specific formula and cross-position effects
5. **Maintain the mandate's margin buffer** under mark-price and collateral stresses
6. **Reduce** leverage in volatile conditions or after losses

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: The [SEC margin bulletin](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-29) and [CFTC crypto advisory](https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/understand_risks_of_virtual_currency.html) explain that leverage amplifies losses and can require additional margin or forced closure.

## Key Rules

- Never confuse platform maximum leverage with an acceptable exposure.
- Calculate effective leverage, stress loss, and venue-specific liquidation state before entry and after material moves.
- Include gap, mark/index divergence, funding, interest, fee, collateral, and forced-liquidation scenarios.
- Reduce exposure or add collateral when the approved margin buffer fails; cross margin can spread losses.
- Position size determines risk; selecting a low leverage setting alone does not.

## Related Skills

- **position-sizing** -- leverage changes capital allocation but not risk amount
- **stop-loss-strategies** -- stops must be set before liquidation price
