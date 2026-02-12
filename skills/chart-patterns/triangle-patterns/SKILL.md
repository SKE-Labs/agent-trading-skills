---
name: triangle-patterns
description: Trade ascending, descending, and symmetrical triangle patterns. Use when anticipating breakouts from consolidation, measuring potential move targets, or timing entries on compression breakouts.
---

# Triangle Pattern Trading

Triangles form during consolidation and typically break out in the direction of the prevailing trend.

## Triangle Types

### Ascending Triangle (Bullish Bias)

- **Flat top** (horizontal resistance)
- **Rising lows** (ascending support)
- Usually breaks upward
- Buyers gaining strength

### Descending Triangle (Bearish Bias)

- **Flat bottom** (horizontal support)
- **Lower highs** (descending resistance)
- Usually breaks downward
- Sellers gaining strength

### Symmetrical Triangle (Neutral)

- **Lower highs** + **higher lows**
- Converging trendlines
- Breaks either direction (usually with trend)
- Coiling for explosive move

## Identification

1. Draw trendlines connecting:
   - At least 2 swing highs (upper line)
   - At least 2 swing lows (lower line)
2. Lines should converge
3. Volume typically decreases during formation

## Entry Strategies

### 1. Breakout Entry

- Enter when price breaks and closes outside triangle
- Volume spike confirms breakout
- Stop: Inside triangle (opposite side)

### 2. Retest Entry

- Wait for breakout
- Wait for price to retest broken trendline
- Enter on bounce/rejection
- Better R:R

## Target Calculation

**Measured Move**:

```
Target = Breakout point ± Height of triangle base
```

Measure the widest part of the triangle, project from breakout.

## Chart Drawing

Use `draw_chart_analysis` with `trend` type:

- Draw both trendlines (upper and lower)
- Requires minimum 4 touch points total (2 each)
- Visualize the compression

## Volume Analysis

| Phase        | Volume    |
| ------------ | --------- |
| Formation    | Declining |
| Breakout     | Spike     |
| Continuation | Sustained |

## Best Practices

- Trade in direction of prior trend
- Wait for close outside triangle (not just wick)
- False breakouts are common—use retest entry
- Wider triangles = Stronger moves
- Tighter apex = More explosive breakout
