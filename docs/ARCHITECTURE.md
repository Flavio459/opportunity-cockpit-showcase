# Architecture

## Public showcase flow

```mermaid
flowchart LR
  A[Discovery] --> B[Normalization]
  B --> C[Evidence]
  C --> D[AI Analysis]
  D --> E[Fit Assessment]
  E --> F[Verifier]
  F --> G[Decision Queue]
  G --> H[Human Gate]
```

## Design principles

### 1. Normalize before reasoning

External opportunity text is treated as untrusted input. Structured fields use explicit missing values instead of invented defaults.

### 2. Evidence admission is explicit

A document existing somewhere is not automatically proof. Evidence must be admitted to the corpus and must directly support the requirement being assessed.

### 3. Retrieval is not proof

Keyword overlap may help retrieve a candidate excerpt, but it cannot by itself upgrade a capability to confirmed.

### 4. Fit and conditions are separate

Technical/profile fit and commercial attractiveness answer different questions and should not be collapsed into one opaque score.

### 5. Verification is independent

The verifier can reject unsupported claims or flag missing information. It does not create evidence.

### 6. Fail closed

The public demo never submits an application, sends a message or performs an external action. Those actions remain behind a Human Gate.

## Private production boundary

The private system may contain additional runtime components such as provider routing, traces, evaluation records, outcome feedback and internal decision rules. They are intentionally excluded from this repository.
