---
name: leverage-management
description: Use leverage safely based on volatility and account size. Use when trading derivatives, managing margin, or sizing leveraged positions.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "2.0"
---

# Leverage Management

Leverage amplifies both gains and losses -- use it responsibly.

## Leverage Basics

| Leverage | $1,000 Controls | Exposure |
| -------- | ---------------- | -------- |
| 1x       | $1,000           | None     |
| 5x       | $5,000           | 5x       |
| 10x      | $10,000          | 10x      |
| 100x     | $100,000         | 100x     |

## Safe Leverage by Volatility

| Volatility Level       | Max Leverage |
| ---------------------- | ------------ |
| Low (Forex majors)     | 10-20x       |
| Medium (Crypto majors) | 3-5x         |
| High (Altcoins)        | 1-2x         |
| Extreme (Memes)        | 1x or none   |

## Leverage by Trading Style

| Style            | Recommended                   |
| ---------------- | ----------------------------- |
| Scalping         | Can use higher (faster exits) |
| Day Trading      | 3-10x depending on asset      |
| Swing Trading    | 1-3x (overnight risk)         |
| Position Trading | 1-2x (long exposure)          |

## Key Formulas

**Effective Leverage**: `Position Size / Account Equity`

Example: $50,000 position on $10,000 equity = 5x effective leverage.

**Liquidation Distance**: `100% / Leverage`

Example: 10x leverage = liquidated at 10% move against position.

**Position sizing with leverage**: `Position Size = (Account x Risk%) / Stop Distance%`. Leverage does not change how much you risk -- it changes how much capital you tie up.

## Impact of Leverage on Losses

| Leverage | 1% Move Against | Account Impact      |
| -------- | --------------- | ------------------- |
| 1x       | -1%             | -1%                 |
| 5x       | -1%             | -5%                 |
| 10x      | -1%             | -10%                |
| 100x     | -1%             | -100% (liquidation) |

## Liquidation Awareness

| Leverage | Approx. Liquidation Distance |
| -------- | ---------------------------- |
| 5x       | 20% against                  |
| 10x      | 10% against                  |
| 20x      | 5% against                   |
| 100x     | 1% against                   |

Always set stops BEFORE the liquidation level.

## Workflow

1. **Assess volatility** of the asset being traded
2. **Select max leverage** based on volatility table above
3. **Calculate effective leverage** -- position size / equity
4. **Verify liquidation distance** -- must be well beyond your stop loss
5. **Maintain margin buffer** -- keep 50%+ margin ratio at all times
6. **Reduce** leverage in volatile conditions or after losses

## Key Rules

- NEVER risk more than 2% of account even with leverage
- NEVER use max available leverage -- use 50% or less of what the platform offers
- NEVER hold high leverage into major news events or overnight (for day trades)
- Calculate liquidation price before every leveraged entry
- Start with low leverage (2-3x max) and increase only with proven edge
- Reduce leverage after losses -- do not increase it to recover

## Related Skills

- **position-sizing** -- leverage changes capital allocation but not risk amount
- **stop-loss-strategies** -- stops must be set before liquidation price
