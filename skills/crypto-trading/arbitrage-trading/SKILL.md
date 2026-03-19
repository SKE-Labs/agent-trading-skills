---
name: arbitrage-trading
description: Exploit price differences across exchanges or trading pairs. Use when spotting price discrepancies, trading cross-exchange spreads, or finding risk-free opportunities.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# Arbitrage Trading

Arbitrage profits from price differences of the same asset across different markets.

## Arbitrage Types

### 1. Cross-Exchange Arbitrage

- Same asset, different exchanges
- Buy on Exchange A (lower price)
- Sell on Exchange B (higher price)

### 2. Triangular Arbitrage

- Three trading pairs form a cycle
- Example: BTC → ETH → USDT → BTC
- Profit from pricing inefficiency

### 3. Futures-Spot Arbitrage

- Difference between spot and futures price
- "Cash and carry" trade
- Collect premium over time

### 4. DEX-CEX Arbitrage

- Price difference between DEX and CEX
- Often larger spreads
- Gas fees are significant cost

## Cross-Exchange Example

| Exchange   | BTC Price   |
| ---------- | ----------- |
| Exchange A | $50,000     |
| Exchange B | $50,200     |
| Spread     | $200 (0.4%) |

Profit = $200 - (Fees + Transfer costs)

## Requirements

| Requirement             | Why                      |
| ----------------------- | ------------------------ |
| Funds on both exchanges | No waiting for transfers |
| Low-latency connection  | Speed matters            |
| Fee consideration       | Must exceed total fees   |
| Volume assessment       | Ensure liquidity         |

## Challenges

| Challenge      | Mitigation                |
| -------------- | ------------------------- |
| Transfer time  | Pre-fund both sides       |
| Slippage       | Check order book depth    |
| Fees           | Calculate all costs first |
| Execution risk | Use limit orders          |

## Profitability Check

Use `get_latest_candle` to fetch current prices across pairs, then calculate net profit manually.

**Cross-Exchange Arbitrage:**

- Gross Spread = Sell Price - Buy Price
- Total Fees = (Buy Price x Buy Fee Rate) + (Sell Price x Sell Fee Rate) + Transfer Cost
- Net Profit = Gross Spread - Total Fees

**Triangular Arbitrage:**

- Expected cross rate = Price A / Price B
- Actual cross rate = observed market rate
- Spread % = (Actual - Expected) / Expected x 100

Only trade if Net Profit > 0

## Best Practices

1. **Pre-fund exchanges** (avoid transfer delays)
2. **Use trading bots** (speed advantage)
3. **Monitor continuously** (opportunities are brief)
4. **Account for all costs** (fees, spreads, gas)
5. **Start small** (test execution)

## Triangular Arbitrage Example

BTC/USDT: 50,000
ETH/USDT: 2,000
ETH/BTC: 0.041

Expected ETH/BTC: 2000/50000 = 0.040
Actual: 0.041

Path: USDT → BTC → ETH → USDT
Profit: ~2.5% (before fees)

## Key Insight

Pure arbitrage is "risk-free" profit in theory. In practice, execution risk, fees, and timing make it challenging. Most profitable for those with speed and capital advantages.

## Related Skills

- **funding-rate-trading** — Funding rate arbitrage (spot + perp) is a specific crypto arbitrage strategy
- **correlation-risk** — Arbitrage positions must account for correlation risk when legs are in different but related assets
- **leverage-management** — Leveraged arbitrage amplifies both the small spreads and the execution risk
