# Security Policy

## Supported versions

This repository is a portfolio/learning project. Only the latest `main` branch receives fixes.

## Reporting a vulnerability

Please **do not** open a public issue for security-sensitive findings.

Email or privately message the repository owner (`muhammad-a-dev`) with:

- a short description of the issue
- steps to reproduce
- impact assessment if known

## Secrets handling

- Never commit `.env`, API keys, tokens, or credentials.
- Use [`.env.example`](.env.example) as the template. Keep placeholder values empty in git; put real `HUGGINGFACE_API_KEY` / `GROQ_API_KEY` values only in a local `.env` or a secret manager.
- Do not log, print, or return raw API keys in responses, exceptions, or CI output.
- Prefer environment variables over hard-coding credentials in examples or tests.
- Rotate any key that may have been exposed (chat, gist, ticket, screenshot).

## Local data stores

Uploaded documents and Chroma embeddings live under `TEMP_UPLOAD_DIR` and `CHROMA_PERSIST_DIRECTORY`. Treat those directories as sensitive if they hold private content — do not commit them, and avoid sharing volume dumps casually.

## Scope notes

This service stores uploaded documents locally and keeps chat history in process memory. Do not deploy it to the public internet without authentication, rate limiting, and hardened storage.
