---
name: sentiment-analysis
description: Build source-dated, deduplicated sentiment evidence or a calibrated sentiment model. Use when separating facts, interpretations, claims, novelty, horizon, and uncertainty across filings, news, analyst commentary, or social sources.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Sentiment Analysis

Build a reproducible, source-dated evidence set. Sentiment may describe language or positioning; it does not become a return forecast without labeled calibration and out-of-sample validation.

## Evidence Fields

| Field | Requirement |
| --- | --- | --- |
| Source | Publisher, author, URL/document ID, publication and event time |
| Provenance | Primary filing/release, original reporting, analysis, or social claim |
| Content | Verifiable facts, management view, and analyst interpretation separated |
| Novelty | New information, update/revision, or duplicate/syndicated item |
| Scope | Entity, event, horizon, and affected metric |

## Labeling

| Label | Meaning |
| --- | --- |
| Positive / negative / mixed / neutral | Direction of language toward the named metric and horizon |
| Fact / interpretation / claim | Epistemic type; unverified claims cannot outweigh primary evidence |
| New / revision / duplicate | Information novelty and deduplication status |

## Numeric Models

If a numeric model is required, derive source reliability, decay, label policy, and aggregation from a labeled training set. Freeze them before evaluation, calibrate scores to a stated outcome/horizon, report uncertainty and class balance, and compare with simple no-sentiment baselines. Never present hand-chosen weights as probabilities.

## Contrarian Signals

Define any extreme by the asset's historical percentile using the same data source. Treat price/sentiment divergence as a hypothesis and state pivot, horizon, and timestamp; do not call it distribution or accumulation without further evidence.

## Workflow

### 1. Gather News Data

```
get_financial_news(topic="AAPL earnings revenue guidance analyst", max_results=20)
get_financial_news(topic="AAPL analyst upgrade downgrade price target", max_results=10)
```

Search both bullish and bearish angles for the same asset.

### 2. Score Each Article

For each unique item, fill the evidence fields and labels. Resolve conflicts with primary documents where possible and preserve disagreements.

### 3. Calculate Composite

Report the evidence table, coverage window, duplicates removed, missing primary evidence, disagreements, and model output only if calibrated. Agreement among syndicated or correlated sources does not create independent confidence.

### 4. Identify Cycle Phase

Compare sentiment and returns on predeclared horizons. Use descriptive labels such as divergence or agreement; allocation still requires a separately validated decision rule.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Baker & Wurgler](https://www.nber.org/papers/w10449) found sentiment effects differ across stock characteristics; it is not valid to convert arbitrary article scores into universal return forecasts.

## Key Rules

- Never invent a composite from subjective weights; use transparent labels or a calibrated model.
- Prioritize primary evidence for facts and explicitly flag unverified claims.
- Use publication time, event time, novelty, and a validated horizon rather than fixed decay weights.
- Do not call sentiment a confirmation unless its incremental held-out value is measured.
- NEVER only seek confirming news -- always search both bullish and bearish angles
- When high-credibility sources disagree, reduce conviction rather than picking a side
- Extreme language can persist and sources are correlated; return `no sentiment edge` when evidence is sparse or stale.

## Related Skills

- **earnings-trading** -- Management tone scoring feeds sentiment
- **economic-calendar-trading** -- Pre-event sentiment gauges positioning
