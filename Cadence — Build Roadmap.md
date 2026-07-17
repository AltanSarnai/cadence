Cadence — Build Roadmap
✅ Phase 0 — Scaffold (done)
Goal: a running Python server.
Built: uv project, FastAPI app, /health endpoint, auto-docs at /docs.
Concepts: uv/pyproject, FastAPI app object, route decorators, uvicorn.
Milestone: /health returns {"status":"ok"}. ✔

Phase 1 — Core port
Goal: content generation works in Python.
Build: reshape into the app/ structure (routers / services / config); port /api/generate using the official Anthropic SDK; port the platform fetchers (Reddit, HN, news) with httpx; serve your existing HTML from static/.
Concepts: project layout, Pydantic request/response models, dependency-loaded config from .env, async HTTP.
Milestone: the existing UI runs on the Python backend and generates a draft.

Phase 2 — Database + multi-tenancy (the SaaS foundation)
Goal: real persistence, isolated per agency.
Build: Postgres + SQLAlchemy 2.0 (async) + Alembic migrations; models Organization → User → Client → Draft; JWT auth; every query scoped to the tenant. Migrate clients.json into the DB.
Concepts: ORM, migrations, multi-tenancy, auth, access control.
Milestone: two separate agencies can log in and see only their own clients.

Phase 3 — RAG in Python
Goal: grounding in each client's real voice, per tenant.
Build: port chunk/embed/search; store vectors in pgvector; ingestion as background jobs (ARQ); per-client ragStore.
Concepts: embeddings, vector search in SQL, async job queues.
Milestone: the "ground in real voice" toggle works, scoped to a client, in Python.

Phase 4 — PyTorch ML (the differentiator + your learning goal)
Goal: measure and enforce voice quality.
Build: train the "does this sound like the client?" classifier (embeddings → small network), serve it as an endpoint, wire it into generation as a quality gate (auto-score / reject-and-regenerate).
Concepts: train/test split, a real neural net, evaluation metrics, model serving.
Milestone: every generated draft gets a voice-fidelity score.

Phase 5 — Harden + deploy
Goal: it's a real product on the internet.
Build: Docker, deploy to Render/Fly, secrets in the host, HTTPS, observability (Langfuse), error tracking, DB backups, rate limits.
Concepts: containers, CI/CD, secrets management, monitoring.
Milestone: a live URL agencies can log into.

Phase 6 — Advanced / the vision layer
Goal: the automation you described in the Slack note.
Build: LoRA fine-tuning (train-vs-RAG comparison); the Slack → generate → deliver-to-Drive workflow; agentic draft→critique→revise pipeline.
Concepts: fine-tuning, event-driven workflows, agent orchestration.
Milestone: a Slack task produces finished content delivered to Drive.