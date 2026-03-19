---
name: market-correlation-trading
description: Trade cross-asset correlations, lead-lag relationships, and correlation breakdowns for macro-informed signals. Use when analyzing how related assets move together, identifying divergences between correlated pairs, or assessing macro regime shifts.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Market Correlation Trading

Assets don't move in isolation. Understanding correlations between assets reveals institutional flows, regime shifts, and trading opportunities when correlations break down.

## Key Correlation Pairs

### Positive Correlations (Move Together)

| Pair | Typical Correlation | Mechanism |
| --- | --- | --- |
| BTC / Nasdaq | +0.5 to +0.8 | Risk-on/off sentiment, tech-adjacent |
| BTC / ETH | +0.7 to +0.95 | Crypto market co-movement |
| EUR/USD / GBP/USD | +0.8 to +0.9 | Both anti-USD |
| Gold / Silver | +0.7 to +0.9 | Precious metals co-movement |
| Tech stocks (AAPL/MSFT/GOOGL) | +0.6 to +0.8 | Sector co-movement |
| Oil / Energy stocks (XLE) | +0.7 to +0.9 | Direct commodity exposure |

### Inverse Correlations (Move Opposite)

| Pair | Typical Correlation | Mechanism |
| --- | --- | --- |
| Gold / Real Yields (TIPS) | -0.7 to -0.9 | Gold is anti-yield |
| USD / Emerging Markets | -0.6 to -0.8 | Strong USD hurts EM |
| USD / Gold | -0.5 to -0.7 | Dollar-denominated pricing |
| VIX / S&P 500 | -0.7 to -0.9 | Fear gauge vs market |
| Bonds (TLT) / Stocks (SPY) | -0.3 to -0.6 | Risk rotation (varies by regime) |

## Trading Correlation Breakdowns

### The Core Insight

When normally correlated assets diverge, **one must revert**. This creates a high-probability trade:

| Scenario | Signal |
| --- | --- |
| BTC rallies but Nasdaq flat/down | BTC may be overextended — watch for pullback |
| Gold falls but real yields also fall | Gold may be undervalued — potential buy |
| Oil rises but energy stocks lag | Energy stocks may catch up — potential buy |
| VIX rises but S&P holds | Hedging activity without selling — watch for resolution |

### Correlation Breakdown Score

| Metric | How to Measure |
| --- | --- |
| Normal correlation (baseline) | 60-day rolling correlation |
| Current correlation | 20-day rolling correlation |
| Divergence | If 20d corr deviates >0.3 from 60d corr → breakdown |
| Duration | >5 days of divergence → significant |

## Lead-Lag Relationships

Some assets tend to move before others:

| Leader | Follower | Typical Lag | Trading Application |
| --- | --- | --- | --- |
| US Treasury yields | Rate-sensitive stocks | 1-3 days | Rising yields → short REITs/utilities |
| DXY (Dollar Index) | EM stocks/currencies | 1-5 days | Rising DXY → reduce EM exposure |
| VIX futures curve | SPY | Hours to 1 day | VIX backwardation → defensive |
| BTC | Altcoins | 1-3 days | BTC breakout → alts follow |
| Copper | Industrials (XLI) | 1-5 days | Copper rising → bullish for industrials |
| Oil | CPI expectations | Weeks | Oil spike → expect higher CPI print |

## Regime-Dependent Correlations

**Critical**: Correlations are not constant. They shift with market regimes:

| Regime | Correlation Behavior |
| --- | --- |
| Risk-on (normal) | Traditional correlations hold |
| Risk-off (crisis) | "Everything correlates" — stocks, crypto, commodities all drop; only USD, treasuries, gold rise |
| Inflation regime | Stocks and bonds fall together (positive correlation, not typical) |
| Deflation | Stocks fall, bonds rise (traditional negative correlation) |

When regime shifts, existing correlation-based trades can fail spectacularly. Monitor macro context.

## Workflow

### 1. Identify Correlation Context

Use `get_fundamentals` to check performance of related assets:

```
get_fundamentals(ticker="SPY")
get_fundamentals(ticker="QQQ")
get_fundamentals(ticker="TLT")
get_fundamentals(ticker="GLD")
```

Compare recent performance (1W, 1M, 3M) across correlated pairs.

### 2. Research Macro Context

```
get_financial_news(query="correlation stocks bonds 2026 regime", limit=10)
get_financial_news(query="dollar emerging markets impact", limit=10)
```

Understand what's driving current correlations — is it macro (Fed policy, inflation), sector-specific, or event-driven?

### 3. Check Economic Calendar

```
get_economics_calendar(from="2026-03-19", to="2026-03-26", impact="high")
```

High-impact events can trigger regime shifts that break correlations.

### 4. Identify Divergences

Compare related assets:
- Are normally correlated assets diverging? (leader/follower breakdown)
- Are normally inverse assets moving together? (regime shift signal)
- How long has the divergence persisted? (>5 days = significant)

### 5. Report to Orchestrator

Provide structured correlation analysis:
- **Key correlations**: Which pairs are in focus and their current state
- **Divergences detected**: Assets that should be moving together but aren't
- **Lead-lag signals**: If a leader has moved, what follower is expected to catch up
- **Regime assessment**: Risk-on/off, inflation/deflation, and how it affects correlations
- **Trading implications**: Specific assets that may be mispriced based on correlation analysis
- **Risk flag**: Correlated position exposure across the portfolio

## Sector Rotation Signals from Correlations

| Observation | Interpretation | Action |
| --- | --- | --- |
| Yields rising + financials outperforming | Early/mid cycle expansion | Overweight cyclicals |
| Yields falling + utilities outperforming | Late cycle / recession fear | Rotate to defensives |
| Oil rising + materials outperforming | Inflationary pressure | Consider commodity exposure |
| Tech leading + small caps lagging | Narrow rally (fragile) | Caution on broad market longs |
| Small caps leading + breadth improving | Broad-based rally (healthy) | More aggressive positioning |

## Best Practices

| Do | Don't |
| --- | --- |
| Use 60-day baseline vs 20-day current | Assume correlations are fixed |
| Monitor regime shifts (risk-on/off) | Trade correlations without macro context |
| Treat correlated positions as one bet | Size each correlated position independently |
| Check correlation before adding related positions | Assume diversification when correlated |
| Use lead-lag for timing, not direction alone | Blindly follow the leader |

## Common Mistakes

- **Assuming correlations are permanent** — BTC/Nasdaq correlation was near zero in 2017, +0.8 in 2022, and varies since. Always use recent data.
- **Ignoring regime shifts** — In a crisis, everything correlates to the downside. Traditional diversification fails exactly when you need it most.
- **Confusing correlation with causation** — Two assets moving together doesn't mean one causes the other. Both may respond to a third factor (e.g., Fed policy).
- **Not adjusting position sizing** — If you're long BTC and long QQQ, and they're 0.7 correlated, you have concentrated risk. Use the correlation-risk skill for proper sizing.
- **Stale correlation data** — Correlations from 6 months ago may not reflect today. Always use rolling windows.

## Related Skills

- **sector-rotation** — Sector-level correlations reveal rotation opportunities when normally uncorrelated sectors converge
- **correlation-risk** — Portfolio-level correlation risk management uses these macro correlation insights for position sizing
- **economic-calendar-trading** — Macro events (Fed, CPI) are primary drivers of correlation regime shifts
