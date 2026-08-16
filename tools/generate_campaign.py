#!/usr/bin/env python3
"""Generate an inspectable multi-platform launch draft pack from a verified JSON brief.

This tool creates drafts only. It never publishes, sends messages, or calls platform APIs.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from textwrap import dedent


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def generate(brief: dict) -> dict[str, str]:
    name = brief["project"]
    url = brief["url"]
    version = brief.get("version", "latest")
    caps = brief.get("capabilities", [])
    audience = ", ".join(brief.get("audience", []))
    problem = brief["problem"]
    install = brief.get("install", "")
    example = brief.get("example", "")
    limitations = brief.get("limitations", [])
    cta = brief.get("call_to_action", "Feedback is welcome.")
    source_lines = "\n".join(f"- {x}" for x in brief.get("sources", []))

    return {
        "00-campaign-brief.md": dedent(f"""        # {name} {version} Campaign Brief

        Audience: {audience}

        Problem: {problem}

        Capabilities:
        {bullets(caps)}

        Example: {example}

        Install:
        ```bash
        {install}
        ```

        Limitations:
        {bullets(limitations)}

        Call to action: {cta}

        Sources:
        {source_lines}
        """),
        "01-github-discussion.md": dedent(f"""        # Discussion draft: {name} {version}

        What problem should a storyworld compiler solve before generation?

        {name} {version} addresses this by:
        {bullets(caps)}

        Try it here: {url}

        {cta}
        """),
        "02-reddit.md": dedent(f"""        # Reddit draft

        **Title:** I built {name} to address continuity and provenance problems in creative AI workflows

        **Body:**

        {problem}

        The current release includes:
        {bullets(caps)}

        Quickstart:
        ```bash
        {install}
        ```

        This is an invitation to test the workflow and point out what is unclear or broken. {cta}

        Sources:
        {source_lines}
        """),
        "03-hacker-news.md": dedent(f"""        # Show HN draft

        **Title:** Show HN: {name} — a provider-neutral storyworld compiler

        **Text:**

        I built {name} because {problem.lower()}

        It currently supports:
        {bullets(caps)}

        The interesting design choice is treating scenes as canonical and comics, storyboards, and cinematic plans as projections.

        Repository: {url}

        Limitations: {" ".join(limitations)}
        """),
        "04-x-thread.md": dedent(f"""        # X thread draft

        1/ I built {name} because {problem}

        2/ The core capabilities:
        {bullets(caps)}

        3/ The key idea: keep story identity and provenance stable while providers and output formats change.

        4/ Try it: {url}

        5/ {cta}
        """),
        "05-linkedin.md": dedent(f"""        # LinkedIn draft

        I released {name} {version}, a project for {audience}.

        The problem: {problem}

        The lesson from building it: creative AI needs durable semantic state, evaluation, and provenance—not only better prompts.

        Current capabilities:
        {bullets(caps)}

        Learn more: {url}

        {cta}
        """),
        "06-devto.md": dedent(f"""        # Dev.to article outline

        ## Why creative generation needs a semantic layer

        {problem}

        ## What {name} does

        {bullets(caps)}

        ## Quickstart

        ```bash
        {install}
        ```

        ## Limitations and next steps

        {bullets(limitations)}

        ## Try it

        {url}
        """),
        "07-huggingface.md": dedent(f"""        # Hugging Face announcement draft

        {name} is a provider-neutral storyworld compiler for multimodal creative workflows.

        Use case: {example}

        Project: {url}

        This announcement should be paired with a working Space, model, dataset, or technical demo before publication.
        """),
        "08-mcp.md": dedent(f"""        # MCP community draft

        {name} exposes a semantic boundary around storyworld inspection, validation, compilation, projection, and provenance.

        The intended MCP operations are narrow and auditable rather than a generic command proxy.

        Project: {url}

        Feedback requested: which operation would you actually use, and what permission or safety boundary would you require?
        """),
        "09-source-ledger.md": dedent(f"""        # Source ledger

        {source_lines}
        """),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brief", type=Path)
    parser.add_argument("--output", type=Path, default=Path("campaign-drafts"))
    args = parser.parse_args()

    brief = json.loads(args.brief.read_text(encoding="utf-8"))
    args.output.mkdir(parents=True, exist_ok=True)
    for filename, content in generate(brief).items():
        (args.output / filename).write_text(content, encoding="utf-8")
        print(args.output / filename)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
