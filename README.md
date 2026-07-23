# 🇪🇺 Software Engineering Internship Tracker — Europe

Auto-updated list of **open software-engineering internships in Europe** —
AI/ML, Data, Mobile, Frontend, Backend/Infra, QA and Security roles — at
28 top tech companies, scraped directly from each company's careers
API every 6 hours by GitHub Actions.

> 🕐 Last updated: **2026-07-23 19:50:10 UTC** · 📌 **17** open internships
> · 🆕 = added in the last 7 days

⭐ Star this repo to keep an eye on new openings — or watch *Releases/Activity* for commits titled “new internship(s)”.

| Company | Open internships |
|---|---|
| Adobe | — |
| Airbnb | — |
| [Amazon](#amazon) | 8 |
| Anthropic | — |
| [Apple](#apple) | 3 |
| Bloomberg | — |
| [Cisco](#cisco) | 1 |
| Cloudflare | — |
| Databricks | — |
| GitHub | — |
| [Google](#google) | 1 |
| Hudson River Trading | — |
| [Intel](#intel) | 1 |
| Jane Street | — |
| [Meta](#meta) | 2 |
| Microsoft | — |
| NVIDIA | — |
| Netflix | — |
| OpenAI | — |
| Oracle | — |
| PayPal | — |
| Pinterest | — |
| Salesforce | — |
| Snap | — |
| [Snowflake](#snowflake) | 1 |
| Spotify | — |
| Stripe | — |
| Uber | — |
| Citadel Securities | *no API — entire site behind a Cloudflare browser challenge; needs a headless browser* |
| LinkedIn | *careers site only links to linkedin.com/jobs, which is authwalled and prohibits scraping* |

---

## Amazon

| Role | Category | Location | Posted | First seen |
|---|---|---|---|---|
| [2027 Software Dev Engineer Intern](https://www.amazon.jobs/en/jobs/10418355/2027-software-dev-engineer-intern) | Software | Dublin, IRL | 2026-05-13 | 2026-07-09 |
| [Software Dev Engineer internship - Embedded Development](https://www.amazon.jobs/en/jobs/3134271/software-dev-engineer-internship-embedded-development) | Backend/Infra | Berlin, Berlin, DEU | 2025-12-01 | 2026-07-09 |
| [Software Dev Engineer Internship - Embedded Development (Linux)](https://www.amazon.jobs/en/jobs/3130528/software-dev-engineer-internship-embedded-development-linux) 🆕 | Backend/Infra | Dresden, Saxony, DEU | 2025-11-21 | 2026-07-20 |
| [2026 Applied Scientist Intern, Amazon University Talent Acquisition](https://www.amazon.jobs/en/jobs/3128215/2026-applied-scientist-intern-amazon-university-talent-acquisition) | AI/ML | Luxembourg, LUX | 2025-11-18 | 2026-07-09 |
| [2026 Applied Scientist Intern, Amazon University Talent Acquisition](https://www.amazon.jobs/en/jobs/3126764/2026-applied-scientist-intern-amazon-university-talent-acquisition) | AI/ML | London, England, GBR | 2025-11-14 | 2026-07-09 |
| [2026 Applied Scientist Intern, Amazon University Talent Acquisition](https://www.amazon.jobs/en/jobs/3120058/2026-applied-scientist-intern-amazon-university-talent-acquisition) | AI/ML | Barcelona, Catalonia, ESP | 2025-11-03 | 2026-07-09 |
| [2026 Applied Scientist Intern, Amazon University Talent Acquisition](https://www.amazon.jobs/en/jobs/3115016/2026-applied-scientist-intern-amazon-university-talent-acquisition) | AI/ML | Berlin, Berlin, DEU | 2025-10-24 | 2026-07-09 |
| [2026 Software Dev Engineer Intern - Germany](https://www.amazon.jobs/en/jobs/3074226/2026-software-dev-engineer-intern-germany) | Software | Berlin, Berlin, DEU | 2025-09-05 | 2026-07-13 |

## Apple

| Role | Category | Location | Posted | First seen |
|---|---|---|---|---|
| [SoC Performance Modeling Internship - Platform Architecture](https://jobs.apple.com/en-us/details/200629965/soc-performance-modeling-internship-platform-architecture) | Backend/Infra | London | 2025-11-04 | 2026-07-09 |
| [SoC Performance Modeling Internship - Platform Architecture (m/f/d)](https://jobs.apple.com/en-us/details/200622296/soc-performance-modeling-internship-platform-architecture-m-f-d) | Backend/Infra | Munich | 2025-09-22 | 2026-07-09 |
| [GPU Internship - Platform Architecture](https://jobs.apple.com/en-us/details/200617616/gpu-internship-platform-architecture) | Backend/Infra | London | 2025-08-26 | 2026-07-09 |

## Cisco

| Role | Category | Location | Posted | First seen |
|---|---|---|---|---|
| [ML Researcher Intern - Prague - Czechia](https://careers.cisco.com/global/en/job/2005347) | AI/ML | Prague, Praha, Czechia | 2026-04-29 | 2026-07-09 |

## Google

| Role | Category | Location | Posted | First seen |
|---|---|---|---|---|
| [Apprenticeship in Application Development, Informatiker:in EFZ Applikationsentwicklung, August 2027](https://www.google.com/about/careers/applications/jobs/results/135233176434811590) | Software | Zürich, Switzerland | 2026-07-01 | 2026-07-09 |

## Intel

| Role | Category | Location | Posted | First seen |
|---|---|---|---|---|
| [AI Software Engineering Intern](https://intel.wd1.myworkdayjobs.com/en-US/External/job/Poland-Gdansk/AI-Software-Engineering-Intern_JR0285471) | AI/ML | Poland, Gdansk | 2026-07-08 | 2026-07-09 |

## Meta

| Role | Category | Location | Posted | First seen |
|---|---|---|---|---|
| [Research Scientist Intern, Photorealistic Telepresence (PhD)](https://www.metacareers.com/jobs/924149567345400) | AI/ML | London, UK | — | 2026-07-09 |
| [Research Scientist Intern, AI/ML, Core Ads Growth (PhD)](https://www.metacareers.com/jobs/771948392580541) | AI/ML | London, UK; Zurich, Switzerland | — | 2026-07-09 |

## Snowflake

| Role | Category | Location | Posted | First seen |
|---|---|---|---|---|
| [Software Engineer Intern - Berlin (2026)](https://careers.snowflake.com/us/en/job/3a9baeaf-b107-41fb-a9b3-a98ab78275ed) | Software | Berlin, Germany | 2026-06-02 | 2026-07-09 |


---

## How this works

A [Python scraper](scraper/) queries each company's official careers API
(Greenhouse, Ashby, Workday, Eightfold or their in-house endpoints), filters
titles matching *intern / internship / co-op*, keeps only software-engineering
roles ([scraper/categories.py](scraper/categories.py)) located in Europe
([scraper/regions.py](scraper/regions.py)), and diffs against
[`data/jobs.json`](data/jobs.json). A GitHub Actions
[workflow](.github/workflows/update.yml) runs it on a cron schedule and commits
only when something changed. Positions that disappear from a careers page are
closed automatically.

Found a problem or want another company added? Open an issue or PR.
