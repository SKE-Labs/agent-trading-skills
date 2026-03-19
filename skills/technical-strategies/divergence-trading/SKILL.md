---
name: divergence-trading
description: Identify regular and hidden divergences across RSI, MACD, Stochastic, and OBV for reversal and continuation signals. Use when price makes new highs/lows but indicators disagree, or when confirming trend exhaustion.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending", "ranging"]
---

# Divergence Trading

Divergence occurs when price and an indicator move in opposite directions — a powerful early warning of trend change or continuation.

## Divergence Types

### Regular Divergence (Reversal Signal)

| Type | Price Action | Indicator Action | Signal |
| --- | --- | --- | --- |
| **Bullish Regular** | Lower Low (LL) | Higher Low (HL) | Bearish momentum weakening → potential reversal up |
| **Bearish Regular** | Higher High (HH) | Lower High (LH) | Bullish momentum weakening → potential reversal down |

### Hidden Divergence (Continuation Signal)

| Type | Price Action | Indicator Action | Signal |
| --- | --- | --- | --- |
| **Bullish Hidden** | Higher Low (HL) | Lower Low (LL) | Uptrend pullback ending → continuation up |
| **Bearish Hidden** | Lower High (LH) | Higher High (HH) | Downtrend rally ending → continuation down |

## Multi-Indicator Divergence

### RSI Divergence

Best for identifying overbought/oversold exhaustion:

```
get_indicator(indicator="rsi")
```

| Setup | RSI Zone | Reliability |
| --- | --- | --- |
| Bullish regular div at RSI <30 | Oversold | High |
| Bearish regular div at RSI >70 | Overbought | High |
| Bullish regular div at RSI 30-50 | Neutral | Medium |
| Hidden div in any zone | — | Medium-High |

### MACD Divergence

Best for identifying momentum shifts:

```
get_indicator(indicator="macd")
```

Compare MACD histogram peaks/troughs with price peaks/troughs:
- Histogram shrinking while price extends → momentum fading
- MACD line diverging from price → stronger signal than histogram alone

### Stochastic Divergence

Best for ranging markets and extreme zones:

```
get_indicator(indicator="stoch")
```

| Setup | Stochastic Zone | Reliability |
| --- | --- | --- |
| Bullish div at %K <20 | Oversold | High |
| Bearish div at %K >80 | Overbought | High |
| Div in mid-range (20-80) | Neutral | Low — skip |

### OBV (On-Balance Volume) Divergence

Confirms whether volume supports the price move:

```
get_indicator(indicator="obv")
```

- Price making new highs but OBV declining → Distribution (smart money selling)
- Price making new lows but OBV rising → Accumulation (smart money buying)

## Strength Scoring

More indicators diverging = stronger signal:

| Indicators Diverging | Strength | Action |
| --- | --- | --- |
| 1 indicator | Weak | Note but don't trade alone |
| 2 indicators | Moderate | Trade with confirmation candle + S/R |
| 3+ indicators | Strong | High-probability setup, trade with confidence |

### Example Scoring

```
RSI shows bullish divergence:     +1
MACD histogram shows divergence:  +1
OBV also diverging:               +1
At key support level:             +1 (bonus)
→ Total: 4/4 = Very Strong Signal
```

## Identification Rules

### Minimum Requirements for Valid Divergence

| Requirement | Value | Why |
| --- | --- | --- |
| Min candles between peaks/troughs | 5 | Fewer is noise, not divergence |
| Max candles between peaks/troughs | 50 | Too far apart = weak connection |
| RSI must be in extreme zone | <30 or >70 | Mid-range divergence is unreliable |
| Price swing must be clear | Visible on chart | Micro-swings don't count |

### False Divergence Filters

Avoid false signals by checking:

1. **Minimum separation**: At least 5 candles between the two comparison points
2. **Extreme zones**: RSI/Stochastic should be in overbought/oversold territory for regular divergence
3. **Clear swings**: Both price swings must be obvious, not hidden in noise
4. **Timeframe**: Higher timeframe divergence is far more reliable than LTF
5. **No crossing**: If RSI crosses 50 between the two points, the divergence is invalidated

## Entry Strategy

1. **Identify divergence** on primary timeframe using at least 2 indicators
2. **Confirm at key level**: Divergence at S/R, order block, or Fibonacci level = highest probability
3. **Wait for confirmation candle**: Engulfing, hammer, or pin bar at the divergence zone
4. **Enter on confirmation candle close** (conservative) or on next candle open (aggressive)
5. **Stop loss**: Beyond the most recent swing (the second point of divergence)
6. **Target**: Previous swing high/low (regular div) or trend continuation target (hidden div)

## Workflow

### 1. Get Indicator Data

```
get_indicator(indicator="rsi")
get_indicator(indicator="macd")
get_indicator(indicator="stoch")
```

### 2. Compare Price and Indicator Swings

For each indicator:
- Identify the last two significant peaks (for bearish divergence) or troughs (for bullish)
- Compare price direction vs indicator direction
- Note if divergence exists and in which zone

### 3. Score the Divergence

Count how many indicators show divergence (1-4 scale). Check if at key level for bonus point.

### 4. Get Historical Data for Drawing

```
get_candles_around_date(symbol="BTCUSD", interval="4h", date="2026-03-15")
```

### 5. Mark Divergence on Chart

Use `draw_chart_analysis` to draw trend lines showing the divergence:

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

### 6. Report to Orchestrator

- **Divergence type**: Regular or hidden, bullish or bearish
- **Indicators involved**: Which indicators and their values
- **Strength score**: X/4
- **Key level confluence**: What S/R level coincides
- **Entry zone**: Where to enter and confirmation needed
- **Stop and target levels**: Based on swing structure

## Best Practices

| Do | Don't |
| --- | --- |
| Use 2+ indicators for confirmation | Trade single-indicator divergence |
| Look for divergence at key S/R levels | Trade divergence in the middle of nowhere |
| Wait for confirmation candle | Enter the moment you spot divergence |
| Higher TF divergence > Lower TF | Over-rely on 5m divergence |
| Check minimum 5-candle separation | Count every tiny swing as divergence |

## Common Mistakes

- **Trading single-indicator divergence** — One indicator diverging is a note, not a trade. Require 2+ for entries.
- **Mid-range RSI divergence** — RSI at 45 vs 50 is not meaningful divergence. Require extreme zones (<30 or >70) for regular divergence.
- **Micro-timeframe divergence** — 1m divergence is noise. Use 1H+ for reliable signals.
- **No confirmation candle** — Divergence is an early warning, not an entry signal. Always wait for price confirmation.
- **Fighting strong trends** — Divergence can persist for extended periods in strong trends. Use hidden divergence (continuation) in trends, regular divergence only at extremes.

## Related Skills

- **rsi-divergence** — Focused RSI divergence framework; divergence-trading extends it to multiple indicators
- **macd-trading** — MACD histogram divergence is one of the four indicators in the multi-indicator scoring
- **mean-reversion** — Divergence at BB extremes confirms mean reversion setups with high probability
