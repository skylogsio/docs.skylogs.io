---
id: openapi
title: OpenAPI spec
sidebar_position: 11
slug: /api/openapi
---

# OpenAPI spec

The Skylogs API is described by an **OpenAPI 3.0** document — the single source of truth for this reference section.

- **Interactive explorer (Swagger UI):** [api.skylogs.io/api/doc](https://api.skylogs.io/api/doc)
- **Raw spec:** the `docs.json` served alongside the Swagger UI {/* TODO: publish a stable URL for the raw JSON and link it here */}

## Using the spec

- Import it into Postman/Insomnia to get a ready-made request collection.
- Generate typed clients with `openapi-generator` or per-language tools.

## How this reference is maintained

The endpoint pages in this section (Alert rules, Users & teams, Endpoints, Data sources, Provider configs, Status pages, Instances) are **generated** from the spec by `scripts/generate_api_docs.py` in this repo:

```bash
python3 scripts/generate_api_docs.py openapi/docs.json docs/api
```

Regenerate and commit whenever the API changes. The hand-written pages (Overview, Authentication, Ingestion, Rate limits) document semantics the spec can't express — keep those updated manually.
