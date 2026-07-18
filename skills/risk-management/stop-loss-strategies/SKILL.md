---
name: stop-loss-strategies
description: Place strategic stop losses using structure, ATR, or volatility methods. Use when protecting capital, defining trade invalidation, or managing downside risk.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Stop Loss Strategies

Proper stop placement protects capital while giving trades room to work.

## Stop Loss Methods

### 1. Structure-Based (Recommended)

Place below swing low (long) or above swing high (short). Respects market structure with a clear invalidation point.

### 2. ATR-Based

Long example: `Stop = Entry - (ATR × Multiplier)`; mirror for shorts. Select the ATR estimator and multiplier in training data and freeze them.

### 3. Support/Resistance Based

Place beyond (not at) key S/R zones. Below support for longs, above resistance for shorts.

### 4. Moving Average Based

Place below key MA (20, 50, or 200). Dynamic stop level, good for trend following.

### 5. Percentage-Based

Fixed % below entry. Simple but ignores structure -- use only as a position sizing limit.

Stop distance must follow the setup's invalidation and executable volatility/liquidity, not a universal percentage for a trade label. Recalculate quantity whenever the stop changes.

## Buffer Rules

Define the buffer in ticks, spread, and/or ATR and calibrate it by instrument, session, and order type. The purpose is to represent noise and execution uncertainty; do not infer a "stop hunt" from a stopped order.

## Stop Management

**Initial Stop**: Set at entry based on analysis. Based on the invalidation point for the trade thesis.

**Breakeven Stop**: Treat moving to entry as one candidate management rule. It is not risk-free after fees, spread, gaps, and slippage; compare it with the unchanged initial stop out of sample.

**Trailing Stop**: Locks in profits as the trade progresses (see trailing-stop skill).

## Workflow

1. **Identify invalidation** -- the price level where the trade thesis is wrong
2. **Choose method** -- structure-based for most setups, ATR-based for volatile assets
3. **Add buffer** -- use the prevalidated tick/volatility and execution buffer
4. **Choose order mechanics** -- stop-market prioritizes execution; stop-limit controls price but may not fill; confirm venue trigger source
5. **Manage** -- follow the predeclared static, breakeven, time, or trailing rule

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: The [SEC stop-order bulletin](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15) warns that a stop price is a trigger, not a guaranteed execution price, while stop-limit orders may not execute.

## Key Rules

- Define invalidation, order type, trigger source, buffer, and quantity before entry.
- Never widen total authorized loss after entry without a separately approved risk decision.
- Do not assume round-number placement is inferior; test any clustering/buffer hypothesis.
- Model gap-through, halt, rejected order, stop-limit nonexecution, and slippage risk.
- Recalculate quantity and portfolio risk whenever the effective stop changes.

## Related Skills

- **trailing-stop** -- manages exits after initial stop is set
- **position-sizing** -- stop distance is a direct input to position size calculation
