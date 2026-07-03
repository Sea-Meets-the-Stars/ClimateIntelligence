# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Overview

Climate Intelligence is a blog about the science of the climate, biodiversity, and related topics. It is a collaborative effort between the author (J. Xavier Prochaska), Claude, and possibly other humans.

## Git

- **The author performs all git commands.** Claude should not run `git add`, `git commit`, `git push`, or other git operations that modify repository state. Read-only commands (e.g. `git status`, `git log`, `git diff`) are fine when needed to understand the state of the repo.

## Logging

This project follows **strict logging rules**. The full spec, finalized conventions,
and CO2 calculation live in [`Logs/logging.md`](Logs/logging.md) — read it if in doubt.

**Claude must log every prompt related to this project.** Responsibilities are split:

### 1. Daily narrative log — written by Claude (do this every prompt)

After responding to each user prompt, append an entry to the day's log file:

- **Path:** `Logs/YYYY/MM/YYYY-MM-DD.md` (UTC date). Create the `YYYY/MM/`
  subdirectories if missing.
- **File heading (once per day):** `# Logging for YYYY-MM-DD`
- **One section per user prompt** (not per tool call) containing:
  - **UT time** the prompt was received (the transcript's timestamp for the user
    message, or `date -u +"%Y-%m-%dT%H:%M:%SZ"`).
  - **Prompt:** the *verbatim user text only* (do not include IDE/system-reminder
    context).
  - **Model** and **tokens** — tokens are an estimate here; the authoritative
    count is auto-recorded in `log_summary.csv` (see below). Label accordingly.
  - **CO2 estimate** via the formula in `Logs/logging.md`
    (`≈ 0.076 gCO2 per 1,000 tokens`).
  - A **prose narrative** of the work: the thinking, decisions, mistakes, and
    successes — not just what changed.

### 2. Summary table — written automatically by a hook (do NOT write it by hand)

`Logs/log_summary.csv` is appended by a `Stop` hook
([`.claude/hooks/log_usage.py`](.claude/hooks/log_usage.py)) after every turn. It
reads the transcript and records the authoritative `ut_time, tokens_used, model,
co2_grams_estimate`. **Claude must not append rows to `log_summary.csv` itself** —
that would duplicate the hook's row. If the hook is inactive (e.g. it was just
installed and needs `/hooks` or a restart to load), note that rather than
hand-writing rows.

Do not back-fill the four start-up prompts from `claude_prompts/start_up.md`.
