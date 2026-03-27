---
name: market-correlation-trading
description: Trade cross-asset correlations, lead-lag relationships, and correlation breakdowns for macro-informed signals. Use when analyzing how related assets move together, identifying divergences between correlated pairs, or assessing macro regime shifts.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
---

# Market Correlation Trading

When normally correlated assets diverge, one must revert -- creating high-probability trades.

## Correlation Matrix

### Positive (Move Together)

| Pair | Typical Range | Mechanism |
| --- | --- | --- |
| BTC / Nasdaq | +0.5 to +0.8 | Risk-on/off sentiment |
| BTC / ETH | +0.7 to +0.95 | Crypto co-movement |
| EUR/USD / GBP/USD | +0.8 to +0.9 | Both anti-USD |
| Gold / Silver | +0.7 to +0.9 | Precious metals |
| Tech stocks (AAPL/MSFT/GOOGL) | +0.6 to +0.8 | Sector co-movement |
| Oil / Energy stocks (XLE) | +0.7 to +0.9 | Direct commodity exposure |

### Inverse (Move Opposite)

| Pair | Typical Range | Mechanism |
| --- | --- | --- |
| Gold / Real Yields (TIPS) | -0.7 to -0.9 | Gold is anti-yield |
| USD / Emerging Markets | -0.6 to -0.8 | Strong USD hurts EM |
| USD / Gold | -0.5 to -0.7 | Dollar-denominated pricing |
| VIX / S&P 500 | -0.7 to -0.9 | Fear gauge vs market |
| Bonds (TLT) / Stocks (SPY) | -0.3 to -0.6 | Risk rotation (regime-dependent) |

## Divergence Signals

| Scenario | Signal |
| --- | --- |
| BTC rallies but Nasdaq flat/down | BTC overextended, watch for pullback |
| Gold falls but real yields also fall | Gold undervalued, potential buy |
| Oil rises but energy stocks lag | Energy stocks may catch up |
| VIX rises but S&P holds | Hedging without selling, watch for resolution |

Measure divergence: compare 20-day vs 60-day rolling correlation. If 20d deviates >0.3 from 60d = breakdown. Duration >5 days = significant.

## Lead-Lag Relationships

| Leader | Follower | Lag | Application |
| --- | --- | --- | --- |
| US Treasury yields | Rate-sensitive stocks | 1-3 days | Rising yields -> short REITs/utilities |
| DXY (Dollar Index) | EM stocks/currencies | 1-5 days | Rising DXY -> reduce EM exposure |
| VIX futures curve | SPY | Hours-1 day | VIX backwardation -> defensive |
| BTC | Altcoins | 1-3 days | BTC breakout -> alts follow |
| Copper | Industrials (XLI) | 1-5 days | Copper rising -> bullish industrials |
| Oil | CPI expectations | Weeks | Oil spike -> expect higher CPI |

## Regime-Dependent Correlations

| Regime | Correlation Behavior |
| --- | --- |
| Risk-on (normal) | Traditional correlations hold |
| Risk-off (crisis) | Everything correlates -- stocks, crypto, commodities drop; only USD/treasuries/gold rise |
| Inflation | Stocks and bonds fall together (atypical positive correlation) |
| Deflation | Stocks fall, bonds rise (traditional inverse) |

## Workflow

### 1. Check Related Assets

```
get_fundamentals(ticker="SPY")
get_fundamentals(ticker="QQQ")
get_fundamentals(ticker="TLT")
get_fundamentals(ticker="GLD")
```

Compare recent performance (1W, 1M, 3M) across correlated pairs.

### 2. Research Macro Context

```
get_financial_news(topic="correlation stocks bonds regime shift 2026", max_results=10)
get_economics_calendar(from_date="2026-03-20", to_date="2026-03-27", impact="high")
```

Determine whether current correlations are driven by Fed policy, inflation, or event-specific factors. High-impact macro events can trigger regime shifts.

### 3. Identify and Report Divergences

Report: key correlation pairs and current state, detected divergences with duration, lead-lag signals (leader moved, follower expected to catch up), regime assessment (risk-on/off, inflation/deflation), and specific mispriced assets.

## Key Rules

- NEVER assume correlations are permanent -- BTC/Nasdaq was near zero in 2017, +0.8 in 2022; always use recent rolling windows
- NEVER trade correlations without checking the macro regime -- in a crisis, everything correlates to the downside and traditional diversification fails
- NEVER size correlated positions independently -- if you're long BTC and long QQQ at 0.7 correlation, that's concentrated risk
- NEVER confuse correlation with causation -- two assets may both respond to a third factor (e.g., Fed policy)
- When normally inverse assets start moving together, prioritize macro analysis over standard correlation plays

## Related Skills

- **sector-rotation** -- Sector correlations reveal rotation opportunities
- **economic-calendar-trading** -- Macro events drive correlation regime shifts
