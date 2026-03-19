---
name: altcoin-rotation
description: Rotate between BTC, ETH, and altcoins based on market cycles. Use when optimizing portfolio allocation, riding altcoin seasons, or managing crypto exposure.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]
  market_conditions: ["trending"]
---

# Altcoin Rotation Strategy

Rotate between BTC, ETH, and altcoins based on market cycles and dominance trends.

## Market Cycle Phases

| Phase        | BTC Dominance  | Strategy              |
| ------------ | -------------- | --------------------- |
| BTC Season   | Rising (>50%)  | Hold BTC, reduce alts |
| Transition   | Stable         | Begin alt exposure    |
| ALT Season   | Falling (<45%) | Increase alt exposure |
| Capitulation | Spike high     | Cash or BTC only      |

## BTC Dominance Guide

| Dominance  | Market State  | Action                |
| ---------- | ------------- | --------------------- |
| >55%       | BTC dominant  | 80%+ in BTC           |
| 50-55%     | Transitioning | Start adding ETH      |
| 45-50%     | Alt friendly  | Add quality alts      |
| <45%       | Alt season    | Maximize alt exposure |
| Spiking up | Risk-off      | Exit alts to BTC      |

## Rotation Workflow

### 1. Accumulation Phase (Bear Market)

- Focus on BTC and ETH
- DCA into quality only
- Avoid altcoins

### 2. Early Bull (BTC Rally)

- 70% BTC, 25% ETH, 5% alts
- Wait for BTC to stabilize
- Research alt candidates

### 3. Mid Bull (Alt Season Start)

- 40% BTC, 30% ETH, 30% alts
- Rotate into strong altcoin narratives
- Take profits on 2-3x moves

### 4. Late Bull (Peak Alt Season)

- 20% BTC, 20% ETH, 60% alts
- Highest risk, highest reward
- Tight stops, quick profits

### 5. Distribution (Topping)

- Rotate back to BTC/ETH
- Exit altcoins progressively
- Increase stablecoin position

## Alt Selection Criteria

| Factor     | Look For              |
| ---------- | --------------------- |
| Market cap | Top 50 for safety     |
| Narrative  | Strong use case/trend |
| Volume     | High liquidity        |
| Technical  | Breaking out of base  |

## Risk Management

| Rule           | Guideline                |
| -------------- | ------------------------ |
| Single alt max | 10% of portfolio         |
| Total alts max | 30-60% (cycle dependent) |
| Stop losses    | Always set               |
| Profit taking  | Scale out at targets     |

## Key Signals

Watch for rotation triggers:

- BTC consolidating after rally → Alt rotation
- BTC dominance falling → Alt season
- ETH/BTC rising → Risk-on for alts
- BTC breaking down → Exit all alts

## Common Mistakes

- Holding alts through BTC correction
- Chasing pumped altcoins
- Over-allocating to micro-caps
- Not taking profits during alt season

## Related Skills

- **on-chain-analysis** — On-chain metrics (exchange flows, whale behavior) confirm accumulation/distribution phases in the rotation cycle
- **sector-rotation** — Similar rotation concept applied to crypto market cycles instead of economic sectors
- **dca-strategy** — DCA into BTC/ETH during accumulation phases provides disciplined entry during bear markets
