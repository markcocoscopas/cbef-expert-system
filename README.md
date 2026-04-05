# CBEF Expert System

**Constraint-Based Evaluation Framework — Automated Six-Stage Analysis**

A browser-based tool that applies the Constraint-Based Evaluation Framework (CBEF) as defined in Copas (2026h) to any disputed claim in ancient construction or archaeology.

The tool implements all six CBEF stages automatically, using Claude (Anthropic) as its analytical engine with the full CBEF methodology embedded in the system prompt.

## Quick Start

**Requirements:** Python 3.7+ (standard library only — no pip installs) and an [Anthropic API key](https://console.anthropic.com/settings/keys).

```bash
# 1. Clone the repo
git clone https://github.com/markcocoscopas/cbef-expert-system.git
cd cbef-expert-system

# 2. Start the local server
python server.py

# 3. Open in your browser
# http://localhost:8080
```

Enter your API key in the interface, define a claim, and click **Run CBEF Analysis**.

Your API key is sent directly to the Anthropic API — it is never stored, logged, or transmitted anywhere else.

## How It Works

The tool cannot call the Anthropic API directly from the browser (browsers block cross-origin requests for security). The included `server.py` acts as a lightweight local proxy:

```
Browser  →  localhost:8080/api/messages  →  server.py  →  api.anthropic.com
```

The server is ~90 lines of Python using only the standard library. It serves the HTML file and forwards API requests — nothing else.

## The Six Stages

| Stage | Name | Output |
|-------|------|--------|
| 1 | Problem Bounding | Precise testable claim and boundary conditions |
| 2 | Constraint Identification | Hard, soft, and interaction constraints |
| 3 | Parameter Estimation | Conservative / central / high values, all cited |
| 4 | Bounded Scenario Modelling | Pass / marginal / fail per subsystem per scenario |
| 5 | Bottleneck Identification | Ranked binding constraints |
| 6 | Research Question Formulation | Formally stated, empirically resolvable questions |

## Key Design Principles

- **Neutral auditor position.** The system does not advocate for orthodox or heterodox positions. It applies identical quantitative standards to all claims.
- **Published sources only.** All parameter values must be traceable to a published source. Invented data are not permitted.
- **No verdicts — only structured questions.** The framework produces research agendas, not conclusions.
- **Conservative scenario discipline.** The conservative scenario is maximally favourable to the hypothesis under test. A claim that fails under the conservative scenario is strongly disfavoured.

## Files

| File | Purpose |
|------|---------|
| `cbef_expert_system.html` | The CBEF Expert System interface |
| `server.py` | Local proxy server (Python 3.7+, standard library only) |
| `README.md` | This file |
| `CITATION.cff` | Citation metadata |
| `LICENSE` | MIT Licence |

## Companion Publications

- **CBEF Methodology Paper:** Copas, M. (2026h) *Constraint-Based Evaluation Framework (CBEF): A Portable Method for Adjudicating Disputed Claims at the Orthodox–Heterodox Boundary.* Zenodo.
- **CBEF Application Paper:** Copas, M. (2026i) *The Fourth Dynasty Pyramid Programme Under Constraint-Based Evaluation.* Zenodo.

## Citation

```bibtex
@software{copas_cbef_2026,
  author = {Copas, Mark},
  title = {CBEF Expert System},
  year = {2026},
  url = {https://github.com/markcocoscopas/cbef-expert-system},
  doi = {10.5281/zenodo.19382177},
  licence = {MIT}
}
```

## Licence

MIT — see [LICENSE](LICENSE).

---

ORCID: [0009-0005-9777-2019](https://orcid.org/0009-0005-9777-2019)
