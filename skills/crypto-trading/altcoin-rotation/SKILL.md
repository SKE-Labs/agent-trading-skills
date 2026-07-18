---
name: altcoin-rotation
description: Build and test survivorship-aware crypto rotation rankings. Use when allocating among BTC, ETH, and liquid altcoins with relative strength, breadth, liquidity, stress, turnover, and concentration controls.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Altcoin Rotation Strategy

Rank a liquid, survivorship-aware crypto universe and rotate only when relative strength and breadth improve without a BTC stress event.

## Rotation Model

| Input | Reproducible measure | Use |
| --- | --- | --- |
| Relative strength | Candidate/BTC and candidate/ETH total return over frozen lookbacks | Rank, do not predict |
| Breadth | Share of eligible alts outperforming BTC | Require broad participation |
| Liquidity | Median dollar volume, spread, depth, listing age | Exclude untradeable winners |
| BTC stress | BTC drawdown, realized volatility, and market breadth | De-risk when the common factor dominates |
| Concentration | Pairwise correlation and BTC beta | Cap duplicated exposure |

Build the universe from assets that were actually tradable at each historical date. Exclude stablecoins, wrapped duplicates, recent listings without sufficient history, and instruments that fail the account's liquidity floor. Do not use today's top coins in an old backtest.

## Workflow

1. **Establish the BTC regime** from price history, not headlines:
```
get_candles(symbol="BTC/USD", exchange="binance", interval="1d", count=120)
```

2. **Measure relative strength** on the same timestamps and venue:
```
get_candles(symbol="ETH/BTC", exchange="binance", interval="1d", count=120)
get_candles(symbol=<candidate_btc_pair>, exchange=<exchange>, interval="1d", count=120)
```

3. **Rank and gate** candidates by predeclared return lookbacks, breadth, liquidity, and correlation. Treat BTC dominance as optional context only when sourced from a consistent, documented series.

4. **Rebalance on a fixed schedule** with a no-trade buffer so small rank changes do not create fee churn. Compare the rotation with BTC-only, ETH/BTC, and equal-weight eligible-universe benchmarks.

5. **Report** universe date, excluded assets, lookbacks, ranks, breadth, BTC stress state, turnover, expected costs, proposed weights, and the condition that returns the portfolio to its defensive allocation.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Liu, Tsyvinski & Wu](https://www.nber.org/papers/w25882) documented size and momentum factors in crypto returns; this supports relative-strength testing, not fixed BTC-dominance cutoffs or static allocations.

## Key Rules

- NEVER backtest with a present-day survivor list or rank on information unavailable at the rebalance timestamp
- NEVER treat BTC dominance thresholds as universal cycle boundaries
- Size from the portfolio risk budget, liquidity, and correlation; do not copy fixed allocation percentages
- Require a defensive exit for BTC stress, liquidity loss, delisting, or correlation convergence

## Related Skills

- **on-chain-analysis** -- on-chain metrics confirm accumulation/distribution phases
- **dca-strategy** -- DCA into BTC/ETH during accumulation phases
