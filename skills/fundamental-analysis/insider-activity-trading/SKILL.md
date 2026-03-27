---
name: insider-activity-trading
description: Track insider buying and selling for trading signals. Use when assessing management confidence, finding accumulation signals, or confirming fundamental views.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
---

# Insider Activity Trading

Insider transactions reveal management conviction -- buying is a strong signal, selling requires context.

## Insider Significance

| Insider | Significance |
| --- | --- |
| CEO / CFO | Highest |
| Directors | High |
| 10% owners | Medium |
| Other officers | Medium |

## Signal Interpretation

### Buying (Generally Bullish)

Insiders only buy for one reason: they think it's undervalued.

| Factor | Stronger Signal |
| --- | --- |
| Multiple insiders buying | Cluster buying (strongest) |
| Large purchases | Meaningful % of holdings |
| After price drop | Buying the dip |
| C-suite buying | CEO/CFO conviction |

### Selling (Context-Dependent)

Insiders sell for many reasons: diversification, taxes, personal needs. Selling alone is weaker signal.

| Selling Reason | Signal Strength |
| --- | --- |
| Planned (10b5-1) | Neutral (scheduled) |
| Diversification | Weak negative |
| After big run-up | Moderate negative |
| Unusual amount | Stronger negative |
| Multiple C-suite selling | Concerning (strongest) |

## Bullish vs Bearish Patterns

| Bullish | Bearish |
| --- | --- |
| CEO buying the dip | Multiple C-suite selling |
| Cluster buying (3+ insiders) | Selling right after guidance |
| Large $ purchases on weakness | Unusual volume of sales |
| Buying after bad news | Selling before scheduled news |

## Workflow

### 1. Research Insider Activity

```
get_financial_news(topic="AAPL insider buying selling SEC Form 4 filing", max_results=15)
get_fundamentals(ticker="AAPL")
```

Look for: recent Form 4 filings, transaction size, buyer/seller role, and whether purchases are scheduled (10b5-1) or discretionary.

### 2. Assess Pattern

- Single insider selling = low signal, check if 10b5-1 planned
- Single insider buying = moderate signal, check size relative to holdings
- Cluster buying (3+ insiders within 2 weeks) = strong bullish signal
- C-suite selling unusual amounts = red flag, investigate further

### 3. Combine with Fundamentals

Insider activity is a confirming signal, not standalone. Cross-reference with company fundamentals, recent earnings, and technical setup before acting.

## Key Rules

- NEVER trade on insider activity alone -- use as confirmation of fundamental/technical view
- NEVER treat all selling as bearish -- most insider sales are routine (10b5-1 plans, diversification, tax events)
- NEVER ignore cluster buying -- multiple insiders buying within a short window is one of the highest-conviction fundamental signals
- Insider filings lag by 2 business days -- the trade already happened
- Insiders are often early -- conviction is right but timing can be off by weeks/months

## Related Skills

- **earnings-trading** -- Insider activity around earnings signals management confidence
- **sentiment-analysis** -- Insider buying is a high-credibility input to sentiment scoring
