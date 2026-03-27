---
name: news-trading
description: Trade volatility around economic news and corporate events. Use deviation-from-consensus scoring to gauge expected move magnitude. Use when capitalizing on market-moving news, trading earnings, or positioning for scheduled events.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# News Trading Strategy

Trade volatility from scheduled economic events using deviation-from-consensus scoring.

## Setup Conditions

### High-Impact Events

| Event | Impact | Typical Move |
| --- | --- | --- |
| FOMC/Fed Rate | Very High | 100+ pips |
| NFP (Jobs) | Very High | 50-100 pips |
| CPI (Inflation) | High | 50-80 pips |
| GDP | High | 30-50 pips |

### Deviation-from-Consensus Scoring

```
Deviation Score = (Actual - Forecast) / Forecast x 100
```

| Event | Small (skip/minimal) | Moderate (tradeable) | Large (high conviction) |
| --- | --- | --- | --- |
| NFP | +/-25K | +/-50K | +/-100K+ |
| CPI | +/-0.1% | +/-0.2% | +/-0.3%+ |
| GDP | +/-0.2% | +/-0.5% | +/-1.0%+ |

Meeting consensus rarely produces tradeable moves -- the deviation drives the trade.

### Post-Event Wait Periods

| Event Impact | Wait Time |
| --- | --- |
| Very High (FOMC, NFP) | 30-45 min |
| High (CPI, GDP) | 15-30 min |
| Medium (Retail Sales, PMI) | 5-15 min |

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

Find current consensus forecast and range of analyst estimates for each event.

### 3. Plan Scenarios

For each event, pre-plan: **Beat** (direction + entry trigger), **Miss** (opposite direction), **Meet** (no trade).

### 4. Post-Release Entry

After the event, apply the wait period above. Then:

- Observe initial reaction (1-5 min)
- Wait for consolidation (per wait table)
- Enter breakout of post-news consolidation
- Use wider stops (volatility is elevated)
- Target next key level

### 5. Event Clustering

When multiple events release in the same window: increase wait time by 50%, wait for ALL numbers before entering. If data points conflict, skip the trade.

### 6. Report to Orchestrator

Event details, consensus vs actual, deviation score, recommended action, conviction level.

## Key Rules

- NEVER enter during the first 60 seconds after release -- whipsaws dominate
- NEVER hold positions through a high-impact event without a deliberate pre-news plan
- NEVER trade full size on news -- reduce position size by 50-75% to account for volatility
- When clustered events produce conflicting signals, skip the trade entirely
- Always account for widened spreads around news releases

## Related Skills

- **breakout-trading** -- post-news consolidation breakouts follow breakout principles
- **gap-trading** -- news events often produce gap opens
