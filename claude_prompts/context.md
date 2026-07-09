# Context

## Goals

This repository will create the blog "Climate Intelligence".  This file will help create context for Claude as it works on the project.

## Prompts

1. Please grab every major report on climate change from the IPCC and put them my ClimateIntelligence shared Google drive folder. Keep in mind:
    - You can stage a local copy of the files in the context/Reports directory.
    - Use `rclone` to copy the files to the shared folder.
    - If you have any questions about the files, please ask me in the Discussion section below.
    - Log your work

2.  I have downloaded what is the first of what will be many books into the `context/Books/` directory.  Please:
    - Read the book and all of the reports you downloaded.  
    - Push all of the Books to the ClimateIntelligence shared Google drive folder.
    - Generate a "live" context document named `claudes_context.md` in the `context/` directory.  We will continue to update it ad infinitum.  
    - Log your work.

3. Very good.  Now, scour the internet for any and all articles, blog posts, and other sources of information on climate change.  Please:
    - Find the most recent and relevant articles, blog posts, and other sources of information on climate change.
    - Generate a well-curated list of sources of information on climate change.  Place it in the `context/` directory and name it `references.md`.
    - Add what you have learned to the `claudes_context.md` document.
    - Log your work.

4. Search the internet for any publications by the following persons and add their works to your context.  Also add the resources to the `references.md` document.

    - Dr Judith Curry
    - Dr John Christy
    - Dr Roy Spencer
    - Dr Steven E Koonin
    - Dr Roger Pielke
    - Dr Williams Happer
    - Dr Richard Lindzen

5. Download the July 2025 DOE Climate Working Group report and add it to the `context/Reports/` directory.  Include its rebuttal too.  Push to the Drive. Read it and update the `claudes_context.md` document accordingly.

### Biodiversity

1. In `context/Murphy/`, I have put a file named `murphy_biodiversity.txt` that contains URLs of blogs and DOIs of articles on biodiversity.  There is also a file named `Chap1_bibtex.txt` with additional references. Please read all of these to gain a better understanding of the subject.  When you are done, please:
    - Update the `claudes_context.md` document with your understanding of the subject.
    - Update the `CI_Reports/CI_2026_07_09_climate_report.md` document with your understanding of the subject.
    - Log your work.


## Discussion
## Discussion

### Claude's questions — prompt 1 / IPCC reports (2026-07-04)

I interpreted "every major report" as the **complete AR6 assessment cycle** (the
current one; AR7 has not yet published): the three Working Group full reports
(WGI Physical Science Basis, WGII Impacts/Adaptation/Vulnerability, WGIII
Mitigation), the Synthesis Report, and the three Special Reports (SR1.5 Global
Warming of 1.5°C, SROCC Ocean & Cryosphere, SRCCL Climate Change & Land) —
seven PDFs, ~1 GB total, staged in `context/Reports/` and copied to
`ClimateIntelligence:Reports/`. Questions:

1. **Earlier cycles?** Do you also want AR5 (2013–14) or older assessment
   reports? They matter for historical context but are largely superseded by AR6.
2. **Summaries for Policymakers?** I grabbed the full reports only. The SPMs are
   inside the full volumes, but standalone SPM PDFs are handy for quick reference
   and blog citation. Want them added?
3. **Drive layout.** I put the PDFs in a `Reports/` subfolder of the shared
   drive (mirroring `context/Reports/`). Fine, or do you want them at the root?
4. `context/Reports/` is now in `.gitignore` (≈1 GB of PDFs; Drive is their
   home, per this task). Undo if you'd rather track them in git.
