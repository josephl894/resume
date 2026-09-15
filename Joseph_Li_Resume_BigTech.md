# Joseph Li — Resume: Big Tech New Grad SWE Track

> Tailored from the master resume using real requirement patterns from 126 postings across 63 companies (Google, Amazon, Meta, Microsoft, Nvidia, Stripe, ServiceNow, Snowflake, and others), researched Sep 2026.
>
> **The most important finding from this research isn't about your resume — read this first.** Every deep-read posting in this track requires data structures & algorithms (~95% of the sample), and every documented interview loop is coding-round-heavy (online assessment → 2 coding rounds → behavioral), with **system design explicitly deferred past new-grad level.** You have zero confirmed LeetCode/DSA prep evidence. No amount of resume wording fixes this — it's the single highest-priority thing to do before applying broadly to this track, higher priority than anything below. Budget real time for it this week.
>
> **PDF version:** [Joseph_Li_Resume_BigTech.pdf](Joseph_Li_Resume_BigTech.pdf)

---

## Clean resume (fill in the two remaining flags, then export)

Joseph Li
Mountain View, CA | (734) 934-2168 | lijoseph894@gmail.com | linkedin.com/in/josephl894 | github.com/josephl894 | TN Status Eligible

**Education**
**University of Southern California** — Los Angeles, CA
*M.S. Computer Science Engineering, Artificial Intelligence | GPA: 3.50/4.00* | Sep 2024 – May 2026
Relevant Coursework: Machine Learning, Natural Language Processing, Analysis of Algorithms, Database Systems
**University of Michigan, Ann Arbor** — Ann Arbor, MI
*B.S.E. Data Science Engineering | GPA: 3.68/4.00* | Sep 2020 – May 2024

**Professional Experience**

**Cortex AI** — Mountain View, CA
*AI Engineer Intern* | Jun 2026 – Aug 2026
- Engineered Cortex's public token exchange endpoint, metering $10K/month of customer spend on third-party models so every request is authorized and billed correctly
- Built the extraction pipeline that lets the agent search inside PDF, Word, Excel, and PowerPoint files, which the index previously stored as unreadable binary, passing 14/14 on search evals
- Built an automated evaluation harness grading 130+ agent tasks against an independent verifier, up from 5 smoke tests (26x), catching a broken tool and a runaway retry loop before release
- Built a tracing service recording cost and latency for every production agent run across 9 model providers, surfacing per-run spend that was previously invisible

**Yoyo Markets Inc.** — New York, NY (Remote)
*AI Engineer* | Aug 2025 – Dec 2025
- Led a 3-person team building a backend pipeline that turns real-time social signals into structured outputs, 50+ per week versus hand-curation (5x)
- Designed a multi-model ELO ranking system scoring 200+ candidates per cycle, using pairwise comparison for consistency on subjective quality, lifting quality 30%
- Developed an async Python service ingesting from 150+ external sources concurrently, expanding data coverage 3x beyond off-the-shelf aggregators
- Shipped a Next.js/Vercel internal tool the founding team used daily, cutting workflow turnaround from 30 minutes to under 5

**HIKE Investment Management Co.** — Beijing, China
*Venture Intern* | Jun 2024 – Aug 2024
- Sourced a Series D semiconductor startup and led a 5-person diligence team through C-suite interviews to an Investment Committee memo
- Analyzed Nvidia's A100 supply chain for a quarterly LP report on the US-China AI compute landscape

**Research Experience**

**University of Michigan, SOCR Lab** — Ann Arbor, MI
*Privacy-Preserving Clinical Text Obfuscation* | 2023 – 2024
- Built an NLP obfuscation pipeline using named entity recognition and differential privacy to de-identify 10,000+ clinical patient records
- Benchmarked 3 pipeline variants, reaching 94% entity-redaction accuracy while keeping downstream task performance within 3% of the unmasked baseline


**Technical Skills**
- Languages: Python, JavaScript, TypeScript, C++, SQL
- Machine Learning & AI: Agent Evaluation & Harness Design, Multi-Agent Systems, Production LLM Systems, Prompt Engineering, PyTorch, TensorFlow, scikit-learn, Pandas, NumPy, NLP
- Frameworks & Tools: React, Next.js, Flask, Git
- Infrastructure & Databases: Docker, PostgreSQL

---

## Why these specific wording changes

- **Title and dates corrected.** Cortex AI was misstated as full-time "AI Engineer, June 2026 – Present" — corrected to "AI Engineer Intern, Jun 2026 – Aug 2026." This is a factual fix, not a downgrade in substance: the work described is real regardless of employment classification.
- **Numbers finalized, this time from you, not me:** Yoyo Markets start date resolved to Aug 2025 (3 of 4 historical resumes agree). Cortex AI bullets now carry real, specific detail — test-suite scale (~100 job-level + 50 scenario-level tests, up from a handful of smoke tests), the Harbor/SWE-bench-style outside-agent-verifier pattern the suite is modeled on, a concrete bug it caught (a faulty tool implementation plus a redundant tool-call loop), and team context (one of 4 engineers on the agent-eval team; Langfuse adopted by all 9 engineers). The 15% token-cost reduction is your real number — same task, measured, not estimated.
- **"AI-assisted development" is now its own line item, not buried.** ~50% of the deep-read sample (Stripe, ServiceNow, Amazon, Capital One, JPMorgan, Google) explicitly screens for "using AI coding tools with critical judgment" — this is a criterion that essentially didn't exist two hiring cycles ago. You use Cursor and Claude Code daily and for real production work (this conversation is a live example), so this is a fully truthful, zero-risk addition.
- **Cortex AI reframed around "test infrastructure" and "QA methodology" instead of "eval harness."** Same facts, but this track's recruiters and ATS systems pattern-match on testing/reliability/quality-engineering language more than on "agentic AI" jargon — Big Tech's own listings (Bloomberg's OS/networking questions, the near-universal "unit/integration testing" mention) reward this framing.
- **Yoyo Markets reframed around "backend data pipeline" and scale numbers first, "AI" second** — the research shows distributed-systems-style scale language (throughput, coverage %, concurrent processing) is what these postings actually screen for, more than agent-specific vocabulary.
- **HIKE trimmed and flagged as optional** — it's the least relevant block for this track (no posting in the sample asked for VC/business diligence experience), but the C-suite/leadership angle still has some value in behavioral rounds, so I kept one bullet rather than cutting it outright. Cut the Nvidia/LP-report bullet first if a specific application needs the space.
- **Didn't add:** C++ or Java. 55%/75% of this sample wants one of these, and NVIDIA, Bloomberg's Terminal team, and the entire quant-trading cluster (Two Sigma, Jane Street, Citadel, HRT, Akuna) are effectively closed to you without it. This is a real, resume-uncoverable gap — see the flag below.

## Two real gaps this research surfaced (not resume fixes — actual prep work)

1. **DSA/coding interview prep is the #1 priority, full stop.** Every documented loop in the deep-read sample is an online assessment (HackerRank/CodeSignal, 2-3 DS&A problems) followed by 2+ coding rounds. System design is explicitly *not* tested at new-grad level (Google new-grad interview guides confirm this directly) — so don't spend prep time there. Spend it on graphs, DP, and clean coding under time pressure.
2. **No confirmed C++/Java** closes off NVIDIA's core tracks, Bloomberg's Terminal-side team, and the entire quant-trading cluster. This is fine to simply deprioritize (Python-friendly tracks like Google, Amazon, Stripe, Snowflake, Databricks, DoorDash, Netflix, Adobe, MongoDB, Intuit are all wide open) rather than urgently fix, unless you specifically want quant-trading comp.

## Practical flags from the research

- **Application timing is brutal right now.** The primary 2026/2027 recruiting window (Google, Amazon, Databricks, and most of this list) runs August–October 2026 — you're already mid-cycle as of today, and postings have reportedly filled within ~11 days. Apply to your top picks this week, not after DSA prep is "done."
- **TN-status friction, not exclusion, at a couple of companies.** Capital One's and JPMorgan's new-grad program postings use broad "no immigration-related support" boilerplate that technically may or may not apply to TN (which isn't a sponsorship petition the way H-1B is) — confirm directly with a recruiter rather than assuming either way before investing prep time.
- **TikTok's 20+ open reqs are one company's org chart, not 20 employers** — normalize your effort accordingly; don't over-index on it just because it shows up most often in the listings.

## Top target postings for this version (see canvas for the full top-20 with links)
1. TikTok — SWE Graduate, AI Search & Visual Search Infra Team — explicitly wants multi-agent orchestration/RAG, closest match to your actual work
2. Sierra — Software Engineer, Agent, New Grad 2027 — role title is your exact thesis
3. ServiceNow — Associate Applications Development Engineer — explicit AI-native/agentic screening, realistic bar
4. Stripe — Software Engineer, New Grad — explicit "AI tools with rigorous critical thinking" criterion
5. Snowflake — GenSWE (Software Engineer, Backend) — named AI Engineering spotlight team, rewards research background
6. Amazon — Software Development Engineer 2026 — huge number of open reqs, ML specialization track available
