---
name: divergence-trading
description: Identify regular and hidden divergences across RSI, MACD, Stochastic, and OBV for reversal and continuation signals. Use when price makes new highs/lows but indicators disagree, or when confirming trend exhaustion.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Divergence Trading

Divergence occurs when price and an indicator move in opposite directions, signaling potential trend change or continuation.

## Divergence Types

### Regular Divergence (Reversal)

| Type | Price | Indicator | Signal |
| --- | --- | --- | --- |
| **Bullish Regular** | Lower Low | Higher Low | Momentum weakening, potential reversal up |
| **Bearish Regular** | Higher High | Lower High | Momentum weakening, potential reversal down |

### Hidden Divergence (Continuation)

| Type | Price | Indicator | Signal |
| --- | --- | --- | --- |
| **Bullish Hidden** | Higher Low | Lower Low | Uptrend pullback ending, continuation up |
| **Bearish Hidden** | Lower High | Higher High | Downtrend rally ending, continuation down |

## Multi-Indicator Detection

| Indicator | Best For | Extreme Zone |
| --- | --- | --- |
| RSI | OB/OS exhaustion | <30 or >70 for regular div |
| MACD histogram | Momentum shifts | Compare histogram peaks/troughs with price |
| Stochastic | Ranging markets | <20 or >80 (skip mid-range div) |
| MFI (volume proxy) | Smart money confirmation | Rising MFI + falling price = accumulation |

**Strength**: 1 indicator diverging = note only. 2 = trade with confirmation. 3+ = high probability.

## Validation Rules

- Minimum **5 candles** between comparison points (fewer is noise)
- Maximum **50 candles** between comparison points (too far = weak)
- RSI must be in extreme zone (<30 or >70) for regular divergence
- If RSI crosses 50 between the two points, divergence is invalidated
- Both price swings must be visually clear, not micro-swings

## Workflow

1. **Get indicator data**:
   ```
   get_indicator(indicator_code="rsi", symbol=<symbol>, interval=<interval>)
   get_indicator(indicator_code="macd", symbol=<symbol>, interval=<interval>)
   get_indicator(indicator_code="stoch", symbol=<symbol>, interval=<interval>)
   ```

2. **Compare swings**: For each indicator, identify last two significant peaks/troughs and compare direction vs price direction

3. **Score**: Count diverging indicators (1-3). Check if at key S/R level for bonus confluence.

4. **Get candles for chart drawing**:
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```

5. **Mark divergence on chart**:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "trend",
       "points": [
           {"time": <first_low_time>, "price": <first_low_price>},
           {"time": <second_low_time>, "price": <second_low_price>}
       ],
       "options": {"text": "Bullish Divergence (RSI + MACD)"}
   })
   ```

6. **Wait for confirmation candle** (engulfing, hammer, pin bar) at the divergence zone before entry

## Key Rules

- NEVER trade single-indicator divergence alone; require 2+ indicators
- NEVER trade mid-range RSI divergence (RSI 40-60 is meaningless)
- NEVER enter without a confirmation candle; divergence is a warning, not an entry
- Higher timeframe divergence is far more reliable than LTF; use 1H+ minimum
- Divergence can persist in strong trends; use hidden divergence (continuation) in trends, regular divergence only at extremes
- Entry on confirmation candle close; stop beyond the second divergence swing point

## Related Skills

- **rsi-divergence** — focused RSI divergence framework; this skill extends it to multiple indicators
- **macd-trading** — MACD histogram divergence is one of the four indicators in multi-indicator scoring
