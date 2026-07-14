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

### Websites

1. Please review the websites below and update the `claudes_context.md` document with your findings.  Log your work.

    - https://livingplanetindex.org/latest_results

### James Hansen

1. Review the Climate Science Awareness Solutions website and blog posts maintained by Dr. James Hansen.  Update the `claudes_context.md` document with your findings.  Log your work.  Here is the main URL:
`https://www.climatescienceawarenesssolutions.org/communications`

### Biodiversity

1. In `context/Murphy/`, I have put a file named `murphy_biodiversity.txt` that contains URLs of blogs and DOIs of articles on biodiversity.  There is also a file named `Chap1_bibtex.txt` with additional references. Please read all of these to gain a better understanding of the subject.  When you are done, please:
    - Update the `claudes_context.md` document with your understanding of the subject.
    - Update the `CI_Reports/CI_2026_07_09_climate_report.md` document with your understanding of the subject.
    - Log your work.

### Homelessness

1. Please search the New York Times for an article I read a few years ago that described a homeless program.  It offered free housing to the unhoused and then studied the positive impacts on their lives.  It also provided the cost of the program.  If you need my credentials to access the NYT, please ask.  Log your work.

2. Using the links below as a starting point, do a deep dive on the internet on the subject of homelessness.  Then add a new section to the `claudes_context.md` document and add your findings to it.  Then add to the `CI_Reports/CI_2026_07_09_climate_report.md` document as well.  Log your work.

    - https://www.cfthhouston.org/one-year-later-the-new-york-times-article
    - The article(s) in Projects/ClimateIntelligence/context/NYT
    - https://www.urban.org/policy-centers/metropolitan-housing-and-communities-policy-center/projects/denver-supportive-housing-social-impact-bond-initiative

3. Please add to the Report an estimate of the cost per year to house all of the homeless people in the United States based on the data you have gathered.  Log your work.

4. Can you add to the Report an assessment of how other developed nations, especially Canada and Europe, are handling homelessness?  Include specifics on the programs and their costs and outcomes. Be sure to add your references to the `references.md` document. Log your work.

5. Please generate a few figures and charts to support your findings.  Add them to the `CI_Reports/CI_2026_07_09_climate_report.md` document.  Log your work.  Include:

    - A chart showing the number of homeless people in the United States by year.
    - A figure showing the incidence of homelessness by state.
    - A figure showing the incidence of homelessness by country

6. Please see the file `Rebuttals/thayer_2026jul12.txt` which is a critcism of your calculations on homelessness.  Please read it and, if necessary, update your calculations and your Report accordingly.  Be far, balanced, and quantitative.  Either way, provide a response in the Rebuttals section below. Log your work.

#### Rebuttals

##### Response to A. Thayer's critique of the cost estimate (2026-07-13)

Thayer is right on the substance, and the estimate is better for it. I revised
the calculation (`CI_Reports/cost_to_house_homeless.py`, rev. 2) and the Report
§7 accordingly. Point by point, quantitatively:

**(1) "Housing vs. services are different questions." — Conceded; it was the
sharpest point.** Denver's ~$11k/yr was the *housing voucher*; the rest was
services. My original number bundled them and so answered "house *and* support
everyone," not the narrower "put a roof over everyone." The Report now separates
the two. Housing-subsidy-only (voucher ~$11k for the chronic; RRH is already
mostly rent ~$8.5k): **≈ $7–16B/yr, central ~$10B**. Housing + services (net of
offsets): **≈ $6.5–19B/yr, central ~$11B**. Worth noting *why* the two are close:
the services are largely what *produce* the ~$7k/person offset and the high
retention in the RCTs — strip them and you save the services cost but lose much
of the offset and some of the retention. So "just vouchers" is cheaper per
person but buys a weaker outcome; that is a real trade-off, not a free saving.

**(2) "You assumed linear scaling; marginal costs rise." — Largely conceded.**
The pilots housed hundreds; scaling to ~150k+ chronic nationally, in
supply-constrained markets, plausibly raises marginal cost (you bid up rents,
and reach harder cases). I cannot honestly claim to know the marginal-cost
curve, so I now (a) label the figures explicitly as costs *at current average
rates* — a floor — and (b) add a 1.0–1.35× marginal-cost multiplier. This is
also why your point (4) matters so much: in tight markets the marginal unit
doesn't exist at any voucher price.

**(3) "People respond to incentives; you assumed a fixed population." —
Partly conceded, with a bound.** Real effect, and I now show it: the single-night
count (771k) understates the **~1.25M** who use shelter over a year (HUD AHAR
Part 2), and costing that population pushes the net to **~$17B/yr**. Two things
bound the induced-demand worry, though: programs target verified chronic/PIT
individuals via vulnerability indices rather than paying anyone who self-declares,
and the empirical record (Houston, Finland) shows homelessness *falling* under
these programs, not ballooning — the stigma and "trapped-population" evidence
cuts against a large behavioral inflow. So: a genuine upward risk, quantified,
not unbounded.

**(4) "This excludes the cost of *building* housing." — Fully conceded; it is
the biggest point.** Your Santa Cruz thought experiment is exactly right — a
voucher is worthless if there is no room to rent under ~$1k/month. I had flagged
this but not quantified it; now I do. Development runs ~$200k/unit (lower-cost
markets) to ~$550k/unit (California). Building the 152,585 chronic units is a
**one-time ~$30–84B** (~$1–3B/yr amortized); building for the whole PIT
population is **~$150–420B** one-time (~$5–14B/yr amortized). Much of the
population can use *existing* units via vouchers, so the true build need is a
fraction — but where supply binds, this capital cost, not the operating subsidy,
is the real bill. This is the same "binding constraint is housing, not the model"
conclusion the international comparison reached (§7): Finland and Norway
succeeded because they *added supply*; Denmark and Germany run good pilots atop
shortages and their national numbers still rise.

**(5) "Divide by taxpayers, not 350M." — Conceded; trivially fixed.** The Report
now gives all three: **~$32 per resident**, **~$54 per working-age adult**,
**~$93 per federal income-tax payer** per year (central services-inclusive net).
Your point stands and the number is still small — about a tank of gas per
taxpayer per year for the operating cost.

**On the closing question (vouchers/market vs. government provision).** This is
a values/policy question, and per the blog's Principle 4 (keep politics and
ideology out of the science) I won't plant a flag. What I *can* say
descriptively: the evidence base you and I are both citing — Denver, Houston,
Canada's At Home/Chez Soi, Finland — is overwhelmingly **scattered-site,
private-market rental units leased with public subsidy plus services**, i.e.
much closer to your voucher-and-market model than to government-built housing
projects. Finland's Y-Foundation is a hybrid (a nonprofit that *acquires and
builds* stock, then lets it), which is worth noting as a counter-example on the
supply side — precisely because, per point (4), *someone* has to build the units
when the market hasn't. So the honest synthesis is: the delivery evidence favors
market provision of the *housing service*, but market provision has not, on its
own, produced the *units* where they are scarcest — which is the open problem,
not a solved one. We agree on the bottom line: it is affordable, and it should
be done.

### Population

1. Do a deep dive on the internet on the subject of global human population and its evolution over the past 100 years and projections for the future.  Then add a new section to the `claudes_context.md` document and add your findings to it.  Then add to the `CI_Reports/CI_2026_07_09_climate_report.md` document as well.  Be sure to include figures and charts to support your findings. Log your work.

2. For both your Population and Homelessness sections, please be sure to update the `references.md` document with the sources of information you used.

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
