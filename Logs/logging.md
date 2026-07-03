# Logging

## Goals

We want to log all of the work that Claude does for this project.  Not just the code, but the thinking process, the decisions, the mistakes, the successes, etc.  And, the tokens used and an estimate of the CO2 emissions.

## Basics

### Log files

We want Claude to log the following every time we give it a prompt:

- The UT time
- The prompt
- The tokens used
- The model used
- An estimate of the CO2 emissions

Claude should generate a unique log file for every calendar day.  These will appear in the Logs/ directory and its YYYY/MM/ subdirectories.  Claude will create the subdirectories if they do not exist.

### Summary table

There should be a summary table of every log entry in a file named `log_summary.csv` in the Logs/ directory.  The file should have the following columns:
- The UT time
- The tokens used
- The model used
- An estimate of the CO2 emissions

### CO2 emissions calculation

The per-prompt CO2 estimate is computed with a transparent, reproducible formula:

```
CO2 (grams) = (tokens / 1000) × energy_per_1k_tokens × grid_intensity
```

Factors (finalized 2026-07-03; see Discussion Q2):

| Factor | Value | Basis |
|--------|-------|-------|
| `energy_per_1k_tokens` | 0.20 Wh per 1,000 tokens | Combined input+output, large frontier model. Order-of-magnitude estimate; refine when better public data exists. |
| `grid_intensity` | 0.38 gCO2 / Wh (≈ 380 gCO2 / kWh) | **Anthropic data-center region.** Amazon (AWS) is Anthropic's primary provider and Claude compute is sited primarily in the US, so we use a US-average *location-based* grid intensity (≈ US national average). |

**Combined factor:** `0.20 Wh × 0.38 gCO2/Wh = 0.076 gCO2 per 1,000 tokens`.

**Worked example:** 16,000 tokens → `(16000 / 1000) × 0.20 × 0.38 = 1.22 g` ≈ **1.2 gCO2**.

Assumptions and refinements:
- **Location-based, not market-based.** AWS/Google purchase renewables and RECs, so
  a market-based figure would be lower (potentially near zero for fully-matched
  regions). Location-based better reflects physical grid emissions; switch if you
  prefer market-based accounting.
- Region can be narrowed from US-average to a specific AWS region (e.g. `us-east-1`
  on the PJM grid) if we want more precision.
- Input and output tokens are currently weighted equally. Output is more
  compute-intensive; we can split the factor later if desired.
- `energy_per_1k_tokens` is the least certain factor — update it as Anthropic or
  independent studies publish better numbers.

## Prompts

1. Read this file.  Start a discussion with me on Logging. Put your questions in the Discussion section below and I will answer them.  Log your work using the instructions in Basics section above.  

2. I have answered your questions.  Please review the Discussion section below and make sure you are satisfied with the answers.  If you are not, please ask me to clarify.  Add to this doc the calculation for CO2.

3. Add to CLAUDE.md file the instructions for logging and make sure Claude logs after every prompt related to this project.

## Discussion

### Claude's questions (2026-07-03)

**1. Where do token counts come from?**
I cannot reliably read my own exact token usage from inside a turn — the running
totals live in the Claude Code harness, not in my context. Which source do you
want to be authoritative?
  - (a) You paste the figures from `/cost` (or the status line) after each prompt;
  - (b) I record my best *estimate* from text/context length (approximate, and it
    will drift);
  - (c) We add a Claude Code **hook** (e.g. a `Stop` hook) that captures the real
    usage numbers automatically and appends them to the log.
My recommendation: (c) for accuracy, with (b) as a fallback until the hook exists.
Everything I log before then should be treated as an estimate.
>A. Yes, use (c) with (b) as a fallback

**2. What CO2 estimation method / factors should I use?**
I propose a transparent formula so the number is reproducible:
`CO2 (g) = (tokens / 1000) × energy_per_1k_tokens (Wh) × grid_intensity (gCO2/Wh)`.
Proposed defaults (please confirm or replace, and cite a source you trust):
  - `energy_per_1k_tokens` ≈ 0.2 Wh (combined input+output, large frontier model);
  - `grid_intensity` ≈ 0.4 gCO2/Wh (≈400 gCO2/kWh, world-average electricity).
That yields ≈0.08 gCO2 per 1k tokens. Should input and output tokens be weighted
differently (output is more compute-intensive)? Should we use a specific grid
region (e.g. US, or Anthropic's data-center region) instead of world-average?
>A. Use Anthropic's data-center region.

**3. Log file naming and format.**
Plan: one markdown file per calendar day at `Logs/YYYY/MM/YYYY-MM-DD.md`, with one
appended section per prompt. Is `YYYY-MM-DD.md` the filename you want? Any preferred
heading/section structure?
>A. Yes, `YYYY-MM-DD.md` is the filename you want.  The heading should be "Logging for YYYY-MM-DD".

**4. What exactly is "the prompt"?**
Do you want the verbatim user text only, or should I also capture the injected
IDE/system-reminder context that arrives with it? Any redaction rules (e.g. never
log secrets, file contents, or personal data)?
>A. Only log the verbatim user text.

**5. Narrative vs. the five fields.**
The Goals section wants the "thinking process, decisions, mistakes, successes,"
but the Basics list only names five fields (UT time, prompt, tokens, model, CO2).
Should the daily log also contain a prose narrative of my work per prompt, in
addition to the five structured fields? If so, how detailed?
>A. The daily log should contain a prose narrative of Claude's work per prompt. The summary table will provide only the fields. 

**6. Granularity and timestamp meaning.**
One log entry per *user prompt* (not per tool call), correct? And should the UT
time mark when the prompt was received, or when I finished responding?
>A. Per user prompt.

**7. `log_summary.csv` details.**
I'll write a header row plus one row per prompt with the four columns you listed
(UT time, tokens, model, CO2). Confirm the header is wanted, and that times are UTC.
>A. Yes, include the header.

**8. Retroactive logging.**
Should I back-fill log entries for today's earlier start-up prompts (the four in
`claude_prompts/start_up.md`), or begin logging only from this prompt forward?
(Token counts for those would be rough estimates.)
>A. It is ok to not log the earlier start-up prompts.
