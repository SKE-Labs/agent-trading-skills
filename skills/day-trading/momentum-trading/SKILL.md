---
name: momentum-trading
description: Trade strong directional price moves with momentum confirmation. Use when riding breakouts, trading trend continuation, or capitalizing on news-driven moves.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending"]
---

# Momentum Trading

Momentum trading capitalizes on strong directional price moves, entering when momentum is confirmed.

## Regime Filter (Critical)

Momentum strategies only work in trending markets. Always check regime first:

```
get_indicator(indicator="adx")
```

| ADX Value | Momentum Trading? |
| --- | --- |
| >30 | **Yes** — ideal conditions, strong trend |
| 25-30 | **Yes** — moderate trend, standard size |
| 20-25 | **Caution** — weak trend, reduced size only |
| <20 | **No** — ranging market, skip momentum |

If ADX <20, do NOT take momentum trades. Use range-trading or mean-reversion instead. Reference **market-regime-detection** skill for full regime assessment.

## Momentum Identification

### Indicators

```
get_indicator(indicator="rsi")
get_indicator(indicator="macd")
get_indicator(indicator="volume")
get_indicator(indicator="adx")
```

- RSI breaking above 50 (bullish) or below 50 (bearish)
- MACD histogram expanding (consecutive bars growing)
- Volume surge (1.5x+ average)
- ADX >25 and rising
- Candle size increasing

### Price Action

- Higher highs/higher lows accelerating
- Breaking through resistance/support
- Gap openings in direction

## Entry Strategies

### 1. Breakout Momentum

1. Identify consolidation/resistance
2. Wait for breakout with volume
3. Enter on breakout candle close
4. Stop below breakout level

### 2. Retracement Momentum

1. Identify strong momentum move
2. Wait for shallow pullback (38-50%)
3. Enter on pullback completion
4. Stop below pullback low

### 3. Momentum Continuation

1. Already in trend
2. Momentum indicator confirms continuation
3. Add to position or re-enter
4. Trail stops

## Exit Rules

### Take Profit When:

- Momentum indicator diverges
- Volume decreases significantly
- Price reaches resistance
- R:R target achieved

### Stop Loss When:

- Momentum reverses
- Structure breaks
- Pre-defined stop hit

## Best Settings

| Indicator | Settings | Signal              |
| --------- | -------- | ------------------- |
| RSI       | 14       | Cross 50            |
| MACD      | 12,26,9  | Histogram expanding |
| Volume    | 20 MA    | 2x+ average         |

## Workflow

1. **Screen for momentum** (stocks/crypto making moves)
2. **Confirm with volume** (must be above average)
3. **Wait for entry** (breakout or pullback)
4. **Manage position** (trail stops, scale out)
5. **Exit on exhaustion**

## Momentum Decay and Exhaustion

### Signal Duration

Momentum signals have a limited lifespan:

| Indicator | Typical Signal Duration | Watch For |
| --- | --- | --- |
| RSI momentum (cross 50) | 5-8 candles | RSI returning toward 50 |
| MACD histogram expansion | 10-15 candles | Histogram shrinking |
| Volume spike | 3-5 candles | Volume returning to average |
| ADX rise | 15-25 candles | ADX rolling over |

### Exhaustion Detection

Momentum is ending when:

| Signal | Meaning |
| --- | --- |
| Volume declining while price advancing | Smart money exiting, retail chasing |
| MACD histogram shrinking | Momentum decelerating |
| RSI divergence (price HH, RSI LH) | Bearish divergence — reversal warning |
| Candles getting smaller with long wicks | Indecision, buyers/sellers fighting |
| ADX turning down from >40 | Strong trend weakening |

When 2+ exhaustion signals appear, tighten stops or take partial profits.

## Enhanced Workflow

### 1. Check Regime

```
get_indicator(indicator="adx")
```

ADX must be >25. If <20, report to orchestrator that momentum conditions don't exist.

### 2. Confirm Momentum

```
get_indicator(indicator="rsi")
get_indicator(indicator="macd")
get_indicator(indicator="volume")
```

All three should confirm: RSI trending from 50 toward extreme, MACD expanding, volume above average.

### 3. Get Price Data

```
get_candles_around_date(symbol="BTCUSD", interval="1h", date="2026-03-19")
```

Check for accelerating candle sizes and structure (HH/HL for bullish).

### 4. Generate Chart

```
generate_chart(symbol="BTCUSD", interval="1h")
```

### 5. Mark Entry Zone

```
draw_chart_analysis(action="create", drawing={
    "type": "demand",
    "points": [
        {"time": <pullback_start>, "price": <pullback_high>},
        {"time": <pullback_end>, "price": <pullback_low>}
    ],
    "options": {"text": "Momentum Pullback Entry (38-50%)"}
})
```

### 6. Report to Orchestrator

- **Regime confirmation**: ADX value, trend direction
- **Momentum strength**: RSI level, MACD histogram size, volume multiple
- **Entry type**: Breakout or pullback entry
- **Exhaustion signals**: Any early warning signs
- **Decay estimate**: How many candles of momentum likely remain
- **Stop and target**: Based on structure + momentum indicators

## Best Practices

| Do | Don't |
| --- | --- |
| Check ADX >25 before every momentum trade | Trade momentum in ranging markets |
| Enter on pullbacks (38-50% retrace) | Chase extended moves at extremes |
| Monitor exhaustion signals actively | Hold blindly through reversal |
| Take partial profit when signals decay | Wait for "one more high" |
| Use volume as primary confirmation | Enter on price alone |

## Common Mistakes

- **Chasing extended moves** — Entering after a large move when momentum is already decaying. Best entries are pullbacks within the trend.
- **Trading momentum in ranges (ADX <20)** — Momentum signals whipsaw constantly in sideways markets. ADX filter is non-negotiable.
- **Entering without volume confirmation** — Price can move on low volume temporarily. Real momentum requires above-average volume.
- **Fighting the momentum direction** — "It's overextended, it must reverse" is not a strategy. Trend persistence is more common than reversal.
- **Holding through momentum reversal** — When MACD shrinks + volume drops + candles get smaller = exit. Don't wait for the full reversal to confirm.

## Related Skills

- **market-regime-detection** — ADX must confirm trending regime (>25) before taking momentum trades
- **breakout-trading** — Breakout momentum is a primary entry type; breakout-trading provides the consolidation identification framework
- **pullback-trading** — Retracement momentum entries use pullback-trading principles for timing within the trend
