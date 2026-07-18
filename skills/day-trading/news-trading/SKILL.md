---
name: news-trading
description: Plan and evaluate trades around scheduled economic or corporate releases. Use when the user needs primary-source event data, standardized surprise measurement, scenario triggers, and execution-risk controls.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# News Trading Strategy

Trade volatility from scheduled economic events using deviation-from-consensus scoring.

## Setup Conditions

### Event Inputs

Use a live official calendar, release timestamp and revision policy. Record every economically relevant component: for example, headline and core inflation; payrolls, unemployment, wages, and revisions; or a policy decision, statement, projections, and press conference. Do not attach a universal price move to an event name.

### Deviation-from-Consensus Scoring

```
Standardized surprise = (Actual - consensus) / historical standard deviation of surprises
```

Use a rolling, vintage-consistent surprise history and state the consensus provider and cutoff time. If history is insufficient, show the raw surprise and estimate range without inventing a score. Direction also depends on priced expectations, revisions, other components, and policy regime.

## Workflow

### 1. Check Economic Calendar

```
get_economics_calendar(from_date=<start>, to_date=<end>, impact="high")
```

Identify upcoming high-impact events. Note dates, times, affected markets.

### 2. Research Consensus

```
get_financial_news(topic="<event> forecast consensus <month> <year>", max_results=15)
```

Find the current consensus, estimate range, cutoff timestamp, and prior value. Confirm the actual and revisions from the official release, not a headline or social post.

### 3. Plan Scenarios

Pre-plan multiple component combinations and observable price triggers. A headline beat need not imply one direction when revisions, core measures, guidance, or policy expectations conflict.

### 4. Post-Release Entry

Enter only when the selected execution gate is met: spread below a tested limit, quotes stable enough to size, and a closed-bar or order-book trigger. Calibrate any waiting period in bars for the specific market. Use a volatility-based stop with position size reduced to keep risk fixed; include gap, halt, rejection, and slippage scenarios.

### 5. Event Clustering

When releases overlap, attribute the move cautiously and wait until all scheduled components are available. If they conflict or the event timestamp/data vintage is uncertain, return `no trade`.

### 6. Report to Orchestrator

Event details, consensus vs actual, deviation score, recommended action, conviction level.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Federal Reserve research](https://www.federalreserve.gov/econres/feds/macroeconomic-news-announcements-systemic-risk-financial-market-volatility-and-jumps.htm) finds more volatility jumps on announcement days and sensitivity to surprise and uncertainty.

## Key Rules

- Never use unreleased, embargoed, or suspected material nonpublic information.
- Do not hold through an event without an explicit event-risk mandate and gap-loss scenario.
- Size from the stress loss and executable stop distance, not a fixed percentage reduction.
- Skip conflicting clustered releases or failed liquidity gates.
- Model spread widening, slippage, rejected orders, halts, revisions, and timestamp latency.

## Related Skills

- **breakout-trading** -- post-news consolidation breakouts follow breakout principles
- **gap-trading** -- news events often produce gap opens
