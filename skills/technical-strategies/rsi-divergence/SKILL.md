---
name: rsi-divergence
description: Identify bullish and bearish RSI divergence for reversal signals. Use when spotting weakening momentum, finding potential reversal points, or confirming trend exhaustion.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending", "ranging"]
---

# RSI Divergence Trading

Divergence occurs when price and RSI move in opposite directions, signaling potential reversals.

## Divergence Types

### Regular (Reversal) Divergence

| Type        | Price Action | RSI Action | Signal      |
| ----------- | ------------ | ---------- | ----------- |
| **Bullish** | Lower Low    | Higher Low | Buy signal  |
| **Bearish** | Higher High  | Lower High | Sell signal |

### Hidden (Continuation) Divergence

| Type        | Price Action | RSI Action  | Signal               |
| ----------- | ------------ | ----------- | -------------------- |
| **Bullish** | Higher Low   | Lower Low   | Trend continues up   |
| **Bearish** | Lower High   | Higher High | Trend continues down |

## Identification Workflow

1. **Get RSI indicator** using `get_indicator(indicator_code="rsi")`
2. **Identify swing points** on price chart
3. **Compare to RSI swings**:
   - Connect price swing lows/highs
   - Connect corresponding RSI swing lows/highs
4. **Confirm divergence** if slopes differ

## Entry Strategy

### Bullish Divergence Entry

1. Identify bullish divergence at support
2. Wait for bullish candle confirmation
3. Enter above confirmation candle
4. Stop below the swing low
5. Target previous resistance

### Bearish Divergence Entry

1. Identify bearish divergence at resistance
2. Wait for bearish candle confirmation
3. Enter below confirmation candle
4. Stop above the swing high
5. Target previous support

## Best Practices

| Do                      | Don't                    |
| ----------------------- | ------------------------ |
| Trade at key S/R levels | Trade random divergences |
| Wait for confirmation   | Enter immediately        |
| Use HTF divergence      | Rely on 5m divergence    |
| Combine with structure  | Trade in isolation       |

## RSI Levels Reference

| Level | Interpretation                  |
| ----- | ------------------------------- |
| >70   | Overbought (potential reversal) |
| <30   | Oversold (potential reversal)   |
| 50    | Equilibrium                     |

## Key Insight

Divergence shows **momentum** weakening before price reverses. It's a leading indicator but requires confirmation.

## Related Skills

- **divergence-trading** — Extends RSI divergence with multi-indicator scoring across MACD, Stochastic, and OBV
- **macd-trading** — MACD divergence combined with RSI divergence strengthens reversal signals
- **mean-reversion** — RSI divergence at Bollinger Band extremes confirms mean reversion entries
