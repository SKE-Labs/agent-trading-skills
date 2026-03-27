---
name: altcoin-rotation
description: Rotate between BTC, ETH, and altcoins based on market cycles. Use when optimizing portfolio allocation, riding altcoin seasons, or managing crypto exposure.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Altcoin Rotation Strategy

Rotate between BTC, ETH, and altcoins based on market cycle phase and BTC dominance trends.

## Market Cycle Phases

| Phase        | BTC Dominance  | Strategy              | Allocation             |
| ------------ | -------------- | --------------------- | ---------------------- |
| Accumulation | High (>55%)    | BTC/ETH only, DCA     | 80% BTC, 20% ETH      |
| Early Bull   | Stable (50-55%)| Begin alt research    | 70% BTC, 25% ETH, 5%  |
| Mid Bull     | Falling (45-50%)| Rotate into alts     | 40% BTC, 30% ETH, 30% |
| Peak Alt     | Low (<45%)     | Max alt exposure      | 20% BTC, 20% ETH, 60% |
| Distribution | Spiking up     | Exit alts, back to BTC| Reduce to BTC/stables  |

## Alt Selection Criteria

| Factor     | Look For              |
| ---------- | --------------------- |
| Market cap | Top 50 for safety     |
| Narrative  | Strong use case/trend |
| Volume     | High liquidity        |
| Technical  | Breaking out of base  |

## Workflow

1. **Check BTC dominance trend** using news and price data:
```
get_financial_news(query="BTC dominance altcoin season")
get_latest_candle(symbol="BTCUSDT")
```

2. **Assess momentum** to identify cycle phase:
```
get_indicator(indicator_code="rsi", symbol="BTCUSDT", interval="1d")
get_indicator(indicator_code="rsi", symbol="ETHUSDT", interval="1d")
```

3. **Evaluate ETH/BTC ratio** as alt season proxy:
```
get_latest_candle(symbol="ETHBTC")
```

4. **Screen alt candidates** matching selection criteria:
```
get_financial_news(query="top performing altcoins crypto narrative")
```

5. **Report allocation recommendation** with cycle phase, dominance trend, and suggested weights.

## Key Rules

- NEVER hold alts through a BTC correction -- rotate back to BTC at first dominance spike
- NEVER over-allocate to a single alt (cap at 10% of portfolio)
- NEVER chase altcoins that have already pumped 3x+ without consolidation
- Take profits on 2-3x alt moves; scale out, do not wait for tops
- Rotation triggers: BTC consolidating after rally, dominance falling, ETH/BTC rising

## Related Skills

- **on-chain-analysis** -- on-chain metrics confirm accumulation/distribution phases
- **dca-strategy** -- DCA into BTC/ETH during accumulation phases
