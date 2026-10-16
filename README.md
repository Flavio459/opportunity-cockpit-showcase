# Opportunity Cockpit Showcase

> Public executive showcase. The private Opportunity Cockpit, operational data, commercial rules and client workflows remain outside this repository.

## What this repository is

The current public surface is an **Executive AI Command Center** designed to demonstrate how generative AI can support C-Suite operations without removing human control.

The showcase is intentionally static and uses synthetic scenarios. It demonstrates the interaction model, governance concepts, multilingual executive experience and selected implementation patterns; it is **not** the private operational Opportunity Cockpit and it does not perform real external dispatches.

## Current experience

The active showcase demonstrates:

- executive intake and synthesis across three synthetic scenarios;
- multilingual UX in English, Portuguese and Arabic, including RTL support;
- deterministic **Human Decision Gate** before simulated external action;
- governance and risk framing for controlled versus uncontrolled AI usage;
- an audit-seal interaction after explicit human approval;
- executive media assets and a 1080p walkthrough;
- a low-friction **Sprint 01** commercial entry offer.

The active runtime is implemented in `index.html`, `app.js` and `data/i18n.js`.

## Public showcase flow

```text
Synthetic Executive Input
  -> Scenario / Context
  -> AI Synthesis Simulation
  -> Governance & Risk Review
  -> Human Decision Gate
  -> Simulated Dispatch
  -> Audit Evidence
```

No real client action is executed by this repository.

## Relationship to the private Opportunity Cockpit

The **private Opportunity Cockpit** is the operational decision system for real opportunities, evidence, prioritization, proposal preparation, Human Gate and outcome learning.

Concepts such as Proposal Intelligence, commercial routing (`Principal`, `Quick Win`, `Productized Offer`), Wii Finance/V15 product operations, private scoring rules, real proposal history and operational memory belong primarily to the private system. They may be demonstrated publicly later only when that demonstration has a clear commercial purpose.

This separation prevents the public portfolio from becoming a duplicate production system.

## Legacy V1

The repository still preserves the original opportunity-evaluation prototype under `legacy_v1/` and the synthetic dataset in `data/opportunities.json`.

These assets document the earlier evolution of the project. They are **legacy material and are not part of the current Executive AI Command Center runtime**. They are retained for traceability; they should not be interpreted as the current architecture.

## Publication boundary

Public GitHub should prove the ability to design and build the system without publishing the valuable or sensitive operational core.

Intentionally private:

- personal CVs, applications and recruiter/client records;
- real proposals and commercial negotiation history;
- private scoring weights, thresholds and decision rules;
- real opportunity outcomes and operational memory;
- provider credentials, infrastructure and internal traces;
- automation capable of submitting applications, messages or other external actions;
- the private production repository.

See [docs/PUBLICATION_BOUNDARY.md](docs/PUBLICATION_BOUNDARY.md).

## Run locally

No build step is required.

Open `index.html` directly, or serve the directory with any static HTTP server.

## Architecture

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Security and truthfulness

- The showcase uses synthetic scenarios and presentation data unless explicitly stated otherwise.
- The Human Gate is a governance interaction; this static repository does not perform real dispatches.
- Missing or private operational facts must not be invented to make the public demo look complete.
- Public claims should be treated as showcase positioning unless backed by explicit evidence.
- Private operational logic remains outside the showcase.

## Tech

HTML · CSS · JavaScript · static assets · multilingual data · deterministic UI interactions

## Author

Flávio Souza Barros  
Engineering × AI × Automation × Project Systems

## License / reuse

This repository is source-visible for portfolio evaluation, but it is **not released under an open-source license**. See [LICENSE](LICENSE).
