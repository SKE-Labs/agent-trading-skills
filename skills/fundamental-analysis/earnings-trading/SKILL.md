---
name: earnings-trading
description: Trade around earnings announcements for stocks. Use when positioning for earnings, trading post-earnings moves, or analyzing earnings-driven volatility.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Earnings Trading

Analyze and trade earnings only from time-stamped expectations, primary filings, and an explicit event-risk plan. Surprise is important, but price also reflects guidance, revisions, positioning, valuation, liquidity, and regime.

## Earnings Evidence Matrix

| Dimension | Record |
| --- | --- |
| Earnings | GAAP and adjusted EPS, reconciliation, point-in-time consensus, surprise |
| Revenue | Reported revenue, organic/segment mix, consensus, FX effects |
| Outlook | Prior versus new ranges and assumptions; do not reduce guidance to one word |
| Quality | Cash flow, margins, working capital, one-offs, share count |
| Context | Pre-event move, options-implied move if available, valuation, liquidity |

## Priced Expectations

Do not invent a numeric "whisper" from price direction. Report observable proxies separately: estimate revisions and dispersion, pre-event abnormal return, short interest, options-implied move/skew, and source-dated analyst commentary. Label any inference about positioning as uncertain.

## Post-Earnings Drift

Stocks that surprise on earnings tend to continue drifting in the same direction -- one of the most documented market anomalies.

Post-earnings-announcement drift is an empirical research finding, not a fixed probability or holding period. Define standardized unexpected earnings using point-in-time estimates, form size/liquidity buckets, and test horizons without overlapping-sample leakage. Compare closed-bar entry times and fixed, time, and trailing exits after spread and slippage.

## Workflow

### 1. Get Consensus Estimates

```
get_fundamentals(ticker="AAPL")
```

Pull point-in-time EPS/revenue estimates, estimate dispersion, earnings timestamp, and historical surprises. Verify event time and results in the issuer's 8-K/earnings release and 10-Q.

### 2. Research Expectations and Sentiment

```
get_financial_news(topic="AAPL earnings <quarter> <current year> expectations analyst", max_results=15)
```

Look for dated estimate revisions, price-target changes, and positioning proxies. Separate facts from commentary and deduplicate syndicated stories.

### 3. Analyze Call Transcript (Post-Release)

```
get_financial_news(topic="AAPL earnings call transcript summary management tone", max_results=10)
```

Compare the transcript with the prior quarter using reproducible features: quantified outlook changes, topics raised by analysts, answer specificity, and risk-language changes. Quote minimally with timestamps and treat tone as interpretation, not a deterministic label.

### 4. Score and Decide

Report each dimension separately, price reaction versus any implied move, liquidity, and `valid`, `watch`, or `no trade`. If trading, state entry trigger, gap-aware invalidation, time exit, maximum event loss, and source timestamps.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Livnat & Mendenhall](https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1475-679X.2006.00196.x) documents post-earnings-announcement drift, but its magnitude depends on how surprise is measured and does not justify a fixed continuation probability.

## Key Rules

- Do not hold through earnings unless the mandate explicitly permits gap and halt risk.
- Never infer a hidden expectation as fact; show the observable positioning proxies.
- Calibrate entry delay in closed bars for the instrument and session rather than imposing a universal clock time.
- Verify adjusted metrics against GAAP reconciliation and use point-in-time consensus.
- Treat transcript tone and analyst questioning as contextual evidence, not standalone signals.
- Size from the stress gap loss and portfolio risk limit, not a fixed percentage reduction.

## Related Skills

- **sentiment-analysis** -- source-dated expectations and positioning evidence
- **economic-calendar-trading** -- Macro events near earnings amplify volatility
