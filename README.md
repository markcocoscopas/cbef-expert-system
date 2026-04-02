# CBEF Expert System

**An automated implementation of the Constraint-Based Evaluation Framework for adjudicating disputed claims at the orthodox–heterodox boundary in ancient construction and archaeology.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What Is This?

The CBEF Expert System is a browser-based AI tool that applies the **Constraint-Based Evaluation Framework (CBEF)** — a portable methodology for evaluating disputed claims through systematic constraint analysis — to any ancient construction or archaeological hypothesis the user supplies.

It implements the six-stage CBEF procedure defined in Copas (2026h) automatically, using Claude (Anthropic) as its analytical engine with the full CBEF methodology baked into the system prompt.

**Input:** A claim to evaluate, a domain, known parameters, and optional key sources.

**Output:** A structured six-stage analysis report including scenario tables, a ranked bottleneck hierarchy, and formally stated research questions — all derived from published orthodox sources.

---

## The Six Stages

| Stage | Name | Output |
|-------|------|--------|
| 1 | Problem Bounding | Precise testable claim and boundary conditions |
| 2 | Constraint Identification | Hard, soft, and interaction constraints |
| 3 | Parameter Estimation | Conservative / central / high values, all cited |
| 4 | Bounded Scenario Modelling | Pass / marginal / fail per subsystem per scenario |
| 5 | Bottleneck Identification | Ranked binding constraints |
| 6 | Research Question Formulation | Formally stated, empirically resolvable questions |

---

## Key Design Principles

- **Neutral auditor position.** The system does not advocate for orthodox or heterodox positions. It applies identical quantitative standards to all claims.
- **Published sources only.** All parameter values must be traceable to a published source. Invented data are not permitted.
- **No verdicts — only structured questions.** The framework produces research agendas, not conclusions. This is appropriate given the evidentiary situation in most ancient construction disputes.
- **Conservative scenario discipline.** The conservative scenario is explicitly designed to be maximally favourable to the hypothesis under test. A claim that fails under the conservative scenario is strongly disfavoured.

---

## How to Use

The tool is a single self-contained HTML file with no build step and no external dependencies beyond the Anthropic API (which is called at runtime via Claude.ai's infrastructure when run in that environment).

**To run locally:**

1. Clone or download this repository.
2. Open `index.html` in a modern browser.
3. Enter a claim, domain, and any known parameters.
4. Click **Run CBEF Analysis**.

Note: API calls require the tool to be run within an environment that has Anthropic API access configured. When run as an artifact within Claude.ai, this is handled automatically.

---

## Companion Resources

This tool is a companion to the following publications:

- **CBEF Methodology Paper:** Copas, M. (2026h) *Constraint-Based Evaluation Framework (CBEF): A Portable Method for Adjudicating Disputed Claims at the Orthodox–Heterodox Boundary.* Zenodo. [https://doi.org/10.5281/zenodo.19382177]
- **CBEF Application Paper:** Copas, M. (2026i) *The Fourth Dynasty Pyramid Programme Under Constraint-Based Evaluation: A Full Application of the CBEF Framework.* Zenodo. [DOI to be inserted on publication]
- **Pyramid Constraint Engine:** A related tool modelling six Fourth Dynasty structures as a constrained throughput system. [github.com/markcocoscopas/pyramid-constraint-model](https://github.com/markcopas/pyramid-constraint-model) · DOI: [10.5281/zenodo.19332531](https://doi.org/10.5281/zenodo.19332531)

---

## Citation

If you use this tool in published research, please cite:

```
Copas, M. (2026) CBEF Expert System: An Automated Implementation of the
Constraint-Based Evaluation Framework. GitHub.
https://github.com/markcopas/cbef-expert-system
DOI: 10.5281/zenodo.XXXXXXX
```

See `CITATION.cff` for machine-readable citation metadata.

---

## Author

**Mark Copas**  
Independent Researcher, Mallow, Ireland  
ORCID: [0009-0005-9777-2019](https://orcid.org/0009-0005-9777-2019)

---

## Licence

MIT. See `LICENSE` for details.
