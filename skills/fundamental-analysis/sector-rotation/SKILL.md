---
name: sector-rotation
description: Rotate between sectors based on economic and market cycles. Use when optimizing sector allocation, understanding cyclical trends, or positioning for macro shifts.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Sector Rotation Strategy

Rotate investments between sectors based on economic cycle and market conditions.

## Economic Cycle Phases

| Phase               | Economy            | Best Sectors                             |
| ------------------- | ------------------ | ---------------------------------------- |
| **Early Expansion** | Recovery begins    | Financials, Consumer Discretionary, Tech |
| **Mid Expansion**   | Growth accelerates | Industrials, Materials, Tech             |
| **Late Expansion**  | Growth peaks       | Energy, Materials, Financials            |
| **Contraction**     | Slowdown/recession | Utilities, Healthcare, Consumer Staples  |

## Sector Classification

### Cyclical (Economy-Sensitive)

- Consumer Discretionary
- Financials
- Industrials
- Materials
- Energy
- Technology

### Defensive (Recession-Resistant)

- Utilities
- Healthcare
- Consumer Staples
- Real Estate (partial)

## Rotation Signals

| Signal                 | Indicates                     |
| ---------------------- | ----------------------------- |
| Yield curve steepening | Early cycle (cyclicals)       |
| Yield curve flattening | Late cycle (rotate defensive) |
| Fed cutting rates      | Early cycle starting          |
| Fed raising rates      | Late cycle                    |
| Commodities rallying   | Late cycle inflation          |

## Rotation Workflow

1. **Identify economic phase** (leading indicators)
2. **Assess current allocation** (over/underweight)
3. **Identify rotating-in sectors** (early phase sectors)
4. **Identify rotating-out sectors** (late phase sectors)
5. **Execute gradual shift** (not all at once)

## Sector Analysis Tools

Use `get_fundamentals` and `get_financial_news` for:

- Sector ETF performance
- Sector earnings trends
- Relative strength vs S&P 500
- News catalysts

## Key ETFs by Sector

| Sector                 | ETF |
| ---------------------- | --- |
| Technology             | XLK |
| Healthcare             | XLV |
| Financials             | XLF |
| Consumer Discretionary | XLY |
| Consumer Staples       | XLP |
| Energy                 | XLE |
| Industrials            | XLI |
| Utilities              | XLU |
| Materials              | XLB |

## Relative Strength Scoring

Use `get_fundamentals` for each sector ETF to build a relative strength ranking:

1. **Retrieve fundamentals** for all major sector ETFs: XLK, XLV, XLF, XLY, XLP, XLE, XLI, XLU, XLB
2. **Compare % change** over 1-month, 3-month, and 6-month periods
3. **Rank sectors** by relative performance across all timeframes
4. **Identify rotation direction**:
   - Rising relative strength = sector is rotating IN (overweight candidate)
   - Falling relative strength = sector is rotating OUT (underweight candidate)

### Example Ranking Table

| Sector       | ETF | 1M Change | 3M Change | 6M Change | RS Rank | Direction    |
| ------------ | --- | --------- | --------- | --------- | ------- | ------------ |
| Technology   | XLK | +4.2%     | +8.1%     | +15.3%    | 1       | Rotating IN  |
| Financials   | XLF | +3.1%     | +6.5%     | +11.2%    | 2       | Rotating IN  |
| Industrials  | XLI | +1.8%     | +3.2%     | +7.0%     | 3       | Neutral      |
| Healthcare   | XLV | +0.5%     | +1.1%     | +2.3%     | 4       | Neutral      |
| Energy       | XLE | -1.2%     | -3.4%     | -5.8%     | 8       | Rotating OUT |
| Utilities    | XLU | -2.0%     | -4.1%     | -7.2%     | 9       | Rotating OUT |

Sectors ranked 1-3 are rotation-in candidates; sectors ranked 7-9 are rotation-out candidates. The middle ranks are neutral holds.

## Correlation Regime Shift Detection

When normally uncorrelated sectors start moving together, it signals a regime change is underway. This overrides standard sector rotation logic because a macro factor is dominating individual sector dynamics.

### How to Detect

- Monitor **20-day vs 60-day rolling correlation** between sector ETFs
- If the 20-day correlation diverges from the 60-day by **>0.3**, a correlation regime shift is occurring
- Pay special attention to pairs that are normally uncorrelated (e.g., Tech/Utilities, Energy/Healthcare)

### Interpretation

- **Tech and Utilities both rising strongly** = unusual, suggests a macro factor (Fed policy, liquidity injection) is overriding sector dynamics
- **All sectors falling together** = risk-off regime, correlations spike to 1.0 — defensive positioning matters less since everything sells off
- **Defensive and cyclical diverging sharply** = normal sector rotation is active, standard cycle-based strategy applies

When correlation regime shifts are detected, prioritize macro analysis (Fed policy, liquidity conditions) over traditional sector rotation signals.

## Enhanced Workflow

### Step-by-Step Process

1. **Get fundamentals for all sector ETFs** to build relative strength rankings:
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

2. **Rank sectors by relative strength** using the % change data from fundamentals across 1M, 3M, and 6M periods

3. **Research macro context** for sector rotation catalysts:
```
get_financial_news(topic="sector rotation economic cycle 2026", max_results=15)
```

4. **Check economic calendar** for upcoming Fed, inflation, and employment events:
```
get_economics_calendar(from_date="2026-03-19", to_date="2026-04-19", impact="high")
```

5. **Identify rotation signals** by combining:
   - Relative strength rankings (which sectors are leading/lagging)
   - Economic cycle phase (expansion, contraction)
   - Upcoming macro catalysts (Fed meetings, CPI releases)
   - Correlation regime (normal rotation vs macro-driven)

6. **Report sector allocation recommendations** to the orchestrator with:
   - Current cycle phase assessment
   - Top 3 overweight sectors with rationale
   - Top 3 underweight sectors with rationale
   - Key upcoming events that could shift the rotation

## Risk Management

| Rule             | Guideline             |
| ---------------- | --------------------- |
| Diversification  | Never 100% one sector |
| Max allocation   | 30% in any sector     |
| Rotation speed   | Gradual, not sudden   |
| Review frequency | Monthly/quarterly     |

## Current Cycle Assessment

Questions to answer:

- Where are we in the economic cycle?
- What is Fed policy direction?
- Which sectors are leading/lagging?
- What does relative strength show?

## Related Skills

- **market-correlation-trading** — Cross-asset correlations reveal regime shifts that override standard sector rotation
- **economic-calendar-trading** — Fed decisions and macro data releases are primary sector rotation catalysts
- **sentiment-analysis** — Sector-level sentiment confirms whether rotation is driven by fundamentals or positioning
