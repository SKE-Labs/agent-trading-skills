---
name: sentiment-analysis
description: Analyze news sentiment using systematic scoring with source weighting and temporal decay. Use when gauging market mood, confirming technical signals, identifying contrarian opportunities, or building conviction before entries.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Sentiment Analysis

Sentiment analysis gauges market psychology to identify extremes and potential reversals. This skill provides a systematic, quantifiable scoring framework.

## Sentiment Indicators

### News Sentiment

| Signal          | Bullish             | Bearish        |
| --------------- | ------------------- | -------------- |
| Headline tone   | Positive/optimistic | Negative/fear  |
| Coverage volume | Increasing          | Panic coverage |
| Analyst stance  | Upgrades            | Downgrades     |

### Social Sentiment

| Signal            | Extreme Bullish    | Extreme Bearish  |
| ----------------- | ------------------ | ---------------- |
| Social mentions   | Parabolic increase | Capitulation     |
| Retail enthusiasm | Everyone bullish   | Everyone bearish |
| Influencer calls  | "100x moon"        | "Going to zero"  |

### Market Sentiment Indicators

| Indicator          | Bullish                       | Bearish                         |
| ------------------ | ----------------------------- | ------------------------------- |
| Fear & Greed Index | Extreme Fear (contrarian buy) | Extreme Greed (contrarian sell) |
| Put/Call Ratio     | High puts (contrarian buy)    | High calls (contrarian sell)    |
| VIX                | Spike high (buy)              | Very low (caution)              |

## Sentiment Scoring Framework

### Source Hierarchy

Not all sources carry equal weight:

| Source Type | Weight | Examples |
| --- | --- | --- |
| Earnings calls / SEC filings | 5 | 10-K, 10-Q, earnings transcripts |
| Financial wire services | 4 | Reuters, Bloomberg, AP |
| Analyst reports / ratings | 3 | Goldman, Morgan Stanley, JP Morgan |
| Financial news sites | 2 | CNBC, MarketWatch, Seeking Alpha |
| Social media / forums | 1 | Twitter/X, Reddit, StockTwits |

### Individual Article Scoring

For each news item, score on a 1-10 scale:

| Score | Meaning | Examples |
| --- | --- | --- |
| 1-2 | Strongly bearish | Bankruptcy risk, SEC investigation, massive earnings miss |
| 3-4 | Moderately bearish | Guidance cut, analyst downgrade, margin compression |
| 5 | Neutral | Routine filings, lateral moves, expected results |
| 6-7 | Moderately bullish | Earnings beat, analyst upgrade, new product launch |
| 8-9 | Strongly bullish | Massive beat + raised guidance, transformative acquisition |
| 10 | Euphoric | "Best quarter ever" — often a contrarian warning |

### Temporal Decay

Recent news matters exponentially more:

| News Age | Decay Weight | Rationale |
| --- | --- | --- |
| < 1 hour | 1.0 | Full impact, market still digesting |
| 1-4 hours | 0.8 | Largely priced in but still relevant |
| 4-24 hours | 0.5 | Mostly absorbed |
| 1-3 days | 0.2 | Only high-impact events still matter |
| > 3 days | 0.1 | Background context only |

### Composite Sentiment Score

```
For each article:
  weighted_score = article_score × source_weight × decay_weight

Composite = sum(weighted_scores) / sum(source_weight × decay_weight)
```

| Composite | Classification | Trading Signal |
| --- | --- | --- |
| 1.0 - 2.5 | Extreme fear | Contrarian buy zone (if at support) |
| 2.5 - 4.0 | Bearish | Confirms bearish setups |
| 4.0 - 6.0 | Neutral | No sentiment edge — rely on technicals |
| 6.0 - 7.5 | Bullish | Confirms bullish setups |
| 7.5 - 9.0 | Strong bullish | High conviction for longs |
| 9.0 - 10.0 | Extreme euphoria | Contrarian sell zone (if at resistance) |

## Contrarian Trading

Extreme sentiment often marks reversal points:

- **Extreme bullishness** (composite >9.0) → Market top risk
- **Extreme bearishness** (composite <2.5) → Market bottom opportunity
- **Sentiment divergence**: Price making new highs but sentiment declining → Distribution warning
- **Sentiment divergence**: Price making new lows but sentiment improving → Accumulation signal

## Workflow

### 1. Gather News Data

Use `get_financial_news` to retrieve recent articles. Search multiple angles:

```
get_financial_news(query="AAPL earnings revenue guidance", limit=20)
get_financial_news(query="AAPL analyst upgrade downgrade price target", limit=10)
get_financial_news(query="technology sector outlook", limit=10)
```

### 2. Score Each Article

For each article returned:
1. Read headline and summary
2. Assign sentiment score (1-10)
3. Identify source type for weight
4. Note publication time for decay weight

### 3. Calculate Composite Score

Example walkthrough:

| Article | Score | Source Wt | Decay Wt | Weighted |
| --- | --- | --- | --- | --- |
| Reuters: "AAPL beats Q3 by 12%" | 8 | 4 | 1.0 | 32.0 |
| Goldman upgrades to Buy | 7 | 3 | 0.8 | 16.8 |
| CNBC: "iPhone sales surpass" | 7 | 2 | 1.0 | 14.0 |
| SeekingAlpha: "fairly valued" | 5 | 2 | 0.5 | 5.0 |
| Reddit: "AAPL to $300" | 9 | 1 | 1.0 | 9.0 |

Composite = (32 + 16.8 + 14 + 5 + 9) / (4 + 2.4 + 2 + 1 + 1) = 76.8 / 10.4 = **7.4 (Strong Bullish)**

### 4. Assess Sentiment Cycle Phase

| Phase        | Sentiment        | Price   | Action     |
| ------------ | ---------------- | ------- | ---------- |
| Disbelief    | Negative         | Rising  | Accumulate |
| Hope         | Improving        | Rising  | Hold       |
| Optimism     | Positive         | Rising  | Hold       |
| Euphoria     | Extreme positive | Peak    | Distribute |
| Anxiety      | Mixed            | Falling | Watch      |
| Denial       | Still positive   | Falling | Exit       |
| Panic        | Extreme negative | Falling | Watch      |
| Capitulation | Despair          | Bottom  | Accumulate |

### 5. Report to Orchestrator

Provide structured summary:
- **Composite score** and classification (e.g., "7.4 — Strong Bullish")
- **Key drivers**: What's driving sentiment (earnings beat, upgrades, etc.)
- **Contrarian signals**: Any extreme readings warning of reversal
- **Sentiment cycle phase**: Current assessment
- **Confidence**: High (many sources agree) / Medium (mixed) / Low (few sources)
- **Recommendation**: How sentiment confirms or contradicts the technical setup

## Limitations

| Limitation   | Reality                                | Mitigation |
| ------------ | -------------------------------------- | --- |
| Timing       | Sentiment can stay extreme for weeks   | Use as confirmation, not sole trigger |
| Subjectivity | Scoring requires judgment              | Follow the framework consistently |
| Lagging      | News often follows price               | Weight recent news via decay |
| Manipulation | Headlines can mislead                  | Weight wire services over blogs |

## Best Practices

| Do | Don't |
| --- | --- |
| Score systematically using the framework | Go by "gut feel" |
| Weight sources by credibility | Treat all sources equally |
| Apply temporal decay | Give equal weight to week-old news |
| Look for sentiment divergence from price | Ignore price-sentiment divergence |
| Use as confirmation + context | Use as primary entry signal |
| Flag extreme readings as contrarian | Always follow the crowd at extremes |
| Search both bullish and bearish angles | Only seek confirming news |

## Common Mistakes

- **Confirmation bias** — Only seeking news that confirms existing view. Always search both bullish and bearish angles.
- **Recency bias** — Overweighting the last headline. Use the temporal decay framework.
- **Source conflation** — Treating a Reddit post with same weight as Bloomberg. Follow the source hierarchy.
- **Ignoring contradictions** — When high-credibility sources disagree, reduce conviction rather than picking a side.
- **Trading sentiment alone** — Sentiment is a confirming factor. Always combine with technical analysis from the technical analyst.

## Related Skills

- **news-trading** — Sentiment analysis provides the scoring framework that news-trading uses for event reaction assessment
- **economic-calendar-trading** — Pre-event sentiment gauges market expectations and positioning before macro releases
- **earnings-trading** — Management tone scoring and whisper number estimation rely on sentiment analysis techniques
