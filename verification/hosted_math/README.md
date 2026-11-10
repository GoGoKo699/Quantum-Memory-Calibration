# Checking the hosted mathematics

The [workflow](../../.github/workflows/hosted-math.yml) compares the mathematical expressions in the exact proposed Git commit with their actual GitHub rendering. It opens public, commit-pinned pages in a fresh anonymous Chromium context at widths of 1440 and 760 pixels. It checks every tracked Markdown page, including the scientific account, learning material, references, and verification guides.

The comparison retains subscripts, superscripts, fractions, matrix structure, relations, and labels. A missing expression, renderer error, structural difference, or overflowing display makes the check fail. The resulting artifact contains the source inventory, actual DOM captures, screenshots, comparison results, and a report with artifact hashes. Its source revision and tree identify exactly what was checked.

## Run locally

Use Node.js 18 or later, Python 3.10 or later, Git, Playwright, and MathJax. Install the browser runtime outside the repository, then run:

```bash
npm install --prefix /absolute/runtime playwright@1.56.1 mathjax-full@3.2.1
/absolute/runtime/node_modules/.bin/playwright install chromium
NODE_PATH=/absolute/runtime/node_modules node verification/hosted_math/capture_hosted_math.cjs \
  --root /absolute/repository \
  --repository GoGoKo699/Quantum-Memory-Calibration \
  --revision FULL_40_CHARACTER_COMMIT \
  --output /absolute/new-evidence-directory
```

Replace the example paths and commit with actual values. The source inventory reads Git objects at that commit even if the working directory contains uncommitted edits. Each attempt requires a new evidence directory, so a failed capture is retained. For a representative diagnostic, use `probe_hosted_math.cjs` with the same arguments and exactly one `--page` argument.

## Interpretation

A passing automated comparison still requires visual inspection of the saved screenshots against the source, especially substantial proofs, tables, and repaired equations. It does not certify the scientific argument or every future browser and GitHub rendering version. Local TeX compilation supplies the reference side of the comparison; it does not establish how the page actually appeared on GitHub.

The workflow uses read access to this repository and does not log in to GitHub in the captured browser. Its artifacts expire after 14 days. Preserve any evidence needed for a lasting review separately.

[Finite numerical checks](../README.md) · [Repository overview](../../README.md)
