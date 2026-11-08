# Learning Roadmap: Blockchain + AI + Fintech Engineering with Claude Code

**Goals:** become fluent in Claude Code, refresh blockchain development (Solidity, Go, TypeScript), and learn AI
engineering (Python, LLM APIs, RAG, evals, agents, MCP). Build **one** public portfolio that tells one story:
*an engineer who builds AI systems for fintech and blockchain.*

**Target roles (one portfolio, several resume versions):**
- Blockchain / stablecoin engineering, e.g. Coinbase's *Senior Software Engineer, Stablecoins*
- AI engineer / applied AI engineer (LLM apps, RAG, agents)
- Forward deployed engineer / solutions engineer / DevRel (building with customers, teaching, writing)
- Fintech backend (payments, ledgers, Go services)

**Path:** Weeks 1–3 build the blockchain and Go backend core. Weeks 4–5 add AI engineering on top of that same
code (the indexer, ledger and reserve service become the data your AI tools use). The capstone joins all three.

**Rhythm:** one project per weekday (about 1–1.5 hours), and a bigger one on weekends. Each project gets **its own GitHub repo** and **its own chat**.

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
  (From Day 0 on: GitHub CLI `gh` and my `/new-project` skill.) For AI projects (Week 4 on): Python 3 with a virtual
  environment, and an LLM API key.
- **AI projects and API keys:** the key lives in `.env`, which is git-ignored and denied to Claude Code (same rule as
  Week 1 Weekend). Each guide tells me how to set a low monthly spend limit on the API account, uses the cheapest model
  that works, and says roughly what the project will cost. Tests must run **without** a key or network by default
  (mock or recorded responses); live calls go behind a flag or a separate test marker.
- **Guide format:** write `GUIDE.md` for the project in the same format as
  [upgradeable-stablecoin/GUIDE.md](https://github.com/Syriacode/upgradeable-stablecoin/blob/main/GUIDE.md):
  every step has **Learn → Prompt (for Claude Code, in plan mode) → You check → Done when → Commit**.
  Very low-level steps: exact commands, exact words to type, and what I should see.
- **Size:** a weekday project must fit in **1–1.5 hours**. Weekend projects can be longer.
- **Verify before handing over:** build and test a reference solution privately so every command in the guide works.
  Don't push the solution. I write the code with Claude Code myself.
- **Every project repo must include:** the code, tests, a CI workflow, `README.md` (with a "How I used Claude Code" section
  that I write myself), and **`INTERVIEW.md` with 5 interview questions and model answers**.
- **One Claude Code technique per project** (listed in the tables below). Teach it inside the guide, and end the guide
  with a **"Level up"** tip for using Claude Code more fluently.
- **Repo:** one new public GitHub repo per project under Syriacode. Before Day 0, I create empty repos on github.com.
  After Day 0, my `/new-project` skill creates them.
- **When I say "done":** review my repo (run its tests), give honest feedback, then update the **Progress** table in this
  file in Mini-Blockchain and push.
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

### Week 2: Stablecoin-adjacent building blocks

| Status | When | Project | Lang | Blockchain concept | Claude Code technique | Repo |
|---|---|---|---|---|---|---|
| ⬜ | Mon | Merkle airdrop | Solidity + TS | Merkle proofs (rewards distribution) | Claude-written test-data scripts | |
| ⬜ | Tue | Transfer event indexer into SQLite | Go | event logs, indexing, reorgs | **sessions**: `--continue`, `/resume` | |
| ⬜ | Wed | Yield vault (ERC-4626) | Solidity | share accounting, rounding attacks | **context**: `/context`, `/compact`, `/clear` | |
| ⬜ | Thu | Gasless approvals (EIP-2612 permit) | Solidity | signatures, EIP-712, replay protection | debugging: `-vvvv` traces, screenshots | |
| ⬜ | Fri | Mini dApp front end for the testnet token | TypeScript | wallet connection, sending transactions | testing a web page with Claude in a browser | |
| ⬜ | Weekend | Break it, fix it: 4 vulnerable contracts | Solidity | real attack types and fixes | **parallel sessions** (worktrees), `claude -p` | |

> **Note (Week 1 Weekend):** PlayToken was not deployed to Base Sepolia (faucet/funding trouble). Before the Week 2 Fri
> dApp, either finish Steps 8–9 of `base-sepolia-token/GUIDE.md` or have the dApp deploy PlayToken to a local Anvil
> chain. The Week 5 capstone deploys to Base Sepolia, so a funded test wallet is needed by then.

After Week 2: review what clicked before starting Week 3.

### Week 3: Backend services and infrastructure (from job descriptions)

| Status | When | Project | Lang | Blockchain concept | Claude Code technique | Repo |
|---|---|---|---|---|---|---|
| ⬜ | Mon | Payments ledger API: double-entry ledger with Postgres and idempotency keys | Go | payment correctness, exactly-once transfers | **MCP server** (connect Claude Code to Postgres) | |
| ⬜ | Tue | Containerize the chain reader + indexer (Dockerfile, docker-compose with Postgres) | Go + Docker | running node clients and services | background commands (`&`), `/bashes` | |
| ⬜ | Wed | Infrastructure as Code: Terraform for the indexer stack (Docker provider, local) | Terraform | reproducible infra, secrets out of code | **headless `claude -p` in CI** (review a `terraform plan`) | |
| ⬜ | Thu | Stablecoin reserve service: watch mint/burn events, reconcile supply vs. reserves, alert on drift | Go | proof of reserves, reconciliation | **parallel subagents** (one per component) | |
| ⬜ | Fri | Transaction signer service: EIP-155/EIP-1559 signing, keystore, signing policy rules | Go | key management, custody, nonce handling | extended thinking (`think hard`) for design reviews | |
| ⬜ | Weekend | Multi-brand stablecoin factory (CREATE2 clones of the upgradeable stablecoin) | Solidity | factories, minimal proxies, deterministic addresses | **GitHub Actions with `@claude`** PR reviews | |

### Week 4: AI engineering foundations (built on my blockchain and ledger code)

| Status | When | Project | Lang | Concept | Claude Code technique | Repo |
|---|---|---|---|---|---|---|
| ⬜ | Mon | Wallet explainer: CLI that asks an LLM to explain an address in plain English, using **tool use** to fetch balances and recent transfers over RPC | Python | LLM API basics: messages, system prompts, tool use, structured JSON output, tokens and cost | user-level `~/.claude/CLAUDE.md` + `/memory` (a "how to teach me Python and AI" section) | |
| ⬜ | Tue | Evals for the wallet explainer: a golden test set, exact-match checks, LLM-as-judge, a score report | Python | evaluation, regressions, why "it looked right" isn't a test | **notebook editing** (Jupyter): analyze eval results with Claude | |
| ⬜ | Wed | Docs Q&A with RAG: answer questions over EIPs and my course notes, with citations; Postgres + pgvector from the Week 3 docker-compose | Python | embeddings, chunking, retrieval, grounding, "I don't know" answers | choosing models and watching cost (`/model`, `/cost`) | |
| ⬜ | Thu | MCP server for my ledger and indexer: tools like `get_balance`, `list_transfers`, `reconcile` (read-only) | Python or TypeScript | MCP: tools, resources, schemas, least privilege | **build your own MCP server** and add it with `claude mcp add` | |
| ⬜ | Fri | Prompt-injection lab: plant malicious text in RAG docs and transaction memos, watch the app misbehave, add defenses, write tests for each attack | Python | AI security: injection, data exfiltration, tool misuse, output validation | safe handling of untrusted content in Claude Code itself (plan mode + deny rules when reading attacker-controlled files) | |
| ⬜ | Weekend | Payments ops agent: reads the ledger via my MCP server, investigates a failed payment, proposes a refund; **a human must approve any money movement**; evals + Docker | Python | agent loops, guardrails, human-in-the-loop, audit logs | **Claude Agent SDK** (build an agent on the same harness as Claude Code) | |

### Week 5: Security, fintech and shipping to customers (from job descriptions)

| Status | When | Project | Lang | Concept | Claude Code technique | Repo |
|---|---|---|---|---|---|---|
| ⬜ | Mon | Static analysis: run Slither and Aderyn on all my contracts, triage every finding; compare with an LLM review of the same code | Solidity | automated auditing, false positives, where AI review helps and fails | custom slash-command skill (`/audit`) | |
| ⬜ | Tue | Professional audit report for the Week 2 "break it" contracts (severity, impact, fix, test) | Markdown + Solidity | audit process, threat modeling | **output styles** for report writing | |
| ⬜ | Wed | Tokenized treasury fund: permissioned token (allowlist, transfer rules, NAV oracle) + 1-page client brief | Solidity + Markdown | tokenization, compliance controls | writing for executives with Claude | |
| ⬜ | Thu | Forward-deployed sprint: a "customer" hands me a messy CSV export and a half-documented API; integrate it with my ledger, use an LLM to categorize transactions, write a deployment note for their team | Python + Go | reconciliation, data cleaning, AI in a real workflow, customer communication | **have Claude interview me** about requirements before it plans | |
| ⬜ | Fri | Deploy the RAG app or ops agent to a cloud free tier with Terraform, secrets in the cloud's secret store, a health check and logs | Terraform + Docker | cloud deployment, cost control, observability | custom subagent as a cloud **cost and security reviewer** | |
| ⬜ | Weekend | Capstone: **AI-monitored stablecoin.** Stablecoin + reserve service on Base Sepolia, the ops agent explains drift alerts and drafts an incident report, dApp front end; portfolio README; 3-minute demo video | all | end-to-end system: blockchain + AI + fintech | **plugins**: package my kit for reuse | |

### Optional (only when a real job description asks for it)

| Status | Project | Lang | Concept | Claude Code technique | Repo |
|---|---|---|---|---|---|
| ⬜ | Rust intro: Merkle tree crate with proofs and tests | Rust | Merkle trees, Rust ownership | reuse the "teach me" section of `~/.claude/CLAUDE.md` | |
| ⬜ | Fund-flow tracer: follow funds from an address N hops, export a graph and a short findings report (add an LLM-written summary) | Python | blockchain forensics, transaction tracing | notebook editing (Jupyter) | |

---

## Job map (which project proves which requirement)

Added from job descriptions on 2026-11-02. When a project is ✅, add it to the matching resume version.

| Requirement in job posts | Where it shows up | Proved by |
|---|---|---|
| Solidity / EVM smart contracts in production; upgradeability, access control | Coinbase Stablecoins, Chainlink, FTI | Upgradeable stablecoin ✅, ETH Vault ✅, Multisig ✅, Timelock ✅, Permit, Factory |
| Onchain security, audits, key management | Coinbase Stablecoins, Chainlink, Anchorage | Break it/fix it, Slither triage, Audit report, Signer service |
| Go backend services, distributed systems | Coinbase (Stablecoins, Payments, Blockchain Network, Data Foundations), Anchorage, Robinhood | Chain reader ✅, Indexer, Payments ledger, Reserve service, Signer service |
| Payments correctness (ledgers, idempotency) | Coinbase Payments Platform, Mastercard | Payments ledger API |
| Infrastructure as Code (Terraform), Docker, cloud | Coinbase Data Foundations, Anchorage | Containerize, Terraform project |
| Indexing onchain data, event logs, reorgs | Coinbase Data Foundations / Blockchain Network | Transfer event indexer |
| Python / TypeScript, APIs, explaining tech to customers | Alchemy Solutions, PwC | Token balance script, dApp front end, Tokenized fund brief, teaching record |
| Rust, cryptography | Chainlink Product Security | Rust Merkle crate (optional), Permit (EIP-712 signatures) |
| Blockchain forensics, fund-flow tracing, client reports | FTI Consulting | Fund-flow tracer (optional), Audit report |
| Tokenization, custody, stablecoin strategy | PwC, Coinbase Stablecoins, Anchorage | Upgradeable stablecoin ✅, Reserve service, Tokenized fund |

**AI engineering rows** (added 2026-11-08 from general market research; fill in "Where it shows up" when I paste real
AI engineer or forward deployed engineer job descriptions):

| Requirement in job posts | Where it shows up | Proved by |
|---|---|---|
| Python, LLM APIs, tool use / function calling, structured output | AI engineer posts | Wallet explainer |
| Evaluation of LLM systems | AI engineer posts | Wallet explainer evals, ops agent evals |
| RAG, embeddings, vector databases | AI engineer posts | Docs Q&A with RAG |
| Agents, MCP, integrating AI with internal systems | AI engineer / FDE posts | Ledger MCP server, Payments ops agent |
| AI security (prompt injection, guardrails) | AI engineer / security posts | Prompt-injection lab, ops agent approvals |
| Working with customers: messy data, integrations, docs | FDE / solutions engineer posts | Forward-deployed sprint, Tokenized fund brief, teaching record |
| Deploying and running AI services in the cloud | AI engineer / FDE posts | Cloud deploy, Terraform project |
| Agentic coding tools (Claude Code) | AI engineer / developer tools posts | every project's "How I used Claude Code" section |

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
