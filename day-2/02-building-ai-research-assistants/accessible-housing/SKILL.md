---
name: accessible-housing
description: >
  Researches and catalogs accessible housing solutions for adults with
  disabilities in a specified US geographic area, then outputs a structured
  spreadsheet of all options found. Use when user asks for housing options,
  disability housing research, accessible housing report, or invokes
  /accessible-housing with a location. Handles group homes, supported living,
  independent housing, assisted living, and all disability types.
argument-hint: "[location]"
allowed-tools: Read, Grep, WebSearch, WebFetch, Bash, Write
metadata:
  author: Umang Chaudhry, Anikait Rawat
  version: "1.1"
---

# Accessible Housing Solutions

## Purpose

Use this skill when the user:

- Invokes `/accessible-housing <location>` to generate a housing options report
- Asks for a spreadsheet, report, or list of housing options in a specific area
- Asks to verify, update, or refresh an existing housing report
- Needs help understanding housing terminology, funding sources, or how to navigate the system

The first target location is **Nashville, Tennessee (Davidson County)**.

## Instructions

### 1. Parse the Location

- Extract the geographic area from `$ARGUMENTS`
- If no location is provided, default to **Nashville, Tennessee (Davidson County)**
- If ambiguous, ask the user to specify a state, county, city, or region
- Confirm the search area with the user before beginning research

### 2. Research Process

Conduct research using these sources in priority order. For Nashville, Tennessee-specific sources are noted. When researching other states, consult `references/national-search-terms.md` for the state-specific equivalents of each program type.

#### Government & State Agency Sources

1. **State DD Agency** (TN: DIDD) — provider directories, waiver program listings
2. **State Medicaid Program** (TN: TennCare) — HCBS waiver provider lists, managed LTSS providers
3. **State Housing Finance Agency** (TN: THDA) — affordable housing databases, LIHTC property lists
4. **Local Public Housing Authority** (Nashville: MDHA) — public housing, Section 8 vouchers
5. **HUD housing databases** — Section 811, Section 202, affordable housing locators
6. **State Mental Health Authority** (TN: TDMHSAS) — supportive housing programs
7. **State Department of Health** — licensed residential facility lists

#### National Government & Program Sources

8. Medicaid HCBS Waivers — 1915(c), 1915(i), 1915(k), 1115 Demonstration
9. Section 8 / Housing Choice Voucher Program
10. HUD Section 811 Supportive Housing for Persons with Disabilities
11. HUD Section 202 Supportive Housing for the Elderly
12. Low-Income Housing Tax Credit (LIHTC)
13. HOME Investment Partnerships Program
14. Money Follows the Person (MFP)
15. State Olmstead Plan initiatives
16. PACE, National Housing Trust Fund, Continuum of Care, ICF/IID

#### Nonprofit & Advocacy Sources

17. **The Arc** (local chapter) — may operate housing programs
18. **Best Buddies** — inclusive independent living programs
19. **Easterseals, L'Arche, Habitat for Humanity** (local affiliates)
20. **State Council on Developmental Disabilities**
21. Local inclusive housing initiatives

Mark organizations that are research/navigation sources only (not housing providers) — see Inclusion/Exclusion Criteria below.

#### Private & Specialized Housing

22. Accessible apartment locator services
23. Senior living directories with accessibility filters
24. Specialized disability housing developers in the local market
25. Real estate listings with accessibility filters

#### Additional Resources

26. Local paratransit services (Nashville: WeGo Access)
27. 211 / United Way
28. State UCEDD (Nashville: Vanderbilt Kennedy Center) *(research source only)*

### 3. State-Specific Context

When researching a location, always include context on the state's key programs. For Tennessee:

- **ECF CHOICES** — Employment and Community First CHOICES, Tennessee's HCBS waiver for I/DD. Three benefit groups with different support levels.
- **CHOICES** — Tennessee's managed LTSS program for seniors and adults with physical disabilities.
- **TennCare** — Tennessee Medicaid, administered through MCOs: BlueCare, Amerigroup, UnitedHealthcare Community Plan.
- **DIDD** — Tennessee Department of Intellectual and Developmental Disabilities.
- **THDA** — Tennessee Housing Development Agency (Housing Choice Voucher, HOME funds, LIHTC).
- **MDHA** — Metropolitan Development and Housing Agency, Nashville's local PHA.

### 4. Apply Taxonomies

Before populating any records, read `references/taxonomies.md` for all canonical taxonomy values. Use exact terms — no synonyms, no invented categories. Every taxonomy includes a plain-language definition for use in user-facing output.

### 5. Populate the Data Schema and Output

Every housing listing must capture the fields defined below. Fields marked ✅ are required; ⬚ are captured when available.

**Core Identity:** `provider_name` ✅, `address` ✅, `city` ✅, `state` ✅, `zip` ✅, `county` ✅, `latitude` ⬚, `longitude` ⬚, `phone` ✅, `email` ⬚, `website` ⬚

**Housing Classification:** `housing_control_model` ✅, `availability_status` ✅, `support_levels` ✅, `program_model` ✅, `development_type` ✅, `residential_unit_type` ✅, `housemate_status` ⬚

**Population & Eligibility:** `target_population` ✅, `disability_types_served` ✅, `age_range` ⬚, `gender_policy` ⬚, `income_requirements` ⬚

**Funding & Payment:** `funding_accepted` ✅, `payment_model` ✅, `rent_cost_range` ⬚

**Features & Amenities:** `physical_amenities` ⬚, `supportive_amenities` ⬚, `lifestyle_features` ⬚, `mobility_accessibility` ⬚, `sensory_accessibility` ⬚, `cognitive_accessibility` ⬚

**Capacity & Services:** `capacity` ⬚, `bedrooms` ⬚, `bathrooms` ⬚, `services_included` ⬚, `pet_friendly` ⬚, `smoking_policy` ⬚, `paratransit_access` ⬚

**Data Integrity:** `last_verified` ✅, `data_source` ✅, `data_confidence` ✅ (high/medium/low/unverified), `license_number` ⬚, `application_process` ⬚, `notes` ⬚

For detailed accessibility verification beyond high-level tags, consult the checklists in `references/taxonomies.md` (Mobility, Sensory, and Cognitive Accessibility sections).

### 6. Format the Output

Output a structured table with 35 columns in this order: Provider Name, Housing Control Model, Development Type, Residential Unit Type, Program Model, Support Levels, Target Population, Disability Types Served, Address, City, State, ZIP Code, County, Funding Accepted, Payment Model, Rent/Cost Range, Availability Status, Physical Amenities, Supportive Amenities, Lifestyle, Mobility Accessibility, Sensory Accessibility, Cognitive Accessibility, Capacity, Housemates, Pet Friendly, Paratransit Access, Phone, Email, Website, Application Process, Last Verified, Data Confidence, Data Source, Notes.

**Sort order:** Development Type → Support Levels → Provider Name

**Summary header row:** Total properties found, breakdown by development type, breakdown by support level, date of research, geographic area.

**Target:** Minimum 20–30 options per location when available. Include all housing types, support levels, and funding models present in the area.

**Export formats:** CSV and Excel (.xlsx) when possible. Present a markdown preview of the first 10 rows to the user before delivering the full file.

**File naming:** `housing-data-{ST}-{city}-{YYYY-MM-DD}.csv` / `.xlsx`

## Inclusion / Exclusion Criteria

Every row in the housing spreadsheet must represent **an actual place where someone can live.** Use the "Can someone sleep here tonight?" test.

### INCLUDE as a housing data row

- Residential facilities, group homes, apartments, or other dwellings where people live
- Host homes and shared living arrangements
- Transitional housing programs where a person physically lives during the transition
- Specific affordable housing properties (public housing developments, LIHTC properties, Section 202 buildings)
- Assisted living facilities, ICFs, and nursing facilities

### EXCLUDE from housing data rows (document as research sources instead)

- **Funding programs** (Housing Choice Voucher, Section 811 PRA, ECF CHOICES the waiver itself) — these are *how* housing is paid for, not *where* someone lives
- **Advocacy and legal organizations** (Disability Rights TN, P&A agencies)
- **Navigation and referral resources** (Vanderbilt Kennedy Center, FiftyForward, NAMI, 211)
- **Technology vendors** (SimplyHome) — supports independent living but not a housing provider
- **Model/demonstration homes** (DIDD Enabling Technology Model Home) — no one lives there
- **Closed or decommissioned facilities** — verify status before including any state institution
- **Support coordination agencies that don't operate housing**

## Do This / Not That

| Do This | Not That |
|---|---|
| Use exact taxonomy values from `references/taxonomies.md` | Invent new category names or synonyms |
| Include county in every record | Rely only on city names |
| Store disability types as arrays | Store as a single string |
| Use plain-language definitions in user-facing output | Use jargon without explanation |
| Explain "consumer-controlled" vs "provider-controlled" | Assume users understand the distinction |
| Include state-specific waiver info (e.g., ECF CHOICES in TN) | Give only generic federal program info |
| Store source URLs and retrieval dates | Store data without provenance |
| Show `last_verified` date with every listing | Present data as current with no date |
| Say "contact to confirm availability" | Guarantee openings or waitlist times |
| Mark uncertain data as `data_confidence: low` | Present inferred info as confirmed |
| Search multiple source types (min 3) | Give up after one directory |
| Clearly label integrated vs. disability-specific settings | Use vague terms like "community" |
| Only include actual housing in the spreadsheet | Include programs, advocacy orgs, or navigation resources as rows |
| Verify a facility is still open before including it | Include closed facilities without checking |
| Use the "Can someone sleep here tonight?" test | Assume any disability-related org is a housing provider |

## Common Mistakes

1. **Urban bias.** Davidson County has urban, suburban, and semi-rural areas. Search Antioch, Madison, Hermitage, Bellevue, Joelton — not just downtown.
2. **Conflating housing types.** "Group home," "group living," "assisted living," and "shared living" are legally and practically different. Use exact taxonomy terms.
3. **Missing waiver context.** Many options require enrollment in state waivers. Note which benefit group applies and how to apply.
4. **Stale availability data.** Never guarantee availability. Always include `last_verified` and "contact to confirm."
5. **Ignoring the control model.** Consumer-controlled vs. provider-controlled has huge autonomy implications. Always classify.
6. **Incomplete accessibility data.** Many IDD group homes are not wheelchair accessible. Capture physical accessibility separately from disability type served.
7. **Single-source research.** No single database has complete coverage. Triangulate across state directories, Medicaid lists, housing agency databases, and local nonprofits.
8. **Overlooking emerging models.** Tiny homes, ADUs, remote support, intentional communities — don't limit to traditional models.
9. **Paratransit coverage.** Always check whether a property is within the local paratransit service area.
10. **Ignoring the segregation distinction.** Clearly label integrated (scattered site, mixed-use) vs. disability-specific (planned/intentional community) settings.
11. **Including non-housing entries.** Programs, advocacy orgs, navigation resources, tech vendors, and model homes are NOT housing rows. Use the "Can someone sleep here tonight?" test.
12. **Including closed facilities.** Verify operational status before including. Confirm with the state DD agency.

## Quality Checklist

Run this before finalizing any report:

- [ ] Every record has all ✅ required fields populated
- [ ] All taxonomy values match canonical terms exactly (see `references/taxonomies.md`)
- [ ] `housing_control_model` is classified for every listing
- [ ] `support_levels` documented independently of housing type
- [ ] `data_source` contains a valid URL or source reference
- [ ] `last_verified` set to actual verification date
- [ ] `data_confidence` set honestly
- [ ] County populated for every record
- [ ] State-specific program context included where relevant
- [ ] Plain-language definitions used in all user-facing output
- [ ] Integrated vs. disability-specific settings clearly labeled
- [ ] At least 3 source types consulted
- [ ] Paratransit coverage noted
- [ ] Availability data includes "contact to confirm" notice
- [ ] Accessibility features documented separately from disability type
- [ ] Spreadsheet uses exact column order from the output format section
- [ ] Minimum 20–30 options targeted
- [ ] Every row passes the "Can someone sleep here tonight?" test
- [ ] No closed/decommissioned facilities included without verified current status

## Usage Examples

```
/accessible-housing Nashville, Tennessee
/accessible-housing Davidson County, TN
/accessible-housing Memphis, Tennessee
/accessible-housing Austin, Texas
/accessible-housing King County, Washington
```
