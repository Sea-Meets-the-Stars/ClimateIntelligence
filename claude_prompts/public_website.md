# Public Website

## Goals

This prompt doc will create and maintain the public website for Climate Intelligence


## Context

See your context file `context/claudes_context.md` for the current context.

All of the figures (and related code) in this Repository.

The Organization website is `https://github.com/Climate-Intelligence`

the site repo needs to be named Climate-Intelligence.github.io. It will then publish at https://climate-intelligence.github.io/.

See the file `context/public_website_PLANNING.rst` for the planning for the website.


## Prompts

### Create

1. I am going to have you build out the public website.  Begin by reading all
of the files in the Context section above.  Then ask me a series of questions to
understand the website and its goals.  Put those in Q&A section below.
Use Fable if you can.  Log your work as per this Repo's logging conventions.

2. I have answered the first round of questions.  Please review them, react accordingly, and ask another round of questions.  
Use Fable if you can.  Log your work as per this Repo's logging conventions.

3. I have answered the second round of questions.  Please review them, react accordingly, and ask another round of questions if necessary.  
I am working through the GitHub for X section now.
Use Fable if you can.  Log your work as per this Repo's logging conventions.

4. I have answered the third round of questions.  Please review them, react accordingly.
I will then install the additional dependencies. 
Use Fable if you can.  Log your work as per this Repo's logging conventions.

5. Build the site
Use Fable if you can.  Log your work as per this Repo's logging conventions.


## Q&A
### Create — round 1 (2026-10-10, Fable 5.1)

I read `context/claudes_context.md` (all 18 sections), `context/public_website_PLANNING.rst`,
`principles.md`, `README.md`, `ToDo.md`, `blogs/ideas.md`, the earlier
`claude_prompts/website.md` Q&A (banner graphic + taglines), and surveyed the
figures and scripts in `CI_Reports/`, `blogs/blog001/`, `presentations/2026_WMKO/`,
and `docs/`. I also confirmed (read-only) that the `Climate-Intelligence` GitHub
organization exists (created 2026-10-10) with zero repositories so far, and that
this development repo is public under `Sea-Meets-the-Stars`.

The planning doc is already quite concrete. My questions aim at the decisions it
leaves open, the things it does not mention, and a few places where I would push
back. Please answer inline after each **Answer:**.

**A. Identity and voice**

1. The site's one-line description. The README says "A blog on the science of the
   climate — and a lot more." The banner tagline is "Where climate science meets
   artificial intelligence." Which goes in the site header / `<title>` / Atom
   feed subtitle, or do you want a third?

   Answer: How about "Coping with the greatest two exponentials affecting our future:  
   Climate Crisis and Artificial Intelligence"?

2. Is Climate Intelligence presented as *your* blog (J. Xavier Prochaska, with
   Claude as collaborator), or as a project/organization with you as founding
   author? This drives the About page, the author field on posts, and whether
   ablog's author list has one entry or several (undergrads, a future Board per
   `ToDo.md`).

   Answer:  Yes, my blog.  I am the founder and sole author for now

3. How visible should the human+AI collaboration be on the site? Options: (a) a
   sentence on About only; (b) a dedicated "How this blog is made" page that
   explains the workflow and links to the token/CO2 logging; (c) a per-post
   footer such as "Drafted with Claude; reviewed by the author." I lean toward
   (b)+(c) because transparency is the whole point of the logging system.

   Answer: (b)+(c)

4. Should the six Guiding Principles from `principles.md` appear verbatim on the
   site (their own page, or on About)? And the five topic areas (climate
   physics, biodiversity, global population, unhoused, AI) as the site's
   top-level categories?

   Answer:  Yes, I like that

**B. Content at launch**

5. What exists to publish on day one? I see Blog 001 (figures done, text in
   Google Docs), the 2026-07-09 climate report, the CO2 report, the
   work-hours report, and the WMKO talk. Which of these, if any, go on the site
   at launch, and in what form (post, standalone page, PDF download)?

   Answer:  At day 1, it will only be the Blog.  

6. The planning doc lists Blog, Podcast, and Shorts as content streams. Do a
   podcast and shorts actually exist or are planned soon? If not, I would launch
   with only the Blog card and add the others when there is content, rather
   than ship empty pages.

   Answer:  They are planned, but not yet created.

7. Do you want a "Reports" stream for the longer `CI_Reports/` documents (they
   are not blog posts in tone or length), and a "Talks" stream for the WMKO deck
   and future presentations?

   Answer:  We won't expose the Reports at this time.  Nor the Presentations yet

8. Should the Bokeh token-usage/CO2 plot (`Logs/token_usage_and_co2_emissions.html`)
   be exposed on the site, as the logging spec anticipated? If yes, should it be
   a live page updated on each build (the site repo would need the CSV) or a
   periodically copied snapshot?

   Answer:  Yes, it should be a live page updated on each build

**C. Architecture decisions the plan leaves open**

9. Theme: `pydata-sphinx-theme` or `furo`? My recommendation is pydata: it has a
   proper top navbar for the content streams, a sidebar that ablog's widgets
   slot into, and light/dark mode. Furo is cleaner for pure docs but weaker for
   a multi-section blog. Confirm or override.

   Answer: Ok, let's try pydata

10. Tags vs categories. I propose categories = the five topic areas (one per
    post) and tags = free-form (e.g. "exponentials", "IPCC", "Hansen",
    "planetary boundaries"). Agree? Any tags you already know you want?

    Answer:  Yes, that sounds good.  For tags, let's start with "exponentials", "planetary boundaries" 

11. Comments on the live site: none, giscus (GitHub Discussions in the site
    repo), or external? Giscus is free and keeps comments in GitHub, but readers
    need a GitHub account. The plan also says collaborators comment on drafts in
    Google Docs, so public comments may be a separate decision.

    Answer:  Let us try `giscus`

12. License for site content. The dev repo is BSD-3-Clause, which suits code.
    For prose and figures I would use CC BY 4.0 (attribution required, reuse
    allowed). Alternatives: CC BY-NC 4.0 (no commercial reuse) or all rights
    reserved. Which?

    Answer:  Ok, use CC BY-NC 4.0

13. Custom domain: do you own or intend to buy one (e.g. climateintelligence.org)?
    If undecided, I will build for `climate-intelligence.github.io` and leave
    the CNAME hook in place.

    Answer:  Stick with `climate-intelligence.github.io` for now and leave the CNAME hook in place

14. Analytics: none, or a privacy-friendly option (Plausible, GoatCounter,
    Umami)? None is the simplest and the most consistent with the blog's ethos.

    Answer:  None is fine

**D. Workflow and the two-repo rule**

15. The plan says "once a post is finalized, its rst moves into the site repo."
    But the figure *scripts* live here. Should the site repo hold only the
    rendered PNGs (my recommendation: keep the site build independent, as the
    plan says), with each figure caption linking back to the script in this
    dev repo for reproducibility?

    Answer:  Use your recommendation.

16. Who creates the `Climate-Intelligence.github.io` repo? Per CLAUDE.md I do
    not run git commands that change state. I propose: you create the empty
    public repo in the org and set Pages to "GitHub Actions"; I scaffold the
    whole site into a local clone and you commit and push. Confirm, and tell me
    the local path where you want the clone (e.g. `~/Projects/Climate-Intelligence.github.io`).

    Answer: I confirm.  And the path you suggested is fine.  Give me the instructions
    of what to do to make the empty public repo.  Provide that in the "GitHub for X" section below.

17. Should the site scaffold be built and verified in the `ocean14` conda env,
    or in a fresh env matching the CI's Python 3.12 and pinned
    `requirements.txt`? I recommend a fresh env so the local build proves the
    CI build.

    Answer:  I have bumped the Python requirement to 3.13 in setup.py.  
    I have created a new conda environment with Python 3.13 named `CI`.
    Please clean up `setup.py` and `requirements.txt` to be a modern
    approach to installation.

18. Do you want to transfer this dev repo into the `Climate-Intelligence` org,
    and should it stay public? `Logs/` contains verbatim prompts and the
    `context/` folder holds copyrighted PDFs (Murphy textbook, NYT article).
    My concern: a public dev repo redistributes those PDFs. Consider making it
    private, or at least adding `context/Murphy/*.pdf` and `context/NYT/` to
    `.gitignore` going forward.

    Answer:  Agreed, let's have the PDFs be gitignored going forward.
    Is there an advantage to moving the dev repo into the `Climate-Intelligence` org?  If not, let's leave it here for now

**E. Look and feel**

19. Should the banner from `docs/CI_graphic.py` be the site's logo/hero image,
    and should I derive a small square favicon and a navbar logo from the same
    script (adding it as a new output of that script)?

    Answer: Yes, use that banner for the public website.  
    We made a new graphic for the WMKO public talk that I wish to 
    use for the README of the dev repo. 
    It is the one with the blog, podcast, and shorts, etc.
    Let me know if you can't find it

20. Color palette: match the banner's palette, or let the theme defaults stand
    at launch? Light theme only, or offer a dark-mode toggle?

    Answer:  Sure, try to match the banner's palette.

21. The planning doc converts Google Docs to rst via pandoc. For Blog 001 the
    figures were made here with matplotlib. Do you want me to draft a figure
    directive convention (rst `.. figure::` with caption, source link, and
    alt text) now, so every post follows one pattern from the start?

    Answer:  Yes, draft a figure directive convention 

**F. Scope of what I build next**

22. Once you answer, I intend to deliver in one pass: the full site scaffold
    (`conf.py`, `index.rst`, stream pages, About, `requirements.txt` with
    pinned versions, `deploy.yml`, `README.rst`), a placeholder first post so
    the postlist and feed render, and a local build log. Anything to add or
    remove from that list before I start?

    Answer:  That list is good, but we need to iterate one or two more
    times before you proceed with the build.

### Create — round 2 (2026-10-10, Fable 5.1)

**Reactions to round 1, and what I did about them**

- *Packaging (Q17).* Replaced `setup.py` with a PEP 621 `pyproject.toml`
  (Python ≥ 3.13, BSD-3-Clause, package data for `climate_intelligence/data/`,
  extras `blog` = bokeh and `dev` = pytest + IPython). `requirements.txt` now
  just installs the project in editable mode. A dry-run install in the `CI` env
  resolves. The `bin/` scripts are no longer installed as console scripts; they
  are analysis scripts, run them directly. Install with
  `conda run -n CI python -m pip install -e ".[blog,dev]"`. `setup.py` is
  deleted from the working tree; you will need to `git rm` it.
- *PDFs (Q18).* Already handled: `.gitignore` has had `*.pdf` for a while and
  `git ls-files` shows no PDF is tracked. Nothing to do.
- *Moving the dev repo into the org (Q18).* Advantages are modest: one owner
  for both repos, org-level teams for undergrads or a Board, and GitHub
  redirects old URLs. Disadvantages: none technical, but `Sea-Meets-the-Stars`
  is presumably your lab's org and the repo's history and license say so. My
  recommendation: leave it for now, revisit when there are collaborators who
  need org permissions.
- *README graphic (Q19).* Found it: `s3_ci_concept.png` from
  `presentations/py/ci_schematic.py` (hub with Blog and Podcast, spokes to
  YouTube, TikTok, Instagram). Copied to `docs/CI_concept.png` and swapped into
  `README.md` in place of the banner. The banner is reserved for the site.
- *Tagline (Q1).* I like the idea but at 14 words it is too long for a navbar
  or a `<title>`. See Q23.
- *giscus (Q11).* Needs the site repo to be public with Discussions enabled and
  the giscus app installed. Added to the GitHub instructions below.
- *CC BY-NC 4.0 (Q12).* Fine. One note: figures built from Our World in Data
  are CC BY, which is compatible. The site footer and About will carry the
  license; the dev repo stays BSD for code.
- *Live CO2 page (Q8).* This is the one answer that collides with the plan's
  rule that the site build must not depend on the dev repo. See Q25.

**Round 2 questions.** Please answer inline after each **Answer:**.

**A. Identity and voice**

23. Tagline placement. Proposal: the navbar and `<title>` show just "Climate
    Intelligence"; the landing-page hero shows your sentence in full; and the
    Atom feed subtitle and HTML meta description use a short form. Candidates
    for the short form (pick, edit, or keep the long one everywhere):
    - "Two exponentials, one future: climate and AI."
    - "Coping with the two great exponentials: the climate crisis and AI."
    - "The climate crisis and artificial intelligence, read carefully."

    Answer: "Coping with the two great exponentials: the climate crisis and AI."

24. Author display. ablog shows an author on each post. "Xavier" (as in the
    planning sketch), "J. Xavier Prochaska", or "X. Prochaska"? And should the
    About page name your UCSC affiliation and a contact email, or stay
    personal (no affiliation, contact via GitHub Discussions only)?

    Answer:  "J. Xavier Prochaska".  Yes on UC Santa Cruz affiliation but no contact email.

**B. The live CO2 page**

25. Mechanism. For the Bokeh page to update on each build, the site build needs
    `log_summary.csv` and the plot script. Options:
    - (a) The site's deploy workflow downloads the CSV from this dev repo's raw
      GitHub URL at build time and runs a copy of the plot script that lives in
      the site repo. Simple, but the site build now depends on the dev repo
      being public and online (it fails gracefully to the last snapshot if I
      add a fallback).
    - (b) A GitHub Action in *this* repo, on every push to `main`, copies the
      CSV into the site repo and triggers its deploy. Keeps the site build
      self-contained but needs a cross-repo token (a fine-grained PAT stored
      as a secret).
    - (c) Snapshot: I regenerate the HTML here and you copy it to the site repo
      when you publish a post. No automation, but zero coupling.
    I recommend (a) with a weekly scheduled rebuild so the page moves even when
    no post is published. Which?

    Answer: (a)

26. The plot shows prompt-level data: timestamps, token counts, model names.
    Nothing sensitive, but it does publish your working hours. OK?

    Answer: OK

27. Headline framing for that page. Cumulative grams of CO2 and the car-miles
    equivalent are already in the plot. Do you also want a short prose intro
    explaining the method (linking the formula from `Logs/logging.md`), and
    should the page be titled "Our footprint", "Cost of this blog", or
    something else?

    Answer: Title as "Our footprint" and do include a short prose intro explaining the method (linking the formula from `Logs/logging.md`)

**C. Navigation and pages**

28. Navbar at launch. Proposal: Blog · About · Principles · How it's made ·
    Footprint. Podcast and Shorts are hidden until there is content (no
    "coming soon" pages). The social spokes from the concept graphic (YouTube,
    TikTok, Instagram) appear as footer icons only once the accounts exist. Do
    any of those accounts exist today?

    Answer: I like your suggestions.  These accounts do not exist yet.

29. Per-post footer wording (Q3c). Proposal: "Drafted with Claude (Anthropic);
    reviewed and edited by the author. See How it's made." Edit as you like.

    Answer: "Built with Claude (Anthropic). See How it's made."

30. "How it's made" content. I plan: the two-repo workflow, Google Docs
    drafting and review, pandoc conversion, the logging and CO2 accounting
    with a link to the Footprint page, and the guiding principles' role in
    editing. Anything to add or leave out, for example the names of
    reviewers or undergrads?

    Answer:  Add -- The Blog is human written with JXP constructing the figures using Claude.  The Blog is reviewed and edited by friends of JXP.

**D. The first post**

31. Blog 001 is the only day-one content. Is its text final? If yes, download
    it as `.docx` into `blogs/blog001/` and I will convert it with pandoc into
    the site repo. If not, I will create a short placeholder post so the
    postlist and feed render, and we swap in Blog 001 when it is ready.

    Answer:  Create a placeholder post for now.  I will finish the blog in the next day or two

32. Blog 001 metadata: title, publication date (the post date drives the
    archive and the feed), category (I assume "Global population" or "AI"
    given the exponentials theme), and tags (I assume "exponentials").

    Answer:  You can find the draft of `Blog 001` on my shared Google Drive folder
    by using rclone and accessing `ClimateIntelligence:Blogs/Blog 001`. 
    It is a Google doc
    

33. Post URL scheme. ablog defaults to `/blog/2026/10/15/my-first-post/`. I
    prefer the plan's shorter `/posts/2026/my-first-post/`. Confirm?

    Answer: I am simply numbering them.  So, use `/posts/001/blog-001/`

**E. Look and feel**

34. Logo and favicon (Q19). The banner is wide and does not shrink to a
    square. For the navbar logo and favicon I would make a compact mark from
    the same script: the "CI" letters in the banner's navy with the warm
    accent, or the temperature-trend curve alone. Preference, or shall I make
    both and you choose?

    Answer:  Make both

35. Palette mapping (Q20). From `docs/scripts/CI_graphic.py`: primary navy
    `#123b52`, accent `#c24a3f`, text `#16222e`, muted `#6b7885`, background
    `#fbfcfe`. pydata-sphinx-theme exposes these as CSS variables, so I would
    set primary = navy and secondary = accent, and keep the theme's dark mode
    with lightened versions. OK to offer the dark-mode toggle?

    Answer: OK

36. Figure directive convention (Q21). Proposal, for every figure:

    .. code-block:: rst

       .. figure:: media/fig2_population_growth.png
          :alt: World population 10,000 BCE to 2025 on a log axis, with fitted exponential periods
          :width: 100%
          :name: fig-blog001-2

          **Figure 2.** World population since 10,000 BCE. Data: HYDE 3.3 and
          UN WPP 2024. Source code: `make_fig2_population_growth.py
          <https://github.com/Sea-Meets-the-Stars/ClimateIntelligence/blob/main/blogs/blog001/make_fig2_population_growth.py>`_.

    Rules: bold "Figure N." leads the caption; data sources named in the
    caption; source link to the script on `main` in this repo; alt text
    describes what the figure shows, not its title. Should the source link
    pin a commit hash instead of `main` (more reproducible, more tedious)?

    Answer: Use your suggestions but no need for a commit hash

**F. Process**

37. Local build check. When I scaffold, I will build in the `CI` env with the
    pinned `requirements.txt` of the site repo and leave the build log in this
    repo's `Logs/`. Do you want sphinx's `-W` (warnings fail the build) on from
    day one, as the plan suggests?

    Answer: Yes, use `-W` from day 1

38. You said one or two more rounds. After you answer this round, is there a
    particular area you still want to probe (design, workflow, content), or
    shall I propose a wireframe of the landing page as the next round?

    Answer: No, we are nearly ready

### Create — round 3 (2026-10-10, Fable 5.1)

**Reactions to round 2, and what I did about them**

- *Logo and favicon (Q34).* Made both, as new outputs of
  `docs/scripts/CI_graphic.py` (run in `ocean14`): `docs/CI_mark_letters.png`
  (navy rounded tile, "C" in the page colour, "I" in the warm accent) and
  `docs/CI_mark_curve.png` (light tile with a navy edge, the banner's observed
  dots and accent trend curve). Both are 1024 px square with a transparent
  corner so they sit well on a navbar. Re-running the script also re-encoded
  the two existing banner PNGs; the design is unchanged, so discard those two
  diffs if you prefer no churn.
- *Blog 001 (Q31, Q32).* Read the draft over rclone (`v3 – 2026-09-26 RN
  edits`). Working title "Humans Suck at Exponentials" (a comment says the
  title will not stay), five figures matching `blogs/blog001/`, and one
  reviewer comment still open (the "what do you mean by emissions" note on
  Figure 4). I will build a placeholder post now and convert Blog 001 when
  you say it is final.
- *URL scheme (Q33).* `/posts/001/blog-001/` works directly from the folder
  `docs/posts/001/blog-001/index.rst`; no ablog date pattern needed.
- *CO2 page (Q25a).* The site's workflow will fetch `Logs/log_summary.csv`
  from the raw URL on `main` of this repo at build time, run a copy of the
  Bokeh script kept in the site repo, and fall back to the last committed
  HTML if the fetch fails. A weekly cron rebuild keeps it moving between
  posts. One dependency: the CSV must be on `main` here, and you are
  currently on `public-website`.
- *Everything else* (short tagline in header and feed, full sentence as
  hero; "J. Xavier Prochaska", UC Santa Cruz, no email; navbar Blog · About ·
  Principles · How it's made · Footprint; footer "Built with Claude
  (Anthropic). See How it's made."; "Our footprint" with a method intro;
  figure convention without commit hashes; `-W` from day one) is decided and
  goes straight into the scaffold.

**State of the GitHub steps** (checked read-only at 15:14 UTC): the org still
has no repositories and there is no clone at
`~/Projects/Climate-Intelligence.github.io`. Also, `pandoc` is not installed
on this machine and the `CI` env has no Sphinx stack yet. See Q43.

**Round 3 questions.** Short, and the last before the build.

39. Blog 001 category. It spans all five topics (COVID, population, AI, CO2,
    fertility). ablog allows several categories per post. Options: (a) tag it
    with all relevant categories; (b) pick one, probably "Artificial
    Intelligence" or "Global population"; (c) add a sixth category
    "Cross-cutting" for posts like this. I lean (a).

    Answer: (a)

40. Which mark where? My recommendation: the curve mark as the navbar logo
    beside the wordmark, and the letters mark as the favicon, since "CI"
    still reads at 16 px and the curve does not. Or one mark for both?

    Answer: Go with your recommendation

41. "Reviewed and edited by friends of JXP." Should How it's made name them
    (and the "RN" of the draft's version line), or keep it anonymous? If
    named, give me the list.

    Answer: Keep them annonymous for now.  I will eventually add a "Contributors" list

42. The placeholder post. I would make it a short, permanent launch note at
    `/posts/000/welcome/` ("What this blog is, and how it is made"), dated
    the day the site goes live, so the postlist and feed are never empty and
    Blog 001 keeps its number. Or a throwaway stub I delete when Blog 001
    lands?

    Answer: Yes, create a short, permanent launch note at `/posts/000/welcome/`

43. Tooling before the build. I need `pandoc` (for Blog 001 later) and the
    site's Python stack in the `CI` env. May I run
    `conda install -n CI -c conda-forge pandoc` and
    `conda run -n CI pip install -r <site>/requirements.txt`? Both touch only
    the `CI` env.

    Answer: Add what you need to `requirements.txt` and I will run the install command

44. giscus. Once the site repo exists with a Discussions category named
    `Comments`, I can fetch the repo and category IDs myself with the GitHub
    API; nothing else is needed from you. Confirm the category name, and
    whether comments are on for every post by default.

    Answer: I think we are set for that

45. Go. When the repo is created and cloned, and you have answered 39–44,
    prompt #4 can simply be "build it". Anything else you want settled first?

    Answer:  Agreed.

### Create — round 4 (2026-10-10, Fable 5.1): reactions to round 3, ready to build

**Dependencies (Q43).** Added a `site` extra to `pyproject.toml` with the
packages the site needs, unpinned here so the `CI` env resolves to current
releases: `sphinx`, `ablog`, `pydata-sphinx-theme`, `sphinx-design`,
`sphinxcontrib-youtube`, and `pypandoc-binary` (which bundles the `pandoc`
executable, so no brew or conda install is needed). `requirements.txt` now
installs `-e .[blog,dev,site]`. A dry-run in the `CI` env resolves to Sphinx
9.1.0, ablog 0.11.13, pydata-sphinx-theme 0.23.0, sphinx-design 0.7.0,
sphinxcontrib-youtube 1.5.0, pypandoc-binary 1.17. The site repo's own
`requirements.txt` will pin exactly these. Please run:

.. code-block:: bash

   conda run -n CI python -m pip install -r requirements.txt

**State of GitHub (checked read-only at 15:31 UTC).**

- Site repo exists, public; the clone at
  `~/Projects/Climate-Intelligence.github.io` is there, on `main`, with no
  commits yet. Exactly what the scaffold needs.
- Pages is set to build from GitHub Actions (`build_type: workflow`). Done.
- Discussions is on with the six default categories. No `Comments` category
  was created, so giscus will use **Announcements** (maintainers open
  threads, readers reply), which is what I wanted anyway. I have the repo
  and category IDs from the API.
- I could not confirm from the API whether the giscus app is installed on
  the repo (that query needs org-admin scope my token lacks). If it is not,
  the comment box will show a giscus error after launch and installing the
  app fixes it with no rebuild. Not a blocker.
- `Logs/log_summary.csv` is on `main` of this dev repo, so the Footprint
  page's build-time fetch will work. It will lag your local CSV until you
  merge `public-website`.

**Decisions carried into the build.**

- Blog 001 will carry all five categories (Q39).
- Navbar logo = curve mark; favicon = letters mark (Q40).
- Reviewers stay anonymous; How it's made says "reviewed and edited by
  friends of the author" and leaves room for a Contributors list (Q41).
- Permanent launch note at `/posts/000/welcome/`, dated the day you push
  (Q42). I will set the date to the day I scaffold; edit it if the push
  slips.
- Comments on by default for every post (Q44).

**No further questions.** Prompt #5 builds the site into the clone. You then
review the local build, commit, and push.

## GitHub for X

Steps for you to run, in order. Everything here is in the GitHub web UI or your
shell; none of it requires me.

1. **Create the site repo.** At https://github.com/organizations/Climate-Intelligence/repositories/new
   set Repository name exactly `Climate-Intelligence.github.io`, visibility
   **Public** (required for free Pages and for giscus), and leave "Add a
   README", `.gitignore`, and license **unchecked** so the repo is empty. Click
   Create repository.

2. **Set Pages to deploy from Actions.** In the new repo: Settings → Pages →
   Build and deployment → Source: **GitHub Actions**. Nothing else to pick; the
   workflow I write will register itself on the first push.

3. **Enable Discussions (for giscus).** Settings → General → Features → check
   **Discussions**. Then open the Discussions tab once so GitHub creates the
   default categories; I will use a category named `Comments` (create it under
   Discussions → Categories → New category, format "Announcement" so only
   maintainers can start threads and readers can only reply).

4. **Install the giscus app.** Visit https://github.com/apps/giscus → Install →
   choose the `Climate-Intelligence` organization → "Only select repositories"
   → `Climate-Intelligence.github.io`. I will fill in the repo and category IDs
   from https://giscus.app when I scaffold.

5. **Clone it locally.** In your shell:

   .. code-block:: bash

      cd ~/Projects
      git clone https://github.com/Climate-Intelligence/Climate-Intelligence.github.io.git

   The clone will be empty. I will scaffold into it; you commit and push.

6. **After the first push,** check the Actions tab for the "Build and deploy
   site" run, then https://climate-intelligence.github.io/.

Optional, only if you choose option (b) in Q25: create a fine-grained personal
access token scoped to the site repo with Contents: read and write, and add it
as a secret named `SITE_REPO_TOKEN` in *this* dev repo (Settings → Secrets and
variables → Actions).
