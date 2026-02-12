---
name: range-trading
description: Buy support and sell resistance within ranging markets. Use when markets lack trend direction, trading consolidation, or identifying accumulation/distribution.
---

# Range Trading

Range trading profits from price oscillating between clear support and resistance levels.

## Range Identification

### Characteristics

- Price bouncing between two levels
- Lack of clear higher highs/lower lows
- Volume decreasing during range
- Multiple tests of both boundaries

### Range Types

- **Horizontal range**: Clear flat S/R
- **Ascending range**: Higher highs and higher lows within channel
- **Descending range**: Lower highs and lower lows within channel

## Entry Strategy

### Buy at Support

1. Price reaches range support
2. Wait for rejection candle (hammer, engulfing)
3. Enter on confirmation
4. Stop below support
5. Target range resistance

### Sell at Resistance

1. Price reaches range resistance
2. Wait for rejection candle (shooting star, engulfing)
3. Enter on confirmation
4. Stop above resistance
5. Target range support

## Workflow

1. **Identify range** (minimum 2 touches each side)
2. **Mark levels** using `draw_chart_analysis` with `support`/`resistance`
3. **Wait at boundaries** (don't trade middle of range)
4. **Enter with confirmation** (reversal candle)
5. **Target opposite boundary**
6. **Watch for breakout** (end of range)

## Risk Management

| Rule               | Guideline                  |
| ------------------ | -------------------------- |
| Stop placement     | Just beyond range boundary |
| Target             | 70-80% of range width      |
| Entry zone         | Outer 20% of range         |
| Break invalidation | Close beyond range         |

## Range Quality

| Factor   | Strong Range      | Weak Range |
| -------- | ----------------- | ---------- |
| Bounces  | Clean, multiple   | Weak, few  |
| Width    | Wide enough (3%+) | Too narrow |
| Duration | Multi-day/week    | Few hours  |
| Volume   | Low during range  | Erratic    |

## Breakout Watch

Ranges eventually break. Watch for:

- Volume surge at boundary
- Failed bounce (weak rejection)
- Multiple tests of same level
- HTF trend resuming

When breakout occurs, stop trading range, consider breakout trade.
