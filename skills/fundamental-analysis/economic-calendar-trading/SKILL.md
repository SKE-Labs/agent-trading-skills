---
name: economic-calendar-trading
description: Trade around scheduled economic events using impact ranking, deviation scoring, and structured scenario analysis. Use when positioning for FOMC, CPI, NFP, GDP, or other macro events, or when assessing how upcoming events affect existing positions.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Economic Calendar Trading

Trade around scheduled economic releases that move markets. The key insight: it's not the number that matters, but the **deviation from consensus** that drives price.

## Event Impact Ranking

| Event | Impact Score | Frequency | Release Time (ET) | Assets Affected |
| --- | --- | --- | --- | --- |
| FOMC Rate Decision | 10 | 8x/year | 2:00 PM + presser 2:30 PM | All markets |
| Non-Farm Payrolls (NFP) | 9 | 1st Friday/month | 8:30 AM | USD, Stocks, Bonds |
| CPI (Inflation) | 8.5 | ~10th-15th/month | 8:30 AM | Stocks, Bonds, Crypto |
| GDP | 7 | Quarterly | 8:30 AM | Broad market |
| PCE (Fed's inflation) | 7 | Monthly | 8:30 AM | Fed-sensitive assets |
| PMI (Manufacturing/Services) | 6 | Monthly | 10:00 AM | Sector-specific |
| Retail Sales | 5.5 | Monthly | 8:30 AM | Consumer stocks |
| Jobless Claims | 4 | Weekly | 8:30 AM | USD, short-term |

## Deviation Scoring Framework

The magnitude of surprise vs forecast drives the move:

```
Deviation Score = (Actual - Forecast) / Forecast × 100
```

### Significant Deviation Thresholds

| Event | Small Deviation | Moderate | Large (market-moving) |
| --- | --- | --- | --- |
| NFP | ±25K jobs | ±50K jobs | ±100K+ jobs |
| CPI (YoY) | ±0.1% | ±0.2% | ±0.3%+ |
| GDP (QoQ) | ±0.2% | ±0.5% | ±1.0%+ |
| Fed Funds Rate | — | ±25bps surprise | ±50bps surprise |
| PMI | ±0.5 pts | ±1.0 pts | ±2.0+ pts |
| Retail Sales | ±0.2% | ±0.5% | ±1.0%+ |

**Key rule**: A "miss" or "beat" only matters relative to consensus. CPI at 3.2% when consensus is 3.1% is a small miss. CPI at 3.5% when consensus is 3.1% is market-moving.

## Trading Strategies

### 1. Pre-Event Positioning

- Analyze expectations vs likely outcome
- Position 1-2 days before with reduced size
- Best for events with clear directional bias based on leading indicators

### 2. Post-Event Continuation (Safest)

- Wait for initial volatility to settle
- Enter in the direction of the established move
- Wait time varies by impact:

| Event Impact Score | Wait Time Before Entry | Rationale |
| --- | --- | --- |
| 9-10 (FOMC, NFP) | 30-45 min | Maximum volatility, whipsaws common |
| 7-8.5 (CPI, GDP, PCE) | 15-30 min | High vol but settles faster |
| 5-6 (PMI, Retail Sales) | 5-15 min | Moderate vol, quicker absorption |
| <5 (Claims, etc.) | Immediate OK | Low impact, fast pricing |

### 3. Fade Overreaction

- Wait for extreme move (>2 ATR in <30 min)
- Fade back toward pre-event price or VWAP
- Only for experienced traders — requires conviction and wider stops

### 4. Event Cluster Awareness

When multiple events hit in the same window (e.g., NFP + unemployment rate + wages):
- Increase wait time by 50%
- Reduce position size further (75% reduction vs normal 50%)
- Watch for conflicting signals across data points

## FOMC Deep Analysis

### Hawk/Dove Language Scoring

When analyzing FOMC statements and press conferences via `get_financial_news`:

**Hawkish keywords** (rate hikes, tightening):
- "Elevated inflation", "above target", "further tightening may be appropriate"
- "Strong labor market", "robust demand", "upside risks to inflation"
- Dot plot median moves higher

**Dovish keywords** (rate cuts, easing):
- "Progress on inflation", "approaching target", "appropriately calibrated"
- "Cooling labor market", "moderating demand", "downside risks to employment"
- Dot plot median moves lower, "cuts" language increases

**Neutral/Balanced**:
- "Data dependent", "meeting by meeting", "both sides of mandate"

| FOMC Outcome | Market Reaction | Typical Duration |
| --- | --- | --- |
| Dovish surprise | Risk-on: stocks up, USD down, bonds up, crypto up | 1-3 days trend |
| Hawkish surprise | Risk-off: stocks down, USD up, bonds down, crypto down | 1-3 days trend |
| As expected | Muted initial, then trade the statement/presser nuance | Hours |
| Dovish hold (no cut when expected) | Sharp risk-off, then assess | 1-2 days |

## Pre-Event Workflow

### 1. Check Calendar

```
get_economics_calendar(from="2026-03-19", to="2026-03-26", impact="high")
```

Identify all events in the coming week. Flag any with Impact Score ≥7.

### 2. Research Context and Consensus

```
get_financial_news(query="FOMC rate decision March 2026 expectations", limit=15)
get_financial_news(query="CPI inflation forecast consensus", limit=10)
```

Extract:
- **Consensus forecast** (the number the market expects)
- **Range of estimates** (helps gauge surprise magnitude)
- **Leading indicators** (what other data suggests about the release)
- **Market positioning** (are traders already positioned for a specific outcome?)

### 3. Build Scenario Matrix

For each upcoming high-impact event:

| Scenario | Probability | Expected Market Reaction | Position Recommendation |
| --- | --- | --- | --- |
| Beat consensus (by threshold) | Est % | Direction, magnitude | Long/short, size |
| Meet consensus | Est % | Muted/continuation | Hold/no action |
| Miss consensus (by threshold) | Est % | Direction, magnitude | Long/short, size |

### 4. Position Size Reduction Rules

| Event Impact Score | Position Reduction | Stop Width |
| --- | --- | --- |
| 9-10 | Reduce 75% or close | 2× normal |
| 7-8.5 | Reduce 50% | 1.5× normal |
| 5-6 | Reduce 25% | 1.25× normal |
| <5 | Optional reduction | Normal |

### 5. Report to Orchestrator

Provide:
- **Upcoming events** ranked by impact with dates/times
- **Consensus expectations** for each event
- **Scenario matrix** with probability-weighted outcomes
- **Position recommendations**: Reduce, close, hold, or new entry
- **FOMC analysis**: Hawk/dove assessment if applicable
- **Event clustering**: Flag if multiple events coincide

## Risk Management

| Rule | Guideline |
| --- | --- |
| Position size | Reduce by impact score (see table above) |
| Holding into events | Reduce or close before Score ≥8 events |
| Stop loss | Wider stops (volatility expansion expected) |
| Spreads | Account for widening — limit orders only |
| Correlated positions | Reduce all correlated positions, not just direct exposure |
| New entries | Avoid opening new positions 2h before Score ≥8 events |

## Best Practices

| Do | Don't |
| --- | --- |
| Know the calendar — check every Monday | Get surprised by scheduled events |
| Trade the reaction, not the prediction | Bet on the number before release |
| Wait the full recommended time per impact | Rush in during initial whipsaw |
| Use deviation scoring for magnitude | Treat all beats/misses equally |
| Research consensus thoroughly before event | Trade events without knowing expectations |
| Reduce correlated exposure across positions | Only reduce the directly affected position |

## Common Mistakes

- **Trading the prediction** — Guessing the number is gambling. Trade the reaction after the number drops.
- **Entering too early after release** — The first 5-15 minutes often reverse. Wait the recommended time.
- **Ignoring event clusters** — NFP day also has unemployment and wages. One data point can contradict another.
- **Same position size** — Not reducing size before high-impact events is the most common risk management failure.
- **Forgetting spread widening** — Market orders around events hit terrible fills. Always use limit orders.

## Related Skills

- **news-trading** — News trading covers both scheduled economic events and unscheduled corporate news
- **sentiment-analysis** — Pre-event sentiment helps gauge market positioning and whisper expectations
- **sector-rotation** — Economic data releases (Fed, CPI, GDP) are primary catalysts for sector rotation shifts
