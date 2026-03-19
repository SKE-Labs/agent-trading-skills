---
name: channel-trading
description: Trade within ascending, descending, and horizontal channels. Use when range trading, riding trends with defined boundaries, or finding breakout setups.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending", "ranging"]
---

# Channel Trading

Channels define price boundaries for trading bounces or anticipating breakouts.

## Channel Types

### Ascending Channel (Bullish)

- Both lines slope upward
- Buy at lower line, sell at upper line
- Break below = Reversal

### Descending Channel (Bearish)

- Both lines slope downward
- Sell at upper line, cover at lower line
- Break above = Reversal

### Horizontal Channel (Range)

- Parallel horizontal lines
- Classic range trading
- Break either direction = New trend

## Channel Drawing

1. **Identify 2+ swing lows** → Draw support line
2. **Identify 2+ swing highs** → Draw resistance line
3. Lines should be **parallel** (or near parallel)
4. Minimum **4 total touch points**

Use `draw_chart_analysis` with `trend` type for both lines.

## Trading Strategies

### 1. Channel Bounce (Range Trading)

- Buy at channel support (lower line)
- Sell at channel resistance (upper line)
- Stop: Beyond the channel boundary
- Works best in horizontal channels

### 2. Trend Channel Trading

- In ascending channel: Focus on buying support
- In descending channel: Focus on selling resistance
- Trade WITH the channel direction

### 3. Channel Breakout

- Wait for break and close outside channel
- Volume spike confirms
- Target: Measured move (channel width)

## Entry Refinement

When price reaches channel boundary:

1. Look for reversal candlestick
2. Check RSI divergence
3. Confirm LTF structure shift
4. Enter with confirmation

## Risk Management

| Entry Point        | Stop Loss                 |
| ------------------ | ------------------------- |
| Channel support    | Below support + buffer    |
| Channel resistance | Above resistance + buffer |
| Breakout           | Inside channel            |

## Channel Health

Signs of **strong** channel:

- Clean, respected boundaries
- Multiple touches each side
- Consistent bounces

Signs of **weakening** channel:

- Failing to reach boundary
- Deeper pullbacks
- Decreasing momentum

Watch for potential breakout when channel weakens.

## Related Skills

- **multi-timeframe-analysis** — Channels on HTF define the trend; LTF channels refine entry zones
- **breakout-trading** — When channels weaken and break, switch to breakout trading for the continuation move
- **range-trading** — Horizontal channels are ranges; apply range-trading strategies within them
