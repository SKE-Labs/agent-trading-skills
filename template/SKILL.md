---
name: skill-name
description: What this skill does and when to use it. Use when [trigger condition 1], [trigger condition 2], or [trigger condition 3].
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
  target_agents: ["*"]  # Wildcard = available to all agents
  market_conditions: ["trending"]       # trending, ranging, volatile, all
---

# Skill Title

Brief introduction explaining the concept.

<!--
  TOOL BOUNDARY RULES:
  Skills must ONLY reference tools available to the target agent:

  technical_analyst: get_indicator, get_candles_around_date, get_specific_candle_data,
                     draw_chart_analysis, generate_chart, get_latest_candle
  fundamental_analyst: get_financial_news, get_fundamentals, get_economics_calendar
  orchestrator: calculate_position_size, draw_position, create_trading_signal,
                update_trading_signal, generate_chart, get_latest_candle,
                get_financial_news, get_economics_calendar, memory tools, spawn tools

  For cross-domain needs, use delegation notes:
  "The orchestrator handles position sizing and signal creation."
  "The technical analyst provides chart analysis and indicator data."
  "The fundamental analyst researches news and economic context."
-->

## Identification

How to identify the pattern, setup, or condition:

1. **Step one** — Description
2. **Step two** — Description
3. **Step three** — Description

## Key Levels / Parameters

| Parameter | Value | Notes |
| --------- | ----- | ----- |
| Level 1   | X%    | Usage |
| Level 2   | Y%    | Usage |

## Entry Strategy

1. **Identify setup** using the criteria above
2. **Wait for confirmation** (rejection candle, structure break, etc.)
3. **Enter position** with defined risk
4. **Set stop loss** at [specific level]
5. **Set targets** at [target levels]

## Risk Management

| Rule           | Guideline       |
| -------------- | --------------- |
| Stop loss      | X pips/% beyond |
| Risk per trade | 1-2% max        |
| Risk:Reward    | Minimum 1:2     |

## Workflow

Include concrete tool call examples (match the fibonacci-trading style):

### 1. Get Data

```
get_indicator(indicator="rsi")
```

### 2. Analyze

Describe what to look for in the data.

### 3. Mark on Chart

```
draw_chart_analysis(action="create", drawing={
    "type": "support",
    "points": [
        {"time": <timestamp>, "price": <price>},
        {"time": <timestamp>, "price": <price>}
    ],
    "options": {"text": "Label"}
})
```

### 4. Report to Orchestrator

Provide structured summary including:
- Setup identified and confidence level
- Key levels (entry, stop, target)
- Relevant indicator values
- Any risk flags or caveats

## Best Practices

| Do                      | Don't                |
| ----------------------- | -------------------- |
| Wait for confirmation   | Enter blindly        |
| Use multiple timeframes | Trade single TF only |
| Follow risk rules       | Oversize positions   |

## Common Mistakes

- Mistake 1 and why it's problematic
- Mistake 2 and why it's problematic

## Related Skills

- **skill-name** — How it complements this skill
- **skill-name** — How it complements this skill
- **market-regime-detection** — Verify this strategy fits current market conditions
