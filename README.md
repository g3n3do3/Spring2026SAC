# Spring2026SAC

Academic execution engine for Spring 2026 at Santa Ana College.

Courses: CMPR 114, CMPR 115, CMPR 159
Objective: ML/AI readiness by end of Summer 2026.
Web app: [linear-algebra-ai.replit.app](https://linear-algebra-ai.replit.app)

## Usage

```bash
python3 study_engine.py
```

Generates the study plan for the current week and saves it to `plans/`.

## Structure

- `SYSTEM_PROMPT.md` — Execution engine prompt for Claude Code integration
- `study_engine.py` — Weekly plan generator (Strang-aligned, ≤90 min/week)
- `plans/` — Generated weekly plans (Markdown + JSON)