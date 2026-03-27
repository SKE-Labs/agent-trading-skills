---
name: earnings-trading
description: Trade around earnings announcements for stocks. Use when positioning for earnings, trading post-earnings moves, or analyzing earnings-driven volatility.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
---

# Earnings Trading

Trade volatility and price moves around quarterly earnings, where **surprise vs expectations** drives the reaction.

## Earnings Impact Matrix

| Scenario | Typical Reaction |
| --- | --- |
| Beat EPS + Beat Revenue + Raise Guidance | Strong rally (highest conviction long) |
| Beat EPS + Beat Revenue | Moderate pop |
| Meet expectations | Muted / slight dip |
| Miss EPS or Revenue | Drop |
| Miss + Lower Guidance | Strong sell-off (highest conviction short) |

## Whisper Number

The published consensus is the "official" expectation, but the **real expectation** (whisper number) determines the reaction.

- Stock runs up 15% into earnings = market expects a big beat regardless of published consensus
- "Beat consensus by 2% but stock drops" = whisper was much higher than consensus
- "Missed by 1% but stock rallies" = whisper was even lower than consensus

Estimate the whisper from pre-earnings price action and sentiment:
- Strong rally into earnings = whisper well above consensus
- Pre-earnings selling = whisper below consensus
- Flat = whisper roughly equals consensus

## Post-Earnings Drift

Stocks that surprise on earnings tend to continue drifting in the same direction -- one of the most documented market anomalies.

- Stocks beating EPS by >10% continue drifting same direction ~65% of the time for 60+ days
- Drift is strongest in the first 5 trading days
- Drift is significantly stronger when accompanied by raised guidance
- Entry: after initial reaction settles (1-2 hours post-release or next open)
- Use a trailing stop rather than fixed target

## Workflow

### 1. Get Consensus Estimates

```
get_fundamentals(ticker="AAPL")
```

Pull EPS estimates, revenue estimates, earnings date, and historical beat/miss pattern.

### 2. Research Expectations and Sentiment

```
get_financial_news(topic="AAPL earnings Q1 2026 expectations analyst", max_results=15)
```

Look for analyst notes, price target changes, pre-earnings sentiment shifts, and whisper number clues.

### 3. Analyze Call Transcript (Post-Release)

```
get_financial_news(topic="AAPL earnings call transcript summary management tone", max_results=10)
```

Score management tone:
- **Confident**: Specific numbers, guidance raised, "record revenue", "ahead of schedule"
- **Cautious**: Hedging, qualifiers, "headwinds", "cautious outlook", "monitoring closely"
- **Evasive**: Deflecting analyst questions, pivoting to unrelated metrics -- most bearish signal

Key signal: tone shift vs prior quarter. "Confident" to "Cautious" is a red flag even if they beat.

### 4. Score and Decide

Rate on three dimensions: EPS (beat/meet/miss), Revenue (beat/meet/miss), Guidance (raised/maintained/lowered). Combine with management tone and whisper number assessment for the final signal.

## Key Rules

- NEVER hold full position size through earnings -- reduce by at least 50%
- NEVER ignore the whisper number -- most "irrational" post-earnings moves are explained by whisper vs consensus gap
- NEVER rush entry after release -- wait for initial volatility to settle (1-2 hours minimum for large caps)
- "Buy the rumor, sell the news" applies frequently: stocks run up into expected good earnings, then sell on the actual news even on a beat
- If analysts press hard on a topic during Q&A and management deflects, that area is likely weak
- Best post-earnings drift setups: large EPS beat (>10%) + raised guidance + confident management tone

## Related Skills

- **sentiment-analysis** -- Whisper number estimation via sentiment
- **economic-calendar-trading** -- Macro events near earnings amplify volatility
