---
name: arbitrage-trading
description: Exploit price differences across exchanges or trading pairs. Use when spotting price discrepancies, trading cross-exchange spreads, or finding risk-free opportunities.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Arbitrage Trading

Identify price inefficiencies across markets or trading pairs for potential profit.

> **Note:** Agent can identify arbitrage opportunities via price comparison but cannot execute cross-exchange trades directly. Use this skill to detect and report opportunities.

## Arbitrage Types

| Type             | Mechanism                                  | Key Cost Factor   |
| ---------------- | ------------------------------------------ | ----------------- |
| Cross-Exchange   | Same asset priced differently on two venues | Transfer fees     |
| Triangular       | Three-pair cycle (BTC->ETH->USDT->BTC)    | Trading fees x3   |
| Futures-Spot     | Premium between spot and perp/futures      | Funding rate      |
| DEX-CEX          | Price gap between decentralized and centralized | Gas fees     |

## Profitability Check

**Cross-Exchange:**
- Gross Spread = Sell Price - Buy Price
- Net Profit = Gross Spread - (Buy Fee + Sell Fee + Transfer Cost)

**Triangular:**
- Expected cross rate = Price_A / Price_B
- Actual cross rate = observed market rate
- Spread % = (Actual - Expected) / Expected x 100

Only viable if Net Profit > 0 after all fees.

## Workflow

1. **Fetch current prices** for the target asset across pairs:
```
get_latest_candle(symbol="BTCUSDT")
get_latest_candle(symbol="ETHUSDT")
get_latest_candle(symbol="ETHBTC")
```

2. **Calculate cross rates** and compare to actual market rates for triangular arb detection.

3. **Check for futures-spot spread** via funding rate data:
```
get_financial_news(query="BTC funding rate perpetual futures premium")
```

4. **Estimate all costs** (maker/taker fees, withdrawal fees, gas, slippage) and compute net profit.

5. **Report opportunity** with: pair(s), spread %, estimated fees, net profit, and time sensitivity.

## Triangular Arbitrage Example

```
BTC/USDT: 50,000 | ETH/USDT: 2,000 | ETH/BTC: 0.041
Expected ETH/BTC: 2000/50000 = 0.040
Actual: 0.041 → ~2.5% spread (before fees)
Path: USDT → BTC → ETH → USDT
```

## Key Rules

- NEVER report an opportunity without deducting all fees (trading, transfer, gas, slippage)
- NEVER assume execution is instant -- note that cross-exchange opportunities decay in seconds
- Pre-funded accounts on both sides are required for cross-exchange arb; transfers kill the edge
- Spreads under 0.3% are rarely profitable after fees
- Check order book depth: thin liquidity means slippage will eat the spread

## Related Skills

- **funding-rate-trading** -- funding rate arb (spot + perp) is a specific delta-neutral strategy
- **altcoin-rotation** -- cross-pair price analysis overlaps with rotation screening
