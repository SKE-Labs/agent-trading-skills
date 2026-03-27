# Trading Skills Specification

Trading skills are structured knowledge modules that teach AI agents how to analyze markets, identify trading setups, manage risk, and generate actionable insights.

## Skill Structure

Each skill lives in its own folder with a `SKILL.md` file:

```
skills/
└── category-name/
    └── skill-name/
        ├── SKILL.md           # Required
        ├── references/        # Optional: detailed docs
        └── assets/            # Optional: templates, images
```

## Required Fields

Every `SKILL.md` must include YAML frontmatter with:

| Field         | Description                                                        |
| ------------- | ------------------------------------------------------------------ |
| `name`        | Unique identifier (lowercase, hyphens for spaces)                  |
| `description` | What the skill does and **when to use it** (trigger conditions)    |
| `license`     | License identifier (e.g., `Apache-2.0`)                            |

Optional metadata:

| Field              | Description                        |
| ------------------ | ---------------------------------- |
| `metadata.author`  | Skill author                       |
| `metadata.version` | Semantic version string            |

### Description Best Practices

The `description` field appears in the agent's "Available Skills" prompt section and determines when a skill is loaded. It must clearly state:

1. **What** the skill does
2. **When** the agent should use it (trigger conditions)

**Good:**
```yaml
description: Identify bullish and bearish order blocks where institutional orders were executed. Use when analyzing price action for high-probability entry zones, detecting smart money accumulation/distribution, or finding areas where price may react on retest.
```

**Weak:**
```yaml
description: A skill for order blocks trading.
```

## Recommended Sections

| Section            | Purpose                                        |
| ------------------ | ---------------------------------------------- |
| **Identification** | How to identify the pattern or setup            |
| **Workflow**       | Step-by-step procedure with tool integration    |
| **Key Rules**      | Compact bullets: critical rules + "NEVER:" items |
| **Related Skills** | Max 2 items, one line each                      |

## Verbosity Guidelines

- **Target: 60-100 lines** per skill. Max ~120 lines for complex skills.
- **One-line intro** — no multi-paragraph theory.
- **Compact tables** over prose for parameters, levels, and criteria.
- **Merge, don't separate** — combine entry strategy and workflow into one section.
- **No standalone "Common Mistakes" or "Best Practices" sections.** Merge critical items into Key Rules as "NEVER:" bullets.
- **No theoretical content the agent cannot act on** (e.g., formulas requiring APIs the agent lacks).
- **No generic risk management advice** in non-risk skills ("1-2% per trade" belongs in the position-sizing skill, not repeated everywhere).
- **Related Skills:** max 2 items, one line each: `- **skill-name** — relationship note`

## Tool References

Skills may reference tools available to AI analysts. Always include required parameters:

| Tool                      | Signature                                                           | Purpose                                      |
| ------------------------- | ------------------------------------------------------------------- | -------------------------------------------- |
| `get_indicator`           | `get_indicator(indicator_code, symbol, interval)`                   | Technical indicator values (RSI, MACD, etc.) |
| `get_candles_around_date` | `get_candles_around_date(symbol, interval, date)`                   | 21 candles around a target date              |
| `get_latest_candle`       | `get_latest_candle(symbol)`                                         | Current price data                           |
| `generate_chart`          | `generate_chart(symbol, interval)`                                  | Candlestick chart images                     |
| `draw_chart_analysis`     | `draw_chart_analysis(action, drawing={type, points, options})`      | Draw zones, levels, trends, fib on chart     |
| `draw_position`           | `draw_position(action, drawing={type, points, options})`            | Draw long/short position markers             |
| `get_financial_news`      | `get_financial_news(topic, max_results)`                            | Financial news from trusted sources          |
| `get_fundamentals`        | `get_fundamentals(ticker)`                                          | Stock fundamentals (valuation, earnings)     |
| `get_economics_calendar`  | `get_economics_calendar(from_date, to_date, impact)`                | Economic events (NFP, CPI, FOMC)             |
| `calculate_position_size` | `calculate_position_size(symbol, entry_price, stop_loss)`           | Risk-based position sizing                   |

**Rules:**
- Skills must **NEVER** reference `execute()` or any code execution tool. These do not exist. Use inline formulas or reference the appropriate tool above.
- Always include `symbol` and `interval` parameters in tool call examples (use `<symbol>` and `<interval>` as placeholders when context-dependent).
- Reference only tools the agent actually has access to. For cross-domain needs, use delegation notes: "The orchestrator handles position sizing and signal creation."
