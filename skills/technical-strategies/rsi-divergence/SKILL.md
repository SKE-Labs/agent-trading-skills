---
name: rsi-divergence
description: Identify bullish and bearish RSI divergence for reversal signals. Use when spotting weakening momentum, finding potential reversal points, or confirming trend exhaustion.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.1"
---

# RSI Divergence Trading

Divergence between price and RSI signals weakening momentum before price reverses.

## Divergence Types

### Regular (Reversal)

| Type        | Price Action | RSI Action | Signal      |
| ----------- | ------------ | ---------- | ----------- |
| **Bullish** | Lower Low    | Higher Low | Buy signal  |
| **Bearish** | Higher High  | Lower High | Sell signal |

### Hidden (Continuation)

| Type        | Price Action | RSI Action  | Signal               |
| ----------- | ------------ | ----------- | -------------------- |
| **Bullish** | Higher Low   | Lower Low   | Trend continues up   |
| **Bearish** | Lower High   | Higher High | Trend continues down |

## RSI Zones

| Level | Interpretation |
| ----- | -------------- |
| >70   | Overbought — bearish regular divergence strongest here |
| <30   | Oversold — bullish regular divergence strongest here |
| 50    | Equilibrium — divergence here is unreliable |

## Workflow

1. **Get RSI**:
   ```
   get_indicator(indicator_code="rsi", symbol=<symbol>, interval=<interval>)
   ```

2. **Identify swing points** on price chart and corresponding RSI swings

3. **Compare slopes**: if price makes LL but RSI makes HL → bullish divergence. If price makes HH but RSI makes LH → bearish divergence.

4. **Get candles** for chart marking:
   ```
   get_candles_around_date(symbol=<symbol>, interval=<interval>, date=<date>)
   ```

5. **Mark divergence**:
   ```
   draw_chart_analysis(action="create", drawing={
       "type": "trend",
       "points": [
           {"time": <first_swing_time>, "price": <first_swing_price>},
           {"time": <second_swing_time>, "price": <second_swing_price>}
       ],
       "options": {"text": "Bullish RSI Divergence"}
   })
   ```

6. **Wait for confirmation candle** (engulfing, hammer, pin bar) at divergence zone before entry

### Entry

- **Bullish**: enter above confirmation candle at support; stop below swing low; target previous resistance
- **Bearish**: enter below confirmation candle at resistance; stop above swing high; target previous support

## Key Rules

- NEVER trade divergence at random price levels; require key S/R confluence
- NEVER enter without confirmation candle; divergence is an early warning, not an entry
- NEVER rely on 5m divergence; use 1H+ for reliable signals
- RSI must be in extreme zone (<30 or >70) for regular divergence to be valid
- Combine with structure analysis; divergence + S/R = high probability

## Related Skills

- **divergence-trading** — extends RSI divergence with multi-indicator scoring (MACD, Stochastic, OBV)
- **macd-trading** — MACD divergence combined with RSI divergence strengthens reversal signals
