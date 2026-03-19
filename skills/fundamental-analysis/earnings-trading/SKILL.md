---
name: earnings-trading
description: Trade around earnings announcements for stocks. Use when positioning for earnings, trading post-earnings moves, or analyzing earnings-driven volatility.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["volatile"]
---

# Earnings Trading

Trade volatility and price moves around quarterly earnings announcements.

## Earnings Impact

| Scenario              | Typical Reaction |
| --------------------- | ---------------- |
| Beat + Raise guidance | Strong rally     |
| Beat expectations     | Moderate pop     |
| Meet expectations     | Muted/slight dip |
| Miss expectations     | Drop             |
| Miss + Lower guidance | Strong sell-off  |

## Trading Strategies

### 1. Pre-Earnings Positioning

- Analyze expectations vs reality
- Position 1-5 days before
- Risk: Binary outcome

### 2. Earnings Run-Up

- Buy small caps 2-4 weeks before
- Sell before announcement
- Capture anticipation, avoid event

### 3. Post-Earnings Drift

- Strong beats continue trending up
- Enter after initial reaction settles
- Ride continuation for days/weeks

### 4. Fade Overreaction

- Gap down on decent earnings = Buy
- Gap up on mediocre = Sell
- Requires experience

## Analysis Workflow

Use `get_financial_news` and `get_fundamentals` to:

1. **Research expectations**

   - EPS estimate
   - Revenue estimate
   - Key metrics (users, margins, guidance)

2. **Assess sentiment**

   - Analyst upgrades/downgrades
   - Recent news impact
   - Sector performance

3. **Plan trade**
   - Entry point
   - Position size (reduce for earnings)
   - Exit scenarios

## Risk Management

| Rule            | Guideline            |
| --------------- | -------------------- |
| Position size   | 50% of normal max    |
| Stop loss       | Wider than normal    |
| Hedging         | Consider options     |
| Holding through | Only with conviction |

## Post-Earnings Analysis

After release, analyze:

- Beat/miss on EPS
- Beat/miss on revenue
- Guidance changes
- Management commentary
- Price reaction vs expectations

## LLM Transcript Analysis

Use `get_financial_news` to find earnings call transcripts and summaries, then analyze management tone and language for trading signals.

### Searching for Transcripts

```
get_financial_news(topic="AAPL earnings call transcript summary management", max_results=10)
```

Focus on post-call summaries, analyst recaps, and direct transcript excerpts.

### Management Tone Scoring

Score management tone into three categories:

- **Confident** — Specific numbers cited, guidance raised, forward-looking commitments. Phrases: "record revenue", "ahead of schedule", "exceeding expectations", "strong pipeline"
- **Cautious** — Hedging language, qualifiers, vague timelines. Phrases: "headwinds", "cautious outlook", "challenging environment", "monitoring closely"
- **Evasive** — Avoiding direct answers, deflecting analyst questions, pivoting to unrelated metrics. This is the most bearish signal — management avoids topics when the news is bad

### What to Look For

- **Guidance language changes vs prior quarter** — Did they shift from "confident" to "cautious"? That's a red flag even if they beat this quarter
- **Key bullish phrases**: "record revenue", "ahead of schedule", "raising full-year guidance", "accelerating growth"
- **Key bearish phrases**: "headwinds", "cautious outlook", "restructuring", "right-sizing", "transitional quarter"
- **Analyst Q&A tone** — If analysts press hard on a topic and management deflects, that area is likely weak

## Post-Earnings Drift Statistics

Post-earnings drift is one of the most well-documented market anomalies — stocks that surprise on earnings tend to continue moving in the same direction.

### Key Statistics

- Stocks that beat EPS by >10% continue drifting in the same direction for 60+ days approximately **65% of the time**
- Drift is **strongest in the first 5 trading days**, then gradually fades over the next 55 days
- Drift is **significantly stronger when accompanied by raised guidance** — the combination of beat + raise is the highest-conviction signal
- Stocks that miss badly show similar drift in the negative direction

### Drift Trading Strategy

1. **Entry**: After the initial earnings reaction settles (1-2 hours post-release, or next market open)
2. **Hold period**: 5-20 trading days to capture the bulk of the drift
3. **Trail stop**: Use a trailing stop rather than a fixed target — drift can extend further than expected
4. **Best setups**: Large EPS beat (>10%) combined with raised guidance and positive management tone

## Whisper Number Concept

The published consensus estimate is the "official" market expectation, but the **real expectation** (the whisper number) is often different — and it's the whisper number that actually determines the stock's reaction.

### How Whisper Numbers Form

- If a stock has **run up 15% into earnings**, the market is pricing in a big beat even if the published consensus is modest
- Institutional traders and options markets often reflect the whisper number through pre-earnings positioning
- The whisper number is almost always higher than consensus for stocks with momentum, and lower for beaten-down names

### Why This Matters

- **"Beat consensus by 2% but stock drops"** = The whisper number was much higher than consensus. The stock technically beat but disappointed the real expectation
- **"Missed consensus by 1% but stock rallies"** = The whisper number was even lower than consensus. The miss was less bad than feared
- This explains most "irrational" post-earnings moves

### Estimating the Whisper Number

Use price action leading into earnings combined with sentiment analysis:

```
get_financial_news(topic="AAPL earnings expectations whisper sentiment analyst", max_results=15)
```

- Strong pre-earnings rally = whisper number is well above consensus
- Pre-earnings selling = market bracing for disappointment, whisper below consensus
- Flat price action = whisper roughly equals consensus

## Enhanced Workflow

Use the fundamental analyst tools to build a complete earnings analysis:

### Step 1: Get Consensus Estimates

```
get_fundamentals(ticker="AAPL")
```

Pull EPS estimates, revenue estimates, earnings calendar date, and historical beat/miss pattern.

### Step 2: Research Analyst Expectations and Sentiment

```
get_financial_news(topic="AAPL earnings Q1 2026 expectations analyst", max_results=20)
```

Look for recent analyst notes, price target changes, and pre-earnings sentiment shifts.

### Step 3: Assess Management Tone from Call Summaries

```
get_financial_news(topic="AAPL earnings call transcript summary management", max_results=10)
```

After the call, analyze management tone using the LLM Transcript Analysis framework above. Score as Confident, Cautious, or Evasive.

### Step 4: Score the Earnings

Rate the earnings on three dimensions:

- **EPS**: Beat / Meet / Miss (and by how much)
- **Revenue**: Beat / Meet / Miss (and by how much)
- **Guidance**: Raised / Maintained / Lowered

The combination determines the overall signal. Beat + Beat + Raise is the strongest bullish signal. Miss + Miss + Lower is the strongest bearish signal.

### Step 5: Report to Orchestrator

Compile the full analysis: consensus vs actual on all metrics, management tone score, guidance changes, whisper number assessment, and recommended post-earnings action. Pass to the orchestrator for final decision-making.

## Key Insight

"Buy the rumor, sell the news" often applies. Stocks run up into good expected earnings, then sell on the news even if they beat. Surprise matters more than absolute numbers.

## Related Skills

- **sentiment-analysis** — Pre-earnings sentiment scoring helps estimate the whisper number and market expectations
- **news-trading** — Earnings are a key news event; news-trading provides the post-event reaction framework
- **sector-rotation** — Earnings trends across a sector reveal rotation signals and cycle positioning
