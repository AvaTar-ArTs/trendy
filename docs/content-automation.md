# Content Creation and Distribution Automation

## Objective

Turn one verified project update into a coordinated but platform-native campaign:

```text
release evidence
→ campaign brief
→ platform variants
→ fact/provenance check
→ approval queue
→ platform publication
→ analytics collection
→ learning record
→ next content
```

Automation should reduce repetitive work while preserving human judgment, community fit, and platform compliance.

## The content source of truth

Every campaign begins with a structured brief containing:

- project name and canonical URL
- release version
- problem solved
- target audience
- three to five verified capabilities
- installation command
- concrete example
- screenshots or demo URLs
- limitations
- license and provenance notes
- call to action
- source links
- embargo or preferred publication window
- platforms requested
- approval status

Do not generate claims that are absent from the brief or linked evidence.

## Content atoms

Create reusable atoms once:

- one-sentence positioning
- short description
- technical explanation
- founder/build story
- architecture diagram
- demo script
- quickstart
- FAQ
- limitation note
- quote-sized insight
- call for testers
- call for contributors
- release changelog
- source bibliography

Then compose each platform’s post from those atoms.

## Platform-native variants

| Surface | Best format | Automation posture |
|---|---|---|
| GitHub Release | changelog, upgrade notes, assets, verification | automate draft; human publish |
| GitHub Discussions | question, design decision, feedback request | generate draft; human post and reply |
| Reddit | community-specific technical value, no generic promotion | draft only until community rules are checked |
| Hacker News | concise technical “Show HN” explanation | draft and preflight; human submission and discussion |
| X | short hook, thread, image/video, build progress | generate variants; human approve |
| LinkedIn | professional story, lesson, architecture, outcome | generate variants; publish only with authorized API/session |
| Dev.to | tutorial or engineering post | generate full draft; human edit and publish |
| Hugging Face | model/Space/dataset card, demo, technical notes | generate card and announcement; human review |
| MCP communities | tool purpose, schema, permissions, setup, safety | generate technical announcement; human adapt |
| Product Hunt | launch story, maker comment, screenshots, use case | generate launch kit; human coordinate launch |
| Newsletter | narrative summary, links, lessons, next step | automate draft; human send |
| Website/blog | canonical long-form article | generate from verified atoms; human review |
| Video | script, shot list, captions, description, chapters | automate preproduction; render/publish after approval |

## Automation levels

### Level 0 — research

Collect public signals, repository changes, release notes, comments, and performance metrics.

### Level 1 — draft

Generate platform-specific drafts, titles, hashtags/topics, image prompts, scripts, and source lists.

### Level 2 — preflight

Check links, prohibited claims, missing source citations, duplicate copy, character limits, required fields, and community-specific rules.

### Level 3 — approval queue

Present a campaign bundle for review. Record approved, rejected, and edited variants.

### Level 4 — publish

Use an official API or approved connected app where available. Otherwise open a prepared draft for manual publication. Never automate around platform access controls.

### Level 5 — learn

Collect reach, clicks, installs, comments, forks, downloads, signups, conversions, retention, and qualitative feedback. Feed only verified lessons back into future briefs.

## Platform access notes

- Reddit provides an official API for submitting posts, with OAuth and responsible-use requirements. See the [Reddit API documentation](https://www.reddit.com/dev/api/) and [Reddit Data API terms guidance](https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki).
- LinkedIn provides a versioned Posts API for organic and sponsored posts, with access and authorization requirements. See the [official Posts API documentation](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api).
- Hacker News provides an official read API, but publishing is generally a human/browser workflow. See the [official Hacker News API repository](https://github.com/HackerNews/API).
- GitHub provides APIs for repository releases, discussions, issues, and project data. Use authenticated, permission-scoped actions.
- Hugging Face provides native model, dataset, Space, and paper surfaces; use their cards, metadata, and platform conventions.
- X, Dev.to, Product Hunt, and other platforms may change access rules or require app approval. Treat browser/manual approval as the fallback rather than scraping.

## Approval gates

Require human approval before:

- first publication to any platform
- posting to a community with rules or cultural context
- publishing claims about performance, revenue, users, or adoption
- publishing content containing personal data
- publishing generated images, voice, or likenesses
- sending direct messages or invitations
- making purchases, paid promotions, or sponsorships
- deleting, editing, or replying to public content at scale

## Content QA checklist

- [ ] Canonical URL is correct.
- [ ] Version and date are correct.
- [ ] Every factual claim has a source or repository evidence.
- [ ] No unsupported “first,” “best,” “viral,” or “top” language.
- [ ] No fabricated metrics.
- [ ] License and upstream provenance are clear.
- [ ] Example actually runs.
- [ ] Platform character limits are respected.
- [ ] Community rules have been checked.
- [ ] The call to action asks for useful participation.
- [ ] A human approved publication.
- [ ] Analytics fields are prepared before launch.

## Recommended AvatarArts automation

Build this in order:

1. brief schema and campaign manifest
2. release-note extractor
3. content atom generator
4. platform variant generator
5. link and claim checker
6. approval queue
7. platform adapters
8. analytics collector
9. repurposing planner
10. trend-to-content recommender

The first useful deliverable is not a social bot. It is a reproducible campaign pack that a human can inspect, edit, approve, publish, and measure.
