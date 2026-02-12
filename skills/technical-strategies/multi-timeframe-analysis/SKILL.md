---
name: multi-timeframe-analysis
description: Analyze markets using 3 timeframes (higher, primary, lower) for confluence. Use when determining trend direction, timing entries with precision, or validating trade setups across timeframes.
---

# Multi-Timeframe Analysis (MTF)

Analyze 3 timeframes to align trend, structure, and entry for high-probability trades.

## Timeframe Selection

| Primary TF | Higher TF | Lower TF | Use Case         |
| ---------- | --------- | -------- | ---------------- |
| 1D         | Weekly    | 4H       | Position trading |
| 4H         | 1D        | 1H       | Swing trading    |
| 1H         | 4H        | 15m      | Intraday swing   |
| 15m        | 1H        | 5m       | Day trading      |

## Timeframe Roles

| Role        | Purpose         | Analysis Focus   |
| ----------- | --------------- | ---------------- |
| **Higher**  | Trend direction | Major S/R, bias  |
| **Primary** | Trade structure | Patterns, setups |
| **Lower**   | Entry timing    | Precise entries  |

## Analysis Workflow

### Step 1: Higher Timeframe (Bias)

1. Generate chart with `generate_chart`
2. Identify trend: HH/HL (bull) or LH/LL (bear)
3. Mark major S/R zones
4. Determine bias: Bullish, Bearish, or Ranging

### Step 2: Primary Timeframe (Setup)

1. Generate chart for primary TF
2. Find trade setups aligned with HTF bias
3. Identify patterns, order blocks, FVGs
4. Mark key levels using `draw_chart_analysis`

### Step 3: Lower Timeframe (Entry)

1. Wait for price to reach setup zone
2. Look for LTF confirmation (BOS, rejection)
3. Execute entry with tight stop

## Confluence Scoring

| Alignment      | Score  | Action                |
| -------------- | ------ | --------------------- |
| All 3 TF agree | High   | Trade with confidence |
| 2 TF agree     | Medium | Trade with caution    |
| TFs conflict   | Low    | Wait or skip          |

## Common Mistakes

- Trading LTF against HTF trend
- Skipping HTF analysis
- Over-analyzing (paralysis)

## Key Rule

**Trade in HTF direction, enter on LTF confirmation.**
