---
name: breakout-trading
description: Trade consolidation breakouts with volume confirmation. Use when anticipating trend continuation, catching early moves, or trading pattern completions.
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
| Volume         | Spike (2x+)            | Low or declining    |
| Close          | Beyond level           | Wick only           |
| Follow-through | Continued momentum     | Quick reversal      |
| Time           | Sustained (3+ candles) | Immediate rejection |

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

- **Measured move**: Height of consolidation
- **Fibonacci extension**: 1.27, 1.618
- **Next resistance/support**: Key level
