---
name: news-trading
description: Trade volatility around economic news and corporate events. Use deviation-from-consensus scoring to gauge expected move magnitude. Use when capitalizing on market-moving news, trading earnings, or positioning for scheduled events.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["volatile"]
---

# News Trading Strategy

News trading captures volatility from scheduled economic events and corporate announcements.

## High-Impact Events

### Economic Calendar

| Event           | Impact    | Typical Move |
| --------------- | --------- | ------------ |
| FOMC/Fed Rate   | Very High | 100+ pips    |
| NFP (Jobs)      | Very High | 50-100 pips  |
| CPI (Inflation) | High      | 50-80 pips   |
| GDP             | High      | 30-50 pips   |
| Retail Sales    | Medium    | 20-40 pips   |

### Corporate Events

- Earnings releases
- Guidance updates
- M&A announcements
- Product launches

## Trading Strategies

### 1. Pre-News Positioning

- Analyze expectations vs likely outcome
- Position before announcement
- High risk—binary outcome
- Use smaller size

### 2. Straddle (Options)

- Go long both call and put
- Profit from large move either direction
- Requires options access

### 3. Post-News Reaction

- Wait for initial spike
- Look for reversal or continuation
- Trade the follow-through
- Safer but less profit

### 4. Fade the Move

- Wait for overreaction
- Trade reversal back to mean
- Experienced traders only

## Entry Workflow (Post-News)

1. **Wait for news release**
2. **Observe initial reaction** (1-5 minutes)
3. **Wait for consolidation** (5-15 minutes)
4. **Enter breakout** of post-news consolidation
5. **Wide stop** (volatility is high)
6. **Target** next key level

## Risk Management

| Rule              | Guideline                 |
| ----------------- | ------------------------- |
| Position size     | Reduce by 50-75%          |
| Stop loss         | Wider than normal         |
| No pre-news holds | Close before announcement |
| Spreads           | Widen significantly       |

## News Sources

Use `get_financial_news` tool to:

- Research upcoming events
- Gauge market expectations
- Understand current sentiment
- After event: Analyze reaction

## Deviation-from-Consensus Framework

The key insight in news trading is that the **deviation from consensus** moves markets, not the absolute number. A 200K NFP print means nothing without knowing the forecast — if consensus was 195K, it's a non-event; if consensus was 150K, it's a massive beat.

### Formula

```
Deviation Score = (Actual - Forecast) / Forecast × 100
```

A positive score means a beat; negative means a miss. The magnitude determines the expected market move and your conviction level.

### Deviation Thresholds by Event

| Event           | Small (muted move) | Moderate (tradeable) | Large (high conviction) |
| --------------- | ------------------ | -------------------- | ----------------------- |
| NFP (Jobs)      | ±25K               | ±50K                 | ±100K+                  |
| CPI (Inflation) | ±0.1%              | ±0.2%                | ±0.3%+                  |
| GDP             | ±0.2%              | ±0.5%                | ±1.0%+                  |

### How to Use

- **Small deviation**: Low conviction — consider skipping or using minimal size
- **Moderate deviation**: Standard news trade setup — use reduced position size per risk rules
- **Large deviation**: High conviction — use full news-trading position size, expect sustained directional move

Larger deviation = larger expected move = more conviction in the trade direction.

## Event Clustering Awareness

When multiple economic events release in the same window (e.g., NFP + unemployment rate + average hourly earnings on the same day), signals can conflict and create confusion.

### Rules for Clustered Events

- **Increase wait time by 50%** — if normal wait is 30 min, wait 45 min when events cluster
- **Reduce position size further** — apply 75% reduction instead of the standard 50% reduction
- **Wait for ALL numbers before entering** — do not react to the first release alone
- **If data points conflict** (e.g., strong jobs number + rising unemployment + weak wages), wait even longer or **skip the trade entirely**

Conflicting signals during event clusters are one of the top causes of whipsaw losses in news trading.

## Post-Event Wait Periods

| Event Impact                | Wait Time  | Rationale                    |
| --------------------------- | ---------- | ---------------------------- |
| Very High (FOMC, NFP)      | 30-45 min  | Maximum whipsaws             |
| High (CPI, GDP)            | 15-30 min  | Moderate volatility          |
| Medium (Retail Sales, PMI) | 5-15 min   | Quick absorption             |
| Low (weekly data)          | Immediate OK | Minimal impact             |

These wait periods allow the initial spike-and-reversal pattern to play out. Most whipsaw losses happen in the first few minutes after a high-impact release.

## Enhanced Workflow

Use the fundamental analyst tools to build a complete news trading plan:

### Step 1: Check Economic Calendar

```
get_economics_calendar(from_date="2026-03-19", to_date="2026-03-26", impact="high")
```

Identify all upcoming high-impact events for the week. Note dates, times, and which markets are affected.

### Step 2: Research Consensus for Each Event

```
get_financial_news(topic="NFP jobs forecast consensus March 2026", max_results=15)
```

For each high-impact event, search for the current consensus forecast. Note the range of analyst estimates, not just the median.

### Step 3: Plan Scenarios (Beat / Miss / Meet)

For each event, pre-plan three scenarios:

- **Beat consensus**: Which direction to trade, what deviation score would trigger entry
- **Miss consensus**: Opposite direction, same scoring framework
- **Meet consensus**: No trade — meeting expectations rarely produces tradeable moves

### Step 4: Wait Recommended Time Post-Release

After the event releases, apply the post-event wait periods table above. During clustered events, extend the wait by 50%.

### Step 5: Report Findings to Orchestrator

Compile the analysis: event details, consensus vs actual, deviation score, recommended action and conviction level. Pass this to the orchestrator for final decision-making.

## Avoid These Mistakes

- Trading during first 60 seconds (whipsaws)
- Ignoring widened spreads
- Over-leveraging before news
- Not knowing the scheduled events

## Related Skills

- **economic-calendar-trading** — Comprehensive economic event framework with deviation scoring and FOMC analysis
- **sentiment-analysis** — Pre-news sentiment scoring helps estimate the whisper number and market expectations
- **earnings-trading** — Earnings are a key news event; earnings-trading provides EPS/revenue-specific frameworks
