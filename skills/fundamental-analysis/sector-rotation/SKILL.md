---
name: sector-rotation
description: Rotate between sectors based on economic and market cycles. Use when optimizing sector allocation, understanding cyclical trends, or positioning for macro shifts.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Sector Rotation

Rotate sector allocation based on economic cycle phase, relative strength, and macro catalysts.

## Economic Cycle Sectors

| Phase hypothesis | Economy | Sectors often evaluated |
| --- | --- | --- |
| **Early Expansion** | Recovery begins | Financials, Consumer Discretionary, Information Technology |
| **Mid Expansion** | Growth accelerates | Industrials, Materials, Tech |
| **Late Expansion** | Growth peaks | Energy, Materials, Financials |
| **Contraction** | Slowdown/recession | Utilities, Healthcare, Consumer Staples |

Treat this map as an economic hypothesis, not a deterministic allocation rule. Classifications, constituents, and sensitivities change.

**Cyclical** (economy-sensitive): Consumer Discretionary, Financials, Industrials, Materials, Energy, Information Technology
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
| Communication Services | XLC |
| Real Estate | XLRE |

## Workflow

### 1. Build Relative Strength Rankings

```
get_candles(symbol=<sector_etf>, exchange=<exchange>, interval="1D", count=260)
get_candles(symbol="SPY", exchange=<exchange>, interval="1D", count=260)
```

Use the current 11-sector GICS universe. Rank predeclared total-return horizons relative to the benchmark, with volatility, drawdown, liquidity, and turnover. Prevent look-ahead by using classifications and constituents known on each date; compare with equal-weight and benchmark baselines.

### 2. Research Macro Context

```
get_financial_news(topic="sector rotation economic cycle <current year>", max_results=15)
get_economics_calendar(from_date=<start>, to_date=<end>, impact="high")
```

Identify cycle phase, Fed policy direction, and upcoming macro catalysts that could shift rotation.

### 3. Detect Correlation Regime Shifts

When normally uncorrelated sectors start moving together, a macro factor is dominating individual sector dynamics:
- Tech and Utilities both rising strongly = macro factor (Fed policy, liquidity) overriding sector rotation
- All sectors falling together = risk-off regime, defensive positioning matters less
- Defensive and cyclical diverging sharply = normal rotation is active, standard cycle strategy applies

When correlation regime shifts are detected, prioritize macro analysis over traditional rotation signals.

### 4. Report Recommendations

Provide the as-of date, classification universe, relative-strength/volatility table, uncertain cycle assessment, turnover/tax assumptions, and proposed weights or `no change`. Derive weights from the portfolio mandate and concentration limits rather than always selecting three winners and losers.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Moskowitz & Grinblatt](https://onlinelibrary.wiley.com/doi/pdf/10.1111/0022-1082.00146) documented industry momentum; use the current [GICS methodology](https://www.spglobal.com/spdji/en/documents/methodologies/methodology-gics.pdf) for classification rather than assuming a fixed business-cycle map.

## Key Rules

- Enforce the portfolio mandate's sector and issuer concentration limits; do not invent a universal cap.
- Rebalance on a fixed schedule and include turnover, spread, taxes, and tracking error.
- NEVER rely solely on historical cycle patterns -- confirm with current relative strength data and macro context
- Choose and validate the review frequency before testing.
- When all sectors correlate (crisis mode), standard rotation logic breaks down -- prioritize capital preservation

## Related Skills

- **market-correlation-trading** -- Cross-asset correlations reveal regime shifts
- **economic-calendar-trading** -- Fed and macro data are primary rotation catalysts
