---
name: leverage-management
description: Use leverage safely based on volatility and account size. Use when trading derivatives, managing margin, or sizing leveraged positions.
---

# Leverage Management

Leverage amplifies both gains and losses—use it responsibly.

## Leverage Basics

| Leverage | $1,000 Account           | $10,000 Position |
| -------- | ------------------------ | ---------------- |
| 1x       | $1,000 controls $1,000   | No leverage      |
| 5x       | $1,000 controls $5,000   | 5x exposure      |
| 10x      | $1,000 controls $10,000  | 10x exposure     |
| 100x     | $1,000 controls $100,000 | 100x exposure    |

## Safe Leverage Guidelines

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

## Effective Leverage Calculation

Use the `execute` tool to calculate effective leverage and liquidation price:

**Effective Leverage:**
```
execute(command='python3 -c "pos_size=50000;equity=10000;eff_lev=pos_size/equity;print(f\"Position: \${pos_size:,}\\nEquity: \${equity:,}\\nEffective Leverage: {eff_lev:.1f}x\")"')
```

**Liquidation Distance:**
```
execute(command='python3 -c "leverage=10;liq_dist=100/leverage;print(f\"Leverage: {leverage}x\\nLiquidation at: {liq_dist:.1f}% against position\")"')
```

Even without explicit leverage, position sizing creates effective leverage.

## Risk with Leverage

| Leverage | 1% Move Against | Account Impact      |
| -------- | --------------- | ------------------- |
| 1x       | -1%             | -1%                 |
| 5x       | -1%             | -5%                 |
| 10x      | -1%             | -10%                |
| 100x     | -1%             | -100% (liquidation) |

## Leverage Risk Rules

1. **Calculate liquidation price** before entering
2. **Never risk more than 2%** even with leverage
3. **Reduce leverage** in volatile conditions
4. **Maintain margin buffer** (50%+ margin ratio)
5. **Avoid max leverage** (use 50% or less of available)

## Position Sizing with Leverage

```
Position Size = (Account × Risk %) / (Stop Distance %)
```

Leverage doesn't change how much you risk—it changes how much capital you tie up.

## Liquidation Awareness

| Leverage | Approx. Liquidation Distance |
| -------- | ---------------------------- |
| 5x       | 20% against                  |
| 10x      | 10% against                  |
| 20x      | 5% against                   |
| 100x     | 1% against                   |

Always set stops BEFORE liquidation level.

## Best Practices

- Start with low leverage (2-3x max)
- Increase only with proven edge
- Never max out available leverage
- Reduce leverage after losses
- Journal leverage impact on results
