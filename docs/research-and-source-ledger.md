# Research, Sources, and Reasoning Ledger

Updated 2026-08-15. This ledger records the evidence and reasoning behind the future-trends roadmap.

## Research questions

- Which technical areas are gaining adoption across more than one ecosystem?
- Which trends align with AvatarArts’ existing capabilities rather than requiring a new identity?
- Which layer remains valuable when individual models and platforms change?
- What can be demonstrated publicly within 30 days?
- Which trends produce reusable infrastructure across comics, music, video, websites, agents, and products?
- What signals distinguish attention from adoption?
- What should be built before distribution is attempted?

## Source register

| Source | Type | What it contributes | Interpretation |
|---|---|---|---|
| [Anthropic Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Primary engineering source | Skills package instructions, resources, and procedural knowledge; the format was described as portable across platforms. | Skills are a distribution layer for repeatable expertise, not a replacement for tools or state. |
| [Anthropic MCP code execution](https://www.anthropic.com/engineering/code-execution-with-mcp) | Primary engineering source | Large tool surfaces create context and cost problems; code execution and selective tool loading matter. | Keep MCP contracts narrow, discoverable, and auditable. |
| [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Primary engineering source | Context selection and structure strongly affect agent performance. | Canon, memory, and artifact state need deliberate projections rather than dumping the whole archive into context. |
| [Anthropic agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Primary engineering source | Evals make behavioral changes visible before production and compound in value. | Creative systems need continuity, layout, provenance, and identity evals. |
| [Anthropic long-running harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Primary engineering source | Long tasks require state across context windows. | Creative production should be resumable and stateful. |
| [OpenAI agent tools](https://openai.com/index/new-tools-for-building-agents/) | Primary product/research source | Agents combine reasoning, tools, multimodal capabilities, and safety techniques. | The opportunity is a reliable system boundary around actions and evidence. |
| [OpenAI computer use / GPT-5.4](https://openai.com/index/introducing-gpt-5-4/) | Primary product source | General-purpose computer-use capability expands agents from API calls to software interaction. | Use computer use for bounded operations with approval gates, not unconstrained publishing. |
| [Google Cloud AI agent trends](https://cloud.google.com/resources/content/ai-agent-trends-2026) | Industry research | Tracks enterprise movement toward agentic systems. | Useful directional evidence, but vendor-sponsored and not neutral measurement. |
| [Hugging Face Models](https://huggingface.co/models) | Platform signal | Shows model activity across text, vision, video, audio, local, and multimodal categories. | Model variety increases the value of provider-neutral adapters and capability metadata. |
| [Hugging Face Spaces](https://huggingface.co/spaces) | Platform signal | Shows running demos and community applications, including multimodal and creative interfaces. | Demos are a distribution surface for creator systems. |
| [Hugging Face trending papers](https://huggingface.co/papers/trending) | Platform signal | Connects research attention with implementation and community visibility. | Research-to-demo-to-product loops are strategically useful. |
| [Hugging Face State of Open Source](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026) | Platform research | Provides ecosystem-level observations about open models and community activity. | Open model ecosystems are broadening; licensing and local execution need first-class treatment. |
| [Trendshift](https://trendshift.io/) | Discovery platform | Tracks repository trending, activity, mentions, and historical visibility. | Trendshift is one signal source, not a complete market oracle. |
| [Trendshift Signal](https://trendshift.io/signal) | Product/API page | Exposes engagement-spike analysis across metrics. | Cross-metric divergence is more useful than raw popularity. |
| [Product Hunt](https://www.producthunt.com/) | Launch platform | Shows product categories, launch attention, comments, and follower interest. | Product launches are a separate surface from developer adoption. |
| [PyPI Stats](https://pypistats.org/) | Package analytics | Provides package download history and comparisons. | Downloads are adoption evidence but need cohort and baseline normalization. |
| [npm statistics](https://npm-stat.com/) | Package analytics | Provides package download charts. | Package distribution can be measured separately from GitHub popularity. |
| [MCP Servers](https://mcpservers.org/) | Directory | Demonstrates discovery of MCP servers and agent skills. | MCP distribution and skills distribution should be tracked independently. |
| [Star History](https://www.star-history.com/) | Analytics tool | Provides historical GitHub star curves. | Useful for velocity and launch-campaign comparison, not a quality metric. |
| [Visual Story-Writing](https://arxiv.org/html/2410.07486v2) | Academic research | Represents stories with entities, locations, timelines, actions, and bidirectional visual/text editing. | Supports a storyworld graph and projection model for choTaku. |
| [Launch-Day Diffusion](https://arxiv.org/abs/2511.04453) | Academic research | Studies how launch exposure can affect GitHub star growth and identifies timing and platform effects. | Distribution matters, but star growth is only one outcome. |

## Confidence levels

### High confidence

- Agent systems need structured context, tool boundaries, state, and evaluations.
- Multimodal systems are expanding across models, demos, and local/open ecosystems.
- Skills and MCP are useful complementary packaging layers.
- Provenance, permissions, and safety become more important as systems act across tools.
- A semantic layer can serve more media surfaces than a provider-specific generator.

### Medium confidence

- Local and edge multimodal execution will become strategically important for privacy, cost, latency, and offline creative workflows.
- Creator-facing compilers and continuity systems will be more defensible than prompt-only wrappers.
- Cross-platform trend intelligence will outperform single-platform popularity monitoring for product decisions.

### Lower confidence / hypotheses

- A specific AvatarArts package will rank in the top 1–5% after launch.
- +300% growth will translate into durable adoption.
- Any one model provider, skill directory, or MCP marketplace will remain dominant.
- Product Hunt, Trendshift, or a social platform will produce the best distribution for a particular artifact.

## Reasoning chain

```text
more capable models
→ cheaper generation and more tool access
→ more creative output
→ more identity drift, provenance gaps, and context overload
→ demand for semantic state, continuity, evals, and lineage
→ provider-neutral creative compiler
→ portable skills and narrow MCP contracts
→ reusable products, demos, and distribution surfaces
```

## What was deliberately not treated as proof

- Marketing claims without usage evidence
- Raw star counts without velocity or cohort
- Viral posts without retention
- Model benchmark scores without task-specific evaluation
- Directory listings without installs or downstream use
- Forks that are merely mirrors or vendored upstream trees
- AI trend articles that do not expose methods or data

## Research maintenance protocol

For each new trend:

1. Record the source and publication date.
2. Classify the source as primary, platform signal, academic, industry research, or secondary commentary.
3. Capture the observed signal.
4. Separate fact from interpretation.
5. Score momentum, fit, defensibility, proof speed, distribution, and risk.
6. Add the trend to the roadmap only if it changes a build decision.
7. Create a small test or fixture before committing to a major implementation.
8. Revisit the decision after 30, 60, and 90 days.

## Current conclusion

Build the semantic creative spine first:

```text
canon + identity + memory + lineage + evaluation
```

Then expose it through:

```text
skills + MCP + multimodal adapters + creator products
```

Then distribute it through:

```text
GitHub + Trendshift + Hugging Face + package registries
+ skill directories + product launches + creator platforms
```

This ordering gives AvatarArts a durable center while allowing the surrounding trends to change.
