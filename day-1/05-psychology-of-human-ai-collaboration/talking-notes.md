# Talking Notes: Critical Thinking with AI Agents in Academia
**30-minute lecture — Jesse Spencer-Smith, Ph.D.**

---

## Slide 1 — Title Slide
*No spoken content. Use as audience settles.*

---

## Slide 2 — What Changed Since December 2025 (0–4 min)

**Opening framing (90 seconds):**

"Since roughly December 2025, we've crossed a threshold. The tools many of you have been using — ChatGPT, Claude, Gemini — those were *chat assistants*. You typed a question, you got an answer. The new generation is fundamentally different. These are *agents* — software that plans a multi-step workflow, executes it across your files and tools and apps, and produces artifacts directly. Not a response in a chat window. Actual files, actual edits, actual outputs."

**Concrete examples (90 seconds):**

Walk through the four cards on screen. For each, give one sentence of color:

- **Literature synthesis**: "An agent can read 30 PDFs in a folder, extract claims, cross-reference them, and produce an annotated bibliography — with an audit trail of what it read and what it concluded."
- **Qualitative coding**: "For those of you doing qualitative research, agents can tag excerpts, extract themes, and generate codebooks — but the provenance question is: can you trace *why* it coded something a particular way?"
- **Grant / IRB assembly**: "Multi-step document construction. You give it structured inputs — your aims, your methods section, your timeline — and it assembles a draft. The risk is accepting that draft without checking cross-references."
- **Lab operations**: "Organizing datasets, building reproducibility checklists, generating methods drafts. The mundane infrastructure of research that eats enormous time."

**Key point to land:** "The tool that changed this for non-coders is Cowork — Anthropic's desktop agent. It explicitly frames itself as 'knowledge work beyond coding.' You authorize a folder, and the agent works inside it. We'll come back to the details."

---

## Slide 3 — The Failure Pattern (4–9 min)

**Transition (30 seconds):**

"So the capabilities are real. But here's the problem: the *failure pattern* is the same one we've always had with AI — it's just that the object of trust has gotten bigger."

**Chat vs. Agent era (60 seconds):**

Point to the two comparison cards. "In the chat era, the failure was: 'I believed a plausible paragraph.' You'd get a confident, well-written answer, and you'd accept it because it *sounded* right. In the agent era, the failure is: 'I accepted a plausible workflow outcome' — a report, a folder of organized files, a spreadsheet, an annotated bibliography. It *looks* finished. It *looks* professional. And that's exactly when your guard drops."

**Two mechanisms (2–3 minutes):**

"Two cognitive mechanisms from the psychology literature explain why this keeps happening."

- **Automation bias**: "This is well-documented in aviation, medicine, and now AI. When a system produces output that looks authoritative, humans default to accepting it. The more polished the output, the stronger the bias. And agents produce *very* polished output — because that's what they're optimized for."

- **Attention limits**: "Here's the subtler problem. Agents dramatically increase your throughput. You can produce ten annotated bibliographies in the time it used to take to produce one. But your capacity to *review* hasn't increased. So you start sampling. You check one or two artifacts. You skim the rest. And that's where errors hide."

"The combination is toxic: more output, less scrutiny, higher confidence."

---

## Slide 4 — Cowork: The Academic Agent Model (9–13 min)

**Setup (30 seconds):**

"Let me make this concrete with the system I'll be demoing later. Claude Cowork is the canonical example of a 'desktop agent for academics.'"

**Three operating principles (2–3 minutes):**

Walk through each card:

- **Folder-scoped access**: "You don't give it access to your whole computer. You authorize a specific folder. It can read, create, and edit files inside that boundary. This is important — it means the *scope of potential damage* is bounded."

- **Multi-step execution**: "This isn't Q&A. You give it a task like 'organize these 40 PDFs by methodology and create a summary table,' and it plans a sequence of steps, executes them, and produces outputs. It might take several minutes. It's doing *work*, not answering a question."

- **Runs, not responses**: "This is the key mental model shift. Your unit of oversight is not 'did I get a good answer?' It's 'did this *run* produce trustworthy artifacts?' A run has inputs, steps, outputs, and logs. You need to review all of those."

**Landing the implication:** "This means faculty need to shift from reviewing answers to reviewing runs. That's a different skill, and it's the skill we're going to build in the next fifteen minutes."

---

## Slide 5 — Agent Skills: Reusable Packaged Expertise (13–18 min)

**Definition (60 seconds):**

"Before we get to the verification framework, I need to define a term precisely, because it has a specific technical meaning. *Agent Skills* — capital S — are reusable packaged procedures. Think of them as folders containing instructions, scripts, and resources that an agent can discover and use to perform tasks repeatably. Write once, use everywhere."

**Why faculty should care (2 minutes):**

"Skills are how we *institutionalize good practice*. Instead of hoping every faculty member remembers to check citations, you build an 'Evidence Map Builder' skill that automatically maps every claim to its source. Instead of hoping students anchor their critiques to evidence, you build a 'Rubric Feedback with Quote Anchors' skill."

Walk through the four examples on the left column.

**The risk (1 minute):**

"But here's the flip side — and this is in the right column. Skills also *concentrate risk*. A flawed skill becomes a scalable failure mode. If your Citation Checker skill has a systematic blind spot — say, it doesn't catch paraphrased claims that lack attribution — then everyone using that skill repeats the same mistake, faster."

"That's why the governance column matters: versioning, peer review, allowlisting. Treat skills like software, because they *are* software."

---

## Slide 6 — The 3 Gates + Traces (18–20 min)

**Setup (30 seconds):**

"Okay, here's the core framework. I want you to remember three words: Provenance, Verifiability, Validity. These are the three gates every agent-produced artifact has to pass before you trust it."

**Walk through each gate (2 minutes):**

- **Gate 1 — Provenance & Trace**: "Can you see what happened? Do you have a step log — what it read, what it changed, what tools it used? If the answer is no, treat the output as draft-only. This is the minimum bar."

- **Gate 2 — Verifiability**: "Can you check the output with domain-appropriate methods? For a literature synthesis, that means every claim links to a source excerpt and page. For data extraction, that means spot-checking samples and verifying totals. For rubric feedback, that means every critique is anchored to a quotation from the student's work."

- **Gate 3 — Epistemic Validity**: "What is the output actually *entitled* to claim? Force the output to distinguish: quoted, summarized, inferred, speculated. Require an 'assumptions and uncertainty' section for any research claim."

"Notice the gates escalate in difficulty. Gate 1 is mechanical — you just need a log. Gate 2 requires domain expertise. Gate 3 requires judgment. That's intentional."

---

## Slide 7 — Gate 2 in Practice (20–23 min)

**Concrete examples (2–3 minutes):**

Walk through the table row by row. For each, spend 20–30 seconds on what the check actually looks like in practice:

- **Literature synthesis**: "Open two or three claims at random. Does the cited source actually say what the synthesis claims it says? Is the page number correct? If two out of three fail, stop trusting the whole thing."

- **Data extraction**: "If the agent extracted a table from a set of PDFs, pick five random cells. Check them against the source. Are the totals consistent? Does the schema match what you expected?"

- **Rubric feedback**: "If the agent wrote feedback on a student paper, is each critique anchored to a specific quote from the student's text? Or is it making general claims that could apply to any paper?"

- **Grant assembly**: "Are all required sections present? Do internal cross-references point to the right sections? Does the budget narrative match the budget table?"

- **Methods draft**: "Could someone reproduce the procedure from what's written? Are the parameter values actually the ones in the source data, or did the agent hallucinate plausible numbers?"

**Landing:** "The principle at the bottom matters: verification must be proportional to the stakes. A rough literature scan for your own use? Gate 1 might suffice. A methods section going into a published paper? All three gates, rigorously."

---

## Slide 8 — Stop Rules (23–26 min)

**Setup (30 seconds):**

"Sometimes the right answer is to stop the agent entirely. These are your 'kill the run' triggers."

**Walk through each rule (2–3 minutes):**

Spend 20–30 seconds on each:

- **No trace / no provenance**: "If you can't see what happened, you can't audit it. Full stop. This is non-negotiable."

- **Evidence mapping fails**: "You try to trace a claim back to a source and you can't. Maybe the source doesn't exist. Maybe the source says something different. Either way, the output is unverifiable."

- **High variance across reruns**: "Run the same task twice with the same inputs. If the summaries change materially — not just wording, but substance — the output is unstable. You can't trust an unstable output."

- **Permission escalation**: "The agent asks for access to more files, more tools, more scope than the task requires. This is the digital equivalent of someone asking for your whole filing cabinet when they only need one folder."

- **Task drift**: "This is the sneaky one. The agent starts optimizing for *polish* rather than *correctness*. Or it starts pursuing a subtly different goal than the one you set. Common in long runs. You have to check periodically that the agent is still solving *your* problem."

---

## Slide 9 — Faculty Workflow Pattern (26–28 min)

**Walk through the five steps (2 minutes):**

"Here's the pattern that works in practice. Five steps."

1. **Constrain**: "Before you start, define the boundary. What folder? What sources? What tools is the agent allowed to use? Tighter constraints produce more auditable outputs."

2. **Run**: "Let the agent do its work. It produces artifacts and a log."

3. **Gate-check**: "Apply the three gates. Provenance, verifiability, validity. This is where most people skip — and where most failures happen."

4. **Decide**: "Three options: accept the output, revise it with another run, or stop and switch methods entirely. 'Stop' is a valid and underused option."

5. **Teach**: "This is the pedagogical step. If you're having students use agents, require them to submit traces and evidence maps alongside their deliverables. This builds the critical evaluation habit from the start."

**Emphasize the bottom callout:** "That last point is worth repeating. If students submit agent-assisted work without traces and evidence maps, you have no way to evaluate what they actually *did* versus what the agent did."

---

## Slide 10 — Why Now: Research Themes (28–29 min)

**Quick tour (60 seconds):**

"Just to give you the 'why now' context — four things converged since December 2025."

- **Desktop agents for non-coders**: "Cowork is the example we've been discussing, but this is a broader trend. Agents that operate on your desktop, in your files, with permission prompts."

- **MCP (Model Context Protocol)**: "This is a standardization effort for how agents interact with tools. The key feature for us: tool invocations are supposed to be visible to humans, and humans can deny them. Exactly the oversight posture we need."

- **Open standards**: "The Agentic AI Foundation is working on cross-platform interoperability. This means the skills you build for one agent may work across others."

- **Multi-dimensional evaluation**: "The research community is catching up. Princeton's HAL harness, for example, evaluates agents not just on accuracy but on reliability, safety, robustness, and traceability. These are the dimensions that matter for academic use."

---

## Slide 11 — Closing Slide (29–30 min)

**Closing statement (60 seconds):**

"One takeaway. Agents amplify both your capability and your blind spots. The 3 Gates — Provenance, Verifiability, Validity — are your defense."

"The workflow pattern: Constrain, Run, Gate-Check, Decide, Teach."

"If you remember nothing else from this session, remember this: the failure mode has shifted from 'I believed a plausible paragraph' to 'I accepted a plausible workflow outcome.' The second failure is harder to detect and more consequential. The gates are how you catch it."

*Pause. Take questions if time allows.*

---

## Backup Notes: Handling Common Audience Questions

**Q: "Isn't this just adding more work?"**
A: "In the short term, yes. But consider the alternative: unverified agent outputs in published papers, student work, and grant applications. The reputational and scholarly cost of a retraction or error is much higher than the cost of a gate-check."

**Q: "How do I know if students are actually checking their traces?"**
A: "Require the trace as a submission artifact. Spot-check them the same way you'd spot-check citations. Over time, you develop a sense for traces that look real versus traces that were generated after the fact."

**Q: "What about agents that don't produce traces?"**
A: "That's a Gate 1 failure. If the tool doesn't give you a trace, you can't audit the output. Either use a different tool or treat the output as unverified draft material."

**Q: "Can I use this framework for my own research, not just student work?"**
A: "Absolutely. The gates apply to any agent-produced artifact. The higher the stakes — journal submission, grant application, policy recommendation — the more rigorously you should apply all three gates."
