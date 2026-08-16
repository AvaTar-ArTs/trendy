# Rising Signals: Hot, Top 1–5%, and +300%

This document defines a practical research framework for finding repositories that are heating up before they become obvious.

## What is verified

Trendshift describes an **engagement spike signal** that looks for repositories with diverging engagement counts across metrics. Its tracked activity includes stars, forks, merged pull requests, issues, and closed issues.

Sources:

- [Trendshift](https://trendshift.io/)
- [Trendshift Signal](https://trendshift.io/signal)
- [Trendshift GitHub Trending archive](https://trendshift.io/github-trending-repositories)
- [Trendshift repository activity example](https://trendshift.io/repositories/25296)
- [GitHub Trending](https://github.com/trending)
- [GitHub community discussion of trending velocity](https://github.com/orgs/community/discussions/163970)
- [Launch-Day Diffusion research](https://arxiv.org/abs/2511.04453)

Trendshift does **not** publish a complete ranking formula. Therefore the thresholds below are operating definitions for research and launch planning, not claims about an official scoring algorithm.

## Definitions

### Hot

A repository is **hot** when it is showing unusually strong recent activity across at least two signals:

- star velocity
- fork velocity
- merged pull requests
- issue activity
- external mentions
- release or launch event

A single metric spike is weak evidence. Cross-metric movement is stronger.

### Rising

A repository is **rising** when the current window is materially stronger than its own recent baseline.

Use a 7-day current window against a prior 28-day daily average, or a 24-hour window against a prior 14-day daily average for fast-moving launches.

### Top 1–5%

“Top 1–5%” means percentile rank within a defined comparison set:

- same language
- same topic/category
- similar repository age
- similar size or baseline activity
- same time window

Never compare a new Python project directly with a mature 400k-star project and call the result meaningful.

### +300%

Use the mathematically explicit interpretation:

```text
growth_percent = ((current - baseline) / baseline) * 100
```

A result of **+300%** means the current value is four times the baseline.

For example:

- baseline: 2 stars/day
- current: 8 stars/day
- growth: +300%

If someone says “300% of baseline,” that means three times baseline, or +200% growth. Record which interpretation is being used.

## Practical alert tiers

| Tier | Suggested rule | Meaning |
|---|---|---|
| Watch | +50% in one metric | Worth checking |
| Rising | +100% in two metrics | Clear acceleration |
| Hot | +200% in two or more metrics, with activity breadth | Strong attention spike |
| Breakout candidate | +300% in stars or forks plus another active signal | Investigate immediately |
| Top 5% candidate | 95th percentile or higher in comparison cohort | Strong relative performer |
| Top 1% candidate | 99th percentile or higher in comparison cohort | Exceptional relative performer |

These are research thresholds, not promises of Trendshift placement.

## Recommended composite score

For a candidate repository, score four dimensions from 0–100:

1. **Velocity** — recent growth relative to baseline
2. **Acceleration** — whether growth is increasing rather than merely steady
3. **Breadth** — number of independent engagement signals moving
4. **Quality** — releases, documentation, issue response, contributors, and working demos

A simple planning score:

```text
hot_score =
  0.35 * velocity +
  0.25 * acceleration +
  0.20 * breadth +
  0.20 * quality
```

Suggested interpretation:

- 0–39: normal activity
- 40–59: watch
- 60–74: rising
- 75–89: hot
- 90–100: breakout candidate

Do not use the score as a substitute for judgment. Inspect the repository, source quality, provenance, and whether the activity is legitimate.

## Applying this to AvatarArts

The most useful first comparison set is:

- Python repositories
- AI agent / AI skills / MCP / creative automation topics
- repositories updated within the last 90 days
- repositories with fewer than 10,000 stars
- repositories with a working README and release

Primary flagship:

- [choTaku](https://github.com/AvaTar-ArTs/choTaku)

Companion:

- [origin-story](https://github.com/AvaTar-ArTs/origin-story)

Do not spread a launch across every AvatarArts repository. Concentrated momentum makes the signal easier to interpret and gives users one clear destination.

## Research procedure

1. Define the cohort before measuring.
2. Capture current stars, forks, issues, merged PRs, and release date.
3. Capture the same metrics again after 24 hours, 7 days, and 28 days.
4. Calculate absolute change and percentage change.
5. Rank within the cohort by percentile.
6. Flag +300% growth only when the baseline is large enough to be meaningful.
7. Require at least two activity dimensions for a “hot” label.
8. Check external mentions and release context.
9. Inspect for spam, copied code, artificial stars, or misleading activity.
10. Record the result in the launch log.

## Small-baseline warning

Percentage growth is unstable when the baseline is near zero:

- 1 → 4 stars is +300%, but may not indicate broad adoption.
- 100 → 400 stars is also +300%, and is a much stronger signal.

Always store both the percentage and the absolute change.

## Ethical boundary

Do not buy stars, use fake accounts, exchange coordinated artificial engagement, or spam communities. GitHub has previously documented abuse involving artificial stars and forks, and those tactics damage both trust and repository standing.

The objective is to create a useful project that earns attention through a clear problem, working software, useful examples, responsive maintenance, and honest distribution.
