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

Skills may reference tools available to AI analysts. Always include required parameters.

### Market data

| Tool                      | Signature                                                                         | Notes                                                              |
| ------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `get_candles`             | `get_candles(symbol, exchange, interval, count=1)`                                | Last N candles (1–200). `count=1` for spot price, `count>1` for context. |
| `get_candles_around_date` | `get_candles_around_date(symbol, exchange, interval, date)`                       | 21 candles centered on a target date.                              |
| `get_specific_candle_data`| `get_specific_candle_data(symbol, exchange, interval, timestamp)`                 | Nearest candle to a unix timestamp.                                |
| `get_indicators`          | `get_indicators(indicator_code, symbol, exchange, interval, count=1)`             | One indicator per call. `count>1` returns history for slope/divergence. |
| `view_chart`              | `view_chart(symbol, exchange, interval, from_date?, to_date?)`                    | Renders a candlestick chart image (vision-capable models).         |
| `get_order_flow`          | `get_order_flow(symbol, interval, lookback=50)`                                   | Binance taker buy/sell + delta + CVD (crypto only).                |

### Research

| Tool                      | Signature                                                                         | Notes                                                              |
| ------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `get_financial_news`      | `get_financial_news(topic, time_range?, max_results=10, fetch_content=False)`     | `time_range` is `"day" | "week" | "month"`.                        |
| `get_fundamentals`        | `get_fundamentals(ticker, data_type="overview")`                                  | `data_type` selects overview, valuation, earnings, etc.            |
| `get_economics_calendar`  | `get_economics_calendar(from_date, to_date, country?, impact?, event?)`           | Dates are `YYYY-MM-DD`. `impact` is `"High" | "Medium" | "Low"`.   |
| `get_social_media_sentiment` | `get_social_media_sentiment(ticker)`                                           | Reddit-based sentiment counts.                                     |
| `get_user_watchlist`      | `get_user_watchlist()`                                                            | User's favorited tickers.                                          |

### Signals & risk

| Tool                      | Signature                                                                         | Notes                                                              |
| ------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `preview_position_size`   | `preview_position_size(symbol, side, entry, stop_loss, risk_usd?, risk_pct?)`     | Advisory sizing — no order placed.                                 |
| `get_portfolio_risk_state`| `get_portfolio_risk_state()`                                                      | Balance, margin used, committed risk, remaining R budget.          |
| `get_user_trading_insights`| `get_user_trading_insights(ticker?, status?, trade_type?)`                       | Lists active/executed/closed signals.                              |
| `create_trading_insight`  | `create_trading_insight(symbol, side, entry, stop_loss, take_profits, trade_type, risk_usd?, notes?)` | Creates a signal; user-approval required.                          |
| `update_trading_insight`  | `update_trading_insight(signal_id, entry?, stop_loss?, take_profits?, status?, notes?)` | Edit a pending insight.                                            |

### Chart drawing & UI

| Tool                      | Signature                                                                         | Notes                                                              |
| ------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `draw_chart_analysis`     | `draw_chart_analysis(action, drawing={type, points, options})`                    | Types: `demand`, `supply`, `consolidation`, `breakout`, `support`, `resistance`, `level`, `trend`, `fib_retracement`, `highlight`. All require 2 points. |
| `draw_position`           | `draw_position(action, drawing={type, points, options})`                          | Types: `long_position`, `short_position`. `options.stopLoss`/`takeProfit` are raw prices. |
| `change_user_chart`       | `change_user_chart(symbol, exchange?, interval?)`                                 | Switches the live chart view.                                      |
| `request_chart_screenshot`| `request_chart_screenshot(reason)`                                                | HITL — pauses for the user's live TradingView screenshot.          |

### Agent-run tools

| Tool                      | Signature                                                                         | Notes                                                              |
| ------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `execute_trade`           | `execute_trade(signal_id)`                                                        | Executes a pending insight at market.                              |
| `close_position`          | `close_position(signal_id, exit_price, reason)`                                   | Closes an open position.                                           |
| `adjust_stop_loss`        | `adjust_stop_loss(signal_id, new_stop_loss, reason)`                              | Tighten only (long can only raise, short can only lower).          |
| `adjust_take_profit`      | `adjust_take_profit(signal_id, take_profits, reason)`                             |                                                                    |
| `cancel_signal`           | `cancel_signal(signal_id, reason)`                                                | Cancel before execution.                                           |
| `write_artifact`          | `write_artifact(content)`                                                         | Replace the running agent's persistent markdown artifact.          |
| `create_price_trigger`    | `create_price_trigger(symbol, trigger_price, direction, action, specialist_profile?, specialist_task?, wake_note?, ...)` | On a crossing, either delegate a bounded specialist or wake the owning agent. `action` is `"specialist"` or `"wake_agent"`. |
| `delegate_to_specialist`  | `delegate_to_specialist(profile, name, task, schedule="now", ...)`               | Delegate one bounded assignment to a fixed-profile specialist. Durable agents only; specialists cannot nest. |
| `send_notification`       | `send_notification(title, body, type?)`                                           | Push to user.                                                      |

Public tool and prompt text must use agent, agent run, and specialist. Retired
spawn/mini names may remain in Park's internal Python filenames but must not be
introduced into skills.

### Code execution

The `execute` tool runs shell commands in a restricted sandbox (PATH scrubbed to `/usr/local/bin:/usr/bin:/bin`, `PYTHONPATH` cleared). Use it for slope/divergence math that isn't already an indicator and for short numpy/pandas snippets. Reach for `get_indicators` first — it returns pre-computed values and caches.

```
execute python3 -c "ema=[<ema_50_history>]; s=(ema[-1]-ema[-5])/ema[-5]*100; print(f'slope_pct={s:.3f}')"
```

**Exchange parameter:** `exchange` is REQUIRED for `get_candles`, `get_candles_around_date`, `get_specific_candle_data`, `get_indicators`, and `view_chart`. Use the venue name (lowercase) — e.g., `"binance"` for crypto, `"nasdaq"` / `"nyse"` for stocks, and `"global"` for forex / commodities / indices that don't trade on a specific venue.

**Rules:**
- Always include all required parameters in tool examples (use `<symbol>` / `<exchange>` / `<interval>` placeholders when context-dependent).
- Reference only tools the agent actually has access to. For cross-domain needs, use delegation notes: "The orchestrator handles position sizing and signal creation."
- Prefer the canonical tool name over phrasing it generically — agents grep on tool names.
