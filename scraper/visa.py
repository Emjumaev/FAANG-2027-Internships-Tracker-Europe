"""Per-company visa-sponsorship stance for internships.

This is hand-maintained reference data, not scraped: each entry was checked
against the company's student FAQ or the wording of its current intern
postings (see `source`). Policies change and individual postings override the
company default, so the listing itself is always the final word.

status values:
  "yes"      sponsors intern visas / explicitly accepts candidates who need one
  "limited"  case-by-case — depends on the role, country or visa type
  "no"       postings require existing work authorization, no sponsorship
  "unknown"  nothing conclusive published
"""

STATUS_LABEL = {
    "yes": "✅ Sponsors",
    "limited": "⚠️ Case-by-case",
    "no": "❌ No sponsorship",
    "unknown": "❔ Unknown",
}

VISA = {
    "Adobe": {
        "status": "unknown",
        "note": "Edinburgh/London 13-month and Bucharest 6-9 month intern postings don't state right-to-work terms",
        "source": "https://builtin.com/job/2026-intern-software-engineer/7422310",
        "confidence": "low",
        "checked": "2026-10-15",
    },
    "Airbnb": {
        "status": "unknown",
        "note": "No Europe-based SWE internship postings found; program is US-only (SF/remote US)",
        "source": "https://builtin.com/job/software-engineering-intern/7916098",
        "confidence": "high",
        "checked": "2026-10-15",
    },
    "Amazon": {
        "status": "unknown",
        "note": "Dublin/London/Berlin 2026 SDE intern postings don't state visa or right-to-work terms; ask recruiter",
        "source": "https://amazon.jobs/en/jobs/2713207/2025-program-manager-intern",
        "confidence": "medium",
        "checked": "2026-10-15",
    },
    "Anthropic": {
        "status": "no",
        "note": "London Fellows must already hold UK work authorization; Anthropic does not sponsor fellows",
        "source": "https://jobs.accel.com/companies/anthropic/jobs/74068663-anthropic-fellows-program",
        "confidence": "high",
        "checked": "2026-10-15",
    },
    "Apple": {
        "status": "unknown",
        "note": "Munich/Zurich intern postings found but none state visa or work-permit terms",
        "source": "https://www.extern.com/post/apple-internship-guide",
        "confidence": "low",
        "checked": "2026-10-15",
    },
    "Bloomberg": {
        "status": "limited",
        "note": "London/Dublin eng intern posts silent; London non-eng intern listing says Bloomberg sponsors (secondary)",
        "source": "https://www.extern.com/post/bloomberg-internship-guide",
        "confidence": "medium",
        "checked": "2026-10-15",
    },
    "Cisco": {
        "status": "no",
        "note": "Krakow/Lisbon postings: must already be able to live and work there with no visa sponsorship; Galway needs EU rights",
        "source": "https://jobright.ai/jobs/info/6a0bf82d963f7a67d95d42af",
        "confidence": "medium",
        "checked": "2026-10-15",
    },
    "Cloudflare": {
        "status": "no",
        "note": "Lisbon and London intern postings: no relocation or visa sponsorship, must already have right to work",
        "source": "https://job-boards.greenhouse.io/cloudflare/jobs/7738938",
        "confidence": "medium",
        "checked": "2026-10-15",
    },
    "Databricks": {
        "status": "unknown",
        "note": "Amsterdam/Berlin/London/Belgrade 2027 intern postings carry no right-to-work or sponsorship wording",
        "source": "https://www.databricks.com/company/careers/university-recruiting/software-engineering-intern-2026-6865687002",
        "confidence": "low",
        "checked": "2026-10-15",
    },
    "GitHub": {
        "status": "unknown",
        "note": "No Europe-based GitHub internship postings found",
        "source": "https://nodesk.co/remote-jobs/github-software-engineering-intern/",
        "confidence": "low",
        "checked": "2026-10-15",
    },
    "Google": {
        "status": "no",
        "note": "London/Zurich/Dublin/Munich 2026 SWE+SRE interns: no immigration sponsorship; must be EMEA student located in-country",
        "source": "https://jobs.anitab.org/companies/google-24698/jobs/58499871-software-engineering-site-reliability-engineering-bs-ms-intern-2026",
        "confidence": "high",
        "checked": "2026-10-15",
    },
    "Hudson River Trading": {
        "status": "yes",
        "note": "London SWE internship listings carry same visa-sponsorship benefit plus paid housing and travel allowance",
        "source": "https://www.themuse.com/jobs/hudsonrivertrading/software-engineering-internship-c-or-python-summer-2027",
        "confidence": "medium",
        "checked": "2026-10-15",
    },
    "IBM": {
        "status": "no",
        "note": "UK internships/placements require right to work in UK (no visa sponsorship); German Ehningen posts require enrolment, no relocation",
        "source": "https://www.themuse.com/jobs/ibm/software-developer-internship-2026",
        "confidence": "high",
        "checked": "2026-10-15",
    },
    "Intel": {
        "status": "unknown",
        "note": "Gdansk/Munich/Leixlip intern postings not verified; Intel's non-US intern postings elsewhere say 'No visa sponsorship'",
        "source": "https://builtin.com/job/software-engineering-intern-bachelor-s/7557806",
        "confidence": "high",
        "checked": "2026-10-15",
    },
    "Jane Street": {
        "status": "yes",
        "note": "London internship listings include visa sponsorship plus flights and accommodation for the program",
        "source": "https://jobsconnect.prosple.com/graduate-employers/jane-street/jobs-internships/software-engineer-internship",
        "confidence": "medium",
        "checked": "2026-10-15",
    },
    "Mastercard": {
        "status": "limited",
        "note": "Lisbon 2026 SWE intern post is silent on visas; other EU early-career posts (Warsaw, Copenhagen, Istanbul) say no sponsorship",
        "source": "https://builtin.com/job/platform-engineering-intern-summer-2026-st-louis-mo/7232224",
        "confidence": "high",
        "checked": "2026-10-15",
    },
    "Meta": {
        "status": "limited",
        "note": "London SWE intern posting: 'Must obtain UK work authorization at time of hire'; sponsorship not stated either way",
        "source": "https://jobs.anitab.org/companies/meta-3-c00df464-9d7f-4a12-a5c0-f043ccf7bf75/jobs/58835198-software-engineer-intern-co-op",
        "confidence": "medium",
        "checked": "2026-10-15",
    },
    "Microsoft": {
        "status": "no",
        "note": "UK SWE intern posting: 'You must be legally authorised to work in the UK to be eligible'; Czech posting same",
        "source": "https://flexa.careers/jobs/microsoft-software-engineer-internship-opportunities-66e806d24731caf085f888f7",
        "confidence": "medium",
        "checked": "2026-10-15",
    },
    "NVIDIA": {
        "status": "unknown",
        "note": "Germany/Poland remote and Munich/Zurich intern postings carry no visa or work-permit wording",
        "source": "https://www.extern.com/post/nvidia-internship-guide",
        "confidence": "low",
        "checked": "2026-10-15",
    },
    "Netflix": {
        "status": "unknown",
        "note": "Warsaw SWE intern posting exists (4th/5th-year students) but states no visa or work-permit terms",
        "source": "https://www.extern.com/post/netflix-internship-guide",
        "confidence": "low",
        "checked": "2026-10-15",
    },
    "OpenAI": {
        "status": "unknown",
        "note": "No Europe-based SWE internship postings found; Ashby board lists US-only intern roles",
        "source": "https://jobs.stripes.co/companies/openai/jobs/65336977-software-engineer-internship-co-op-applied-emerging-talent-fall-2026",
        "confidence": "low",
        "checked": "2026-10-15",
    },
    "Oracle": {
        "status": "unknown",
        "note": "No Europe intern wording found; roles post per country on careers.oracle.com, check right-to-work line",
        "source": "https://simplify.jobs/p/c8105a36-7da9-4019-bfdb-e9668188553d/Java-Software-Engineer-Intern",
        "confidence": "high",
        "checked": "2026-10-15",
    },
    "PayPal": {
        "status": "unknown",
        "note": "London/Luxembourg 2026 intern postings silent; a 2023 London intern posting required existing work authorization",
        "source": "https://www.extern.com/post/paypal-internship-guide",
        "confidence": "medium",
        "checked": "2026-10-15",
    },
    "Pinterest": {
        "status": "limited",
        "note": "Dublin 2027 SWE intern posting 'may be eligible for relocation assistance'; no visa wording either way",
        "source": "https://builtin.com/job/software-engineer-intern-2026/7199234",
        "confidence": "high",
        "checked": "2026-10-15",
    },
    "Salesforce": {
        "status": "unknown",
        "note": "Dublin Summer 2026 SWE intern posting carries no visa or right-to-work wording",
        "source": "https://www.extern.com/post/salesforce-internship-guide",
        "confidence": "medium",
        "checked": "2026-10-15",
    },
    "Snap": {
        "status": "unknown",
        "note": "London ML intern posting has no right-to-work wording; pre-2020 Tier 2 sponsorship anecdote only (Blind)",
        "source": "https://blog.internset.com/what-are-the-eligibility-criteria-for-snap-internships/",
        "confidence": "low",
        "checked": "2026-10-15",
    },
    "Snowflake": {
        "status": "unknown",
        "note": "Berlin 2026 SWE intern posting has no right-to-work or sponsorship wording; no Warsaw data found",
        "source": "https://www.extern.com/post/snowflake-internship-guide",
        "confidence": "low",
        "checked": "2026-10-15",
    },
    "Spotify": {
        "status": "no",
        "note": "London/Stockholm interns must already hold work authorization in that country; no sponsorship/relocation",
        "source": "https://jobs.lever.co/spotify/4261f025-4ea4-4d24-9edd-ec0db9696152",
        "confidence": "high",
        "checked": "2026-10-15",
    },
    "Stripe": {
        "status": "unknown",
        "note": "London and Dublin SWE intern postings contain no right-to-work or sponsorship wording",
        "source": "https://www.extern.com/post/stripe-internship-guide",
        "confidence": "low",
        "checked": "2026-10-15",
    },
    "Uber": {
        "status": "no",
        "note": "Amsterdam/EMEA intern postings require local work authorization; no visa sponsorship for internships",
        "source": "https://www.themuse.com/jobs/uber/2026-software-engineering-internship-amsterdam",
        "confidence": "medium",
        "checked": "2026-10-15",
    },
    "Waymo": {
        "status": "unknown",
        "note": "London MS/PhD ML intern roles exist (Waymo is a UK Skilled Worker sponsor); Warsaw via Formation; wording silent",
        "source": "https://www.extern.com/post/waymo-internship-guide",
        "confidence": "low",
        "checked": "2026-10-15",
    },
}


def visa_for(company):
    """Visa info dict for a company; a harmless 'unknown' entry when unlisted."""
    info = VISA.get(company) or {}
    status = info.get("status", "unknown")
    if status not in STATUS_LABEL:
        raise ValueError("bad visa status {!r} for {}".format(status, company))
    return {
        "status": status,
        "label": STATUS_LABEL[status],
        "note": info.get("note", ""),
        "source": info.get("source", ""),
        "checked": info.get("checked", ""),
    }
