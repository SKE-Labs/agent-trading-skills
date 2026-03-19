---
name: multi-timeframe-analysis
description: Analyze markets using 3 timeframes with signal priority scoring and conflict resolution. Use when determining trend direction, timing entries with precision, or validating trade setups across timeframes.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Multi-Timeframe Analysis (MTF)

Analyze 3 timeframes to align trend, structure, and entry for high-probability trades. Never trade a lower timeframe signal that contradicts the higher timeframe bias.

## Timeframe Selection

| Primary TF | Higher TF | Lower TF | Use Case         |
| ---------- | --------- | -------- | ---------------- |
| 1D         | Weekly    | 4H       | Position trading |
| 4H         | 1D        | 1H       | Swing trading    |
| 1H         | 4H        | 15m      | Intraday swing   |
| 15m        | 1H        | 5m       | Day trading      |

**Rule of thumb**: Each timeframe should be 4-6× the one below it. Pick one combination and use it consistently for at least 30 trades before evaluating.

## Timeframe Roles

| Role        | Purpose         | Analysis Focus                           |
| ----------- | --------------- | ---------------------------------------- |
| **Higher**  | Trend direction | Major S/R, overall bias, regime          |
| **Primary** | Trade structure | Patterns, setups, key levels             |
| **Lower**   | Entry timing    | Precise entries, confirmation, tight stops |

## Signal Priority System

When timeframes give different signals, use this priority scoring:

| # | HTF Bias | Primary Setup | LTF Entry | Score | Action |
| --- | --- | --- | --- | --- | --- |
| 1 | Bullish | Bullish setup | Bullish confirmation | **10/10** | Full size, high confidence |
| 2 | Bullish | Bullish setup | No LTF signal yet | **7/10** | Wait for LTF, don't force |
| 3 | Bullish | Ranging (no setup) | — | **4/10** | Wait for primary to develop setup |
| 4 | Bullish | Bearish setup | Bearish confirmation | **2/10** | Skip — counter-trend is low-probability |
| 5 | Ranging | Bullish setup | Bullish confirmation | **6/10** | Reduced size (no HTF support) |
| 6 | Ranging | Ranging | — | **1/10** | No trade — wait for directional bias |
| 7 | Bearish | Bullish setup | Bullish confirmation | **3/10** | Skip — trading against HTF trend |

**Minimum score to trade**: 6/10 for standard entries, 8/10 for full-size positions.

## Conflict Resolution Rules

When timeframes disagree:

| Conflict | Resolution |
| --- | --- |
| HTF bullish, Primary bearish | **Wait.** Primary is likely a pullback in HTF trend. Look for primary to develop bullish setup. |
| HTF bearish, LTF bullish | **Skip.** LTF bullish signals in HTF downtrend are counter-trend traps. |
| HTF ranging, Primary trending | **Reduce size.** Trade the primary trend but with 50% normal size — no HTF confirmation. |
| All timeframes conflicting | **No trade.** Clarity is a prerequisite, not a luxury. |

**Key principle**: When in doubt, the higher timeframe wins. Period.

## Regime-Aware Timeframe Weighting

Different market regimes change how you weight signals across timeframes:

| Market Regime | HTF Weight | Primary Weight | LTF Weight | Notes |
| --- | --- | --- | --- | --- |
| **Strong trend** (ADX >30) | 50% | 30% | 20% | HTF dominates — trade pullbacks |
| **Moderate trend** (ADX 25-30) | 40% | 35% | 25% | Balanced approach |
| **Ranging** (ADX <20) | 20% | 40% | 40% | Primary and LTF matter more for range boundaries |
| **Volatile/Transitioning** | 30% | 30% | 40% | LTF structure matters most for timing |

Use the **market-regime-detection** skill to classify the regime before applying these weights.

## Analysis Workflow

### Step 1: Higher Timeframe (Bias)

Generate the HTF chart and assess overall trend:

```
generate_chart(symbol="BTCUSD", interval="1D")
```

Then check trend indicators:

```
get_indicator(indicator="ema", options={"period": 50})
get_indicator(indicator="ema", options={"period": 200})
get_indicator(indicator="adx")
```

Determine:
- **Trend direction**: HH/HL (bullish), LH/LL (bearish), or no clear structure (ranging)
- **Trend strength**: ADX >25 = trending, <20 = ranging
- **Key levels**: Mark major S/R zones with `draw_chart_analysis`

```
draw_chart_analysis(action="create", drawing={
    "type": "resistance",
    "points": [
        {"time": <level_start>, "price": <resistance_price>},
        {"time": <level_end>, "price": <resistance_price>}
    ],
    "options": {"text": "HTF Resistance"}
})
```

### Step 2: Primary Timeframe (Setup)

Generate the primary chart aligned with HTF bias:

```
generate_chart(symbol="BTCUSD", interval="4h")
```

Check indicators for setup confirmation:

```
get_indicator(indicator="rsi")
get_indicator(indicator="macd")
get_indicator(indicator="bbands")
```

Find setups that align with HTF:
- If HTF bullish → look for bullish patterns (pullbacks to support, OBs, FVGs)
- If HTF bearish → look for bearish patterns (rallies into resistance)
- Mark setup zones with `draw_chart_analysis`

```
draw_chart_analysis(action="create", drawing={
    "type": "demand",
    "points": [
        {"time": <zone_start>, "price": <zone_top>},
        {"time": <zone_end>, "price": <zone_bottom>}
    ],
    "options": {"text": "4H Demand + Daily Uptrend"}
})
```

### Step 3: Lower Timeframe (Entry)

Generate the LTF chart for precise entry:

```
generate_chart(symbol="BTCUSD", interval="1h")
```

Look for confirmation:

```
get_indicator(indicator="rsi")
get_indicator(indicator="ema", options={"period": 21})
```

Entry triggers:
- Break of structure (BOS) in direction of HTF trend
- Rejection candle at setup zone
- RSI divergence at zone
- Volume spike on LTF confirming direction

### Step 4: Score and Report

Calculate the signal priority score (see table above) and report to orchestrator:
- **HTF bias**: Direction and strength
- **Primary setup**: What pattern/zone was identified
- **LTF confirmation**: What confirmed the entry
- **Signal score**: X/10 with reasoning
- **Recommended action**: Entry, wait, or skip
- **Key levels**: Entry zone, stop loss zone, target zones (marked on chart)

## Confluence Scoring

| Alignment | Score | Action |
| --- | --- | --- |
| All 3 TF agree + indicators confirm | **10/10** | Trade with full confidence |
| All 3 TF agree, mixed indicators | **8/10** | Trade with standard size |
| 2 TF agree, LTF pending | **7/10** | Wait for LTF confirmation |
| 2 TF agree, 1 conflicts | **5/10** | Reduced size or skip |
| TFs conflict | **2/10** | Wait or skip |

## Best Practices

| Do | Don't |
| --- | --- |
| Always start with HTF before zooming in | Jump straight to 5m chart |
| Wait for all 3 TFs to align before entry | Trade 2/3 alignment at full size |
| Use the same TF combination consistently | Switch TF combos trade to trade |
| Mark HTF levels on all lower TF charts | Forget HTF context when on LTF |
| Score every setup before entry | Skip scoring "because it looks good" |
| Adapt to regime (use market-regime-detection) | Apply same weights in all conditions |

## Common Mistakes

- **Trading LTF against HTF trend** — The #1 mistake. A 15m bullish signal means nothing if the daily is bearish. Always defer to HTF.
- **Skipping HTF analysis** — Going straight to entry timeframe misses the big picture. The extra 2 minutes checking HTF saves hours of chasing bad trades.
- **Over-analyzing (paralysis)** — Use exactly 3 timeframes, no more. Adding a 4th or 5th adds confusion, not clarity.
- **Forcing trades in ranging HTF** — When the HTF has no clear trend, your best trade is no trade. Wait for directional bias.
- **Ignoring regime** — Trend-following MTF works in trending markets. In ranges, shift weight to primary/LTF for range boundary trading.

## Related Skills

- **market-regime-detection** — Classify the regime before applying MTF weights; regime determines which timeframe dominates
- **fibonacci-trading** — Use Fibonacci retracements across timeframes for precise entry and target levels
- **market-structure-shift** — Structure analysis (BOS/CHoCH) across timeframes is the foundation of MTF trading
