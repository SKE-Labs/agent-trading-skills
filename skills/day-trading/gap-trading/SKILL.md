---
name: gap-trading
description: Identify and trade opening price gaps using gap type classification and fill statistics. Use when price opens significantly above/below prior close, at market open, or when gaps appear on intraday charts.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# Gap Trading

Trade price gaps by classifying gap type first -- different types require opposite strategies.

## Identification

A gap exists when current open > previous high (gap up) or current open < previous low (gap down).

```
get_candles_around_date(symbol=<symbol>, interval="1D", date=<date>)
```

Gap size = (Open - Previous Close) / Previous Close x 100. Ignore gaps < 0.5% (noise).

## Gap Classification

| Gap Type | Volume vs Avg | Breaks Key S/R? | Trend Context | Fill Rate | Strategy |
| --- | --- | --- | --- | --- | --- |
| **Common** | Normal/low | No | Ranging | ~70% | Fade (trade the fill) |
| **Breakaway** | >2x | Yes | Starting new trend | ~30% | Continuation (gap-and-go) |
| **Runaway** | ~1.5x | No | Mid-trend | ~50% | Continuation |
| **Exhaustion** | >2x | No | Extended trend end | ~80% | Fade (reversal) |

## Workflow

### 1. Detect and Classify

```
get_candles_around_date(symbol=<symbol>, interval="1D", date=<date>)
get_indicator(indicator_code="mfi", symbol=<symbol>, interval="1D")
```

Calculate gap size %. Compare volume to 20-period average. Classify using table above.

### 2. Check Trend Context

```
get_indicator(indicator_code="dmi", symbol=<symbol>, interval="1D")
get_indicator(indicator_code="ema", symbol=<symbol>, interval="1D")
```

Determine if ranging, starting trend, mid-trend, or extended trend to confirm classification.

### 3. Mark Gap Zone

```
draw_chart_analysis(action="create", drawing={
    "type": "highlight",
    "points": [
        {"time": <previous_close_time>, "price": <previous_close>},
        {"time": <gap_open_time>, "price": <gap_open>}
    ],
    "options": {"text": "<Gap Type> Gap (+/-X.X%)"}
})
```

### 4. Apply Strategy

- **Gap Fill (fade)**: For common/exhaustion gaps. Wait 15-30 min, enter on reversal toward previous close. Stop beyond gap extreme.
- **Gap-and-Go (continuation)**: For breakaway/runaway gaps. Wait for first 15-30 min consolidation, enter on breakout in gap direction. Stop below gap open -- if gap fills, thesis is wrong.
- **Gap Reversal**: For exhaustion gaps at trend end. Enter on reversal candle (engulfing, hammer). Target full gap fill.

### 5. Report to Orchestrator

Gap type and rationale, gap size, volume confirmation, strategy recommendation, gap boundaries, fill target, stop level.

## Key Rules

- NEVER enter during the first 15-30 minutes -- initial price discovery is pure noise
- NEVER treat all gaps the same -- common gaps fill ~70%, breakaway gaps only ~30%
- NEVER fade a breakaway gap through major resistance with high volume -- that is fighting institutional flow
- For gap-and-go stops, gap filling = thesis invalidated = exit
- During event-driven gaps (earnings, news), use wider stops

## Related Skills

- **breakout-trading** -- gap-and-go follows breakout principles
- **momentum-trading** -- breakaway gaps create momentum moves
