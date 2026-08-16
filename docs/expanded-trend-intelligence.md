# Expanded Trend Intelligence

Trendy is not limited to GitHub repositories. A creator ecosystem can rise through several connected surfaces, each with different evidence and different meanings.

## Trend surfaces

| Surface | What can rise | Primary signals | Useful AvatarArts application |
|---|---|---|---|
| GitHub / Trendshift | repositories, releases, topics | stars, forks, issues, PRs, mentions, release velocity | choTaku, Origin Story, MCP systems |
| Hugging Face | models, datasets, Spaces, papers | likes, downloads, usage, updates, demos, paper attention | visual models, datasets, creative demos |
| npm | packages and CLIs | weekly downloads, dependents, version cadence, GitHub activity | JavaScript plugins, MCP clients, creator tooling |
| PyPI | packages | downloads, release cadence, dependents, documentation | Python libraries and automation engines |
| Skills directories | agent skills and workflows | installs, usage, ratings, forks, recency, supported agents | Origin Story, creative asset, comic, research skills |
| MCP directories | servers and tools | installs, connections, tool calls, stars, reviews, security posture | bounded choTaku and asset-intelligence servers |
| Product Hunt | products and launches | upvotes, comments, makers, category rank, followers | packaged creator tools and SaaS surfaces |
| Papers and research | papers, benchmarks, methods | citations, saves, downloads, replication, demos | story graphs, continuity, multimodal research |
| Model/tool ecosystems | APIs, models, workflows | inference usage, adoption, latency, cost, integrations | provider-neutral creative adapters |
| Social and community | posts, videos, discussions | qualified mentions, reposts, replies, click-through, technical discussion | launch narratives and public learning |
| Marketplaces | templates, plugins, assets, services | views, saves, installs, purchases, conversion, reviews | Fiverr, Gumroad, Obsidian, Canva, creator products |
| Media/content | videos, images, comics, music, newsletters | watch time, completion, saves, shares, subscribers, repeat use | AvatarArts stories and visual systems |
| Web properties | landing pages, docs, demos | search impressions, clicks, signups, referrals, retention | avatararts.org, GPTJunkie, tool landing pages |
| Developer infrastructure | Docker images, integrations, registries | pulls, dependents, deployment, issue activity | deployable creative services |
| Talent and organizations | creators, maintainers, teams | followers, collaborations, contributions, demand | personal brand and employer-facing proof |

## Signal classes

### Attention

- views
- impressions
- stars
- upvotes
- likes
- mentions
- followers

Attention is useful for discovery but is not proof of adoption.

### Adoption

- installs
- downloads
- active users
- API calls
- model inference
- package dependents
- deployments
- purchases
- repeat sessions

Adoption is stronger than attention because it reflects behavior.

### Community

- forks
- pull requests
- issues
- comments
- discussions
- contributors
- integrations
- remixes

Community signals indicate that other people are doing work with or around the artifact.

### Quality and trust

- successful installations
- documentation completion
- test status
- response time
- release cadence
- security reports
- provenance
- reviews
- retention

Quality signals prevent a shallow viral spike from being mistaken for a durable opportunity.

### Commercial

- conversion rate
- revenue
- average order value
- qualified leads
- repeat buyers
- refund rate
- creator invitations

Commercial signals matter when the goal is a product, service, or sustainable creator business.

## Cross-domain “hot” definition

A thing is **hot** when it shows recent acceleration in at least two independent signal classes and has a credible explanation.

Examples:

- a GitHub release plus stars and forks
- a Hugging Face Space plus usage and model downloads
- a skill plus installs and repeat updates
- a product launch plus comments and signup conversion
- a paper plus a working demo and community replication
- a comic series plus saves, completion, and repeat readers

A view spike alone is a watch signal, not a hot signal.

## Top 1–5% definition

Percentiles must be calculated within a cohort:

- same platform
- same category
- same language or media type
- similar age
- similar baseline
- same time window

Recommended labels:

- top 50% — normal
- top 20% — notable
- top 10% — strong
- top 5% — high-priority rising
- top 1% — exceptional breakout candidate

## +300% definition

```text
growth_percent = ((current - baseline) / baseline) * 100
```

+300% means four times the baseline.

Use both relative and absolute values. A small project moving from 1 to 4 is +300%, but a project moving from 100 to 400 is a much stronger adoption event.

## Signal maturity ladder

| Level | Evidence | Decision |
|---|---|---|
| L0 | one noisy metric | observe |
| L1 | one metric above +50% | watch |
| L2 | two metrics above +100% | investigate |
| L3 | two signal classes above +200% | rising |
| L4 | +300%, top 5%, and credible quality evidence | hot |
| L5 | top 1%, cross-platform adoption, retention, and community | breakout |

## Research source map

### Direct discovery sources

- [Trendshift](https://trendshift.io/)
- [Trendshift Signal](https://trendshift.io/signal)
- [GitHub Trending](https://github.com/trending)
- [Hugging Face Models](https://huggingface.co/models)
- [Hugging Face Spaces](https://huggingface.co/spaces)
- [Hugging Face Trending Papers](https://huggingface.co/papers/trending)
- [Product Hunt](https://www.producthunt.com/)
- [npm statistics](https://npm-stat.com/)
- [PyPI Stats](https://pypistats.org/)
- [skills.sh](https://skills.sh/)
- [MCP Servers](https://mcpservers.org/)
- [Star History](https://www.star-history.com/)

### Interpretation rule

Discovery pages show what is visible. They do not automatically prove quality, safety, originality, or user retention. Every rising candidate needs source inspection, provenance review, installation testing, and an explanation of what caused the movement.

## AvatarArts operating strategy

Use one normalized trend record for every meaningful artifact:

```text
source
artifact
category
cohort
time_window
baseline
current
absolute_change
growth_percent
percentile
signal_classes
quality_evidence
provenance
action
```

Then connect signals across surfaces:

```text
research paper
  → model or method
  → Hugging Face demo
  → GitHub implementation
  → skill or MCP adapter
  → creator workflow
  → published artifact
  → audience response
  → reusable product
```

This is the gap between “finding what is trending” and building a creative intelligence system.
