---
name: position-sizing
description: Calculate risk-based position sizes using fixed %, fractional Kelly, ATR-hybrid, or volatility methods. Use when determining trade size, managing account risk, adjusting for correlated positions, or standardizing risk across trades.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Position Sizing

Position sizing determines how much capital to risk per trade -- the single most important factor in long-term survival.

## Sizing Methods

### 1. Fixed Percentage Risk (Default)

`Quantity = Risk Budget / (abs(Entry - Stop) × contract multiplier + estimated per-unit stop slippage/cost)`

Example: $10,000 account, 1% risk, entry $100, stop $95 => $100 / $5 = 20 shares.

### 2. Volatility-Based (ATR)

`Position Size = (Account x Risk%) / (ATR x Multiplier)`

Select and validate the ATR multiple per instrument and strategy. Wider stops reduce quantity for the same risk budget; they do not create safety by themselves.

### 3. ATR-Hybrid

Combines fixed % risk with ATR-based stop distance: `Position Size = (Account x Risk%) / (ATR x Multiplier)`. Adapts to volatility while maintaining consistent dollar risk per trade.

### 4. Fractional Kelly Criterion

`Full Kelly % = W - (1 - W) / R` where W = win rate, R = avg win / avg loss.

Kelly assumes a positive edge and sufficiently known outcome distribution. Estimate uncertainty, nonstationarity, tail loss, dependence, and constraints; use a conservative fraction only if mandate-approved and cap it by drawdown, liquidity, margin, and concentration limits. Otherwise use the fixed risk budget.

## Method Selection

Default to the portfolio's remaining dollar-risk budget and a structural/volatility stop. Use volatility scaling for comparable risk across assets. Consider fractional Kelly only with stable, net-of-cost, distribution-level evidence; never choose sizing from trade style or a small win-rate sample.

## Risk Limits

Read single-trade, strategy, factor, venue, margin, daily, and drawdown limits from the portfolio mandate. Include existing orders/positions, correlated gap scenarios, borrow/funding, and scheduled-event stress. If a limit is unavailable, do not manufacture one—request it or return no size.

## Workflow

1. **Get entry and stop loss** from the technical analyst's analysis
2. **Check committed risk and balance** via `get_portfolio_risk_state()` (remaining R budget, margin used)
3. **Check for correlated positions** -- are existing positions in correlated assets?
4. **Select sizing method** from mandate and validated strategy assumptions
5. **Preview the size** via `preview_position_size(symbol=<symbol>, side=<BUY|SELL>, entry=<entry>, stop_loss=<stop>, risk_usd=<dollars>)` — returns quantity, leverage, notional. Use it to sanity-check before creating the insight.
6. **Verify all limits** -- single trade, aggregate factor/scenario loss, liquidity, margin, and drawdown budget
7. **Stress events** -- size to the approved gap scenario or return no trade when risk is unbounded
8. **Create the insight** via `create_trading_insight(symbol, side, entry, stop_loss, take_profits, trade_type, risk_usd=<dollars>)` — sizing is recomputed server-side; `preview_position_size` is advisory only.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Kelly's original paper](https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1956.tb03809.x) assumes known probabilities and repeated favorable bets; [risk-constrained Kelly](https://web.stanford.edu/~boyd/papers/kelly.html) adds explicit drawdown control.

## Key Rules

- Do not use Kelly without positive, stable, net-of-cost edge estimates and uncertainty controls.
- NEVER size based on conviction -- "I'm really sure" is not a sizing method
- NEVER increase size after losses to "make it back" -- revenge sizing is the fastest path to ruin
- Size scheduled-event exposure from the mandate's gap/stress loss.
- Aggregate correlated and common-factor positions with current estimates and adverse scenarios.
- Use the same method consistently; do not switch based on recent results
- Round down to executable lot size and recheck notional, margin, stop slippage, and residual risk.

## Related Skills

- **correlation-risk** -- correlated positions must be sized as combined exposure
- **stop-loss-strategies** -- stop distance is a direct input to position size calculation
