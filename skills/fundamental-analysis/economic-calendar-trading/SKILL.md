---
name: economic-calendar-trading
description: Trade around scheduled economic events using impact ranking, deviation scoring, and structured scenario analysis. Use when positioning for FOMC, CPI, NFP, GDP, or other macro events, or when assessing how upcoming events affect existing positions.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "3.0"
---

# Economic Calendar Trading

Trade scheduled economic releases where the **deviation from consensus**, not the number itself, drives price.

## Event Impact Ranking

| Event | Impact | Frequency | Release (ET) | Assets Affected |
| --- | --- | --- | --- | --- |
| FOMC Rate Decision | 10 | 8x/year | 2:00 PM + presser 2:30 PM | All markets |
| Non-Farm Payrolls | 9 | 1st Friday/month | 8:30 AM | USD, Stocks, Bonds |
| CPI (Inflation) | 8.5 | ~10th-15th/month | 8:30 AM | Stocks, Bonds, Crypto |
| GDP | 7 | Quarterly | 8:30 AM | Broad market |
| PCE (Fed's inflation) | 7 | Monthly | 8:30 AM | Fed-sensitive assets |
| PMI (Mfg/Services) | 6 | Monthly | 10:00 AM | Sector-specific |
| Retail Sales | 5.5 | Monthly | 8:30 AM | Consumer stocks |
| Jobless Claims | 4 | Weekly | 8:30 AM | USD, short-term |

## Deviation Thresholds

```
Deviation Score = (Actual - Forecast) / Forecast x 100
```

| Event | Small | Moderate | Large (market-moving) |
| --- | --- | --- | --- |
| NFP | +/-25K jobs | +/-50K jobs | +/-100K+ jobs |
| CPI (YoY) | +/-0.1% | +/-0.2% | +/-0.3%+ |
| GDP (QoQ) | +/-0.2% | +/-0.5% | +/-1.0%+ |
| Fed Funds Rate | -- | +/-25bps surprise | +/-50bps surprise |
| PMI | +/-0.5 pts | +/-1.0 pts | +/-2.0+ pts |
| Retail Sales | +/-0.2% | +/-0.5% | +/-1.0%+ |

## Workflow

### 1. Check Calendar

```
get_economics_calendar(from_date="2026-03-20", to_date="2026-03-27", impact="high")
```

Flag events with Impact >= 7. Check every Monday.

### 2. Research Consensus

```
get_financial_news(topic="CPI inflation forecast consensus March 2026", max_results=10)
```

Extract: consensus forecast, range of estimates, leading indicators, and current market positioning.

### 3. Build Scenario Matrix

For each high-impact event, map beat/meet/miss scenarios with estimated probability, expected market reaction, and position recommendation.

### 4. Post-Release: Wait Before Entry

| Impact Score | Wait Time | Rationale |
| --- | --- | --- |
| 9-10 (FOMC, NFP) | 30-45 min | Maximum volatility, whipsaws common |
| 7-8.5 (CPI, GDP, PCE) | 15-30 min | High vol but settles faster |
| 5-6 (PMI, Retail) | 5-15 min | Moderate vol, quicker absorption |
| <5 (Claims, etc.) | Immediate OK | Low impact, fast pricing |

### 5. Trade the Reaction

- **Continuation**: Enter in the direction of the established move after the wait period
- **Fade overreaction**: Only if move exceeds 2 ATR in <30 min, fade back toward VWAP

### 6. FOMC Analysis

Use `get_financial_news` to analyze FOMC statements and press conferences for hawk/dove tone shifts.

| FOMC Outcome | Market Reaction | Duration |
| --- | --- | --- |
| Dovish surprise | Risk-on: stocks up, USD down, bonds/crypto up | 1-3 days |
| Hawkish surprise | Risk-off: stocks down, USD up, bonds/crypto down | 1-3 days |
| As expected | Muted initial, trade statement nuance | Hours |

## Key Rules

- NEVER trade the prediction -- trade the reaction after the number drops
- NEVER enter during the initial 5-15 minute whipsaw; wait the full recommended time per impact score
- NEVER use market orders around events -- spreads widen, use limit orders only
- NEVER hold full position size into Impact >= 8 events -- reduce or close beforehand
- When multiple events cluster (e.g., NFP + unemployment + wages), increase wait time by 50%
- A "beat" or "miss" only matters relative to consensus -- CPI at 3.2% vs 3.1% consensus is small; 3.5% vs 3.1% is market-moving
- Reduce all correlated positions before events, not just direct exposure

## Related Skills

- **sentiment-analysis** -- Pre-event sentiment gauges positioning
- **sector-rotation** -- Macro data drives sector rotation shifts
