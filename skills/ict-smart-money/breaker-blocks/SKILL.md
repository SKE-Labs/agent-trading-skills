---
name: breaker-blocks
description: Define and test breaker-block polarity-flip setups. Use when a previously labeled candle zone is crossed and later retested as support or resistance.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Breaker Blocks Trading

A discretionary label for a candle zone that is crossed and later tested from the opposite side. It is a support/resistance hypothesis, not evidence of trapped or institutional orders.

## Identification

### Bullish Breaker (Failed Bearish OB)
1. Bearish order block forms
2. Price returns and breaks **through** the OB aggressively (displacement)
3. The broken OB flips to support (bullish breaker)
4. Trade longs when price returns to this zone

### Bearish Breaker (Failed Bullish OB)
1. Bullish order block forms
2. Price returns and breaks **through** the OB aggressively (displacement)
3. The broken OB flips to resistance (bearish breaker)
4. Trade shorts when price returns to this zone

### Testable Features

- Normalize break distance and speed by ATR and elapsed bars.
- Define the zone from exact OHLC fields and an objective swing rule.
- Record overlap with an FVG, higher-timeframe state, and retest count as candidate features—not quality grades.
- Use a closed-bar crossing buffer and prevent future bars from changing the original label.

## Workflow

1. **Find a failed order block** using candle data:
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)
   ```
2. **Confirm the break** with the predeclared swing and close-plus-buffer rule
3. **Mark the breaker zone** using `draw_chart_analysis` with `demand` (bullish) or `supply` (bearish)
4. **Wait for price to return** to the zone from the opposite side
5. **Enter with LTF confirmation** (structure shift or rejection)
6. **Stop loss** beyond the breaker zone
7. **Target** next liquidity level or POI

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: Treat breaker blocks as a discretionary support/resistance labeling convention. [Lo, Mamaysky & Wang](https://www.nber.org/papers/w7613) supports objective pattern testing, not claims about hidden institutional intent.

## Key Rules

- Do not claim knowledge of trapped traders or hidden order intent from candles alone.
- Define displacement in ATR and bars before testing.
- Test first and later retests separately rather than assuming only the first works.
- Return `no trade` when swing, break, retest, liquidity, or cost definitions are incomplete.

## Related Skills

- **order-blocks** — Breakers are failed OBs; understanding OBs is prerequisite
- **fair-value-gaps** — FVGs created during the break add confluence to breaker zones
