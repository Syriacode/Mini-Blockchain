# Learning Roadmap: AI Engineering (+ Blockchain and Fintech) with Claude Code

**Goals:** get hired as an **AI engineer** (the biggest hiring market right now), stay ready for blockchain and fintech
roles, and become fluent in Claude Code along the way.

**Two lanes, one GitHub profile:**
- **AI lane (main, about 70% of the plan).** Python, LLM APIs, structured output, evals, RAG, agents, MCP,
  guardrails, observability, deployment. **No blockchain in these projects**, so they stand on their own for any AI
  employer. Running product: **CourseMate**, an AI teaching assistant over my own course materials (my real edge as
  a professor), plus a customer-integration project for forward-deployed roles.
- **Blockchain + fintech lane (about 30%).** Keep the strongest stablecoin skills sharp (signatures, vaults, security,
  reserves) and the Go payments ledger, which also counts for general backend jobs.

**Target roles, in priority order:**
1. AI engineer / applied AI engineer (LLM apps, RAG, agents)
2. Forward deployed engineer / AI solutions engineer / AI DevRel or education (building with customers, teaching, writing)
3. Fintech backend (Go, payments, ledgers)
4. Blockchain / stablecoin engineering, e.g. Coinbase's *Senior Software Engineer, Stablecoins*

**Path:** Week 1 (blockchain refresh) is done. Then (Nov 9 – Dec 15, 2026): AI foundations with two AI basics
labs, production AI and the Go ledger, then the blockchain lane and interview prep. A job track runs alongside, so
applications start now.

**Rhythm (changed Nov 11):** **one project every other day**, about 1.5–2 hours. The day in between is a
**reading day**: re-read the guide's overview, answer its "Check your understanding" questions without looking, and
look up anything unclear. Quality over quantity. Each project gets **its own chat**, and usually its own GitHub repo
(projects that improve CourseMate or the triage CLI happen on a branch of that repo).

---

## How to start each project (new chat)

1. Open a **new chat** with Claude (in the Claude app, linked to your computer).
2. Paste the **starter message** below, and change the last line to the project you're doing.
3. Claude writes and tests a guide. You do the project in **Claude Code** on your computer, step by step, in **plan mode**.
4. When it's pushed, tell that chat "done". Claude reviews your repo and ticks the box in the progress table below.

### Starter message (copy everything in the box)

```
I'm following my learning roadmap: https://github.com/Syriacode/Mini-Blockchain/blob/main/ROADMAP.md
Please attach the Syriacode/Mini-Blockchain repo and read ROADMAP.md first, then follow its "Rules for Claude" section.

Today's project: <write the project name from the roadmap here, e.g. "Week 1 Mon – ETH Vault">
```

---

## Rules for Claude (read these at the start of every new chat)

- **Who I am:** I teach undergrad computer science and grad-level blockchain classes, and I'm preparing for blockchain,
  AI engineering and fintech jobs. I'm a bit rusty on blockchain development, new to AI engineering, and still learning
  Claude Code. I'll look up anything I don't understand.
- **My setup:** Windows with Git Bash; Claude Code in the terminal; Foundry installed; GitHub user **Syriacode**.
  (From Day 0 on: GitHub CLI `gh` and my `/new-project` skill.) For AI projects: Python 3 with a virtual
  environment, and Ollama for local models.
- **Python is `py` on my machine,** not `python`: guides write `py -m pytest`, `py -m pip install ...`, and
  `!py -m pytest` inside Claude Code. CI on GitHub (Linux) keeps `python`.
- **My PC (for model choices):** Intel i7-1260P, **16 GB RAM**, Intel Iris Xe integrated graphics (**no NVIDIA GPU**,
  so models run on the CPU), plenty of disk. Default to a **3B–4B chat model** plus a small local embedding model;
  7B–8B only as an optional comparison. Run Ollama natively on Windows (not inside Docker) and keep Docker's memory
  limit modest, so Postgres, Docker and the model fit in 16 GB together.
- **Zero-cost rule (no paid APIs or services):** nothing in this roadmap may cost money.
  - **Models run locally with Ollama** (free, open-source): a small chat model and a local embedding model, chosen
    to fit my PC's RAM. Each guide says which model and why, and what to do if it's too slow.
  - **Code is provider-agnostic:** one small `llm.py` interface with a local Ollama backend. Swapping to a hosted API
    later must be a config change, not a rewrite (interviewers will ask about hosted APIs, so the guide explains the
    differences).
  - Optional only: a hosted free tier (e.g. Google's Gemini API free tier) that needs **no billing account or credit
    card**. Never put my course materials in a free tier that trains on inputs unless I say so.
  - **Free building blocks only:** Docker, Postgres + pgvector, FastAPI, GitHub Actions on public repos, Terraform with
    the local Docker provider. No cloud account that asks for a credit card.
  - Tests run **without** a model or network by default (mock or recorded responses); live model calls go behind a
    separate test marker. Any secrets still live in `.env`, git-ignored and denied to Claude Code.
- **AI lane rules:** no blockchain or crypto in AI-lane projects. Use my own course materials (slides, notes,
  assignments I wrote; **never student data or grades**) or invented business data (support tickets, invoices,
  product docs). Python with type hints, Pydantic for structured data, pytest, `ruff`. Prefer plain SDK calls first
  so I understand what frameworks hide; introduce one framework (LangGraph or similar) only where a guide says so.
  Every AI-lane `INTERVIEW.md` includes one **LLM system design** question (e.g. "design a RAG system for 10k
  documents") with a model answer.
- **Guide format:** write `GUIDE.md` for the project in the same format as
  [upgradeable-stablecoin/GUIDE.md](https://github.com/Syriacode/upgradeable-stablecoin/blob/main/GUIDE.md):
  every step has **Learn → Prompt (for Claude Code, in plan mode) → You check → Done when → Commit**.
  Very low-level steps: exact commands, exact words to type, and what I should see.
- **I'm new to AI, so teach the basics first (added Nov 11).** In the overview, explain each AI idea with a tiny
  example I can work out on paper (real numbers, a 2-D vector, a 3-chunk example), before any code. Each step adds
  a **Predict** line (what to expect before running). Keep Claude Code prompts short: the goal and the rules, not a
  full specification I can't follow. I hand-type the one or two small functions where the idea lives, and their
  tests use the same numbers as the paper example. End every guide with **"Check your understanding"**: 5–7
  questions with hidden answers, for the reading day.
- **Every guide starts with a Project overview**, before Step 0, that I can read on its own: what the project is
  about and why it matters; what we'll build (the parts and how they fit, with a small diagram); how we'll test it;
  a short definition of every new tool, technology or term used; and, when the project builds on an earlier one,
  a plain-language recap of what that earlier project built.
- **Size:** a project fits in **about 1.5–2 hours** of hands-on time, with a natural place to stop halfway. One project
  every other day.
- **Verify before handing over:** build and test a reference solution privately so every command in the guide works.
  Don't push the solution. I write the code with Claude Code myself.
- **Every project repo must include:** the code, tests, a CI workflow, `README.md` (run commands, design decisions,
  known limitations; no "How I used Claude Code" section), and **`INTERVIEW.md` with 5 interview questions and
  model answers**.
- **One Claude Code technique per project** (listed in the tables below). Teach it inside the guide, and end the guide
  with a **"Level up"** tip for using Claude Code more fluently.
- **Repo:** one new public GitHub repo per project under Syriacode. Before Day 0, I create empty repos on github.com.
  After Day 0, my `/new-project` skill creates them.
- **When I say "done":** review my repo (run its tests), give honest feedback, then update the **Progress** table in this
  file in Mini-Blockchain and push. Also tell me which resume versions (A, B, C in the Job track) the project belongs
  in, and give me one resume line for each.
- **Job descriptions:** when I paste one, map its requirements to existing or new projects and add them to this roadmap.

---

## Progress

| Status | When | Project | Lang | Blockchain concept | Claude Code technique | Repo |
|---|---|---|---|---|---|---|
| ✅ | — | Simple chain | Python | blocks, hashing, proof-of-work | first prompts, reading code | [Mini-Blockchain/01-simple-chain](01-simple-chain) |
| ✅ | — | Upgradeable stablecoin | Solidity | UUPS proxy, roles, minter allowances, pause, blocklist, fuzz/invariant tests | plan mode, CLAUDE.md, `!` commands, break-it-on-purpose testing | [upgradeable-stablecoin](https://github.com/Syriacode/upgradeable-stablecoin) |
| ✅ | Day 0 | **Project kit** | Bash | — | **custom skill** (`/new-project`), GitHub CLI, **permission rules** | [claude-project-kit](https://github.com/Syriacode/claude-project-kit) |

### Week 1: Refresh the basics

| Status | When | Project | Lang | Blockchain concept | Claude Code technique | Repo |
|---|---|---|---|---|---|---|
| ✅ | Mon | ETH Vault: deposit, withdraw, events | Solidity | payable, mappings, reentrancy | `@file` mentions; **rewind** (Esc Esc) | [eth-vault](https://github.com/Syriacode/eth-vault) |
| ✅ | Tue | 2-of-3 Multisig wallet | Solidity | multi-party approvals, admin-key protection | **test-driven**: failing tests first | [multisig-wallet](https://github.com/Syriacode/multisig-wallet) |
| ✅ | Wed | Chain reader CLI: latest block, balances | Go | RPC, blocks, go-ethereum | learning a new language with Claude | [chain-reader-cli](https://github.com/Syriacode/chain-reader-cli) |
| ✅ | Thu | Timelock: delayed admin actions | Solidity | governance, time-based security | **custom subagent** (security reviewer) | [timelock](https://github.com/Syriacode/timelock) |
| ✅ | Fri | Token balance script | TypeScript | ERC-20 reads, events, viem | **hooks** (auto-format on edit) | [token-balance-script](https://github.com/Syriacode/token-balance-script) |
| ✅ | Weekend | Deploy and verify a token on Base Sepolia (built, tested and reviewed; live deploy skipped, see note) | Solidity | test wallets, faucets, Basescan verification | secrets safety (deny `.env`), `/code-review` | [base-sepolia-token](https://github.com/Syriacode/base-sepolia-token) |

## Plan: Nov 9 – Dec 15, 2026, one project every other day

Changed on Nov 11: the sprint was one project a day, which went too fast to understand the AI basics. Now there's a
project every other day, a reading day in between, and two **AI basics labs** before the bigger AI projects.
If a project slips, move everything after it; don't squeeze two into one day.

### Phase 1 (Nov 9–15): AI foundations — CourseMate v1 (AI lane)

| Status | When | Project | Lang | Concept | Claude Code technique | Repo |
|---|---|---|---|---|---|---|
| ✅ | Mon Nov 9 | Question triage CLI: classify student/support questions (topic, urgency, needs-human) with an LLM; Pydantic schemas, retries, token and cost log | Python | LLM API basics: messages, system prompts, structured output, temperature, tokens and cost | user-level `~/.claude/CLAUDE.md` + `/memory` ("how to teach me Python and AI") | [question-triage](https://github.com/Syriacode/question-triage) |
| ✅ | Tue Nov 10 | Evals for the triage CLI: 50-example golden set, accuracy per label, LLM-as-judge for explanations, eval gate in CI | Python | evaluation, regressions, "it looked right" isn't a test | Claude-written test-data scripts (generate and then hand-check the golden set) | [question-triage](https://github.com/Syriacode/question-triage) (`evals/`, PR #2) |
| ✅ | Wed Nov 11 | CourseMate RAG: answer questions over my course notes with citations; chunking, embeddings, Postgres + pgvector in docker-compose; "I don't know" when not grounded | Python + Docker | embeddings, chunking, retrieval, grounding | choosing models and watching cost (`/model`, `/cost`) | [coursemate](https://github.com/Syriacode/coursemate) |
| ✅ | Thu Nov 12 | Better retrieval: keyword search (BM25, by hand), vector search, hybrid (RRF), measured with recall@k and MRR on a reviewed golden set; CourseMate uses the winner. (Reranking moved to Optional.) | Python | search quality, measuring retrieval | **notebook editing** (Jupyter): compare runs with Claude | [coursemate](https://github.com/Syriacode/coursemate) (PR #1: vector won, recall@3 0.96 vs. hybrid 0.84) |
| ⬜ | Sat Nov 14 | **AI basics lab 1: how an LLM works.** A notebook with small experiments on the local model: tokens and the tokenizer, next-token prediction, temperature (the same prompt 5 times at 0 and at 1), the context window and silent truncation (`num_ctx`), system vs. user messages, why models make things up | Python + Jupyter | tokens, sampling, context window, hallucination | **Claude as a tutor**: explain this, then quiz me | new repo `ai-basics` |

### Phase 2 (Nov 16–22): CourseMate gets an app and an agent (AI lane)

| Status | When | Project | Lang | Concept | Claude Code technique | Repo |
|---|---|---|---|---|---|---|
| ⬜ | Mon Nov 16 | CourseMate API + UI: FastAPI with streaming responses, a minimal chat web page, conversation history | Python + HTML/TS | serving LLM apps, streaming, sessions | testing a web page with Claude in a browser | |
| ⬜ | Wed Nov 18 | **AI basics lab 2: tool calling and agents from scratch.** What "tool calling" really is (the model writes JSON, your code runs the tool), then a ~40-line agent loop with two tools and no framework; print every message so the loop is visible | Python | tool use, the agent loop, stopping conditions | watch Claude Code's own agent loop (transcript view, `Ctrl+O`) and compare it with mine | `ai-basics` |
| ⬜ | Fri Nov 20 | CourseMate agent: tools to search notes, generate a quiz and draft an announcement; **a human approves anything that gets sent**; agent evals | Python | tool use, human-in-the-loop, agent evals | Claude Agent SDK | |
| ⬜ | Sun Nov 22 | CourseMate MCP server: expose the course tools over MCP and use them from Claude Code | Python | MCP, integrating AI with internal systems | **build your own MCP server** (`claude mcp add`) | |

### Phase 3 (Nov 24 – Dec 5): Production AI + fintech backend

| Status | When | Project | Lang | Concept | Claude Code technique | Repo |
|---|---|---|---|---|---|---|
| ⬜ | Tue Nov 24 | Observability for CourseMate: traces per request (prompt, retrieved chunks, tool calls), latency and cost per answer, a small dashboard; add caching | Python | LLMOps: tracing, cost and latency budgets, caching | **sessions**: `--continue`, `/resume` | |
| — | Thu Nov 26 | Thanksgiving: no project. | | | | |
| ⬜ | Fri Nov 27 | Guardrails and prompt-injection lab: poison notes and tool results, watch CourseMate misbehave, add defenses and output validation, one test per attack | Python | AI security: injection, data leaks, tool misuse | safe handling of untrusted content (plan mode + deny rules) | |
| ⬜ | Sun Nov 29 | Payments ledger API: double-entry ledger, idempotency keys, Postgres | Go | payment correctness, exactly-once transfers | **MCP server** (connect Claude Code to Postgres) | |
| ⬜ | Tue Dec 1 | Forward-deployed sprint: a "customer" hands me a messy invoice CSV and a half-documented API; clean it, load it into my ledger, LLM categorizes line items with evals, deployment note for their team | Python + Go | data cleaning, integration, AI in a real workflow, customer communication | **have Claude interview me** about requirements before it plans | |
| ⬜ | Thu Dec 3 | Ship CourseMate: one-command deploy with Terraform (local Docker provider): app + Postgres containers talking to Ollama on the host, secrets out of code, health check, eval gate in CI before a release; plus a short doc on how the same setup maps to a real cloud | Terraform + Docker | IaC, deployment, CI/CD for LLM apps | **headless `claude -p` in CI** (review a `terraform plan`) | |
| ⬜ | Sat Dec 5 | **AI capstone: CourseMate case study.** Polish, an eval and latency report, architecture diagram, case-study README ("problem → design → results → what I'd do next"), 3-minute demo video (it runs locally) | all | presenting an AI product end to end | **plugins**: package my kit for reuse | |

### Phase 4 (Dec 7–15): Blockchain + fintech lane, interview prep

| Status | When | Project | Lang | Concept | Claude Code technique | Repo |
|---|---|---|---|---|---|---|
| ⬜ | Mon Dec 7 | Gasless approvals (EIP-2612 permit) | Solidity | signatures, EIP-712, replay protection | debugging: `-vvvv` traces, screenshots | |
| ⬜ | Wed Dec 9 | Yield vault (ERC-4626) | Solidity | share accounting, rounding attacks | **context**: `/context`, `/compact`, `/clear` | |
| ⬜ | Fri Dec 11 | Stablecoin reserve service: watch mint/burn events, reconcile supply vs. reserves, alert on drift | Go | proof of reserves, reconciliation | **parallel subagents** (one per component) | |
| ⬜ | Sun Dec 13 | Security day: break it, fix it (2 vulnerable contracts) + Slither/Aderyn on all my contracts + a short audit report | Solidity + Markdown | real attack types, automated auditing | **parallel sessions** (worktrees), `claude -p` | |
| ⬜ | Tue Dec 15 | **Bridge project:** stablecoin ops agent. Reuse the CourseMate agent pattern: it reads the reserve service and ledger, explains drift alerts, drafts an incident report, human approves. Then a **mock interview loop** (see Job track). | Python + Go | applying the AI lane to fintech/blockchain | custom subagent as an **interviewer** that grills me on my repos | |

> **Note (Week 1 Weekend):** PlayToken was not deployed to Base Sepolia. Nothing in the plan needs Base Sepolia now;
> the Phase 4 projects run on a local Anvil chain.

### Optional (after the plan, only when a real job description asks for it)

| Status | Project | Lang | Concept | Repo |
|---|---|---|---|---|
| ⬜ | Reranking for CourseMate: rerank the top 20 hybrid candidates with a small cross-encoder or the local LLM, and prove it with the Nov 12 retrieval eval (recall@k, MRR) and latency | Python | reranking, quality vs. latency | |
| ⬜ | Fine-tune a small open model (LoRA) on question-triage data and compare it with prompting, using the Week 2 evals | Python | fine-tuning vs. prompting, cost/quality trade-offs (free with a Google Colab GPU, if available) | |
| ⬜ | Multi-agent workflow with a framework (LangGraph or similar) | Python | orchestration, state, retries | |
| ⬜ | Merkle airdrop | Solidity + TS | Merkle proofs | |
| ⬜ | Reserve service, Transfer event indexer (optional) | Go | event logs, indexing, reorgs | |
| ⬜ | Mini dApp front end | TypeScript | wallet connection | |
| ⬜ | Tokenized treasury fund + client brief | Solidity + Markdown | tokenization, compliance | |
| ⬜ | Transaction signer service | Go | key management, custody | |
| ⬜ | Multi-brand stablecoin factory | Solidity | CREATE2, minimal proxies | |
| ⬜ | Rust Merkle crate | Rust | Rust ownership | |
| ⬜ | Fund-flow tracer | Python | blockchain forensics | |

---

## Job track (runs alongside the projects, about 20–30 minutes a day)

Work happens in my private repo **Syriacode/job-search**. Dates follow the every-other-day plan. Golden rule: apply only to companies I can verify are real
and have a history. Salary floor: $150k. Phoenix on-site/hybrid, remote, or relocation for the right employer.
Aim for about **70% AI applications, 30% blockchain/fintech**.

**Resume versions:**
- **(A) AI engineer / applied AI / forward deployed** — AI lane projects and the Go ledger. **No blockchain on it.**
- **(B) AI solutions / DevRel / AI education** — the same AI projects, led by teaching, curriculum design, talks and writing.
- **(C) Blockchain + fintech backend** — Week 1, Phase 4, the ledger, plus one line on AI work.

| Status | When | Job task |
|---|---|---|
| ⬜ | Nov 9–12 | Draft resumes A, B and C from what's ✅ now and the teaching record. A and B fill in as the week goes. |
| ⬜ | Nov 13–14 | GitHub profile README and LinkedIn (headline, About, Featured) aimed at **AI engineering first**; pin AI repos as they land. |
| ⬜ | Nov 15–16 | Visa prep: ask my immigration attorney whether I'm counted against the H-1B cap and how long a transfer takes. Write a two-line answer for "Do you need sponsorship?" |
| ⬜ | Nov 17–22 | Target list of 40 verified companies (AI startups, enterprises building AI, AI platform companies, EdTech, fintech, a few crypto). Send the **first 5 applications**. |
| ⬜ | Nov 23 – Dec 5 (daily) | **1–2 applications a day** + **30 minutes of Python coding practice** (arrays, hashing, two pointers, BFS/DFS: AI engineer loops still include a coding round). |
| ⬜ | Dec 5–6 | Publish the CourseMate demo video + a LinkedIn post. Practice 2 **LLM system design** questions out loud (from my `INTERVIEW.md` files). |
| ⬜ | Dec 7–15 (daily) | **1–2 applications a day**, follow up on earlier ones, reach out to 1 person a day at target companies (alumni, ex-students, conference contacts). |
| ⬜ | Dec 15 | Mock interview loop: one coding round, one LLM system design, one behavioral (5 STAR stories), one "walk me through your repo". Turn one `GUIDE.md` into a public tutorial (DevRel writing sample). |

**Target by Dec 15:** resume A that reads as a real AI engineer, a recorded CourseMate demo with evals and a case
study, about 30–40 tailored applications sent, and a practiced interview loop.

---

## Job map (which project proves which requirement)

Added from job descriptions on 2026-11-02. When a project is ✅, add it to the matching resume version.

| Requirement in job posts | Where it shows up | Proved by |
|---|---|---|
| Solidity / EVM smart contracts in production; upgradeability, access control | Coinbase Stablecoins, Chainlink, FTI | Upgradeable stablecoin ✅, ETH Vault ✅, Multisig ✅, Timelock ✅, Permit, ERC-4626 vault |
| Onchain security, audits, key management | Coinbase Stablecoins, Chainlink, Anchorage | Security day (break it/fix it, Slither, audit report), Signer service (optional) |
| Go backend services, distributed systems | Coinbase (Stablecoins, Payments, Blockchain Network, Data Foundations), Anchorage, Robinhood | Chain reader ✅, Payments ledger, Reserve service, Indexer (optional) |
| Payments correctness (ledgers, idempotency) | Coinbase Payments Platform, Mastercard | Payments ledger API |
| Infrastructure as Code (Terraform), Docker, cloud | Coinbase Data Foundations, Anchorage | Ship CourseMate (Terraform + Docker), Payments ledger |
| Indexing onchain data, event logs, reorgs | Coinbase Data Foundations / Blockchain Network | Reserve service, Transfer event indexer (optional) |
| Python / TypeScript, APIs, explaining tech to customers | Alchemy Solutions, PwC | Token balance script, Forward-deployed sprint, teaching record |
| Rust, cryptography | Chainlink Product Security | Rust Merkle crate (optional), Permit (EIP-712 signatures) |
| Blockchain forensics, fund-flow tracing, client reports | FTI Consulting | Fund-flow tracer (optional), Security day audit report |
| Tokenization, custody, stablecoin strategy | PwC, Coinbase Stablecoins, Anchorage | Upgradeable stablecoin ✅, Reserve service, Stablecoin ops agent, Tokenized fund (optional) |

**AI engineering rows** (added 2026-11-08 from general market research; fill in "Where it shows up" when I paste real
AI engineer or forward deployed engineer job descriptions). None of these depend on blockchain:

| Requirement in job posts | Where it shows up | Proved by |
|---|---|---|
| Python, LLM APIs, structured output, tool use | AI engineer posts | Question triage CLI ✅, CourseMate agent |
| Evaluation of LLM systems | AI engineer posts | Triage evals, retrieval evals (recall@k), agent evals, CI eval gate |
| RAG, embeddings, vector databases, search quality | AI engineer posts | CourseMate RAG ✅, Better retrieval |
| Serving LLM apps (APIs, streaming) | AI engineer posts | CourseMate API + UI |
| Agents, MCP, integrating AI with internal systems | AI engineer / FDE posts | CourseMate agent + MCP server |
| AI security (prompt injection, guardrails) | AI engineer / security posts | Guardrails and prompt-injection lab |
| LLMOps: tracing, cost, latency, caching | AI engineer posts | Observability for CourseMate |
| Working with customers: messy data, integrations, docs | FDE / solutions engineer posts | Forward-deployed sprint, teaching record |
| Deploying AI services, CI/CD | AI engineer / FDE posts | Ship CourseMate (Terraform + Docker + CI eval gate) |
| Agentic coding tools (Claude Code) | AI engineer / developer tools posts | every project's Claude Code technique (Progress tables) and `GUIDE.md` |

---

## Level-up tips collected so far

1. **Plan mode first** (Shift+Tab): review what Claude intends before it touches files.
2. **Break it on purpose:** after tests pass, have Claude remove a safety check and confirm a test fails. That's how you know the tests protect something.
3. **`CLAUDE.md` is Claude's memory for a repo.** Keep it accurate, because every session reads it.
4. **When Claude does something you'd want every time, turn it into a skill.** (Day 0)
5. **Put a skill's mechanical steps in a tested script, and keep risky commands as visible steps.** Permission rules only see the command Claude types, not what runs inside a script. (Day 0)
6. **Commit before you experiment, then rewind (`Esc Esc` → Restore code) to undo it.** Rewind only tracks Claude's
   file edits, not shell commands, so git is the backstop. `@`-mention the file a prompt is about, so Claude works from
   exactly that file. (Week 1 Mon)
7. **Commit the failing tests, then let git prove the fix.** After a red commit, `git diff --stat test/` shows in one line
   whether Claude changed your specification or your code. Put "never edit a test to make it pass" in `CLAUDE.md`.
   (Week 1 Tue)
8. **Tell Claude how to teach you, once, in `CLAUDE.md`.** When learning a language, ask for comparisons to what you
   already know, predict before you ask, and hand-type the one function where the real idea lives. Reuse the section
   for Rust in Week 4. (Week 1 Wed)
9. **Give the reviewer a different job from the builder, and measure it before you trust it.** A subagent has fresh
   context, limited tools and one job. Plant a bug and run it blind, because a clean report means nothing until you've
   seen it catch something. Then turn each real finding into a test. (Week 1 Thu)
10. **Turn rules that must always hold into hooks, and keep CI as the backstop.** `CLAUDE.md` is advice; a hook runs
    every time. Test a hook by piping JSON into it before you trust it, keep it fast and narrow, and exit 2 with a
    clear message when Claude needs to fix something. Hooks only see Claude's own tool calls, so the same check also
    belongs in CI. (Week 1 Fri)
11. **Keep secrets out of Claude's reach by design, then use rules as a seatbelt.** A deny list is an enumeration, and
    there's always another command, alias or script. Keep the valuable secret where Claude can't read it (an encrypted
    keystore, a separate terminal for passwords), test deny rules with a canary, and scan git history in CI. Run
    `/code-review` on a branch **before** an irreversible step, so it sees exactly what you're about to ship.
    (Week 1 Weekend)
12. **Put who you are in user memory, and what the repo needs in project memory.** `~/.claude/CLAUDE.md` follows you
    into every project; each repo's `CLAUDE.md` stays short and true for anyone who clones it. When Claude behaves
    oddly, run `/memory` first to see which files shaped the session. Run `git branch` before your first push, so
    your work lands on `main`. (Week 2 Mon)
13. **Let Claude write the test data and its checker, but own the labels, and measure the judge before you trust it.**
    Commit Claude's draft before you review it, so `git diff` shows what a human changed, and make the code refuse
    unreviewed rows. An LLM judge is a model too: give it a balanced, hand-labelled calibration set (as many passes as
    fails), read its reasons, and don't let a low threshold hide a judge that grades the wrong thing. (Week 2 Tue)
14. **Match the model to the job, and read the meter.** Plan with the strongest model and execute with a cheaper one
    (`opusplan`), drop to Haiku for simple text, and switch at natural breaks, because each model keeps its own prompt
    cache. Check `/usage` (or `/cost`) at the end of a session, not only when you hit a limit. The same rule applies
    inside your own app: don't pay for a model call you don't need, keep prompts as small as the job allows, and use
    the smallest model that passes your evals. (Week 2 Wed)
15. **Explore in a notebook, keep in a module, and let Claude read the outputs.** A notebook is the quickest way to
    *see* what a model does (vectors, scores, misses), and Claude Code reads notebook outputs and edits single cells,
    so you can ask "why did this question miss?" about real numbers instead of guesses. Code you rely on still
    belongs in tested `.py` files that the notebook only calls. Save every run you may compare (`--save
    evals/runs/NAME.json`) and have Claude diff runs question by question. Run the notebook in CI
    (`nbconvert --execute`), because a notebook nobody re-runs quietly breaks. (Week 2 Thu)
