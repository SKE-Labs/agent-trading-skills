---
name: kill-zones
description: Analyze intraday session seasonality and test time-window filters. Use when timing a strategy around exchange, London, New York, or Asian trading sessions with correct timezone and daylight-saving handling.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "4.0"
---

# Kill Zones Trading

Named session windows used by ICT-style traders. Activity, volatility, spreads, and returns vary intraday, but the best window is instrument-, venue-, season-, and strategy-specific.

## Session Schedule

| Session | Reference window | Required handling |
| ---------- | --------------- | ------------------------------------ |
| **Asian** | Relevant exchange/local session | Exchange holidays and product hours |
| **London** | Europe/London local time | Convert with historical/current DST |
| **New York** | America/New_York local time | Convert with historical/current DST |

Define candidate window boundaries in local session time, then convert every timestamp with a timezone database. Do not publish fixed UTC windows across DST changes.

## Session Behaviors

For each instrument, measure time-of-day median volume, spread, realized volatility, jump frequency, and the strategy's net returns. Treat prior-session ranges and sweeps as hypotheses; sessions do not create a mandatory daily direction.

## Workflow

1. **Pre-session**: Mark Asian session high/low, identify HTF key levels, note scheduled news events
   ```
   get_candles_around_date(symbol=<symbol>, exchange=<exchange>, interval="15m", date=<asian_session_date>)
   ```
2. **Session open**: measure spread, volatility, and any predeclared sweep; do not label price discovery manipulation
3. **Entry timing**: apply the strategy's calibrated window and closed-bar trigger
4. **Session context**:
   - Record which prior-session levels were crossed and whether price closed back inside
   - Estimate subsequent-return distributions without imposing bullish/bearish labels

## Evidence and Validation

- Treat the setup as a testable hypothesis, not a prediction. Define thresholds, entry, invalidation, and exit before evaluating outcomes.
- Calibrate on the same instrument, venue, session, and timeframe. Use closed candles and a held-out or walk-forward sample; record every variant tried.
- Include spread, fees, slippage, borrow or funding, partial fills, and latency. Reject the setup when net expectancy is not positive or depends on one narrow parameter.
- Return observed inputs, missing data, cost assumptions, entry, invalidation, exit, and a valid, watch, or no-trade status.
- Research basis: [Ito & Hashimoto](https://www.nber.org/papers/w12413) documents intraday seasonality in FX activity, volatility, and spreads; it does not establish universal profitable windows or a mandatory direction.

## Key Rules

- Do not call opening moves manipulation without order-level evidence.
- Allow trades outside named windows when the validated strategy and liquidity gates pass.
- Never assume London or another session is most profitable; show instrument-specific held-out results.
- Include DST, holidays, half-days, venue hours, and scheduled announcements.
- Treat time-window and structural labels as features whose incremental value must be tested.

## Related Skills

- **liquidity-zones** — Kill zone opens frequently sweep Asian session liquidity before reversing
- **market-structure-shift** — test objective structure events inside the chosen session window
