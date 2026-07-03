# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Overview

Climate Intelligence is a blog about the science of the climate, biodiversity, and related topics. It is a collaborative effort between the author (J. Xavier Prochaska), Claude, and possibly other humans.

## Git

- **The author performs all git commands.** Claude should not run `git add`, `git commit`, `git push`, or other git operations that modify repository state. Read-only commands (e.g. `git status`, `git log`, `git diff`) are fine when needed to understand the state of the repo.

## Logging

- This project follows **strict logging rules**, which will be specified in `Logs/logging.md` (to be created by the author shortly).
- Once `Logs/logging.md` exists, Claude must read it and adhere to its rules in every session.
