---
name: gap-trading
description: Identify and trade opening price gaps using gap type classification and fill statistics. Use when price opens significantly above/below prior close, at market open, or when gaps appear on intraday charts.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["volatile", "trending"]
---

# Gap Trading

A gap occurs when price opens significantly higher or lower than the previous close, leaving a void on the chart. Different gap types have very different trading implications.

## Gap Types

| Gap Type | Characteristics | Fill Rate | Trading Approach |
| --- | --- | --- | --- |
| **Common** | Within range, low volume, no catalyst | ~70% fill within 5 sessions | Fade (trade the fill) |
| **Breakaway** | Through key S/R, high volume, catalyst | ~30% fill | Trade continuation (gap-and-go) |
| **Runaway** (Continuation) | Mid-trend, moderate volume, confirms trend | ~50% fill | Trade continuation |
| **Exhaustion** | End of extended trend, very high volume, climactic | ~80% fill | Fade (reversal) |

## Gap Classification

To classify a gap, check these criteria:

| Criteria | Common | Breakaway | Runaway | Exhaustion |
| --- | --- | --- | --- | --- |
| Volume vs average | Normal or low | >2× average | 1.5× average | >2× average |
| Breaks key S/R? | No | Yes | No (already in trend) | No (at trend end) |
| News catalyst? | No | Usually yes | Optional | Often yes |
| Trend context | Ranging | Starting new trend | Mid-trend | Extended trend (>10 legs) |

## Identification

Use `get_candles_around_date` to detect gaps:

```
get_candles_around_date(symbol="AAPL", interval="1D", date="2026-03-19")
```

A gap exists when:
- **Gap up**: Current open > Previous high
- **Gap down**: Current open < Previous low
- **Gap size**: (Open - Previous Close) / Previous Close × 100

| Gap Size | Classification |
| --- | --- |
| < 0.5% | Micro gap — usually noise, ignore |
| 0.5% - 1.5% | Small gap — common gaps |
| 1.5% - 3% | Medium gap — potentially significant |
| > 3% | Large gap — likely breakaway or exhaustion |

Check volume for classification:

```
get_indicator(indicator_code="mfi")
```

## Trading Strategies

### 1. Gap Fill (Fade)

For common and exhaustion gaps — trade back toward the previous close:

- **Entry**: After gap, wait for first 15-30 min candle to close
- **Confirmation**: If price starts reversing toward gap, enter
- **Target**: Previous close (full fill) or 50% fill (conservative)
- **Stop**: Beyond gap extreme + buffer

### 2. Gap-and-Go (Continuation)

For breakaway and runaway gaps — trade in the gap direction:

- **Entry**: After gap, wait for first 15-30 min consolidation, enter on breakout
- **Confirmation**: Volume remains elevated, price holds above gap (for gap up)
- **Target**: Gap size projected from gap level (measured move)
- **Stop**: Below gap open (for gap up) — if gap fills, the thesis is wrong

### 3. Gap Reversal

For exhaustion gaps at the end of extended trends:

- **Entry**: After gap shows reversal candle (engulfing, hammer/shooting star)
- **Confirmation**: Volume decreasing after initial spike, RSI divergence
- **Target**: Full gap fill, then previous S/R levels
- **Stop**: Beyond gap extreme

## Workflow

### 1. Detect Gap

```
get_candles_around_date(symbol="AAPL", interval="1D", date="2026-03-19")
```

Compare current open to previous close/high/low. Calculate gap size %.

### 2. Check Volume

```
get_indicator(indicator_code="mfi")
```

Compare gap session volume to 20-period average. >2× = significant.

### 3. Classify Gap Type

Using the classification criteria above, determine if Common, Breakaway, Runaway, or Exhaustion.

### 4. Check Trend Context

```
get_indicator(indicator_code="dmi")
get_indicator(indicator_code="ema")
```

Is this gap in a trending or ranging market? How extended is the current trend?

### 5. Mark Gap Zone

```
draw_chart_analysis(action="create", drawing={
    "type": "highlight",
    "points": [
        {"time": <previous_close_time>, "price": <previous_close>},
        {"time": <gap_open_time>, "price": <gap_open>}
    ],
    "options": {"text": "Breakaway Gap (+2.3%)"}
})
```

### 6. Report to Orchestrator

- **Gap type** and classification rationale
- **Gap size** (% and absolute)
- **Volume confirmation** (above/below average)
- **Strategy recommendation**: Fill (fade) or continuation (gap-and-go)
- **Key levels**: Gap boundaries, fill target, stop level

## Risk Management

| Rule | Guideline |
| --- | --- |
| Gap fill stop | Beyond gap extreme (if fading) |
| Gap-and-go stop | Below gap open (gap filling = wrong) |
| First 15-30 min | Never enter during — wait for initial price discovery |
| Gap + event | If gap caused by news/earnings, use wider stops |

## Best Practices

| Do | Don't |
| --- | --- |
| Classify gap type before trading | Treat all gaps the same |
| Wait 15-30 min for initial price discovery | Enter at the open |
| Check volume for confirmation | Ignore volume |
| Use gap statistics to inform bias | Assume all gaps fill |
| Combine with S/R levels | Trade gaps in isolation |

## Common Mistakes

- **Assuming all gaps fill** — Common gaps fill ~70%, but breakaway gaps only ~30%. Classification matters.
- **Entering at the open** — The first 15-30 minutes are pure noise. Wait for initial price discovery.
- **Ignoring volume** — A gap on low volume (common gap) vs high volume (breakaway) require opposite strategies.
- **Fighting breakaway gaps** — Fading a breakaway gap through major resistance with high volume is fighting institutional flow.
- **Wrong stop placement** — Gap-and-go stops must be below the gap open. If the gap fills, your thesis is invalidated.

## Related Skills

- **breakout-trading** — Gap-and-go trades follow breakout principles with volume confirmation
- **momentum-trading** — Breakaway gaps create momentum moves; ride them with momentum techniques
- **volume-profile-trading** — Volume profile helps identify whether the gap fills or holds based on volume at price
