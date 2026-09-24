# Opportunity Cockpit Showcase

> Public portfolio showcase. The production/core system and personal operational data remain private.

**Opportunity Cockpit** is an evidence-aware decision interface for professional opportunities. It demonstrates how AI-assisted analysis can support a human decision without inventing missing facts or automatically taking external action.

## Problem

Opportunity discovery produces too much information and too little decision clarity. A useful system must answer quickly:

- Is this worth reviewing?
- What is known versus missing?
- Which requirements are supported by evidence?
- What blocks the next action?
- Is the recommendation reliable enough for human review?

## Solution

This showcase implements a safe, static version of the workflow:

```text
Discovery
  -> Normalization
  -> Evidence
  -> AI Analysis
  -> Fit
  -> Evaluation
  -> Decision
  -> Proposal Preparation
  -> Human Gate
```

The demo uses **synthetic companies, jobs and evidence only**.

## What this proves

- structured opportunity normalization;
- explicit unknown / missing states;
- evidence-aware fit assessment;
- separation between fit and commercial conditions;
- verifier warnings;
- fail-closed human gate;
- privacy-aware publication boundaries;
- simple deployment with no backend or paid dependency.

## What is intentionally not public

- personal CVs and applications;
- real client or recruiter data;
- private scoring weights and strategic thresholds;
- internal benchmarks, traces and outcomes;
- provider credentials or infrastructure;
- automation that submits applications or messages;
- the private production repository.

See [docs/PUBLICATION_BOUNDARY.md](docs/PUBLICATION_BOUNDARY.md).

## Run locally

No build step is required.

Open `index.html` directly, or serve the directory with any static HTTP server.

## Architecture

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Security and truthfulness

- No real secrets are required.
- Demo data is synthetic.
- Missing information stays missing.
- Retrieval or keyword overlap is not treated as proof.
- No performance, conversion, ROI or hiring claims are made.
- External action remains behind a Human Gate.

## Tech

HTML · CSS · JavaScript · static JSON · evidence-oriented domain design

The private implementation also explores provider-neutral AI boundaries, evaluation records, traces and outcome feedback, but those internals are not published here.

## Author

Flávio Souza Barros  
Engineering × AI × Automation × Project Systems


## License / reuse

This repository is source-visible for portfolio evaluation, but it is **not released under an open-source license**. See [LICENSE](LICENSE).
