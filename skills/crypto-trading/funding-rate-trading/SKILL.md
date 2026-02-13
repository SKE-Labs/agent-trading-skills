---
name: funding-rate-trading
description: Trade based on perpetual futures funding rate signals. Use when funding is extreme, finding market sentiment, or earning funding payments.
---

# Funding Rate Trading

Perpetual futures use funding rates to keep price aligned with spot—creating trading opportunities.

## Funding Rate Basics

- **Positive funding**: Longs pay shorts (market is bullish)
- **Negative funding**: Shorts pay longs (market is bearish)
- Paid every 8 hours (typically)
- Rate is annualized (0.01% every 8h ≈ 10.95% APR)

## Funding Rate Signals

| Funding Rate            | Market Sentiment     | Trade Idea       |
| ----------------------- | -------------------- | ---------------- |
| Very Positive (>0.05%)  | Overleveraged longs  | Contrarian short |
| Positive (0.01-0.05%)   | Bullish              | No signal        |
| Neutral (~0.01%)        | Balanced             | No signal        |
| Negative (<0%)          | Bearish              | Potential bottom |
| Very Negative (<-0.05%) | Overleveraged shorts | Contrarian long  |

## Trading Strategies

### 1. Funding Rate Arbitrage

- Go long spot + short perp (positive funding)
- Collect funding payments
- Delta neutral (market direction doesn't matter)
- APR = Funding rate × 3 × 365

### 2. Extreme Funding Reversal

- Very high positive = Look for shorts
- Very negative = Look for longs
- Wait for liquidation cascade
- Contrarian trade

### 3. Funding as Confirmation

- Use funding to confirm market sentiment
- High funding + resistance = Stronger short signal
- Negative funding + support = Stronger long signal

## Funding Arbitrage Setup

Use the `execute` tool to calculate APR from funding rate:

```
execute(command='python3 -c "rate=0.05;apr=rate*3*365;daily=rate*3;print(f\"Funding Rate: {rate}%\\nAPR: {apr:.2f}%\\nDaily: {daily:.2f}%\")"')
```

**Setup Steps:**
1. **Calculate APR** = Funding rate × 3 × 365
2. **If APR > 20%**, consider arb trade
3. **Long spot** (or low-leverage long)
4. **Short perp** equal size
5. **Collect funding** every 8 hours
6. **Close both** when rate normalizes

## Risk Considerations

| Risk                       | Mitigation                  |
| -------------------------- | --------------------------- |
| Funding can flip           | Monitor closely             |
| Exchange risk              | Use reputable exchanges     |
| Liquidation (if leveraged) | Keep leverage low           |
| Opportunity cost           | Compare to other strategies |

## Monitoring

Track funding across exchanges:

- Binance, Bybit, OKX perpetuals
- Compare spot vs perp price
- Historical funding context

## Key Insight

Extreme funding often precedes reversals. When "everyone is long" (high positive funding), the market often corrects to liquidate overleveraged positions.
