# Joseph Li — Master Resume (Source of Truth)

> **What this file is:** Per the `resume-tailor` skill, this is your complete master resume — every bullet you should actually use, restored and upgraded. Items marked `[NEED: ...]` require a real number from you before this goes out — do not submit with placeholders still in it.
>
> **PDF version:** [Joseph_Li_Resume_MASTER.pdf](Joseph_Li_Resume_MASTER.pdf) — a general-purpose default. Use this one for networking, referrals, or any application that doesn't cleanly fit Big Tech / AI-Agent-Startup / FDE; use the three tailored PDFs for target-track applications.
>
> **Update:** Pure Global and the Autonomous Research Agent project have been **permanently removed**, not just de-prioritized — correctly. Unverifiable experience you ghosted after a couple weeks is a background-check liability, and a project you can't speak to the architecture of in an interview will get exposed in the first follow-up question (both are exactly what `tech-resume-optimizer` warns against: "only claim technologies you can discuss deeply"). See the flag below about what this means for your Technical Skills section.

---

Joseph Li
Mountain View, CA | (734) 934-2168 | lijoseph894@gmail.com | linkedin.com/in/josephl894 | github.com/josephl894 | TN Status Eligible

> **Round 5 — bullet length fixed against the UCC examples.** Round 4 swung too far: chasing specificity produced 40-to-45-word bullets stacking four clauses each, which is unreadable in a 30-second scan even though every word was accurate. UCC's own samples run **13 to 24 words with exactly one idea per bullet** ("Cleaned and filtered COVID related tweets using PySpark with Hadoop, and decreased computation time by 87.5%"). Every bullet on the resume is now **16 to 28 words, averaging 20**. The fix was choosing the single strongest detail per bullet rather than enumerating every component — so the integrations bullet names the span from OAuth to tool schemas instead of listing schema, client, OAuth, and webhooks separately. Nothing was lost to vagueness; the cut material is interview content, not resume content (see the interview-prep note below). Shorter bullets also *freed* roughly a third of a page, so the research entry got split back into two readable bullets instead of one dense one.
>
> **Round 4 — rebuilt against the [UMich Career Center resume guidance](https://careercenter.umich.edu/article/resume-resources):** Their two load-bearing rules are that employers scan for 30 to 60 seconds, and that formatting must be consistent enough to survive that scan — "put job titles, organization names, dates, and locations in the same location each time." The old layout violated this by jamming organization and location together on one line and leaving the right margin empty. Every entry now uses one system across Education, Professional Experience, and Research Experience: **bold organization on the left, location on the right; italic role or degree on the left, dates on the right; bullets below.** Skills also moved from the top to the bottom, matching UCC's prescribed section order (Contact, Summary, Education, Experience, Skills) and their Masters-level technical example — which has the side benefit of putting Cortex AI directly under Education, so the 30-second scan hits your strongest content immediately. Verbs were upgraded against UCC's action-verb list ("Grew" to "Expanded", "Chose" to "Designed", "Wrote" to "Developed"), and every bullet was checked against their **Bullet Plus formula: Action Verb + What + How/Why/Impact.**
>
> **Round 3 rewrite (per your friend's analysis):** Their diagnosis was that the problem was never missing experience — it was that the bullets read like project write-ups instead of accomplishments. Four changes applied across all four versions: (1) **bullets cut short and led with the action**, so the first six words say what you built rather than how many engineers were on the team ("One of 4 engineers" is gone — it spent prime real estate on context, not contribution); (2) **all arrows and prose em-dashes removed** — they were making a skimming recruiter re-read sentences; (3) **the differentiating tech moved into the bullets** (Langfuse, independent-verifier grading, multi-agent ELO) instead of living only in Technical Skills, where it looked like tools you'd merely read about; (4) **design rationale added** where you have a real answer — the Yoyo ELO bullet now says *why* pairwise ranking beat absolute LLM scoring, which is the kind of judgment an AI hiring manager actually screens for. Two of their points still need input from you before they can be closed out; see "Open questions from the round-3 review" at the bottom.
>
> **Update:** Cortex AI title corrected to "AI Engineer Intern" (was misstated as full-time "AI Engineer"), and dates corrected to Jun–Aug 2026 (was misstated as "Present"). Bullets rewritten with real, verified detail: test-suite scale (~100 job-level + 50 scenario-level tests, up from a handful of smoke tests), the Harbor/SWE-bench-style outside-agent-verifier design pattern behind it, a real concrete catch (a faulty tool implementation + a redundant tool-call loop), and team context (4-engineer agent-eval team; Langfuse adopted by all 9 engineers). No Personal Projects section — per your review, the two available candidates (a 2-semester-old Weenix OS kernel project and a 3+-year-old EECS 485 MapReduce/search-engine project) don't clear the bar in the current market: the Weenix project was largely AI-assisted from a template, and the MapReduce project is old enough that "built from scratch" now reads as a weekend-AI task rather than a hard-won distributed-systems credential. Better to lean fully on real work experience than pad with either.

## Education

**University of Southern California** — Los Angeles, CA
M.S. Computer Science Engineering, Artificial Intelligence | GPA: 3.50/4.00 | Sep 2024 – May 2026
Relevant Coursework: Machine Learning, Natural Language Processing, Analysis of Algorithms, Database Systems

**University of Michigan, Ann Arbor** — Ann Arbor, MI
B.S.E. Data Science Engineering | GPA: 3.68/4.00 | Sep 2020 – May 2024

## Professional Experience

**Cortex AI** — Mountain View, CA
*AI Engineer Intern* | Jun 2026 – Aug 2026
- Built Slack, Notion, and Google Workspace integrations agents call as tools, from OAuth authorization to the typed schemas the model calls against
- Built a server-side Langfuse proxy tracing every agent run, keying token cost to the billing ledger and exposing the hotspots the team optimized
- Expanded the agent test suite from 5 smoke tests to 150+ graded by an independent verifier, catching a broken tool implementation and a redundant tool-call loop before release
- Cut per-request token cost 15% on identical tasks by eliminating redundant tool calls and tightening context-window management

**Yoyo Markets Inc.** — New York, NY (Remote)
*AI Engineer* | Aug 2025 – Dec 2025
- Led a 3-person team building the AI pipeline that generates prediction markets from real-time social signals, 50+ per week versus hand-curation (5x)
- Designed a multi-agent ELO ranking system scoring 200+ candidate markets per cycle, using pairwise comparison for consistency on subjective quality, lifting quality 30%
- Built an async Python scraper polling 150+ high-signal Twitter/X accounts concurrently, expanding signal coverage 3x beyond public trend aggregators
- Shipped a Next.js/Vercel dashboard the founding team used daily, cutting publishing time from 30 minutes to under 5

**HIKE Investment Management Co.** — Beijing, China
*Venture Intern* | Jun 2024 – Aug 2024 *(your current PDF says "Jun 2025 - Aug 2024" — that's backwards and needs fixing; your older resumes confirm Jun–Aug 2024 is correct)*
- Sourced a Series D semiconductor startup and led a 5-person diligence team through C-suite interviews to an Investment Committee memo
- Analyzed Nvidia's A100 supply chain for a quarterly LP report on the US-China AI compute landscape

## Research Experience

**University of Michigan, SOCR Lab** — Ann Arbor, MI
*Privacy-Preserving Clinical Text Obfuscation* | 2023 – 2024
- Built an NLP obfuscation pipeline using named entity recognition and differential privacy to de-identify 10,000+ clinical patient records
- Benchmarked 3 pipeline variants, reaching 94% entity-redaction accuracy while keeping downstream task performance within 3% of the unmasked baseline

---

## Technical Skills

**⚠️ Flag before you finalize this section:** LangChain, LangGraph, RAG, FAISS, n8n, Docker, PostgreSQL, CI/CD, pytest, Fine-Tuning, and Vector Databases were on your older resumes almost entirely on the strength of Pure Global + the removed project. With both gone, nothing left in this resume backs those specific tools. Per the truthfulness line in `resume-tailor` ("don't add skills you don't have... be ready to explain every claim in an interview"), only keep a tool here if you have real hands-on experience with it from Cortex AI, Yoyo Markets, coursework, or personal use — and could talk through it if an interviewer asked a follow-up. I split the list below into what's clearly backed by a remaining bullet vs. what needs your confirmation — **please tell me which of the "needs confirmation" items to keep vs. cut** so I can finalize this.

**Round 2, per your direct pushback:** "AI Dev Tools" removed entirely (you're right — not a real differentiator, shouldn't take up a category). "CI/CD (GitHub Actions)" removed (overclaims one workflow-dispatch as an intern into "CI/CD experience" — a recruiter would discount it). And the list was genuinely sparse for an MS-in-AI + BSE-Data-Science-Engineering candidate — added real ML/web breadth backed by first-hand evidence found on your own machine (see below), not guesses.

This master list is the **aggregation of everything used across the 3 tailored resumes** — each tailored version pulls a track-appropriate subset, not this full list verbatim.

- **Languages:** Python, JavaScript, TypeScript, C++, SQL
- **AI/Agent Engineering:** Agent Evaluation & Harness Design, Multi-Agent Systems, Production LLM Systems, Prompt Engineering, NLP, Langfuse (LLM observability)
- **ML & Data Libraries:** PyTorch, TensorFlow, scikit-learn, Pandas, NumPy
- **Frameworks & Tools:** React, Next.js, Flask, Vercel, PostHog, Git
- **Infrastructure & Databases:** Docker, PostgreSQL

**New additions this round — flag any you don't actually recall, otherwise they stay:**
- **JavaScript, React** — implied by TypeScript and Next.js. Omitting the underlying language/framework when you list the superset/wrapper looks like an oversight to a recruiter, not caution.
- **Flask** — direct evidence: your EECS 485 Insta485 project (`p1-insta485-static`, `p2-insta485-serverside`) is a Flask app — real blueprint/view/model/template structure, not a guess.
- **scikit-learn, TensorFlow, Pandas, NumPy** — direct evidence from real cache directories that only exist if the tool was actually installed and run on your machine: `scikit_learn_data`, `.keras` (TensorFlow's Keras API), plus your EECS 445 (Michigan ML coursework). Pandas/NumPy are near-universal companions to this stack and to the Yoyo Markets/CSCI-550-adjacent data work already on this resume.
- Also found but **not added** (too uncertain to defend without more specifics from you): Gensim and LightGBM both have real cache/build evidence on your machine (a `lightgbm-3.2.1` folder and its own compilation log), but I don't know the context well enough to write a defensible one-line justification — tell me what project these were for if you want them added.

**Removed, per your call — not because the research was wrong, but because you get final say on your own resume:**
- **AI Development Tools** (Cursor, Claude Code) — gone entirely, not folded elsewhere.
- **CI/CD (GitHub Actions)** — gone entirely. REST APIs stays only on the FDE version, where "API integration" is explicitly named in real postings.

**Still out, pending a real project to back them:** LangChain, LangGraph, RAG, FAISS / vector databases, n8n, pytest, fine-tuning, AWS. These were on older resumes on the strength of Pure Global and the removed agent project. Nothing currently on this resume backs them, so they stay off until you can point to work you'd be comfortable defending in a follow-up question. If any of them were genuinely used at Cortex AI or Yoyo Markets, say so and I'll add them *and* work them into the relevant bullet — which is the only way they carry weight (see the round-3 note below).

**Round 3 — your friend's critique (the useful part):** their strongest point is that a skill listed in this section but absent from every bullet reads as "a tool I've heard of," not "a tool I've shipped with." That's a real ATS-and-human failure mode and it cuts against the previous round's instinct to broaden the list. The fix applied here was *not* to trim the list back (you correctly wanted breadth for ATS) but to make sure the **differentiating** skills — agent evaluation, Langfuse, multi-agent systems — now appear inside the experience bullets where a hiring manager can see them in context. Breadth items like C++, Pandas, and Docker can stay unbacked; that's normal and expected for a new grad. Headline AI skills cannot.

## Three tailored versions now exist — use these, not this file, for actual applications

This master file stays your source of truth, but each track now has its own resume built from real research (100+ postings each, researched Sep 2026), not speculation:

- **[Joseph_Li_Resume_BigTech.md](Joseph_Li_Resume_BigTech.md)** — Google, Amazon, Meta, Microsoft, Nvidia, Stripe, Snowflake, and 57 more. **Key finding: your DSA/coding-interview prep matters far more than any resume wording — every loop in the research is coding-round-heavy with no system design at new-grad level, and you have zero confirmed LeetCode signal. Fix that before optimizing this resume further.**
- **[Joseph_Li_Resume_AIAgentStartup.md](Joseph_Li_Resume_AIAgentStartup.md)** — Netic, Ambral, Sierra, Baseten, Cleric, Weights & Biases, and 70+ more. Your eval-harness work at Cortex AI is close to a direct match for this track's rarest, most-rewarded skill.
- **[Joseph_Li_Resume_FDE.md](Joseph_Li_Resume_FDE.md)** — Palantir, Netic, Baseten, Harvey, Snowflake, and 42 more. **Key finding: timing, not skill, is your biggest blocker — you already graduated/started full-time in the exact window most "new grad FDE" programs use as an eligibility floor, which hard-excludes you from Palantir, Applied Intuition's new-grad track, and Ramp's internship pipeline. The real wedge is programs that gate on years-of-experience instead (Netic, Harvey, Baseten, Handshake AI, Wipro, IBM) — see that file for the prioritized list.**

Full research (300+ postings total, requirement-frequency breakdowns, and 15-20 best-fit postings per track with links) is in the [job-search-command-center canvas](/Users/joseph/.cursor/projects/Users-joseph-Desktop-Important-playground/canvases/job-search-command-center.canvas.tsx).

## What removing Pure Global + Projects means for length

Without those two sections, everything comfortably fits **one page** — three experience blocks (Cortex AI, Yoyo Markets, HIKE) plus one research entry, across all three tailored versions.

## Detail that moved off the resume and into interview prep

Shortening the bullets meant cutting real technical detail. None of it is gone — it's the material you lead with when an interviewer asks a follow-up. Know these cold:

**Integrations (bullet 1).** Each provider under `cortex-api/src/modules/apps/connections/types/<provider>/` is four things: a declarative schema file defining every action's typed input/output (Slack's is 272 lines, and this schema *is* the tool definition the model sees), an authenticated REST client, one handler per action, and an event trigger like `ON_CHANNEL_NEW_MESSAGE` that starts a workflow from a provider webhook. Plus the OAuth connect/callback controller and encrypted credential storage in `values/`. Slack alone exposes 6 actions.

**Langfuse (bullet 2).** The naive design is shipping the Langfuse SDK inside the desktop app, which fails twice: it puts your secret key in a binary users can unpack, and every provider names models differently so `anthropic.claude-sonnet-5`, `google/models/gemini-x`, and `claude-sonnet-5/vertex` fragment into separate dashboard rows. The real implementation is a server-side ingest route, `POST /telemetry/langfuse/ingest`, on the edge worker: the client posts Langfuse batches with its normal edge JWT and the edge substitutes Langfuse Basic auth server-side. On the way through, `cortex-edge-proxy/src/langfuse.ts` (360 lines, later ported to Python for LiteLLM) normalizes model IDs across **9 upstream providers** (`openai`, `azure`, `fireworks`, `amazonbedrock`, `anthropic`, `vertex`, `google`, `exchangetoken`, `muskapi`) and maps the result to `billingModelId` from the catalog — so displayed cost reconciles with the ledger instead of drifting against a second price table. Be ready to explain the `userId` fallback chain: JWT `email` claim, then `X-Cortex-User-Email` header, then JWT `sub`.

**Test suite (bullet 3).** The design point the bullet compresses into "independent verifier" is that tests grade the agent's *actual output artifact*, not its self-reported success — modeled on Harbor's outside-agent-verifier pattern used for SWE-bench.

**ELO ranking (Yoyo).** Why pairwise rather than absolute scoring: LLMs are poorly calibrated at assigning absolute quality scores but comparatively reliable at head-to-head preference judgments. Same reason LMSYS Chatbot Arena and RLHF preference models use it.

## Open questions from the round-3 review

Your friend's points 3 and 4 can't be closed without facts only you have. Their own advice on this was right and worth repeating: *if the data can't be accurately measured, don't force it — better to write something real and explainable.* So these are left as-is rather than dressed up.

1. **What did the 150+ tests actually prevent?** Right now the bullet names two specific catches (a broken tool implementation, a redundant tool-call loop), which is good and concrete. What would make it much stronger is a downstream number: did the agent's task success rate move, did a class of bug stop reaching production, did release confidence change in some measurable way? If you have even a rough before/after pass rate, that bullet becomes the best one on the resume.
2. **At what request volume was the 15% token cut realized?** "15% cheaper" reads very differently at 1,000 requests/day than at 50. If you know the volume or the absolute monthly dollar figure, that context is worth more than the percentage alone.
3. **Was the starting point really 5 smoke tests?** Your friend's write-up says 5, and I used it because it's far punchier than "a handful." You'd told me only "simple smoke test." Confirm the number, or give me the real one.
4. **Why pairwise ELO instead of absolute scoring?** I wrote the rationale as "pairwise comparison proved more consistent on subjective market quality" — this is the standard and correct reason to prefer ELO/arena-style ranking (it's why LMSYS Chatbot Arena and RLHF preference models work this way), so it's defensible on first principles. But **confirm this matches your actual reasoning at the time.** If you picked it for a different reason, that reason is the one that belongs on the resume, because it's the one you can tell the story of under questioning.

One place I deliberately did **not** follow your friend: they suggested naming specific models and frameworks (GPT, Claude, a named agent framework) in the bullets. I left those out because I don't have confirmation of which you actually used at Cortex, and a model name you can't speak to in depth is exactly the kind of detail that invites a bad follow-up question. Tell me what was really in the stack and I'll add it.

## Formatting checklist (UMich Career Center criteria)

Everything below is now satisfied in the generated PDFs. Keep the list so you can re-check after any manual edit.

- [x] **One page** — all four versions verified at exactly 1 page
- [x] **Reverse chronological within every section** — Cortex (2026) → Yoyo (2025) → HIKE (2024); USC → UMich
- [x] **Consistent positioning** — organization left / location right, role left / dates right, identical in all three sections
- [x] **Bullets, not paragraphs** — no prose blocks anywhere except the optional FDE summary
- [x] **Quantified where possible** — 5→150+, 15%, 5x, 200+, 3x, 30 min→5 min, 94%, 3x within 3%
- [x] **Bullet Plus formula** (Action Verb + What + How/Why/Impact) — every bullet audited
- [x] **Tailored per target** — three track-specific versions plus this master
- [x] Single column, standard sans-serif, 10pt body, no tables/text boxes/graphics (ATS-safe)
- [x] LinkedIn and GitHub both present in the contact line, on one line
- [x] HIKE dates read Jun 2024 – Aug 2024
- [ ] Rename files to `Li_Joseph_Resume_[Track].pdf` before sending, if a given portal sorts by filename

**One deliberate deviation:** UCC's Masters example runs two pages, and their one-page rule is written "for most undergraduates." I kept all versions to one page anyway, because tech new-grad recruiting still treats one page as the norm regardless of degree level.
