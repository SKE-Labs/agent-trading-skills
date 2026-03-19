---
name: market-regime-detection
description: Identify current market regime (trending, ranging, or volatile) to select appropriate trading strategies. Use when starting any analysis, when conditions seem uncertain, or when existing strategies are underperforming.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending", "ranging", "volatile"]
---

# Market Regime Detection

Markets cycle between distinct regimes. Strategies that work in trending markets fail in ranges, and vice versa. Detecting the current regime is the first step before applying any other skill.

## Regime Types

| Regime | Characteristics | ADX | BB Width | Price Action |
| --- | --- | --- | --- | --- |
| **Trending Up** | HH + HL, price above MAs | >25 | Expanding | Strong directional candles |
| **Trending Down** | LH + LL, price below MAs | >25 | Expanding | Strong directional candles |
| **Ranging** | No clear HH/LL, price oscillates around MAs | <20 | Narrow | Dojis, small bodies, wicks |
| **Volatile** | Large swings both directions, whipsaws | 20-25 | Very wide | Large candles, frequent reversals |

## Detection Methods

### 1. ADX (Average Directional Index)

Primary regime classifier:

| ADX Value | Regime | Confidence |
| --- | --- | --- |
| >40 | Strong trend | High |
| 25-40 | Moderate trend | Medium |
| 20-25 | Weak/transitioning | Low — wait for clarity |
| <20 | Ranging | High |

Use `get_indicator(indicator_code="dmi")` to retrieve current DMI/ADX values.

### 2. Bollinger Band Width

Measures volatility expansion/contraction:

| BB Width Percentile (vs 100 periods) | Regime Signal |
| --- | --- |
| >80th percentile | High volatility — trending or volatile |
| 40th-80th percentile | Normal conditions |
| <20th percentile | Squeeze — breakout imminent |

Use `get_indicator(indicator_code="bbands")` to get upper, middle, lower bands. Calculate width:

```
BB Width = (Upper - Lower) / Middle × 100
```

### 3. ATR Percentile

Confirms volatility level:

| ATR vs 20-period SMA of ATR | Signal |
| --- | --- |
| ATR > 1.5× avg | Elevated volatility |
| ATR 0.8-1.2× avg | Normal |
| ATR < 0.8× avg | Low volatility (squeeze) |

Use `get_indicator(indicator_code="tr")` for current True Range.

### 4. EMA Slope

Trend direction and strength:

- **50 EMA rising + price above** → Bullish trend
- **50 EMA falling + price below** → Bearish trend
- **50 EMA flat + price crossing repeatedly** → Range

Use `get_indicator(indicator_code="ema")` and compare recent values.

## Composite Regime Classification

Combine all four methods for highest accuracy:

| ADX | BB Width | ATR | EMA Slope | → Regime |
| --- | --- | --- | --- | --- |
| >25 | Expanding | Above avg | Sloping | **Trending** |
| <20 | Narrow | Below avg | Flat | **Ranging** |
| 20-25 | Very wide | >1.5× avg | Choppy | **Volatile** |
| <20 | Very narrow (<20th pctl) | Very low | Flat | **Squeeze** (breakout coming) |

**Decision rules:**
- If 3/4 indicators agree → **High confidence** regime classification
- If 2/4 agree → **Medium confidence** — reduce position size, use conservative entries
- If split → **No trade** — wait for clarity

## Regime Change Detection

Watch for transitions:

| Signal | Meaning |
| --- | --- |
| ADX crosses above 25 from below | Range → Trend beginning |
| ADX crosses below 20 from above | Trend → Range beginning |
| BB Width expands >50% in 5 periods | Breakout/volatility spike |
| BB Width contracts to <20th percentile | Squeeze forming — breakout imminent |
| EMA slope reverses direction | Potential trend reversal |

## Strategy Selection Matrix

| Regime | Use These Skills | Avoid These Skills |
| --- | --- | --- |
| **Trending Up** | moving-average-crossover, pullback-trading, momentum-trading, fibonacci-trading, flag-pennant, breakout-trading | mean-reversion, range-trading |
| **Trending Down** | moving-average-crossover, pullback-trading (short), fibonacci-trading, flag-pennant | range-trading, dca-strategy (wait) |
| **Ranging** | range-trading, mean-reversion, bollinger-bands, supply-demand-zones, double-top-bottom | momentum-trading, breakout-trading, moving-average-crossover |
| **Volatile** | scalping-strategy (reduced size), stop-loss-strategies (wider), position-sizing (smaller) | All trend-following, all mean-reversion |
| **Squeeze** | breakout-trading (prepare), triangle-patterns, wedge-patterns | range-trading (range about to break) |

## Workflow

### 1. Get ADX Reading

```
get_indicator(indicator_code="dmi")
```

Check the ADX value. If >25 → trending. If <20 → ranging.

### 2. Get Bollinger Bands

```
get_indicator(indicator_code="bbands")
```

Calculate BB Width = (upper - lower) / middle × 100. Compare to recent readings to determine percentile.

### 3. Get ATR

```
get_indicator(indicator_code="tr")
```

Compare current ATR to the average of recent ATR values.

### 4. Get EMA for Slope

```
get_indicator(indicator_code="ema")
```

Compare the last 5-10 EMA values. Rising = bullish trend, falling = bearish trend, flat = range.

### 5. Classify and Visualize

Use `draw_chart_analysis` to highlight the current regime on chart:

```
draw_chart_analysis(action="create", drawing={
    "type": "highlight",
    "points": [
        {"time": <regime_start_timestamp>, "price": <candle_high>},
        {"time": <current_timestamp>, "price": <candle_low>}
    ],
    "options": {"text": "TRENDING (ADX: 32)"}
})
```

### 6. Report Regime to Orchestrator

Summarize findings:
- **Current regime** and confidence level
- **Key metrics**: ADX value, BB width percentile, ATR relative to average
- **Recommended skills** to apply
- **Skills to avoid** in current conditions
- **Transition signals** to watch for

## Best Practices

| Do | Don't |
| --- | --- |
| Check regime before every analysis | Assume yesterday's regime holds today |
| Use multiple indicators for confirmation | Rely on ADX alone |
| Reduce size during transitions (ADX 20-25) | Force trades in unclear regimes |
| Re-check regime on higher timeframes | Only check one timeframe |
| Note regime at start of every analysis | Skip straight to pattern/indicator analysis |

## Common Mistakes

- **Trading trend strategies in a range** — Moving average crossovers generate constant whipsaws in ranging markets. Check ADX first.
- **Ignoring regime transitions** — The ADX 20-25 zone is a no-man's land. Wait for clarity rather than guessing.
- **Using single indicator** — ADX can lag. Combine with BB width and ATR for earlier detection.
- **Not adapting position size** — Even correct regime classification needs smaller size during volatile or transitioning periods.

## Related Skills

- **multi-timeframe-analysis** — Regime detection on HTF sets the context; MTF analysis refines entries within the regime
- **bollinger-bands** — BB Width is a key regime detection input and Bollinger strategies adapt to the detected regime
- **momentum-trading** — Only applicable when regime is trending (ADX >25); regime detection gates momentum setups
