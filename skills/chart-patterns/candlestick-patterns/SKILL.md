---
name: candlestick-patterns
description: Define and test objective candlestick geometry. Use when labeling OHLC patterns, comparing body/wick rules, or evaluating a closed-bar entry with context and cost controls.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Candlestick Pattern Trading

Candlestick patterns are compact OHLC descriptions. Use them to define observable bar geometry, not to infer psychology or direction by themselves.

## Pattern Identification

### Single-Candle Reversals
- **Hammer / Hanging Man** — Small body, long lower wick (2x+ body). Hammer at support = bullish; Hanging Man at resistance = bearish.
- **Inverted Hammer / Shooting Star** — Small body, long upper wick (2x+ body). Inverted Hammer at support = bullish; Shooting Star at resistance = bearish.
- **Doji** — Open ≈ Close (tiny body). Indecision; reversal signal at extremes.

### Multi-Candle Reversals
- **Engulfing** — Bullish: current real body contains the prior real body and closes up. Bearish: mirror it. State explicitly whether wicks must also be engulfed.
- **Piercing Line / Dark Cloud Cover** — Second candle opens gap, closes 50%+ into prior candle.
- **Morning Star / Evening Star** — 3-candle: large, small/doji, large opposite direction.

### Continuation
- **Three White Soldiers / Three Black Crows** — Three consecutive strong candles closing progressively higher/lower.

Normalize definitions before scanning: express body and wick sizes as fractions of the candle range or ATR, set the doji tolerance, and use only completed candles. Do not rank patterns until the ranking has been tested on the target market.

## Workflow

### 1. Identify Key Level

Use `get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval=<interval>, date=<date>)` to find S/R levels from price action (swing highs/lows, prior rejection zones).

### 2. Confirm Pattern at Level

Wait for a candlestick pattern to form at the key level. Confirm:
- Direction matches HTF bias
- Volume context via `get_indicators(indicator_code="mfi", symbol=<symbol>, exchange=<exchange>, interval=<interval>)`

### 3. Mark Key Candles

```
draw_chart_analysis(action="create", drawing={
    "type": "highlight",
    "points": [{"time": <pattern_candle_time>, "price": <pattern_candle_high>}],
    "options": {"text": "Engulfing"}
})
```

### 4. Enter

Enter on next candle open or break of pattern extreme. Stop beyond pattern's extreme wick. Target the next key S/R level.

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Marshall, Young & Rose](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=980583) found candlestick rules were not generally profitable on large U.S. stocks, so use patterns as contextual features rather than standalone signals.

## Key Rules
- Treat a pattern as a feature and compare it with a price-only baseline.
- Test higher-timeframe state and nearby levels for incremental value rather than requiring them universally.
- A doji is geometry, not direction; define any adjacent-bar trigger in advance.
- HTF patterns carry far more weight than LTF
- Keep real-body engulfing and full-range engulfing as separate, predeclared variants
- Morning/Evening Stars require 3rd candle to close beyond midpoint of 1st candle

## Related Skills
- **multi-timeframe-analysis** — HTF patterns far more reliable
- **supply-demand-zones** — test overlap with objectively defined candle zones
