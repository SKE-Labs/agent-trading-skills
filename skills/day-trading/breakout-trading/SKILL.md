---
name: breakout-trading
description: Trade consolidation breakouts with volume confirmation. Use when anticipating trend continuation, catching early moves, or trading pattern completions.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["ranging"]
---

# Breakout Trading

Breakout trading captures explosive moves when price breaks out of consolidation or key levels.

## Breakout Types

### 1. Horizontal Breakout

- Break of flat resistance/support
- Clear level with multiple touches
- Most common type

### 2. Pattern Breakout

- Triangle, wedge, flag completion
- Pattern target projects from breakout
- Often more reliable

### 3. Trend Breakout

- Break of trendline
- Indicates trend change
- Requires confirmation

## Entry Strategies

### 1. Aggressive Entry (On Break)

- Enter as price breaks level
- Fastest entry, highest risk
- Use for strong conviction

### 2. Conservative Entry (Retest)

- Wait for breakout
- Wait for retest of broken level
- Enter on bounce
- Miss some moves, better R:R

### 3. Confirmation Entry

- Wait for candle close beyond level
- Volume must confirm
- Most reliable, less profit

## Validation Criteria

| Factor         | Valid Breakout         | False Breakout      |
| -------------- | ---------------------- | ------------------- |
| Volume         | Spike (1.5x+ average)  | Low or declining    |
| Close          | Beyond level           | Wick only           |
| Follow-through | Continued momentum     | Quick reversal      |
| Time           | Sustained (3+ candles) | Immediate rejection |

### Volume Confirmation Thresholds

Volume is the #1 validator of breakouts:

| Volume vs 20-period Average | Signal |
| --- | --- |
| >2.0× average | Strong breakout — high confidence |
| 1.5-2.0× average | Valid breakout — normal confidence |
| 1.0-1.5× average | Weak — wait for more confirmation |
| <1.0× average | Likely false breakout — skip or fade |

Use `get_indicator(indicator_code="mfi")` and compare to recent average.

### False Breakout Statistics

~60% of all breakouts fail. Protect yourself with these rules:

| False Breakout Signal | Action |
| --- | --- |
| Price returns inside range within 3 candles | Exit immediately — thesis invalidated |
| Volume declines after breakout candle | Tighten stop to breakeven |
| Breakout wick >50% of candle body | Weak close — wait for retest |
| Multiple failed breakouts at same level | Level may be exhausted — look for different setup |

### Breakout Pullback Timing

~65% of valid breakouts retest the breakout level within 5-10 candles:

- **Retest entry** (conservative): Wait for pullback to broken level, enter on bounce
- **Better R:R**: Stop is tighter (just below the retested level)
- **Risk**: ~35% of breakouts never pull back — you miss the trade
- **Best approach**: Enter 50% on breakout, add 50% on retest

## Workflow

1. **Identify consolidation** or key level
2. **Mark the level** using `draw_chart_analysis`
3. **Set alerts** at level
4. **Wait for break** with volume
5. **Enter with preferred strategy**
6. **Stop** below breakout candle or level
7. **Target** measured move or next resistance

## False Breakout Management

False breakouts are common. Protect yourself:

- Wait for confirmation close
- Use retest entry for safety
- Accept that some trades will fail
- Consider trading the failure (reversal)

## Target Calculation

### Measured Move Method

The primary target for breakout trades is the measured move:

```
Target = Breakout Level + Height of Consolidation
```

Example: Range from $95 to $100, breakout above $100 → Target = $100 + $5 = $105

### Additional Targets

- **Fibonacci extension**: 1.272× and 1.618× of consolidation height
- **Next key resistance/support**: Previous swing high/low
- **Volume profile**: Next HVN above/below breakout

## Enhanced Workflow

### 1. Identify Consolidation

```
get_candles_around_date(symbol="BTCUSD", interval="4h", date="2026-03-19")
```

Look for tight range with 3+ touches on support/resistance.

### 2. Mark the Level

```
draw_chart_analysis(action="create", drawing={
    "type": "resistance",
    "points": [
        {"time": <first_touch_time>, "price": <level_price>},
        {"time": <current_time>, "price": <level_price>}
    ],
    "options": {"text": "Breakout Level ($68,500)"}
})
```

### 3. Check Volume for Confirmation

```
get_indicator(indicator_code="mfi")
```

Compare breakout candle volume to 20-period average. Must be >1.5×.

### 4. Confirm with Momentum

```
get_indicator(indicator_code="rsi")
get_indicator(indicator_code="macd")
```

RSI should be trending in breakout direction. MACD histogram should be expanding.

### 5. Mark Entry Zone and Target

```
draw_chart_analysis(action="create", drawing={
    "type": "demand",
    "points": [
        {"time": <breakout_time>, "price": <breakout_level>},
        {"time": <current_time>, "price": <retest_zone>}
    ],
    "options": {"text": "Retest Buy Zone"}
})
```

### 6. Report to Orchestrator

- **Breakout type**: Horizontal, pattern, or trendline
- **Volume confirmation**: X× average (strong/weak)
- **Entry recommendation**: Aggressive (on break) or conservative (retest)
- **Measured move target**: Specific price level
- **Stop loss**: Below breakout level or below breakout candle low
- **False breakout risk**: Assessment based on volume and follow-through

## Related Skills

- **volume-profile-trading** — LVN zones identify where breakout moves accelerate; POC and VA boundaries define key breakout levels
- **momentum-trading** — Breakout momentum entries ride the continuation after consolidation breaks
- **triangle-patterns** — Triangle breakouts are a specific breakout type with well-defined measured move targets
