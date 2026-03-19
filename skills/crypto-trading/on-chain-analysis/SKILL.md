---
name: on-chain-analysis
description: Analyze blockchain data for trading signals (whale movements, exchange flows). Use when understanding smart money, detecting accumulation/distribution, or confirming macro trends.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["all"]
---

# On-Chain Analysis

On-chain analysis examines blockchain data to understand market participant behavior.

## Key On-Chain Metrics

### Exchange Flows

| Metric            | Bullish             | Bearish        |
| ----------------- | ------------------- | -------------- |
| Exchange inflow   | Low                 | High (selling) |
| Exchange outflow  | High (accumulation) | Low            |
| Exchange reserves | Decreasing          | Increasing     |

### Wallet Activity

| Metric                  | Bullish    | Bearish    |
| ----------------------- | ---------- | ---------- |
| Whale accumulation      | High       | Low        |
| Long-term holder supply | Increasing | Decreasing |
| Active addresses        | Growing    | Declining  |

### Network Health

| Metric             | Bullish    | Bearish    |
| ------------------ | ---------- | ---------- |
| Hash rate          | Increasing | Decreasing |
| Transaction volume | Growing    | Stagnant   |
| New addresses      | Growing    | Declining  |

## Trading Signals

### 1. Exchange Outflow Signal

- Large outflows = Accumulation
- Coins moving to cold storage
- Bullish medium-term

### 2. Whale Alert

- Large transactions (>1000 BTC) to exchange = Potential sell
- Large transactions to wallet = Accumulation
- Context matters

### 3. Long-Term Holder Behavior

- LTH supply increasing = Accumulation phase
- LTH selling = Distribution phase
- Often precedes major moves

### 4. Miner Activity

- Miners accumulating = Bullish
- Miners selling heavily = Need to cover costs (bearish)
- Post-halving watch

## Workflow

1. **Check exchange flows** (net inflow/outflow)
2. **Monitor whale wallets** (large transactions)
3. **Assess holder behavior** (LTH vs STH)
4. **Combine with price action**
5. **Form macro thesis**

## Popular Tools

- Glassnode
- CryptoQuant
- IntoTheBlock
- Santiment
- Whale Alert

## Specific Metric Thresholds

Actionable thresholds for key on-chain metrics:

| Metric | Bullish Threshold | Bearish Threshold | Neutral Range |
| --- | --- | --- | --- |
| Exchange Net Flow | <-10K BTC/day outflow | >10K BTC/day inflow | -10K to +10K |
| Whale Txns (>1000 BTC) | Majority to cold wallets | Majority to exchanges | Mixed |
| LTH Supply Change (30d) | >+50K BTC | <-50K BTC | ±50K |
| Active Addresses (vs 30d avg) | >120% of average | <80% of average | 80-120% |

Use these thresholds to classify current conditions as bullish, bearish, or neutral for each metric. When 3+ metrics align in the same direction, the signal is high-confidence.

## MVRV Ratio (Market Value to Realized Value)

MVRV measures whether the market is overvalued or undervalued relative to the aggregate cost basis of all coins.

- **Formula**: MVRV = Market Cap / Realized Cap
- **Realized Cap** = sum of each UTXO valued at its last moved price (aggregate cost basis)

### Interpretation Zones

| MVRV Range | Interpretation | Action |
| --- | --- | --- |
| > 3.5 | Market significantly overvalued — distribution zone | Reduce exposure, take profits |
| 1.0 - 3.5 | Normal range | Standard position sizing |
| < 1.0 | Market below aggregate cost basis — accumulation zone | Historically excellent buy zone |

### Historical Context

- Market tops have historically occurred at MVRV 3.5-4.0
- Market bottoms have historically occurred at MVRV 0.7-1.0
- MVRV returning to 1.0 from below = macro bottom confirmation

## NVT Signal (Network Value to Transactions)

NVT measures whether the network is overvalued or undervalued relative to its actual usage (transaction throughput).

- **Formula**: NVT = Market Cap / Daily Transaction Volume (in USD)

### Interpretation Zones

| NVT Range | Interpretation | Signal |
| --- | --- | --- |
| > 95 | Network overvalued relative to usage | Bearish |
| 45 - 95 | Normal range | Neutral |
| < 45 | Network undervalued relative to usage | Bullish |

### Notes

- **Smoothed NVT Signal** (90-day MA of transaction volume) is more reliable than raw NVT for filtering noise
- NVT spikes can occur during low-activity weekends — use multi-day averages
- NVT works best as a macro indicator, not for short-term timing

## Realized Cap Analysis

Realized Cap represents the aggregate cost basis of all market participants. The relationship between Market Cap and Realized Cap reveals aggregate profit/loss conditions.

### Key Relationships

- **Market Cap > Realized Cap** → Aggregate profit across holders → Risk of distribution (selling to lock in gains)
- **Market Cap < Realized Cap** → Aggregate loss across holders → Accumulation opportunity (capitulation selling exhausted)

### Realized Cap as Support/Resistance

- Realized Cap acts as a macro support/resistance level for Market Cap
- **Market Cap bouncing off Realized Cap** = macro bottom signal (holders refuse to sell at a loss)
- **Market Cap falling below Realized Cap** = deep capitulation (rare, historically the best accumulation zone)

### Unrealized Profit Gap

- Track the gap between Market Cap and Realized Cap
- **Widening gap** = increasing unrealized profit = increasing sell pressure risk
- **Narrowing gap** = profits being taken or prices declining = approaching equilibrium
- **Gap inversion** (Market Cap < Realized Cap) = maximum fear, minimum sell pressure from remaining holders

## Enhanced Workflow

Since the technical analyst does not have direct access to on-chain data APIs, combine the on-chain framework knowledge from this skill with available technical tools:

### Step-by-Step Process

1. **Check current BTC price** to establish baseline:
```
get_latest_candle(symbol="BTCUSDT")
```

2. **Assess momentum and trend** with technical indicators for confirmation:
```
get_indicator(symbol="BTCUSDT", indicator="RSI", interval="1d")
get_indicator(symbol="BTCUSDT", indicator="MACD", interval="1d")
```

3. **Visualize price action** to identify key levels:
```
generate_chart(symbol="BTCUSDT", interval="1d")
```

4. **Apply on-chain framework** from this skill:
   - Estimate MVRV zone based on price relative to historical realized price levels
   - Assess whether current price action aligns with accumulation or distribution patterns
   - Consider NVT implications based on network activity trends
   - Factor in known exchange flow and whale behavior patterns

5. **Mark key on-chain derived levels** on the chart:
```
draw_chart_analysis(action="create", drawing={...})
```
   - Mark estimated realized price as macro support
   - Mark MVRV overvaluation zones as resistance
   - Annotate accumulation/distribution zones

6. **Report macro thesis to orchestrator** with:
   - Current on-chain regime assessment (accumulation, distribution, or neutral)
   - Technical confirmation status (do indicators align with on-chain thesis?)
   - Key price levels derived from on-chain framework
   - Confidence level based on metric alignment

## Limitations

| Limitation      | Reality                                    |
| --------------- | ------------------------------------------ |
| Lagging         | On-chain data often confirms, not predicts |
| Context needed  | Large transfer could be internal           |
| Not timing tool | Better for macro, not day trading          |

## Best Use

On-chain is best for:

- Macro positioning (accumulation zones)
- Confirming trend changes
- Understanding smart money behavior
- Long-term investment decisions

Less useful for:

- Day trading
- Short-term timing
- Quick trades

## Related Skills

- **altcoin-rotation** — On-chain metrics confirm market cycle phases that drive altcoin rotation decisions
- **dca-strategy** — MVRV and realized cap analysis identify macro accumulation zones for enhanced DCA timing
- **market-regime-detection** — On-chain regime assessment complements technical regime detection for crypto markets
