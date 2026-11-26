# Alignment and Control via Exercises

An independent mathematical reading companion to Dirk Bergemann, Andrew Koh and Stephen Morris, *Mechanism Design for Alignment and Control* (September 1, 2026). The exercises, fictional vignettes and worked solutions are written for this workbook. The exposition follows the simplest-case-first structure of *GRH via exercises*. [Original paper](https://arxiv.org/abs/2609.01595v1) · [Reference workbook](https://ultronozm.github.io/grh-workbook/)

**[Read the paper with the exercises side by side](https://aaradhyapandeycs.github.io/bkm-alignment-workbook/study.html)** · [Paper reader and theorem index](https://aaradhyapandeycs.github.io/bkm-alignment-workbook/paper.html) · [All exercises](https://aaradhyapandeycs.github.io/bkm-alignment-workbook/#contents) · [Printable workbook](print/workbook.pdf). The website renders mathematics with MathJax. Choose a sheet to see its paper section and worked exercises together. Switch the paper pane between reading notes and the complete author-hosted PDF. To read it offline, download the repository, extract it and open `docs/index.html` in a browser.

A curator asks an assistant to identify a damaged crate. An assistant with an accurate sensor can pretend its reading is uninformative. And once the curator has offered a contract, the assistant who understated its abilities still has the accurate sensor. What terms would induce it to report honestly *and* act as instructed? That question runs through the workbook, from the first two-type example to the final peer-scored contract.

## Reading map

| Sheet | What you will work out | Paper |
|---|---|---|
| [1. The agent who takes the action](sheets/01-model.md) | Separate what an agent knows, can do and wants. Construct a Blackwell garbling. | §§1–2.2 |
| [2. From a conversation to a contingent plan](sheets/02-revelation.md) | Simulate an indirect equilibrium and lift a joint deviation back to it. | §2.3, Definitions 1–2, Proposition 1 |
| [3. Pricing obedience](sheets/03-obedience.md) | Reconstruct reward differences from paths in a signal graph. Connect the cycle test to finite optimal transport. | §2.4, Lemma 1 |
| [4. Pricing honesty](sheets/04-nested-cycles.md) | Find a second cycle obstruction across reports. Write a finite feasibility program. | §§2.4–2.5, Proposition 2 |
| [5. Sandbagging](sheets/05-sandbagging.md) | Iron a nonmonotone spending limit by hand, then derive the continuum result. | §3, Example I, Proposition 3, Lemma 2, Appendix A |
| [6. Alignment and interpretability](sheets/06-interpretability.md) | Reduce arbitrary closed permission sets to a common cap and derive the welfare comparison. | §3, Example II, Propositions 4–5, Appendix A |
| [7. Higher-order beliefs](sheets/07-beliefs.md) | Track whose probability matters when several agents receive private recommendations. | §4, Definitions 3–5, Proposition 6 |
| [8. Peer discipline](sheets/08-peer-discipline.md) | Compute a scoring ledger and turn a gap between forecasts into a truthful-reporting incentive. | §5, Example III, Proposition 7 |
| [9. Competition](sheets/09-competition.md) | Recover two biases from one observed gap and design coupled rewards backwards. | §5, Example IV, Proposition 8 |
| [10. Oversight](sheets/10-oversight.md) | Compare binary approval, delegation and reward design. Reproduce the regime switches in Figure 11. | §5, Example V, Proposition 9 |
| [11. The monitor's menu](sheets/11-reward-menus.md) | Price two extreme actions to make a biased monitor choose the first-best schedule. | §5, Example V, Proposition 10 |
| [12. A deployment contract](sheets/12-capstone.md) | Combine verification and peer scoring, then change commitment, beliefs and awareness of testing. | §6 and original synthesis problems |

## Three seminar paths

- **Reconstruct the characterization.** Read 1 → 2 → 3 → 4. At the board, construct the release premiums in Sheet 4 before writing down either cycle condition.
- **Study one-agent delegation.** Read 1 → 2 → 5 → 6. Compare the feasible menus in Sheets 5 and 6 before carrying a cap formula from one example to the other.
- **Design a multi-agent audit.** Read 1 → 2 → 7. Continue to 8 for peer scoring, to 9 for competition, or to 10 → 11 for oversight. Finish with 12 to design a mechanism and test its dependence on assumptions.

The core prerequisites are conditional probability, expected utility and elementary optimization. Sheet 3 introduces its graph and transport arguments from scratch. Sheets 5 and 6 use integrals and one-sided derivatives. Every exercise is followed by a hint and a worked solution. In the web edition, open either when you want it.

## Source and scope

The paper studies implementation as an equilibrium existence claim. A prescribed action taken in one truthful equilibrium can coexist with other equilibria. Throughout the workbook, distinguish who observes the state, when a type reports, what a reward can depend on and which actions remain physically available after a lie. These four questions determine which of the paper's constructions applies.

The appendix arguments are integrated into Sheets 5 and 6. The finite transport and linear-programming exercises on Sheets 3 and 4 and the examples on Sheet 12 are pedagogical additions. The final sheet identifies the research directions left open in the paper. This workbook was prepared with AI assistance and is unaffiliated with the paper's authors and the GRH workbook project.

[Read the paper in HTML](https://arxiv.org/html/2609.01595v1) · [Original PDF](https://arxiv.org/pdf/2609.01595v1)

## Rebuilding the editions

Edit the Markdown in `reader/` and `sheets/`. From the repository root, run `python3 tools/build_site.py`, `python3 tools/build_reader.py`, and `python3 tools/build_study.py` to regenerate the website. Run `python3 tools/build_print.py` to regenerate the exercise PDF. The site builder can reuse rendered equations. Its help lists the Node and KaTeX options for new formulas. The print edition requires pdfLaTeX. To update Pages after committing and pushing the sources on `main`, publish the contents of `docs/` at the root of `gh-pages`.
