---
name: insider-activity-trading
description: Parse and evaluate SEC insider filings as delayed contextual evidence. Use when analyzing Form 4 codes, holdings changes, footnotes, amendments, purchase/sale clusters, and 10b5-1 disclosures.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Insider Activity Trading

Use insider filings as delayed, contextual evidence. A transaction may reflect valuation views, compensation, taxes, liquidity needs, ownership policy, or a trading plan; it does not reveal motive by itself.

## Filing Fields

Record issuer, insider role, filing and transaction timestamps, direct/indirect ownership, transaction code, price, shares, post-transaction holdings, footnotes, derivative status, and 10b5-1 disclosure. Confirm amendments and avoid double counting the same beneficial owner.

## Signal Interpretation

### Open-Market Purchases

| Factor | Stronger Signal |
| --- | --- |
| Multiple independent insiders buying | Candidate cluster; define window before testing |
| Large purchases | Meaningful % of holdings |
| After price drop | Buying the dip |
| C-suite buying | CEO/CFO conviction |

### Sales and Other Codes

Separate open-market purchases/sales (`P`/`S`) from grants, option exercises, tax withholding, gifts, and other codes. Read footnotes and plan disclosures; even an open-market purchase or sale has an unobserved motive.

| Selling Reason | Signal Strength |
| --- | --- |
| Planned (10b5-1) | Contextual; inspect adoption date, terms, and amendments |
| Diversification | Weak negative |
| After big run-up | Moderate negative |
| Unusual amount | Stronger negative |
| Multiple C-suite selling | Candidate cluster requiring plan/code/holdings context |

## Bullish vs Bearish Patterns

| Bullish | Bearish |
| --- | --- |
| CEO buying the dip | Multiple C-suite selling |
| Independently defined purchase cluster | Selling right after guidance |
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
- Purchase cluster = count independent insiders within a predeclared window and compare with issuer history
- C-suite selling unusual amounts = red flag, investigate further

### 3. Combine with Fundamentals

Insider activity is a confirming signal, not standalone. Cross-reference with company fundamentals, recent earnings, and technical setup before acting.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: The [SEC Form 3/4/5 bulletin](https://www.sec.gov/file/forms-3-4-5pdf) explains codes and two-business-day reporting, while the [10b5-1 rule](https://www.sec.gov/rules-regulations/2022/12/insider-trading-arrangements-related-disclosures) requires plan-related disclosures.

## Key Rules

- Never trade on a headline; parse the filed form, codes, footnotes, ownership, and amendments.
- Do not equate a 10b5-1 label with neutrality or a transaction with a disclosed motive.
- Normalize transaction value by prior holdings, compensation, market capitalization, and insider history.
- Use filing availability time—not transaction time—to prevent look-ahead bias; Form 4 is generally due within two business days, subject to form rules.
- Define cluster windows and event exclusions before testing; report `no trade` when context is missing.

## Related Skills

- **earnings-trading** -- Insider activity around earnings signals management confidence
- **sentiment-analysis** -- Insider buying is a high-credibility input to sentiment scoring
