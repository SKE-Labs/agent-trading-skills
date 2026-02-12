---
name: fibonacci-trading
description: Use Fibonacci retracement and extension for entries and targets. Use when finding pullback entries, setting profit targets, or identifying key reversal levels.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Fibonacci Trading

Fibonacci ratios identify key retracement and extension levels for entries and targets.

## Key Fibonacci Levels

### Retracement Levels (Entries)

| Level | Use                      |
| ----- | ------------------------ |
| 23.6% | Shallow pullback         |
| 38.2% | Moderate pullback        |
| 50.0% | Half retracement         |
| 61.8% | Golden ratio (key level) |
| 78.6% | Deep pullback            |

### Extension Levels (Targets)

| Level        | Use                 |
| ------------ | ------------------- |
| -27% (127%)  | Conservative target |
| -62% (162%)  | Standard target     |
| -100% (200%) | Extended target     |
| -162% (262%) | Aggressive target   |

## Drawing Fibonacci

### For Bullish Setups

- Draw from **swing low** to **swing high**
- Retracements show potential buy zones
- Extensions show upside targets

### For Bearish Setups

- Draw from **swing high** to **swing low**
- Retracements show potential sell zones
- Extensions show downside targets

## Entry Strategy

1. **Identify clear swing** (impulsive move)
2. **Draw Fibonacci retracement**
3. **Wait for pullback** to key levels (38.2%, 50%, 61.8%)
4. **Enter with confirmation**:
   - Rejection candle
   - Structure break on LTF
   - Confluence with S/R
5. **Stop loss** beyond 78.6% or 100%
6. **Targets** at extension levels

## Confluence Zones

Best Fibonacci trades have confluence:

- Fib level + Order block
- Fib level + S/R zone
- Fib level + Moving average
- Fib level + Trendline

## Workflow

### 1. Identify Swing Points

Use `get_candles_around_date` to get exact OHLCV data around the swing high and swing low.

### 2. Draw Fibonacci Retracement

Use `draw_chart_analysis` with type `fib_retracement` to draw directly on the TradingView chart:

- **Bullish setup:** Point 1 = swing low, Point 2 = swing high
- **Bearish setup:** Point 1 = swing high, Point 2 = swing low

```
draw_chart_analysis(action="create", drawing={
    "type": "fib_retracement",
    "points": [
        {"time": <swing_low_timestamp>, "price": <swing_low_price>},
        {"time": <swing_high_timestamp>, "price": <swing_high_price>}
    ],
    "options": {"text": "Fib Retracement"}
})
```

TradingView automatically renders all standard levels (0%, 23.6%, 38.2%, 50%, 61.8%, 78.6%, 100%).

### 3. Mark Key Confluence Zones

Use `draw_chart_analysis` with type `demand` or `supply` to highlight zones where Fibonacci levels overlap with other structures:

```
draw_chart_analysis(action="create", drawing={
    "type": "demand",
    "points": [
        {"time": <zone_start_time>, "price": <zone_top>},
        {"time": <zone_end_time>, "price": <zone_bottom>}
    ],
    "options": {"text": "61.8% + OB"}
})
```

### 4. Confirm with Indicators

Use `get_indicator` to check for confluence:

- `get_indicator(indicator="rsi")` — Look for oversold at fib support
- `get_indicator(indicator="macd")` — Check for momentum shift

### 5. Position Entry

After confirmation, the orchestrator handles:

- `calculate_position_size` for risk-based sizing
- `draw_position` with type `long_position` or `short_position`

## Best Practices

| Do                     | Don't                   |
| ---------------------- | ----------------------- |
| Draw from clear swings | Use every tiny swing    |
| Wait for confluence    | Trade Fib alone         |
| Use 61.8% as primary   | Ignore the golden ratio |
| Combine time frames    | Only use one TF         |
