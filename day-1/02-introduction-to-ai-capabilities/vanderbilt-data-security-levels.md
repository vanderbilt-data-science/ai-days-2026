## Vanderbilt Data Security Levels & AI Tools

Vanderbilt classifies all university data into four levels based on sensitivity, legal requirements, and risk. Each level determines what security controls are required and which AI tools are appropriate to use with that data.

### Level 1 — Public

Data intended for public release or distribution. Little to no risk if disclosed.

**Examples of Level 1 data:**

- University news and press releases
- Published educational materials and course catalogs
- Job postings
- Public directory information
- Marketing content and website copy

**AI tools approved for Level 1 data:** All Vanderbilt-provided tools (ChatGPT Edu, Amplify, Microsoft Copilot), plus third-party AI tools following cybersecurity guidance. Claude, Claude Code, Claude Cowork are here as well. 

---

### Level 2 — Internal Use Only

Data that is private to Vanderbilt and should not be shared with non-VU individuals without permission. Disclosure could cause competitive disadvantage or reputational damage.

**Examples of Level 2 data:**

- Internal budgets and financial planning documents
- Non-public contracts and vendor agreements
- Internal policies and standard operating procedures
- Meeting calendars and scheduling information
- Performance data and internal metrics
- Unpublished research (pre-publication)
- Aggregated, de-identified data
- Internal survey results
- Building blueprints and facilities information
- Email distribution lists

**AI tools approved for Level 2 data:** ChatGPT Edu, Amplify, Microsoft Copilot

---

### Level 3 — Restricted

Data that is confidential by law, regulation, or contract, and should not be shared with unauthorized persons. Significant risk with legal implications if disclosed.

**Examples of Level 3 data:**

- Personally Identifiable Information (PII) — names combined with SSNs, dates of birth, etc.
- Student education records protected by FERPA
- Research health information
- Personal data covered by GDPR
- Donor information
- Passwords and access credentials
- Data covered by Non-Disclosure Agreements (NDAs)
- Data governed by Data Use Agreements (DUAs)
- Personnel records and HR information

**AI tools approved for Level 3 data:** Amplify and Microsoft Copilot (excluding regulated datasets such as HIPAA, FERPA, and GLBA data). Majk is also approved at this level.

> **Important:** ChatGPT Edu is **not** approved for Level 3 data. Do not enter restricted information into ChatGPT Edu.

**Required storage:** VUIT-managed systems only (OneDrive, SharePoint, Teams, Azure, Box, AWS).

---

### Level 4 — Critical

The most sensitive data — confidential by law or contract **and** requiring bespoke security controls. Severe risk including potential heavy legal fines.

**Examples of Level 4 data:**

- Payment Card Industry (PCI) data — credit card numbers, cardholder data
- Student financial aid data protected by GLBA
- Controlled Unclassified Information (CUI)
- Export-controlled information (ITAR, EAR)
- Law enforcement records (CJIS)
- Data requiring specialized compliance frameworks

**AI tools approved for Level 4 data:** None of the standard AI tools are approved for Level 4 data without prior consultation with the Office of Cybersecurity. Case-by-case solutions are required.

**Required storage:** Requires direct consultation with Vanderbilt's Office of Cybersecurity for case-by-case security solutions.

---

### Quick Reference

| Data Level | Sensitivity | ChatGPT Edu | Amplify | Copilot | Majk |
|---|---|---|---|---|---|
| Level 1 — Public | None | ✅ | ✅ | ✅ | ✅ |
| Level 2 — Internal | Moderate | ✅ | ✅ | ✅ | ✅ |
| Level 3 — Restricted | High | ❌ | ✅* | ✅* | ✅ |
| Level 4 — Critical | Severe | ❌ | ❌ | ❌ | ❌ |

*\*Excluding regulated datasets (HIPAA, FERPA, GLBA)*

---

### Key Takeaways

1. **When in doubt, classify up.** If you're unsure whether data is Level 2 or Level 3, treat it as Level 3.
2. **Never put restricted or critical data into ChatGPT Edu.** It is approved only for Levels 1 and 2.
3. **Level 4 data requires a conversation with Cybersecurity** before using any AI tool or storage system.
4. **The same data can be classified differently depending on format** — aggregated/de-identified data may be Level 2, while the underlying individual records are Level 3 or 4.
5. **Third-party AI tools** (free or subscription-based) should follow Vanderbilt's cybersecurity guidance and are generally appropriate only for Level 1 data unless specifically vetted.

---

*Sources: [Vanderbilt Office of Cybersecurity — Data Classification Guidance](https://www.vanderbilt.edu/cybersecurity/guidelines/data-classification/) · [VUIT GenAI Tools Compared](https://it.vanderbilt.edu/genai-tools-compared/) · [Vanderbilt Generative AI Tools](https://www.vanderbilt.edu/generative-ai/tools/)*
