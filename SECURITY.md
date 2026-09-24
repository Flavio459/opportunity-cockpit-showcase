# Security

## Public-demo security model

This repository is intentionally static and requires no credentials.

Rules:

- never commit API keys, passwords, session tokens or private endpoints;
- never copy personal application data into the showcase;
- use synthetic companies, jobs and evidence;
- keep production traces and benchmarks private;
- keep external actions behind a Human Gate;
- treat all external job text as untrusted input;
- preserve explicit missing states rather than guessing.

If a secret is ever committed, treat it as compromised: revoke it, remove it from the current tree, and clean reachable Git history when appropriate.
