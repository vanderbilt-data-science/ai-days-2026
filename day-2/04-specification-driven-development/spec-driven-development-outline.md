# Specification-Driven Development: Building Research Tools Without Coding

**90-Minute Conference Talk | Myranda**
*Course 4: Agentic Solution Development and Deployment*

---

## Core Argument

Faculty don't need to learn programming to build functional research tools. They need to learn **specification writing** — the art of communicating precisely what a tool should do. AI coding agents handle the implementation.

**Audience:** Non-CS faculty who want to build data processing scripts, visualization dashboards, or analysis pipelines without prior programming experience.

**Learning Outcomes:**
1. Write a clear, complete specification for a research tool
2. Direct an AI coding agent to build that tool
3. Apply test-driven development principles without writing test code yourself
4. Evaluate agent output for correctness and quality

---

## Session Structure (90 min)

| Segment | Slides | Duration | Content |
|---------|--------|----------|---------|
| Introduction & Framing | 1–3 | 10 min | The core argument, who this is for, the real barrier |
| Part 1: The Specification | 4–7 | 15 min | What is a spec, anatomy, vague vs. strong |
| Part 2: The Workflow | 8–10 | 10 min | Spec→Agent→Test→Evaluate→Refine loop |
| **Example Case 1** | 12–15 | **15 min** | Medical Scheduling |
| **Example Case 2** | 16–19 | **15 min** | Digital Nashville |
| Part 3: Testing & Evaluation | 23–27 | 15 min | TDD with agents, quality checks, pitfalls |
| Wrap-up & Q&A | 28–30 | 5 min | Takeaways, resources, discussion |

---

## Slide-by-Slide Outline

### Slide 1 — Title
**Specification-Driven Development**
*Building Research Tools Without Coding*

Myranda | Course 4: Agentic Solution Development and Deployment | 90 Minutes

---

### Slide 2 — Session Roadmap
Four sections with visual blocks:
1. **Why Specs Matter** — 15 min
2. **The Workflow** — 10 min
3. **Example Cases** — 30–45 min
4. **Testing & Evaluation** — 15 min

---

### Slide 3 — Software Engineering Principles

How software engineering principles are useful to you. 


---
NOTE: Claude originally suggested I use this quote:

"The barrier to building research tools isn't coding. It's knowing what you want — precisely enough for a machine to build it."

But I don't know who that quote is from (if it's even real) - and I don't think I even like it! Just goes to show that you really need to remain the expert in your projects :)

*The core insight of specification-driven development*

---

### Slide 4 — What We Assumed vs. What's True Now
Two-column comparison:

| The Old Assumption | The New Reality |
|--------------------|-----------------|
| You need to code to build tools | You need to specify clearly |
| Programming is the bottleneck | Communication is the bottleneck |
| Agents just write code for you | You direct agents with precision |
| Output quality = model quality | Output quality = specification quality |
| Non-CS faculty can't build tools | Domain expertise + specs = powerful tools |

---

### Slide 5 — What Is a Specification?
**Definition:** A precise, testable description of what a tool should do — not how it should do it.

A specification answers four questions:
1. What problem does this tool solve?
2. What goes in? What comes out?
3. What rules must always hold?
4. How will I know if it's working?

---

### Slide 6 — Anatomy of a Good Specification
Five components shown as cards:

| # | Component | Answers |
|---|-----------|---------|
| 1 | **Goal** | One sentence: what problem does this solve? |
| 2 | **Inputs/Outputs** | What data, files, or parameters does it accept? What does it produce? In what format? |
| 3 | **Constraints** | What rules must always be true? |
| 4 | **Acceptance Criteria** | How do you test it? |

---

### Slide 7 — Vague Request vs. Strong Specification
Side-by-side comparison:

| Vague Request | Strong Specification |
|--------------|---------------------|
| "Make a chart of my survey data" | "Read survey_data.csv; for each Likert question, generate a horizontal bar chart (% per response); export as PNG at 300 DPI named by question ID" |
| "Process my interview transcripts" | "Read all .txt files in /transcripts/; extract sentences containing keywords from keywords.txt; output matches.csv with columns: filename, line_number, sentence" |

---

### Slide 8 — The Spec-Driven Workflow
Five-step loop:

**Specify → Direct → Test → Evaluate → Refine**

1. **Specify** — Write a complete, precise specification
2. **Direct** — Hand the spec to your coding agent
3. **Test** — Run the tool on sample data
4. **Evaluate** — Check against acceptance criteria
5. **Refine** — Update the spec based on findings

*↺ Repeat until criteria are met*

---

### Slide 9 — Directing an Agentic Coding Tool
Two-column layout:

**What to Include:**
- Your full specification 
- The language/environment you're using
- A sample of your input data
- What "done" looks like (acceptance criteria)
- Any constraints (libraries, output format)

**What NOT to Do:**
- Don't describe the implementation (unless it's critical to do so!)
- Don't ask for multiple tools at once
- Don't skip the acceptance criteria
- Don't accept output without testing
- Don't re-prompt without updating the spec

---

### Slide 10 — What Agents Need From You
Three cards:

1. **Clarity of Intent** — What is this tool for? Who uses it? What decision does it enable?
2. **Concrete Examples** — Show a sample input and the expected output. A picture is worth a thousand vague words.
3. **Testable Criteria** — How will we both know when it's right? Describe the tests, not just the goal.

---

### Slide 11 — [SECTION DIVIDER: Example Cases]
*See the workflow in action*

---

### Slides 12–15 — CASE STUDY 1: Medical Scheduling Agent

**Slide 12 — Case 1: Introduction**
- **Client:** SOS Care Now — Chicago home healthcare
- **Problem:** Coordinators matched patients to providers manually — slow and error-prone
- **The Tool:** LangGraph agent + Streamlit — matches patients to providers by availability and travel time
- **Integrations:** Google Calendar · Google Maps · Gmail · HuggingFace Spaces

**Slide 13 — Case 1: The Specification**
- **Goal:** Scaffold a template repo — correct structure, signatures, docstrings, TODOs
- **Inputs → Outputs:** Business rules + provider data → 20+ files, 3 API integrations
- **Key constraint:** "Avoid hardcoding Chicago-specific values outside config.py" — one sentence, shaped the entire architecture
- **Acceptance Criteria:** 10-item checklist — binary, testable, runnable

**Slide 14 — Case 1: Demo / Walkthrough**
1. Open the build instruction (1,000+ words — all 5 spec components explicit)
2. Paste into Claude Code — agent scaffolds 20+ files in one session
3. Run the Final Checklist — every Python file parses; imports resolve; no placeholders remain
4. Show agent/graph.py and data_manager.py — correct signatures, TODOs in place

**Slide 15 — Case 1: Lessons Learned**
- **One constraint, one architecture** — "Avoid hardcoding" shaped the whole design and made a Florida fork trivial to set up
- **The spec served three audiences** — directed the agent, onboarded the student, documented for the client
- **What the first iteration missed** — provider emails blank in seed data; spec needed an explicit edit workflow

---

### Slides 16–19 — Digital Nashville

**Slide 16 — Case 2: Introduction**

**Slide 17-18 — Case 2: The Specification**

**Slide 19 — Case 2: Lessons Learned**
- What worked well?
- What did the spec miss?
- Key takeaway to generalize for the audience

---

### Slide 22 — [SECTION DIVIDER: Testing & Evaluation]

---

### Slide 23 — Test-Driven Development with Agents
**Key Insight:** Write your tests *before* asking the agent to build the tool.

Why this works:
- Clarifies your own thinking before you start
- Gives the agent clear, measurable success criteria
- Makes evaluation mechanical, not subjective
- **You write test descriptions — the agent writes both the tool AND the tests**

---

### Slide 24 — Three Levels of Tests

| Level | Name | Question | Example |
|-------|------|----------|---------|
| 1 | Smoke Test | Does it run without crashing? | "Run the script on the sample file. It should complete without errors." |
| 2 | Correctness Test | Does it produce the right output for known inputs? | "Given survey_sample.csv with 10 rows, output should have exactly 10 bars." |
| 3 | Edge Case Test | Does it handle missing data, empty files, bad inputs? | "If the keywords file is empty, script should exit with a clear error message." |

---

### Slide 25 — Evaluating Agent Output
Two-column layout:

**Four Questions to Ask:**
- Does the output match the specification?
- Does it pass all acceptance criteria?
- Is it readable and maintainable?
- Does it handle edge cases?

**Red Flags:**
- Output that "looks right" but was never tested
- Agent added features you didn't ask for
- Acceptance criteria never checked
- Works on sample data but fails on real data
- You can't explain what it does

---

### Slide 26 — When the Agent Gets It Wrong: Update the Spec
- Don't just re-prompt — that rarely helps
- Instead, ask: what was ambiguous or missing in my spec?

Four steps:
1. **Identify the gap** — was the spec unclear? Missing a constraint?
2. **Add a concrete example** — examples fix most spec failures
3. **Strengthen acceptance criteria** — make the test more specific
4. **Re-direct** with the updated spec

> **Rule: Every failed output is feedback on your specification.**

---

### Slide 27 — Common Pitfalls
- Writing specs that describe implementation, not behavior
- Skipping acceptance criteria entirely
- Asking for too much in one specification
- Accepting output without testing
- Not updating the spec when requirements change
- Assuming the agent knows your domain — be explicit

---

### Slide 28 — Key Takeaways
1. **Specification writing is the core skill** — not coding
2. **The loop never ends** — Specify → Direct → Test → Refine
3. **Tests before tools** — write acceptance criteria first
4. **Quality = specification quality** — garbage in, garbage out
5. **You are the domain expert** — agents are your implementation team

---

### Slide 29 — Resources & Next Steps
- Course 4: Agentic Solution Development and Deployment [link]
- Specification template — handout available today
- Example specifications from today's cases [link]

**Practice assignment:**
- Write a spec for a tool you actually need
- Pick something small — a 30-minute task, not a 3-month project
- Test it before polishing it
- When you get stuck: the spec is usually missing a constraint or example

---

### Slide 30 — Q&A / Open Discussion
Discussion prompts:

- What's the hardest part of writing a clear specification?
- Where in your research workflow would this help most?
- What tool would you build if you could build anything?

---

## Appendix: Specification Template (Handout)

```
## Tool Specification: [Name]

### Goal
[One sentence: what problem does this solve?]

### Inputs
- [Input 1: type, format, example]
- [Input 2: type, format, example]

### Outputs
- [Output 1: type, format, example]

### Constraints
- [Rule that must always hold]
- [Rule that must always hold]

### Acceptance Criteria
- [ ] Given [X input], output should be [Y]
- [ ] Given [edge case input], behavior should be [Z]
- [ ] Script should handle [error condition] by [behavior]

### Examples
Input:  [example]
Expected Output:  [example]
```
