# REVIEW CLEAN
# Multi-Persona Review: Evidence Command Center (index.html)
### Date: 2026-04-01
### Summary: 6 P0, 17 P1, 16 P2 (after deduplication)
### Status: 6/6 P0 FIXED, 12/17 P1 FIXED, 0/16 P2 (deferred)

---

## P0 -- Critical

- **[STAT-1]** [FIXED] Statistical Methodologist: Donut chart conic-gradient angles are severely wrong (line ~1017). Contradiction segments total 98.5 deg (27.4%) but should be 176.1 deg (48.9%). Visually under-represents the contradiction rate by nearly half.
  - Suggested fix: Replace with `conic-gradient(#ef4444 0deg 12.3deg, #f97316 12.3deg 165.5deg, #fbbf24 165.5deg 176.1deg, #2a2a45 176.1deg 360deg)`

- **[DOM-1/STAT-2]** [FIXED] Domain Expert + Statistician: ActionableEvidence card says "5,279 scored" but source summary.json says 6,229 total MAs (line ~774). The 1.3% only works with 6,229 denominator. Story section repeats "5,279 assessable" (line ~940). Internal inconsistency.
  - Suggested fix: Change to "6,229 scored" on card and "6,229" in story text. Or if 5,279 is valid, update the 1.3% to 1.5%.

- **[DOM-2]** [FIXED] Domain Expert: "48.9% contradiction" headline used 5+ times without defining "contradiction" (lines ~657, 753, 930). 87% of contradictions are significance flips (power differences), not direction reversals. Overstated for BMJ submission.
  - Suggested fix: Add operational definition on first mention; note majority are significance discordances.

- **[DOM-3]** [FIXED] Domain Expert: "Only 1.3% actionable" framing is misleading — the 6-criteria scoring is bespoke/unvalidated, and many MAs failing these criteria inform clinical guidelines (lines ~682, 939-942).
  - Suggested fix: Reframe as "met all six pre-specified quality criteria" + add caveat about GRADE-informed guidelines.

- **[DOM-4]** [FIXED] Domain Expert: EvidenceOracle displays LogReg AUC 0.871 but RandomForest achieved 0.925. Nature Medicine would ask why the weaker model is highlighted (line ~730).
  - Suggested fix: Add "(logistic regression; random forest: 0.925)" or explain interpretability rationale.

- **[A11Y-3]** [FIXED] Accessibility: Architecture SVG diagram (line ~1187) has no accessible alternative — no role, title, desc, or aria-label. Screen readers get no information about data flow.
  - Suggested fix: Add `role="img"` + `aria-label` describing the data flow between engines.

---

## P1 -- Important

- **[DOM-5]** [FIXED] Domain: "we can predict which evidence will break" — sensationalist for scientific showcase (lines ~950, 1456). AUC 0.871 with 5-fold CV, no external validation.
  - Suggested fix: "predictive signals for evidence instability identified" + note need for external validation.

- **[DOM-6]** Domain: "A credit score for evidence" — implies calibration and predictive validity not yet established. Consistency component = 100.0 for all MAs (degenerate). (lines ~827, 959)
  - Suggested fix: Reframe as "exploratory composite trust metric"; disclose consistency component issue.

- **[DOM-9]** [FIXED] Domain: "The Complete Audit of Medical Evidence" — overstated; 501 reviews is a fraction of 8,000+ Cochrane reviews (line ~652).
  - Suggested fix: "A Systematic Audit of 501 Cochrane Reviews"

- **[DOM-10]** Domain: No confidence intervals on any key metric — AUC 0.871 (SD=0.042), 48.9% contradiction rate, 1.3% actionability (multiple lines).
  - Suggested fix: Report key metrics with uncertainty.

- **[A11Y-1]** [FIXED] Accessibility: Footer text `#4a4a6a` on `#0f0f1a` = 2.25:1 contrast, fails WCAG AA (lines ~534, 1363).
  - Suggested fix: Change to `#8888a8` (5.56:1).

- **[A11Y-6/ENG-8]** [FIXED] Accessibility + Engineering: No `prefers-reduced-motion` support. Particles, counters, fade-ins, cycling headlines, pulsing dots all animate without respecting user preference.
  - Suggested fix: Add CSS media query + JS matchMedia check.

- **[SEC-1]** [FIXED] Security: `document.querySelector(link.getAttribute('href'))` — if nav links were ever dynamic, this becomes CSS selector injection (line ~1593).
  - Suggested fix: Use `document.getElementById(href.slice(1))`.

- **[ENG-1]** Engineering: Particle O(n^2) loop with per-segment canvas state changes (lines ~1421-1435). 1,770 distance checks/frame with unique strokeStyle per line.
  - Suggested fix: Batch lines at uniform alpha or use spatial grid.

- **[ENG-2]** [FIXED] Engineering: Scroll event handler for nav highlight is unthrottled (line ~1597).
  - Suggested fix: Use requestAnimationFrame gating or IntersectionObserver.

- **[ENG-5]** [FIXED] Engineering: Three IntersectionObservers never disconnected after firing (lines ~1515, 1531, 1576).
  - Suggested fix: `observer.disconnect()` after one-shot; `unobserve(target)` for fade-ins.

- **[ENG-6]** Engineering: setInterval for cycling headlines never cleared (line ~1464). DOM writes every 4s indefinitely.
  - Suggested fix: Pause via IntersectionObserver when hero is off-screen.

- **[A11Y-5]** [FIXED] Accessibility: `<nav>` has no `aria-label="Main navigation"` (line ~629).
  - Suggested fix: Add `aria-label`.

- **[A11Y-12]** [FIXED] Accessibility: Hamburger menu doesn't trap focus or close on Escape (line ~1542).
  - Suggested fix: Add Escape handler; manage focus within menu.

- **[A11Y-13]** [FIXED] Accessibility: Publications table has no `<caption>` (line ~1293).
  - Suggested fix: Add `<caption class="sr-only">Publication status for each Evidence Intelligence Suite project</caption>`.

- **[A11Y-15]** [FIXED] Accessibility: No `<main>` landmark wrapping page content.
  - Suggested fix: Wrap content in `<main id="ecc-main">`.

- **[A11Y-16]** [FIXED] Accessibility: Canvas element not marked as decorative for screen readers (line ~647).
  - Suggested fix: Add `aria-hidden="true" role="presentation"`.

- **[DOM-8]** Domain: Nature Medicine target for EvidenceOracle is aspirational — no external validation, no prospective assessment.
  - Suggested fix: Note "pending prospective validation" or adjust target.

---

## P2 -- Minor

- **[STAT-3]** Accuracy 80.6% vs 80.7% rounding ambiguity (line ~1085).
- **[SEC-2]** CSP: Inline style/script blocks prevent strict CSP deployment.
- **[ENG-3]** Resize handler unthrottled (line ~1382).
- **[ENG-4]** visibilitychange can trigger double animation frames (line ~1442).
- **[ENG-9]** PRNG comment says "xoshiro128**" but implementation is Park-Miller LCG (line ~1386).
- **[ENG-10]** Inline style on Tier 2/3 grids duplicates CSS (lines ~720, 815).
- **[ENG-11/A11Y-17]** Redundant `tabindex="0"` on anchor elements in quick launch.
- **[ENG-12/13]** SVG text-transform and letter-spacing attributes have no effect (line ~1279).
- **[ENG-14]** Hardcoded `#0f0f1a` in donut hole/timeline dots — use CSS variable.
- **[ENG-15]** Brand gradient repeated 5 times — use CSS custom property.
- **[DOM-11]** "p-hacking signals" should be "excess significance patterns" (line ~923).
- **[DOM-12]** "quality issues are pervasive" — unquantified editorial claim (line ~923).
- **[DOM-13]** IPD Simulator: "IPD reconstruction" should be "pseudo-IPD reconstruction" (line ~845).
- **[DOM-17]** "Built with Claude Code" needs ICMJE AI disclosure note for manuscripts.
- **[A11Y-9]** Icon glyphs lack `aria-hidden="true"` — redundant screen reader announcements.
- **[A11Y-22]** `scroll-behavior: smooth` doesn't respect reduced motion (line ~10).

---

## False Positive Watch
- `el.textContent = headlines[idx]` — safe, hardcoded array, no innerHTML
- `bar.style.width = data-w + '%'` — safe, all data-w hardcoded
- Park-Miller PRNG for particles — acceptable for visual variety (not crypto)
- No `</script>` inside script blocks — verified clean
- EvidenceScore data-w bar widths verified correct (% of max grade count)
