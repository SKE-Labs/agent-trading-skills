---
name: momentum-trading
description: Trade strong directional price moves with momentum confirmation. Use when riding breakouts, trading trend continuation, or capitalizing on news-driven moves.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Momentum Trading

Enter confirmed directional moves and ride them until momentum decays.

## Setup Conditions

### Regime Filter (Required)

```
get_indicator(indicator_code="dmi", symbol=<symbol>, interval=<interval>)
```

| ADX Value | Action |
| --- | --- |
| >30 | Ideal -- full size |
| 25-30 | Valid -- standard size |
| 20-25 | Weak -- reduced size only |
| <20 | Skip -- use range-trading instead |

### Exhaustion Signals (Exit when 2+ appear)

- Volume declining while price advancing
- MACD histogram shrinking
- RSI divergence (price HH, RSI LH)
- Candles smaller with long wicks
- ADX turning down from >40

## Workflow

### 1. Check Regime

```
get_indicator(indicator_code="dmi", symbol=<symbol>, interval=<interval>)
```

ADX must be >25. If <20, report to orchestrator that momentum conditions do not exist.

### 2. Get Price Data and Confirm Momentum

```
get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
get_indicator(indicator_code="rsi", symbol=<symbol>, interval=<interval>)
get_indicator(indicator_code="macd", symbol=<symbol>, interval=<interval>)
get_indicator(indicator_code="mfi", symbol=<symbol>, interval=<interval>)
```

All three must align: RSI trending from 50 toward extreme, MACD histogram expanding, volume above average. Check for accelerating candle sizes and HH/HL (bullish) or LH/LL (bearish) structure.

### 3. Entry

**Breakout**: Enter on breakout candle close, stop below breakout level. **Pullback**: Wait for 38-50% retracement, enter on completion, stop below pullback low.

### 4. Report to Orchestrator

ADX value and trend direction, RSI/MACD/volume readings, entry type, exhaustion signals, stop and target levels.

## Key Rules

- NEVER take momentum trades when ADX < 20 -- signals whipsaw in ranging markets
- NEVER enter without volume confirmation -- price can move on low volume temporarily but real momentum requires above-average volume
- NEVER chase extended moves at extremes -- best entries are pullbacks within the trend
- NEVER hold through momentum reversal (MACD shrinking + volume dropping + smaller candles = exit)
- NEVER fight momentum direction -- trend persistence is more common than reversal

## Related Skills

- **breakout-trading** -- breakout momentum is a primary entry type
- **pullback-trading** -- retracement entries use pullback principles for timing
