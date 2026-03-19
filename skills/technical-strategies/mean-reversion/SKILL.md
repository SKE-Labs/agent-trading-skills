---
name: mean-reversion
description: Trade price extremes back toward the statistical mean using z-scores, Bollinger Bands, and RSI. Use when price is overextended from its average in ranging markets, or when identifying exhaustion at extremes.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["ranging"]
---

# Mean Reversion

Price tends to revert to its statistical mean after moving to extremes. Mean reversion strategies profit from this tendency — buying oversold conditions and selling overbought ones.

**Critical**: Mean reversion only works in ranging markets. In trending markets, "oversold" keeps getting more oversold. Always check regime first using **market-regime-detection** (ADX must be <25).

## Detection Methods

### 1. Z-Score Method

Measures how many standard deviations price is from the mean:

```
Z-Score = (Price - SMA) / Standard Deviation
```

| Z-Score | Condition | Signal |
| --- | --- | --- |
| > +2.0 | Strongly overbought | Sell / short (mean reversion) |
| +1.0 to +2.0 | Moderately overbought | Watch for reversal |
| -1.0 to +1.0 | Normal range | No signal |
| -1.0 to -2.0 | Moderately oversold | Watch for reversal |
| < -2.0 | Strongly oversold | Buy / long (mean reversion) |

**Entry rule**: Enter at Z-Score > |2.0|, target Z-Score = 0 (the mean).

### 2. Bollinger Band Method

Bollinger Bands (20 SMA ± 2 StdDev) provide visual mean reversion levels:

```
get_indicator(indicator_code="bbands")
```

| Price Position | Signal |
| --- | --- |
| Touches/pierces lower band + reversal candle | Buy toward middle band (SMA) |
| Touches/pierces upper band + reversal candle | Sell toward middle band (SMA) |
| Inside bands near middle | No signal |

**Confirmation**: Band touch + RSI extreme + reversal candle = high probability.

### 3. RSI Extreme Method

```
get_indicator(indicator_code="rsi")
```

| RSI Level | Signal |
| --- | --- |
| RSI < 25 | Deeply oversold → buy |
| RSI 25-30 | Oversold → watch for confirmation |
| RSI 70-75 | Overbought → watch for confirmation |
| RSI > 75 | Deeply overbought → sell |

**Key**: Use 25/75 (not 30/70) for mean reversion to filter weaker signals.

## Regime Filter (Critical)

**Before any mean reversion trade**, verify the market is ranging:

```
get_indicator(indicator_code="dmi")
```

| ADX Value | Mean Reversion? |
| --- | --- |
| < 20 | **Yes** — ideal conditions |
| 20-25 | **Caution** — reduced size only |
| > 25 | **No** — trending market, skip mean reversion |

If ADX > 25, do NOT take mean reversion trades. Use trending strategies instead (momentum-trading, pullback-trading).

## Entry Strategy

### Setup Requirements (All Must Be Met)

1. **Regime check**: ADX < 25 (ranging market)
2. **Extreme reading**: Z-Score > |2.0| OR RSI < 25/>75 OR BB touch
3. **Confirmation candle**: Reversal candle at extreme (engulfing, hammer, doji)
4. **No upcoming high-impact events**: Check that no FOMC/NFP/CPI within 24h

### Entry Execution

1. **Identify extreme** via BB + RSI + Z-Score
2. **Wait for confirmation candle** at extreme
3. **Enter on confirmation candle close** toward the mean
4. **Stop loss**: Beyond the extreme (below lower BB for longs, above upper BB for shorts)
5. **Target**: Middle band (SMA 20) for conservative, opposite band for aggressive

### Target Setting

| Target | Level | Win Rate (est.) |
| --- | --- | --- |
| Conservative | Middle band (20 SMA) | ~65% |
| Standard | 75% of range to middle | ~55% |
| Aggressive | Opposite band | ~35% |

**Recommended**: Take partial profit at middle band, trail remainder.

## Workflow

### 1. Check Regime

```
get_indicator(indicator_code="dmi")
```

If ADX > 25 → **Stop**. This is a trending market. Report to orchestrator that mean reversion is not applicable.

### 2. Assess Bollinger Bands

```
get_indicator(indicator_code="bbands")
```

Check if price is at or beyond bands. Calculate Band Width for squeeze detection.

### 3. Check RSI

```
get_indicator(indicator_code="rsi")
```

Is RSI at extreme (<25 or >75)? Align with BB reading.

### 4. Check EMA for Mean Level

```
get_indicator(indicator_code="ema")
```

This is the target — the mean price is reverting toward.

### 5. Get Historical Data

```
get_candles_around_date(symbol="BTCUSD", interval="4h", date="2026-03-19")
```

Check for confirmation candle at the extreme.

### 6. Mark Setup on Chart

```
draw_chart_analysis(action="create", drawing={
    "type": "demand",
    "points": [
        {"time": <extreme_time>, "price": <lower_bb>},
        {"time": <current_time>, "price": <entry_zone>}
    ],
    "options": {"text": "Mean Reversion Buy (RSI: 22, Z: -2.3)"}
})
```

### 7. Report to Orchestrator

- **Regime confirmation**: ADX value and ranging classification
- **Extreme readings**: Z-Score, RSI, BB position
- **Confirmation**: Candle pattern at extreme
- **Entry zone**: Price level for entry
- **Target**: Middle band / mean level
- **Stop**: Beyond the extreme
- **Confidence**: Number of confirming signals (BB + RSI + Z-Score = 3/3 high)

## Best Practices

| Do | Don't |
| --- | --- |
| Always check ADX < 25 before trading | Use mean reversion in trending markets |
| Require 2+ confirming signals | Trade on BB touch alone |
| Wait for confirmation candle | Enter the instant price touches BB |
| Take profit at the mean (SMA) | Hold for opposite band every time |
| Use the 20 SMA as the "mean" target | Target arbitrary levels |
| Combine with volume profile (VAL/VAH) | Ignore volume context |

## Common Mistakes

- **Mean reversion in trends** — The #1 killer. "Oversold" in a downtrend means it will probably get more oversold. ADX must be <25.
- **No confirmation candle** — A BB touch is necessary but not sufficient. Wait for the reversal candle.
- **Holding for opposite band** — Mean (middle band) is the realistic target. Opposite band is a bonus, not the plan.
- **Ignoring squeeze signals** — When BB Width contracts to <20th percentile, a breakout is coming. Mean reversion will fail when the range breaks.
- **Fighting fundamentals** — If a stock is at lower BB because of terrible earnings, it's not "oversold" — it's repricing. Mean reversion is for oscillation, not fundamental repricing.

## Related Skills

- **bollinger-bands** — BB touches are the primary visual mean reversion signal; this skill adds z-score and RSI frameworks
- **market-regime-detection** — ADX must confirm ranging market (ADX <25) before any mean reversion trade
- **range-trading** — Mean reversion works within ranges; range-trading provides boundary identification
