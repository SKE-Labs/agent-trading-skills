---
name: skill-name
description: What this skill does and when to use it. Use when [trigger condition 1], [trigger condition 2], or [trigger condition 3].
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Skill Title

Brief one-line introduction.

## Identification

How to identify the pattern, setup, or condition:

1. **Step one** — Description
2. **Step two** — Description
3. **Step three** — Description

| Parameter | Value | Notes |
| --------- | ----- | ----- |
| Level 1   | X%    | Usage |
| Level 2   | Y%    | Usage |

## Workflow

### 1. Get Data

```
get_indicator(indicator_code="rsi", symbol=<symbol>, interval=<interval>)
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

Provide structured summary: setup, confidence, key levels (entry, stop, target), indicator values, risk flags.

## Key Rules

- Rule 1
- Rule 2
- NEVER: Critical mistake to avoid and why

## Related Skills

- **skill-name** — relationship note
- **skill-name** — relationship note
