# Joseph Li — Resume: Forward Deployed Engineer Track

> Tailored from the master resume using real requirement patterns from 121 postings across 47 companies (Palantir, OpenAI, Anthropic, Scale AI, Netic, Baseten, Harvey, Snowflake, and others), researched Sep 2026.
>
> **Update:** per your instruction, graduation-date eligibility windows (Palantir new-grad, Applied Intuition new-grad, Ramp's internship) are no longer treated as exclusions — they're back in the priority list below. Citizenship/security-clearance requirements (Palantir Government, Scale AI Public Sector, C3.ai Federal, Anduril, Together AI Singapore) are a separate, legal constraint unrelated to graduation date, so those stay excluded.
>
> **PDF version:** [Joseph_Li_Resume_FDE.pdf](Joseph_Li_Resume_FDE.pdf)

---

## Clean resume

Joseph Li
Mountain View, CA | (734) 934-2168 | lijoseph894@gmail.com | linkedin.com/in/josephl894 | github.com/josephl894 | TN Status Eligible

**Summary**
AI engineer with hands-on production experience designing evaluation frameworks and quality metrics for agentic LLM systems, paired with direct executive- and client-facing experience (C-suite diligence interviews, Investment Committee presentations). Comfortable owning ambiguous technical problems end-to-end in fast-moving, customer-embedded environments.

**Education**
University of Southern California — M.S. Computer Science Engineering, Artificial Intelligence | GPA: 3.50/4.00 | Sep 2024 – May 2026
University of Michigan, Ann Arbor — B.S.E. Data Science Engineering | GPA: 3.68/4.00 | Sep 2020 – May 2024

**Technical Skills**
- AI/ML & Evaluation: Agent Evaluation & Harness Design, Multi-Agent Systems, Production LLM Systems, Prompt Engineering, PyTorch, scikit-learn, NLP, Langfuse
- Languages: Python, JavaScript, TypeScript, C++, SQL
- Frameworks & Tools: React, Next.js, Flask, PostHog, Git
- Infrastructure & APIs: Docker, PostgreSQL, REST APIs

**Professional Experience**

**Cortex AI** — Mountain View, CA
*AI Engineer Intern* | Jun 2026 – Aug 2026
- Built the integrations that let customers' AI agents act inside their own Google Workspace, Slack, and Notion accounts, covering OAuth authorization, encrypted credential storage, and the typed action APIs the agent invokes as tools
- Instrumented production agent runs with Langfuse, replacing guesswork with per-run attribution of token spend, tool calls, and latency, and isolating the cost hotspots the team prioritized to optimize
- Grew the agent test suite from 5 smoke tests to 150+ job and scenario tests graded by an independent verifier on real output instead of the agent's self-reported success, catching a broken tool implementation and a redundant tool-call loop before release
- Cut per-request token cost 15% on identical tasks by eliminating redundant tool calls and tightening context-window management

**Yoyo Markets Inc.** — New York, NY (Remote)
*AI Engineer* | Aug 2025 – Dec 2025
- Led a 3-person team and owned end-to-end the AI pipeline that turns real-time social signals into prediction markets, taking output from hand-curated to 50+ per week (5x) under ambiguous, fast-changing requirements
- Chose multi-agent ELO ranking over absolute LLM scoring after pairwise comparison proved more consistent on subjective quality, scoring 200+ candidates per cycle, lifting quality scores 30%, and removing a daily manual review bottleneck
- Built a custom async Python scraper polling 150+ external sources concurrently, expanding real-time coverage 3x beyond off-the-shelf aggregators
- Shipped a Next.js/Vercel internal tool embedded with the founding team as primary stakeholders, cutting their publish workflow from 30 minutes to under 5

**HIKE Investment Management Co.** — Beijing, China
*Venture Intern* | Jun 2024 – Aug 2024
- Sourced a Series D semiconductor startup and led a 5-person diligence team through direct C-suite interviews, translating technical and market complexity into an investment memo presented to the Investment Committee
- Analyzed Nvidia's A100 supply chain and roadmap for a quarterly LP report, communicating findings to non-technical fund stakeholders and shaping the fund's compute-infrastructure thesis

**Research Experience**

**Privacy-Preserving Clinical Text Obfuscation** — UMich SOCR Lab | 2023 – 2024
- Built and benchmarked an NLP obfuscation pipeline (NER + differential privacy), reaching 94% entity-redaction accuracy across 3 pipeline variants on 10,000+ patient records

---

## Why these specific wording changes

- **Added a Summary line — the only resume in your 3 versions that has one.** FDE hiring is more narrative/pitch-driven than the other two tracks (interview loops are built around live "ambiguous case study" and "customer-conversation simulation" rounds, not pure technical screens), so a 2-line frame that states your pitch explicitly earns its place here.
- **Cortex AI reworded around "evaluation framework" and "quality metrics" specifically** — the single most-repeated technical qualifier across the deep-read sample (Snowflake, Harvey, Scale AI, Cursor, Sierra all use close to this exact phrasing).
- **"Partnering with product and research teams to set the quality bar"** is a defensible inference from what "building an eval harness from the ground up" entails — confirm this matches how your role actually works before submitting.
- **HIKE bullets elaborated slightly** ("translating technical and market complexity," "communicating findings to non-technical fund stakeholders") — your best evidence against the #1 non-technical qualifier in the sample: comfort presenting to executive stakeholders.
- **Title and dates corrected.** Cortex AI was misstated as full-time "AI Engineer, June 2026 – Present" — corrected to "AI Engineer Intern, Jun 2026 – Aug 2026."
- **Numbers finalized, this time from you, not me:** Yoyo Markets start date resolved to Aug 2025 (3 of 4 historical resumes agree). Cortex AI bullets now carry real, specific detail: test-suite scale (~100 job-level + 50 scenario-level tests, up from a handful of smoke tests), the Harbor/SWE-bench-style outside-agent-verifier pattern it's modeled on, a concrete bug it caught (a faulty tool implementation plus a redundant tool-call loop), and team context (one of 4 engineers on the agent-eval team; Langfuse adopted by all 9 engineers). The 15% token-cost reduction is your real, measured number.

## Priority target list (graduation-date gates no longer treated as exclusions)

| # | Company / Role | Comp | Why |
|---|---|---|---|
| 1 | **Palantir — Forward Deployed Software Engineer, New Grad (Commercial)** | $135K–$145K | The most prestigious new-grad FDE brand in the market; broadest early-career hiring band of any FDE program found; distinctive "decomposition" interview round |
| 2 | **Netic — FDE, New Grad 2026–2027** | Not disclosed | Best content match: Python/FastAPI + TS/React + "evaluation frameworks" requirement lines up almost 1:1 with your stack |
| 3 | **Applied Intuition — Forward Deployed Engineer, New Grad (Dec 2026)** | Not disclosed | Autonomy/simulation software, strong brand, new-grad-titled |
| 4 | **Ramp — Software Engineer, AI Forward Deployed** | $189K–$330K | Strong fintech FDE comp; apply to the full-time role directly (skip the internship pipeline, which is a different req) |
| 5 | **Harvey AI — Founding Forward Deployed Engineer** | $165K–$200K | Explicitly names "practical experience with evals" — direct match to Cortex AI |
| 6 | **Baseten — Forward Deployed Engineer** | $165K–$330K | Own engineering blog states the FDE team includes new grads from Waterloo alongside 15-year veterans |
| 7 | **Handshake AI — Forward Deployed Engineer I** | $155K–$300K | Explicit 1–4 year band, agent-architecture/evals focus |
| 8 | **IBM — Forward Deployed Engineer, Entry Level** | $100.8K–$151.2K | Explicitly entry-level, real ladder, TN-compatible (requires RTP, NC relocation) |
| 9 | **Snowflake — Forward Deployed Engineer, Applied AI** | $126K–$181.7K | Closest verbatim content match (evals, quality metrics, agent quality) of anything found in the full 121-posting sample |
| 10 | **Wipro — Junior Forward Deployed Engineer** | $68.4K–$79K | Lower comp but a real, accessible Junior→Senior FDE ladder with no clearance issue |

**Still excluded — this is a citizenship/clearance constraint, not a graduation-date one, so it stands regardless:** Palantir's US/UK Government and Intel tracks, Scale AI Public Sector, C3.ai Federal (requires US citizenship), Anduril, Together AI's Singapore FDE (Singapore PR/citizen only), and any Anthropic/Sierra/Mistral role gated on native fluency in a language you don't speak.

**Worth a direct outreach rather than the portal:** Salesforce's Agentforce FDE track (Futureforce, "1,000 AI-native grads Class of 2026") is ambiguous on whether it's a hard campus-only gate — worth emailing a recruiter directly, since the comp band ($143K–$384K across levels) is unusually good if open to you.

## Practical flags from the research
- **~44% of postings require 25–50% travel** — worth thinking through now, not after an offer.
- **Frontier-lab FDE comp ($200K–$440K at OpenAI/Anthropic/Perplexity/xAI) is priced on brand + LLM-native fluency** — these sit in the 3-5+/8+ year bucket, so treat them as a 12-24 month target once you have real FDE or customer-facing engineering reps, not a now-target.
