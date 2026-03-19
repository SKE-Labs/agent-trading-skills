---
name: fibonacci-trading
description: Use Fibonacci retracement and extension for entries and targets. Use when finding pullback entries, setting profit targets, or identifying key reversal levels.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending"]
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

### 2. Calculate Fibonacci Levels

Use the `execute` tool to calculate exact Fibonacci levels for limit orders:

```
execute(command='python3 -c "h=52000;l=45000;r=h-l;print(f\"23.6%: {h-r*0.236:.2f}\\n38.2%: {h-r*0.382:.2f}\\n50.0%: {h-r*0.5:.2f}\\n61.8%: {h-r*0.618:.2f}\\n78.6%: {h-r*0.786:.2f}\")"')
```

For extensions (targets):

```
execute(command='python3 -c "h=52000;l=45000;r=h-l;print(f\"127.2%: {h+r*0.272:.2f}\\n161.8%: {h+r*0.618:.2f}\\n200%: {h+r:.2f}\\n261.8%: {h+r*1.618:.2f}\")"')
```

### 3. Draw Fibonacci Retracement

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

### 4. Mark Key Confluence Zones

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

### 5. Confirm with Indicators

Use `get_indicator` to check for confluence:

- `get_indicator(indicator="rsi")` — Look for oversold at fib support
- `get_indicator(indicator="macd")` — Check for momentum shift

### 6. Report to Orchestrator

After confirmation, provide the orchestrator with entry zone, stop loss, and target levels. The orchestrator handles position sizing and signal creation.

## Best Practices

| Do                     | Don't                   |
| ---------------------- | ----------------------- |
| Draw from clear swings | Use every tiny swing    |
| Wait for confluence    | Trade Fib alone         |
| Use 61.8% as primary   | Ignore the golden ratio |
| Combine time frames    | Only use one TF         |

## Related Skills

- **optimal-trade-entry** — OTE uses the 62-79% Fibonacci zone for precise smart money entries
- **order-blocks** — Fibonacci levels overlapping with order blocks create the strongest confluence zones
- **supply-demand-zones** — Fibonacci retracements into supply/demand zones provide high-probability entries
