---
name: market-correlation-trading
description: Measure time-varying cross-asset correlation, beta, lead-lag, and spread stationarity. Use when evaluating hedges, common factors, regime breaks, divergences, or convergence hypotheses.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Market Correlation Trading

Measure time-varying co-movement and test whether a hedge, factor exposure, or stationary spread exists. Divergence can reflect a regime change; correlation alone does not imply convergence, causation, or lead-lag.

## Measurement

- Align exchange calendars, timestamps, currencies, and return intervals; do not correlate price levels.
- Compute rolling Pearson and rank correlation over predeclared short and long windows, with confidence intervals and enough observations.
- Estimate rolling beta or a multi-factor model when the objective is hedging.
- Require an economically linked, stationary spread and out-of-sample half-life before proposing convergence.
- Test lead-lag with lagged returns while controlling common factors and multiple comparisons.

## Divergence Signals

| Scenario | Signal |
| --- | --- |
| BTC rallies but Nasdaq flat/down | BTC overextended, watch for pullback |
| Gold falls but real yields also fall | Gold undervalued, potential buy |
| Oil rises but energy stocks lag | Energy stocks may catch up |
| VIX rises but S&P holds | Hedging without selling, watch for resolution |

Use 20/60 bars only as example windows. Calibrate the windows and breakdown threshold in training data, then report estimates, uncertainty, and observation count.

## Lead-Lag Hypotheses

For every proposed leader/follower pair, state the economic mechanism, data clock, lags tried, common-factor controls, and held-out result. Never copy a fixed lag table into a trade.

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
get_candles(symbol="SPY", exchange=<exchange>, interval="1D", count=250)
get_candles(symbol="QQQ", exchange=<exchange>, interval="1D", count=250)
get_candles(symbol="TLT", exchange=<exchange>, interval="1D", count=250)
get_candles(symbol="GLD", exchange=<exchange>, interval="1D", count=250)
```

Compare recent performance (1W, 1M, 3M) across correlated pairs.

### 2. Research Macro Context

```
get_financial_news(topic="correlation stocks bonds regime shift <current year>", max_results=10)
get_economics_calendar(from_date=<start>, to_date=<end>, impact="high")
```

Determine whether current correlations are driven by Fed policy, inflation, or event-specific factors. High-impact macro events can trigger regime shifts.

### 3. Identify and Report Divergences

Report return definition, windows, estimates/uncertainty, beta/factor exposures, divergence z-score, stationarity result, costs, and `hedge`, `watch`, or `no trade`. Do not call an asset mispriced from correlation alone.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Ang & Bekaert](https://www.nber.org/papers/w7056) finds correlations and volatilities vary by regime and often rise in bad times; a static correlation table is not a trading signal.

## Key Rules

- Never assume correlations are permanent; show rolling estimates and adverse stresses toward +1 or -1.
- Include macro/factor regime and stress correlations; diversification can weaken without every asset moving together.
- Aggregate positions with shared beta/factor/scenario risk rather than relying on one pair correlation.
- Correlation is not causation or convergence; control for common drivers where possible.
- When a historical relationship changes, test for a regime break before proposing convergence.

## Related Skills

- **sector-rotation** -- Sector correlations reveal rotation opportunities
- **economic-calendar-trading** -- Macro events drive correlation regime shifts
