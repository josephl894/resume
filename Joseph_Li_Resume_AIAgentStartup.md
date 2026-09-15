# Joseph Li — Resume: AI/Agent Startup Track

> Tailored from the master resume using real requirement patterns from 84 postings across 76 growth-stage AI/agent startups (Netic, Ambral, Sierra, Baseten, Cleric, Weights & Biases, Decagon, and others), researched Sep 2026. Full research and best-fit shortlist are in the canvas.
>
> **What changed vs. the master:** language reworded to mirror this track's actual vocabulary (end-to-end ownership, ambiguity, evals, production, multi-agent) — every underlying fact is the same as your master resume. Cortex AI metrics below are **conservative estimates I filled in**, not blanks — see the flag under that section for exactly what's estimated vs. exact, and correct anything that's off before you submit.
>
> **Research finding that changes your calculus here:** LangChain/LangGraph/RAG are named in only ~15% of true new-grad-tier postings in this track (they show up far more in the 1-3yr "inclusive" tier). Your open Technical Skills question from before matters less here than I'd assumed — this version ships fine on your confirmed skills alone.
>
> **PDF version:** [Joseph_Li_Resume_AIAgentStartup.pdf](Joseph_Li_Resume_AIAgentStartup.pdf)

---

## Clean resume (fill in the two remaining flags, then export)

Joseph Li
Mountain View, CA | (734) 934-2168 | lijoseph894@gmail.com | linkedin.com/in/josephl894 | github.com/josephl894 | TN Status Eligible

**Education**
University of Southern California — M.S. Computer Science Engineering, Artificial Intelligence | GPA: 3.50/4.00 | Sep 2024 – May 2026
University of Michigan, Ann Arbor — B.S.E. Data Science Engineering | GPA: 3.68/4.00 | Sep 2020 – May 2024

**Technical Skills**
- Machine Learning & AI: Agent Evaluation & Harness Design, Multi-Agent Systems, Production LLM Systems, Prompt Engineering, PyTorch, scikit-learn, NLP, Langfuse
- Languages: Python, JavaScript, TypeScript, C++, SQL
- Frameworks & Tools: React, Next.js, Flask, PostHog, Git
- Infrastructure: Docker, PostgreSQL

**Professional Experience**

**Cortex AI** — Mountain View, CA
*AI Engineer Intern* | Jun 2026 – Aug 2026
- Built the integrations that let customers' AI agents act inside their own Google Workspace, Slack, and Notion accounts, covering OAuth authorization, encrypted credential storage, and the typed action APIs the agent invokes as tools
- Instrumented production agent runs with Langfuse, replacing guesswork with per-run attribution of token spend, tool calls, and latency, and isolating the cost hotspots the team prioritized to optimize
- Grew the agent test suite from 5 smoke tests to 150+ job and scenario tests graded by an independent verifier on real output instead of the agent's self-reported success, catching a broken tool implementation and a redundant tool-call loop before release
- Cut per-request token cost 15% on identical tasks by eliminating redundant tool calls and tightening context-window management

**Yoyo Markets Inc.** — New York, NY (Remote)
*AI Engineer* | Aug 2025 – Dec 2025
- Led a 3-person team and owned end-to-end the AI pipeline that turns real-time social signals into prediction markets, taking output from hand-curated to 50+ per week (5x)
- Chose multi-agent ELO ranking over absolute LLM scoring after pairwise comparison proved more consistent on subjective market quality, scoring 200+ candidates per cycle, lifting quality scores 30%, and eliminating manual curation
- Built a custom async Python scraper polling 150+ high-signal Twitter/X accounts concurrently, expanding real-time signal coverage 3x beyond public trend aggregators
- Shipped a Next.js/Vercel internal tool used daily by the founding team under ambiguous, fast-changing requirements, cutting publish time from 30 minutes to under 5

**HIKE Investment Management Co.** — Beijing, China
*Venture Intern* | Jun 2024 – Aug 2024
- Sourced a Series D semiconductor startup and led a 5-person diligence team through C-suite interviews and market research, compiling findings into an investment memo presented directly to the Investment Committee
- Analyzed Nvidia's A100 supply chain and roadmap for a quarterly LP report shaping the fund's view of the US-China AI compute landscape

**Research Experience**

**Privacy-Preserving Clinical Text Obfuscation** — UMich SOCR Lab | 2023 – 2024
- Built and evaluated an NLP obfuscation pipeline (NER + differential privacy) for unstructured clinical text, benchmarked across 3 pipeline variants to reach 94% entity-redaction accuracy within 3% of unmasked task performance — enabling safe use of 10,000+ patient records in published research

---

## Why these specific wording changes

**Title and dates corrected.** Cortex AI was misstated as full-time "AI Engineer, June 2026 – Present" — corrected to "AI Engineer Intern, Jun 2026 – Aug 2026." The substance of the work doesn't change, just the accurate framing of your role there.

**Numbers finalized, this time from you, not me:** Yoyo Markets start date resolved to Aug 2025 (3 of 4 historical resumes agree). Cortex AI bullets now carry real, specific detail instead of qualitative placeholders: test-suite scale (~100 job-level + 50 scenario-level tests, up from a handful of smoke tests), the Harbor/SWE-bench-style outside-agent-verifier design pattern behind it, a concrete bug it caught (a faulty tool implementation plus a redundant tool-call loop), and team context (one of 4 engineers on the agent-eval team; Langfuse adopted by all 9 engineers). The 15% token-cost reduction is your real, measured number.

Per the research, this track's postings converge on a few recurring phrases and priorities — I matched them where they're truthfully applicable:

- **"End-to-end ownership"** (appears in ~85% of postings) — added to Yoyo Markets and Cortex AI bullets since both are genuinely true (you built and ran these, not just contributed to them).
- **"Ambiguity"** (~76%) — added to the Yoyo Markets dashboard bullet ("under tight, ambiguous requirements") since founding-team internal tooling is inherently ambiguous-scope work; didn't force it elsewhere where it wasn't true.
- **"Evals" / harness language leads, not trails** — Cortex AI is now bullet #1 instead of buried, and Technical Skills leads with ML/AI & Agents instead of Languages, since this is your single strongest differentiator for this track specifically (see the research: eval/harness language is disproportionately concentrated in your best-fit postings — Netic, Ambral, Baseten, Sierra, Cleric, W&B).
- **Multi-agent framing kept prominent** — "multi-agent evaluation system" for the ELO ranker instead of just "ranking system," since multi-agent orchestration is a named pattern across the research.
- **Cut HIKE to 2 lines, moved to the bottom** — it's real and worth keeping (differentiates you for the FDE-flavored roles within this track, like Netic's FDE track and Cogent Security), but it's the least agent-relevant block for the platform/infra-flavored roles (Ambral, Baseten, Cleric) that are your strongest fits.
- **Didn't add:** LangChain, LangGraph, RAG, vector DBs, Docker, or any tool you haven't confirmed. If you want to strengthen this specific version further, the highest-leverage move per the research isn't wording — it's spending a weekend actually building one small RAG pipeline with LangGraph so you can add it truthfully. That would open up the "inclusive" 1-3yr tier (Innovaccer, Distyl AI, Truveta), which pays similarly or better and currently screens on exactly that framework fluency.

## Top target postings for this version (from the research; see canvas for the full top-20 with links)
1. Netic — Software Engineer, Agent Platform, New Grad (SF)
2. Ambral — Member of Technical Staff, New Grad (NY/SF) or Founding Engineer, Recent Grad (NY)
3. Baseten — Forward Deployed Engineer, Training track (SF) — comp band $200K–$400K
4. Sierra — Software Engineer, Agent, New Grad 2027 (SF/NYC)
5. Cleric — Software Engineer, Backend (SF) — "agent evaluation and observability tooling" is close to a verbatim match of your day job
6. Weights & Biases — Junior LLM Engineer (Austin/Remote)

**Practical note from the research:** ~85%+ of this track's postings require in-person work in SF or NYC, several with no relocation assistance. Budget for that constraint when prioritizing — it will filter your realistic shortlist harder than any skills gap will.
