---
name: arbitrage-trading
description: Exploit price differences across exchanges or trading pairs. Use when spotting price discrepancies, trading cross-exchange spreads, or finding risk-free opportunities.
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

Use the `execute` tool to calculate net profit:

**Cross-Exchange Arbitrage:**
```
execute(command='python3 -c "buy=50000;sell=50200;buy_fee=0.001;sell_fee=0.001;transfer=5;amount=1;gross=sell-buy;fees=(buy*buy_fee)+(sell*sell_fee)+transfer;net=gross-fees;print(f\"Spread: \${gross:.2f}\\nFees: \${fees:.2f}\\nNet Profit: \${net:.2f} ({net/buy*100:.3f}%)\")"')
```

**Triangular Arbitrage:**
```
execute(command='python3 -c "btc_usdt=50000;eth_usdt=2000;eth_btc=0.041;expected=eth_usdt/btc_usdt;actual=eth_btc;spread=(actual-expected)/expected*100;print(f\"Expected ETH/BTC: {expected:.4f}\\nActual: {actual:.4f}\\nSpread: {spread:.2f}%\")"')
```

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
