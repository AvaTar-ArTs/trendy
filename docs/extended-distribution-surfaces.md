# Extended Distribution Surface Matrix

The same release should not be copied everywhere. Each surface needs a native artifact, a distinct promise, and a measurable next action.

## Product Hunt

**Use when:** there is a usable product, hosted demo, plugin, workflow, or creator-facing package.

**Prepare:**

- product name and tagline
- maker profile
- product URL
- launch gallery
- short demo video
- first comment explaining why it exists
- categories
- launch-day response plan
- teaser or scheduled launch page where appropriate

**Primary goal:** qualified product discovery, conversations, signups, and feedback.

**Do not use Product Hunt as:** a substitute for a working product or a request for empty upvotes.

Official references: [Product Hunt](https://www.producthunt.com/), [Launch Guide](https://www.producthunt.com/launch), [Before Launch](https://www.producthunt.com/launch/before-launch).

## skills.sh and agent-skill directories

**Use when:** the artifact is a portable skill with a clear trigger, workflow, resources, and optional scripts.

**Prepare:**

- `SKILL.md`
- concise description
- trigger/use-case language
- installation command
- supported agents
- examples
- safety and permission notes
- version and changelog
- source repository
- test or validation command

**Primary goal:** installs, successful invocations, forks, issue reports, and reusable contributions.

Agent Skills are described as portable, version-controlled packages that can include instructions, scripts, templates, and references. See the [Skills directory](https://www.skills.sh/) and [Agent Skills documentation](https://cursor.com/docs/skills).

**Recommended AvatarArts skills:**

- Origin Story repository comprehension
- choTaku storyworld compilation
- visual layout stabilization
- structured asset registration
- creative provenance inspection
- trend intelligence

## npm

**Use when:** a JavaScript/TypeScript adapter, CLI, MCP client, web component, or plugin can be installed independently.

**Prepare:**

- `package.json`
- README and quickstart
- exported API
- supported Node versions
- tests
- package files allowlist
- changelog
- provenance and license
- publish preview

**Primary goal:** downloads, dependents, successful installs, and downstream usage.

Official reference: [npm publishing documentation](https://docs.npmjs.com/creating-and-publishing-scoped-public-packages/).

## PyPI

**Use when:** a Python component has a stable import or CLI boundary.

**Prepare:**

- `pyproject.toml`
- build metadata
- README
- license
- typed or documented public API
- tests
- TestPyPI validation
- trusted publishing or secure token workflow
- versioned release notes

**Primary goal:** downloads, imports, dependents, successful installation, and repeat use.

Official reference: [Python Packaging User Guide](https://packaging.python.org/tutorials/packaging-projects/).

## Hugging Face

**Use when:** a model, dataset, Space, evaluation, or interactive demo is independently useful.

**Prepare:**

- model/dataset/Space card
- license
- intended use
- limitations
- hardware requirements
- example inputs and outputs
- evaluation notes
- source and training-data provenance
- demo URL
- reproducibility instructions

**Primary goal:** likes, downloads, Space usage, forks, citations, and downstream demos.

References: [Models](https://huggingface.co/models), [Spaces](https://huggingface.co/spaces), [Trending Papers](https://huggingface.co/papers/trending).

## MCP directories and registries

**Use when:** a server exposes a narrow, useful, permission-aware tool boundary.

**Prepare:**

- server description
- tool list
- input/output schemas
- authentication requirements
- permissions
- data handling
- error behavior
- local setup
- hosted endpoint if available
- security notes
- test client or example conversation

**Primary goal:** legitimate installs, tool calls, integrations, and issue reports.

Reference: [MCP Servers directory](https://mcpservers.org/).

## Gumroad, Fiverr, and creator marketplaces

**Use when:** a subsystem can be packaged as a template, service, plugin, automation, asset, or implementation offer.

**Prepare:**

- buyer problem
- deliverable
- before/after example
- scope and exclusions
- installation or handoff process
- license
- support boundary
- screenshots
- price and tiers
- case study

**Primary goal:** qualified leads, purchases, successful delivery, reviews, and repeat work.

Do not list an unfinished research repository as a finished product. Convert it into a bounded offer first.

## Obsidian and creator plugins

**Use when:** a workflow can live inside an existing knowledge or creative environment.

**Prepare:**

- plugin or skill manifest
- install instructions
- compatibility
- sample vault or fixture
- screenshots
- upgrade notes
- privacy and local-data behavior

**Primary goal:** installs, active use, feedback, and retained workflows.

## Website, newsletter, and documentation

**Use when:** a project needs a canonical explanation that survives platform changes.

**Prepare:**

- canonical landing page
- technical article
- visual demo
- FAQ
- changelog
- source ledger
- mailing-list update
- analytics with consent

**Primary goal:** qualified visits, signups, documentation completion, and return visits.

## Campaign composition

For each release, select:

1. one canonical home — usually GitHub or a product site
2. one adoption surface — package registry, skill directory, Hugging Face, or plugin ecosystem
3. one conversation surface — GitHub Discussions, Reddit, Hacker News, or MCP community
4. one launch surface — Product Hunt, newsletter, or a public demo
5. one proof surface — tutorial, video, benchmark, case study, or interactive example

This creates a campaign with different jobs instead of duplicated announcements.

## Suggested choTaku package ladder

| Stage | Artifact | Surface |
|---|---|---|
| Core | source repository and release | GitHub, Trendshift |
| Skill | Origin Story / choTaku skill | skills.sh and compatible agent directories |
| Python | installable compiler package | PyPI |
| JS/MCP | client, CLI, or integration | npm and MCP directories |
| Demo | storyworld-to-artifact interface | Hugging Face Space or hosted site |
| Product | creator-facing starter kit | Product Hunt, Gumroad |
| Service | custom implementation and integration | Fiverr, direct outreach |
| Proof | tutorial and walkthrough | Dev.to, LinkedIn, YouTube, newsletter |

## Automation boundary

Automate:

- content atoms
- platform variants
- metadata
- source links
- package cards
- release notes
- launch checklists
- draft scheduling
- analytics normalization
- repurposing suggestions

Require approval for:

- first submission
- public posting
- community-specific messages
- paid promotion
- claims about users, revenue, ranking, or performance
- direct outreach
- publishing packages or code that may expose secrets
