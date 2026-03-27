---
name: market-regime-detection
description: Identify current market regime (trending, ranging, or volatile) to select appropriate trading strategies. Use when starting any analysis, when conditions seem uncertain, or when existing strategies are underperforming.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Market Regime Detection

Markets cycle between distinct regimes. Detecting the current regime is the first step before applying any other skill.

## Regime Types

| Regime | ADX | BB Width | Price Action |
| --- | --- | --- | --- |
| **Trending Up** | >25 | Expanding | HH + HL, strong directional candles |
| **Trending Down** | >25 | Expanding | LH + LL, strong directional candles |
| **Ranging** | <20 | Narrow | Oscillates around MAs, dojis, small bodies |
| **Volatile** | 20-25 | Very wide | Large swings both directions, whipsaws |

## Detection Methods

**ADX** (primary): >40 strong trend, 25-40 moderate trend, 20-25 transitioning (wait), <20 ranging.

**BB Width** = `(Upper - Lower) / Middle * 100`: >80th percentile = high vol, <20th = squeeze imminent.

**ATR Ratio**: ATR > 1.5x avg = elevated vol, 0.8-1.2x = normal, <0.8x = squeeze.

**EMA Slope**: 50 EMA rising + price above = bullish; falling + price below = bearish; flat + crossing = range.

## Composite Classification

| ADX | BB Width | ATR | EMA Slope | Regime |
| --- | --- | --- | --- | --- |
| >25 | Expanding | Above avg | Sloping | **Trending** |
| <20 | Narrow | Below avg | Flat | **Ranging** |
| 20-25 | Very wide | >1.5x avg | Choppy | **Volatile** |
| <20 | Very narrow | Very low | Flat | **Squeeze** (breakout coming) |

- 3/4 agree → **high confidence**. 2/4 → **medium**, reduce size. Split → **no trade**.

## Regime Change Signals

| Signal | Meaning |
| --- | --- |
| ADX crosses above 25 | Range → trend beginning |
| ADX crosses below 20 | Trend → range beginning |
| BB Width expands >50% in 5 periods | Breakout/volatility spike |
| BB Width contracts to <20th pctl | Squeeze forming |

## Strategy Selection Matrix

| Regime | Use These Skills | Avoid |
| --- | --- | --- |
| **Trending** | moving-average-crossover, fibonacci-trading | mean-reversion |
| **Ranging** | mean-reversion, bollinger-bands, supply-demand-zones | momentum-trading, MA crossover |
| **Volatile** | wider stops, smaller size | all trend-following, all mean-reversion |
| **Squeeze** | breakout-trading (prepare) | range-trading (about to break) |

## Workflow

1. **Get all four inputs**:
   ```
   get_indicator(indicator_code="dmi", symbol=<symbol>, interval=<interval>)
   get_indicator(indicator_code="bbands", symbol=<symbol>, interval=<interval>)
   get_indicator(indicator_code="tr", symbol=<symbol>, interval=<interval>)
   get_indicator(indicator_code="ema", symbol=<symbol>, interval=<interval>)
   ```

2. **Classify** using composite table. Visualize:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "highlight",
       "points": [
           {"time": <regime_start>, "price": <candle_high>},
           {"time": <current_time>, "price": <candle_low>}
       ],
       "options": {"text": "TRENDING (ADX: 32)"}
   })
   ```

3. **Report**: regime, confidence, key metrics, recommended/avoid skills, transition signals to watch

## Key Rules

- NEVER skip regime detection before applying any other strategy
- NEVER force trades in the ADX 20-25 transition zone; wait for clarity
- NEVER rely on ADX alone; combine with BB Width and ATR for earlier detection
- Re-check regime on higher timeframes; HTF regime overrides LTF

## Related Skills

- **multi-timeframe-analysis** — regime on HTF sets context; MTF refines entries within the regime
- **bollinger-bands** — BB Width is a key detection input; BB strategies adapt to detected regime
