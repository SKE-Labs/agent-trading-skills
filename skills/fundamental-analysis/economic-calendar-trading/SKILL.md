---
name: economic-calendar-trading
description: Plan scheduled macro-event risk from official calendars and point-in-time expectations. Use for FOMC, employment, inflation, GDP, or other releases requiring standardized surprise, component, revision, scenario, and execution analysis.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Economic Calendar Trading

Plan macro-event risk from live official calendars, time-stamped consensus, release vintages, and observable price triggers. Surprise matters, but revisions, components, positioning, uncertainty, and regime affect the response.

## Event Map

| Event family | Components to record | Primary source |
| --- | --- | --- |
| FOMC | Decision, statement changes, SEP, press conference | Federal Reserve |
| Employment | Payrolls, unemployment, participation, wages, revisions | BLS |
| Inflation | Headline/core, monthly/annual, category breadth, revisions | BLS/BEA |
| Growth/activity | Real/nominal detail, inventories, revisions, survey components | Source agency |

## Standardized Surprise

```
Standardized surprise = (Actual - consensus) / historical standard deviation of surprises
```

Use a point-in-time consensus and same-definition historical series. State source, sample, standard deviation, revisions, and transformation. If history is insufficient, report raw surprise and forecast range without a synthetic score.

## Workflow

### 1. Check Calendar

```
get_economics_calendar(from_date=<start>, to_date=<end>, impact="high")
```

Refresh before each session and verify date, time, timezone, and revision policy against the official agency calendar; third-party impact labels are screening aids only.

### 2. Research Consensus

```
get_financial_news(topic="<event> forecast consensus <month> <year>", max_results=10)
```

Extract: consensus forecast, range of estimates, leading indicators, and current market positioning.

### 3. Build Scenario Matrix

Map component combinations, revisions, and price triggers. Include `no trade` for mixed releases or failed liquidity conditions; do not assign probabilities without a calibrated model.

### 4. Post-Release Execution Gate

Use a pretested bar-based delay or price-structure trigger. Require verified actuals, acceptable spread/depth, stable timestamps, and a calculable stop; event labels do not determine a universal waiting period.

### 5. Trade the Reaction

- **Continuation candidate**: enter only on the specified closed-bar or retest trigger.
- **Fade candidate**: define overreaction in normalized returns and test separately; VWAP is a benchmark, not a guaranteed destination.

### 6. FOMC Analysis

Use `get_financial_news` to analyze FOMC statements and press conferences for hawk/dove tone shifts.

Analyze the decision, statement redlines, projections, and press conference separately. Measure the response in policy-rate futures/yields and the traded asset; do not infer fixed direction or duration from a hawkish/dovish label.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: Use the official [Federal Reserve calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) and [BLS release calendar](https://www.bls.gov/schedule/) because dates can change; Federal Reserve research shows reaction depends on surprise, disagreement, and regime.

## Key Rules

- Verify actuals and revisions from the primary source before interpretation.
- Use the predeclared execution gate; neither immediate trading nor a fixed wait is universally safe.
- Choose order type from the fill-versus-price-risk tradeoff; limits may not fill and markets may slip.
- Aggregate direct, correlated, and factor exposures in the event stress test.
- Treat clustered or conflicting components as lower confidence or `no trade`.
- Size from stress loss, not a vendor impact score.

## Related Skills

- **sentiment-analysis** -- Pre-event sentiment gauges positioning
- **sector-rotation** -- Macro data drives sector rotation shifts
