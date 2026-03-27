---
name: sector-rotation
description: Rotate between sectors based on economic and market cycles. Use when optimizing sector allocation, understanding cyclical trends, or positioning for macro shifts.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
---

# Sector Rotation

Rotate sector allocation based on economic cycle phase, relative strength, and macro catalysts.

## Economic Cycle Sectors

| Phase | Economy | Best Sectors |
| --- | --- | --- |
| **Early Expansion** | Recovery begins | Financials, Consumer Discretionary, Tech |
| **Mid Expansion** | Growth accelerates | Industrials, Materials, Tech |
| **Late Expansion** | Growth peaks | Energy, Materials, Financials |
| **Contraction** | Slowdown/recession | Utilities, Healthcare, Consumer Staples |

**Cyclical** (economy-sensitive): Consumer Discretionary, Financials, Industrials, Materials, Energy, Tech
**Defensive** (recession-resistant): Utilities, Healthcare, Consumer Staples, Real Estate

## Rotation Signals

| Signal | Indicates |
| --- | --- |
| Yield curve steepening | Early cycle -- favor cyclicals |
| Yield curve flattening | Late cycle -- rotate to defensives |
| Fed cutting rates | Early cycle starting |
| Fed raising rates | Late cycle |
| Commodities rallying | Late cycle inflation |

## Sector ETFs

| Sector | ETF |
| --- | --- |
| Technology | XLK |
| Healthcare | XLV |
| Financials | XLF |
| Consumer Discretionary | XLY |
| Consumer Staples | XLP |
| Energy | XLE |
| Industrials | XLI |
| Utilities | XLU |
| Materials | XLB |

## Workflow

### 1. Build Relative Strength Rankings

```
get_fundamentals(ticker="XLK")
get_fundamentals(ticker="XLF")
get_fundamentals(ticker="XLE")
get_fundamentals(ticker="XLU")
get_fundamentals(ticker="XLV")
get_fundamentals(ticker="XLY")
get_fundamentals(ticker="XLP")
get_fundamentals(ticker="XLI")
get_fundamentals(ticker="XLB")
```

Compare % change across 1M, 3M, and 6M. Rank all sectors. Rising relative strength = rotating IN; falling = rotating OUT. Top 3 are overweight candidates, bottom 3 are underweight candidates.

### 2. Research Macro Context

```
get_financial_news(topic="sector rotation economic cycle 2026", max_results=15)
get_economics_calendar(from_date="2026-03-20", to_date="2026-04-20", impact="high")
```

Identify cycle phase, Fed policy direction, and upcoming macro catalysts that could shift rotation.

### 3. Detect Correlation Regime Shifts

When normally uncorrelated sectors start moving together, a macro factor is dominating individual sector dynamics:
- Tech and Utilities both rising strongly = macro factor (Fed policy, liquidity) overriding sector rotation
- All sectors falling together = risk-off regime, defensive positioning matters less
- Defensive and cyclical diverging sharply = normal rotation is active, standard cycle strategy applies

When correlation regime shifts are detected, prioritize macro analysis over traditional rotation signals.

### 4. Report Recommendations

Provide: current cycle phase assessment, top 3 overweight sectors with rationale, top 3 underweight sectors with rationale, and key upcoming events that could shift the rotation.

## Key Rules

- NEVER concentrate 100% in one sector -- 30% max allocation per sector
- NEVER rotate all at once -- shift gradually across multiple sessions
- NEVER rely solely on historical cycle patterns -- confirm with current relative strength data and macro context
- Review sector allocation monthly at minimum
- When all sectors correlate (crisis mode), standard rotation logic breaks down -- prioritize capital preservation

## Related Skills

- **market-correlation-trading** -- Cross-asset correlations reveal regime shifts
- **economic-calendar-trading** -- Fed and macro data are primary rotation catalysts
