---
name: sentiment-analysis
description: Analyze news sentiment using systematic scoring with source weighting and temporal decay. Use when gauging market mood, confirming technical signals, identifying contrarian opportunities, or building conviction before entries.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "3.0"
---

# Sentiment Analysis

Systematic sentiment scoring that quantifies market psychology to identify extremes, confirm setups, and flag contrarian opportunities.

## Source Hierarchy

| Source Type | Weight | Examples |
| --- | --- | --- |
| Earnings calls / SEC filings | 5 | 10-K, 10-Q, transcripts |
| Financial wire services | 4 | Reuters, Bloomberg, AP |
| Analyst reports / ratings | 3 | Goldman, Morgan Stanley |
| Financial news sites | 2 | CNBC, MarketWatch, Seeking Alpha |
| Social media / forums | 1 | Twitter/X, Reddit, StockTwits |

## Article Scoring (1-10)

| Score | Meaning | Examples |
| --- | --- | --- |
| 1-2 | Strongly bearish | Bankruptcy risk, SEC investigation, massive miss |
| 3-4 | Moderately bearish | Guidance cut, downgrade, margin compression |
| 5 | Neutral | Routine filings, expected results |
| 6-7 | Moderately bullish | Earnings beat, upgrade, new product launch |
| 8-9 | Strongly bullish | Massive beat + raised guidance, transformative deal |
| 10 | Euphoric | "Best quarter ever" -- often a contrarian warning |

## Temporal Decay

| News Age | Decay Weight |
| --- | --- |
| < 1 hour | 1.0 |
| 1-4 hours | 0.8 |
| 4-24 hours | 0.5 |
| 1-3 days | 0.2 |
| > 3 days | 0.1 |

## Composite Score

```
weighted_score = article_score x source_weight x decay_weight
Composite = sum(weighted_scores) / sum(source_weight x decay_weight)
```

| Composite | Classification | Signal |
| --- | --- | --- |
| 1.0 - 2.5 | Extreme fear | Contrarian buy zone (if at support) |
| 2.5 - 4.0 | Bearish | Confirms bearish setups |
| 4.0 - 6.0 | Neutral | No sentiment edge, rely on technicals |
| 6.0 - 7.5 | Bullish | Confirms bullish setups |
| 7.5 - 9.0 | Strong bullish | High conviction longs |
| 9.0 - 10.0 | Extreme euphoria | Contrarian sell zone (if at resistance) |

## Contrarian Signals

- Composite >9.0 at resistance = market top risk
- Composite <2.5 at support = market bottom opportunity
- **Sentiment divergence**: Price new highs + sentiment declining = distribution warning
- **Sentiment divergence**: Price new lows + sentiment improving = accumulation signal

## Workflow

### 1. Gather News Data

```
get_financial_news(topic="AAPL earnings revenue guidance analyst", max_results=20)
get_financial_news(topic="AAPL analyst upgrade downgrade price target", max_results=10)
```

Search both bullish and bearish angles for the same asset.

### 2. Score Each Article

For each article: assign sentiment score (1-10), identify source type for weight, note publication time for decay.

### 3. Calculate Composite

Apply the formula. Report: composite score, classification, key drivers, contrarian signals if any, and confidence level (High = many sources agree, Medium = mixed, Low = few sources).

### 4. Identify Cycle Phase

Disbelief (negative sentiment, rising price) = accumulate. Euphoria (extreme positive, peak) = distribute. Panic/capitulation (despair, bottom) = watch for accumulation.

## Key Rules

- NEVER score by gut feel -- follow the framework for every article systematically
- NEVER treat all sources equally -- a Reddit post is not a Bloomberg wire
- NEVER give equal weight to week-old news -- apply temporal decay
- NEVER use sentiment as primary entry signal -- it confirms technical setups
- NEVER only seek confirming news -- always search both bullish and bearish angles
- When high-credibility sources disagree, reduce conviction rather than picking a side
- Extreme sentiment can persist for weeks -- use as confirmation, not sole trigger

## Related Skills

- **earnings-trading** -- Management tone scoring feeds sentiment
- **economic-calendar-trading** -- Pre-event sentiment gauges positioning
