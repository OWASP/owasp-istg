# Contributing to the OWASP IoT Security Testing Guide

Thanks for contributing. This file is the **operational checklist** — the conventions that are easy to miss and that reviewers will otherwise raise on your pull request. For the *structural* model behind the catalog (hierarchy, identifiers, inheritance, access levels), see [2.3. Testing Methodology](./src/02_framework/methodology.md) and [2.2. Attacker Model](./src/02_framework/attacker_model.md).

General project information and other ways to get involved are on the [OWASP project page](https://owasp.org/www-project-iot-security-testing-guide/#div-contributing).

## Before you start

For anything larger than a typo, **open an issue first**. New test cases and new component specializations benefit a lot from agreeing on scope, category mapping, and identifiers before the writing starts — it is much cheaper to move a test case between categories in an issue thread than in a finished document.

If an issue already exists for the work you want to do, comment on it so it can be assigned to you.

## Never hand-edit the checklists

`checklists/checklist.md` and `checklists/checklist.xlsx` are **generated**. The [`Create checklists`](.github/workflows/create-checklists.yml) workflow runs `scripts/create_checklists.py` on every push to `main` that touches `src/03_test_cases/**.md`, then commits the result as `Update checklists`.

**Your pull request should contain no changes under `checklists/`.** Editing them by hand causes avoidable merge conflicts — `checklist.xlsx` in particular is a binary file that cannot be merged, so a hand-edited copy will block your PR until it is removed.

Your test cases are picked up automatically as long as their headings carry a parseable identifier (see [Required sections](#required-sections)). You can confirm this locally — see [Verifying your change locally](#verifying-your-change-locally).

## Section numbering for specializations

Specialization section numbers (`3.5.1.`, `3.5.2.`, …) are assigned **append-on-merge**: a specialization takes the next free number *at the time it merges*, and keeps it. Numbers are never reserved in advance, and already-merged sections are never renumbered to make room.

This is deliberate. The `3.5.x` number is a **document position**, not an identifier — the stable identifier is the `ISTG-INT[XXX]` tag, which is what test reports and checklists reference. Reserving slots for pull requests that may stall, or renumbering merged sections whenever a new protocol lands, both create more churn than they prevent.

Practically, this means:

- Set your section number in the same pass that resolves your final rebase, just before merge. If another specialization merges while yours is in review, expect to bump it.
- Don't renumber anyone else's section in your PR.
- Because order ends up merge-chronological rather than alphabetical, specializations will be renumbered into alphabetical order **once, at the next major (`v2.0.0`) release**. No test case identifiers change when that happens.

## Writing a test case

Match the surrounding files. The catalog is deliberately lean and consistent: a reader should be able to move between components without re-learning the format.

### Required sections

Each test case is a `###` heading whose text ends with its identifier in parentheses, followed by **Required Access Levels** (an HTML table), **Summary**, **Test Objectives**, **Remediation**, and **References**, in that order. Copy the exact structure from a neighbouring test case rather than retyping it — [`inter_integrated_circuit.md`](./src/03_test_cases/internal_interfaces/inter_integrated_circuit.md) is a good model.

The identifier in the heading is what the checklist generator parses, so it must be present and well-formed. Its format is defined in [methodology.md](./src/02_framework/methodology.md#structure-of-the-catalog-of-test-cases): `ISTG-<COMPONENT>[<SPECIALIZATION>]-<CATEGORY>-<NNN>`, with a three-digit incremental number. Numbers within a category are sequential with no gaps — if you cross-reference a test case, make sure it exists.

### Access levels

Both values come from the [Attacker Model](./src/02_framework/attacker_model.md). The distinction that most often needs correcting:

**The authorization level is the tester's *starting* privilege, not the privilege the test targets.** The framework deliberately does not define a minimum authorization level, because determining whether lower-than-intended access works *is the test*. So a test case for unauthorized access to an interface baselines at **`AA-1`** (anonymous). Writing `AA-1 – AA-4` for such a test is backwards: a tester who already holds `AA-4` manufacturer-level access has no unauthorized access left to demonstrate. If the test case also covers authenticated variants of the mechanism, describe that in the Summary or Test Objectives, not in the access-level table.

For physical access, `PA-4` alone asserts the interface is *always* behind the enclosure. Many debug headers, pads, and test points are reachable without disassembly, which is `PA-3`. Use a range (`PA-3` - `PA-4`) with a short parenthetical explaining what the range depends on, as the existing internal interface specializations do.

### Naming tools

Test objectives may name specific tools where doing so makes the check actionable — this follows established practice in the OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/) and [MASTG](https://mas.owasp.org/MASTG/). Because the guide is vendor-neutral, three rules apply:

- **Never name a commercial tool on its own.** If a paid product is mentioned, at least one open-source or freely available option with comparable capability must appear in the same test objective. The point is to describe the capability a tester needs, then illustrate it — not to route the reader to one vendor.
- **Link documentation, not storefronts.** Prefer a project repository, datasheet, or documentation page over a product landing or purchase page.
- **Do not rank or endorse.** Listing tools as examples is fine; asserting that one is best is not. Keep the phrasing illustrative (`e.g.`, `such as`).

Where a generic term carries the meaning perfectly well — "a logic analyzer", "a serial terminal", "an oscilloscope" — use it, and let the reference section name concrete options.

### Remediation

**One or two sentences, at the level of principle.** As [methodology.md](./src/02_framework/methodology.md#structure-of-test-cases) puts it, these recommendations "are only rough suggestions" — deriving detailed measures for a specific device is the manufacturer's responsibility.

Naming the dominant control inline is welcome where it earns its place (for example readout protection or debug locking such as STM32 RDP Level 2, or an ESP32 eFuse JTAG disable). Configuration walkthroughs, flag-by-flag build guidance, and multi-paragraph hardening advice are not — put a reference to the authoritative guide instead. Every remediation in the catalog today is one or two lines; please keep yours that way.

### References

**Cite only sources that are specific to that test case** — the tools it names, the CVEs or CWEs it describes, and directly relevant research. Do not add a general reading list; a reference section that lists everything tells the reader nothing about what is load-bearing.

Judge a candidate reference by what it *does* for the reader, not by whether the catalog already cites it:

- **Cite it** if it identifies the weakness (a CVE or CWE record), or if it is the authoritative source for detail the test case deliberately does not spell out — for example the hardening guide behind a one-line remediation.
- **Do not cite compliance frameworks** — ETSI EN 303 645, NIST SP 800-213, IEC 62443, the EU CRA, and similar. These assert a requirement rather than describing the defect or the fix, and requirement-to-test mapping cannot be kept consistent when it is scattered across individual test cases. That mapping belongs in a dedicated compliance layer. The one deliberate exception is ISVS, below, because it is the requirements standard this guide is paired with.
- Every reference must have a resolvable URL. A source a reader cannot verify does not belong in a reference list.

Where a test case directly evidences an [OWASP IoT Security Verification Standard](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) requirement, cite it so testers can produce requirement-to-test traceability without re-deriving the mapping. **Give the requirement ID and a short gloss in your own words — do not quote the requirement text verbatim:**

```markdown
- OWASP [IoT Security Verification Standard (ISVS)](https://owasp.org/IoT-Security-Verification-Standard-ISVS/) — Related requirements: V5.1.1 (platform supports disabling or protecting access to debug interfaces such as JTAG, SWD and UART)
```

The ID is the stable contract; the wording is editorial and gets revised. Copying it here creates a second copy that nothing keeps in sync, and a stale quote is worse than no quote because it looks authoritative. Link to ISVS for the wording.

**New test case files should include ISVS cross-references from the outset.** Only cite a requirement where passing or failing the test case is direct evidence for it — a topical resemblance is not enough.

Verify every CVE against the [NVD](https://nvd.nist.gov) before citing it, and make sure your description and severity match the record. Link to the NVD entry rather than to a vendor bulletin where both exist, and describe the *defect*, not the bulletin. Prefer link reference definitions collected at the end of the file, as the existing files do, and strip tracking or session query strings from URLs.

## Table of contents formatting

Each test case file opens with a `## Table of Contents`. Two things are easy to get wrong:

- **Escape the square brackets in the link text** — `ISTG-INT\[I2C\]-AUTHZ-001`. Unescaped brackets break rendering.
- **Do not escape them in the anchor**, and do not drop the `istg-` prefix. The anchor is the heading slugified: lowercased, punctuation removed, spaces to hyphens. `### Slave Enumeration (ISTG-INT[I2C]-INFO-001)` becomes `#slave-enumeration-istg-inti2c-info-001`.

Use `-` bullets indented with tabs:

```markdown
- [Information Gathering (ISTG-INT\[I2C\]-INFO)](#information-gathering-istg-inti2c-info)
	- [Slave Enumeration (ISTG-INT\[I2C\]-INFO-001)](#slave-enumeration-istg-inti2c-info-001)
```

## Adding a component specialization

A specialization inherits all of its parent's categories and test cases by default, and adds only what is specific to the technology. If a parent category genuinely does not apply, list it explicitly as not inherited, with a one-line rationale and a link to the parent category — see the existing internal interface specializations for the pattern. Excluding a category because "another test case covers it" only works if that test case actually exists.

Files to touch:

| File | Change |
|-|-|
| `src/03_test_cases/<component>/<specialization_name>.md` | The new specialization. Use the spelled-out protocol name in `snake_case`. |
| `src/03_test_cases/<component>/README.md` | Name the specialization in the component Overview, and link it. |
| `src/03_test_cases/README.md` | Add the numbered catalog entry. |
| `src/SUMMARY.md` | Add the nested navigation entry. |
| `acknowledgements.md` | Add yourself if you'd like. |

Do **not** touch `checklists/` or the root `README.md`.

## Verifying your change locally

```sh
# Build the book. `create-missing = false`, so a SUMMARY.md entry
# pointing at a file that does not exist is a build failure.
./scripts/mdbook_prepare.sh && mdbook build && ./scripts/mdbook_cleanup.sh

# Confirm the checklist generator sees your test cases.
# The diff should contain exactly your new IDs and nothing else.
pip install -r scripts/requirements
python3 scripts/create_checklists.py && git diff --stat checklists/
```

Then **revert the checklist changes before committing** (`git checkout -- checklists/`) — that run was only to confirm your identifiers parse. CI regenerates them on merge.

Also check that every anchor in your table of contents resolves in the built HTML, and that new external links return a successful response.

## Pull requests

One logical change per pull request, referencing the issue it addresses (`Closes #NN`). Pull requests are squash-merged, so branch history need not be tidy, but the final title becomes the commit message on `main`. Review looks at accuracy first — identifiers, access levels, CVE claims — and consistency second.

If a reviewer asks for a change you disagree with, say so. These conventions exist to keep the guide usable, not to win arguments.
