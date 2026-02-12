---
name: insider-activity-trading
description: Track insider buying and selling for trading signals. Use when assessing management confidence, finding accumulation signals, or confirming fundamental views.
---

# Insider Activity Trading

Insider transactions can signal management's view on company value.

## Insider Types

| Insider    | Significance         |
| ---------- | -------------------- |
| CEO/CFO    | Highest significance |
| Directors  | High significance    |
| 10% owners | Medium significance  |
| Officers   | Medium significance  |

## Signal Interpretation

### Insider Buying (Generally Bullish)

| Factor            | Stronger Signal          |
| ----------------- | ------------------------ |
| Multiple insiders | Cluster buying           |
| Large purchases   | Meaningful % of holdings |
| Recent price drop | Buying the dip           |
| C-suite buying    | CEO/CFO conviction       |

### Insider Selling (Context Matters)

| Selling Reason   | Signal Strength     |
| ---------------- | ------------------- |
| Planned (10b5-1) | Neutral (scheduled) |
| Diversification  | Weak negative       |
| After big run-up | Moderate negative   |
| Unusual amount   | Stronger negative   |
| Multiple selling | Concerning          |

## Key Insight

**Buying is more meaningful than selling.**

- Insiders only buy for one reason: They think it's undervalued
- Insiders sell for many reasons: Diversification, taxes, personal needs

## Trading Strategy

### Following Insider Buys

1. Identify cluster buying (multiple insiders)
2. Check purchase size (meaningful $$$)
3. Research company fundamentals
4. Enter with technical confirmation
5. Set stop based on structure

### Avoiding Insider Sells

1. Note unusual selling patterns
2. Check if scheduled (10b5-1) or not
3. Compare to historical selling
4. Weight as one factor in analysis

## What to Look For

| Bullish Pattern          | Bearish Pattern          |
| ------------------------ | ------------------------ |
| CEO buying dip           | Multiple C-suite selling |
| Multiple insiders buying | Selling after guidance   |
| Large $ purchases        | Unusual volume of sales  |
| Buying after bad news    | Selling before news      |

## Data Sources

Use `get_financial_news` and `get_fundamentals` to find:

- Recent insider transaction filings
- Form 4 SEC filings
- Transaction patterns
- Historical comparison
- Company fundamentals context

## Limitations

| Limitation     | Reality                         |
| -------------- | ------------------------------- |
| Lagging        | Filings come 2 days after trade |
| Small sample   | May have few transactions       |
| Context needed | Selling reasons vary            |
| Not timing     | Insiders often early            |

## Best Practice

Use insider activity as:

- Confirmation of fundamental view
- Warning sign (unusual selling)
- One input among many
- Not as sole trading signal
