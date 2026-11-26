# Manuscript source record

Venkatesa Chandrasekaran submitted *An algebraic quantization of gravity from the null cone* on 25 November 2026. This review assesses version 1 (`arXiv:2611.34924v1`). Page numbers refer to its 83-page PDF, equation and paragraph links point to the same version in arXiv HTML, and any TeX line references refer to `main.tex` in the v1 source archive. [Version history](https://arxiv.org/abs/2611.34924v1) · [PDF](https://arxiv.org/pdf/2611.34924v1) · [HTML](https://arxiv.org/html/2611.34924v1) · [TeX archive](https://arxiv.org/src/2611.34924v1) · [Review overview](../README.md) · [Equation finder](../EQUATIONS.md)

The author granted arXiv a perpetual, non-exclusive license to distribute the submission. This repository does not redistribute the manuscript files (they are git-ignored under `source/`); instead, public review notes link directly to the versioned arXiv pages, and the commands below retrieve and verify local copies directly from arXiv. [Submission license](https://arxiv.org/licenses/nonexclusive-distrib/1.0/)

## Verify the reviewed files

From the repository root, run this block in a shell with `curl`, `sha256sum` and `tar`. The SHA-256 hashes verify the exact PDF, source archive, main TeX file and bibliography used for this review.

```sh
(
  set -e
  cd source
  curl -fL -o paper.pdf https://arxiv.org/pdf/2611.34924v1
  curl -fL -o arxiv.tar https://arxiv.org/src/2611.34924v1
  sha256sum -c <<'HASHES'
d17caccbee57cfbee6fc2eeed2e5a53467c9401be979fd2952aa2bf92d5443af  paper.pdf
1251f05ae2fac0bc307286550e115f3a9ef9228187822b9f40aad9c33b3407be  arxiv.tar
HASHES
  tar -xzf arxiv.tar main.tex references.bib
  sha256sum -c <<'HASHES'
9c4f69a7cae0a885c134be3b03a7d9dc989be1e4c60cbe2b94dc57b420f41ba4  main.tex
21583ac6858e2c49f9bc8fa67740dacbcc2277891b346dfd2639a26b9cad2992  references.bib
HASHES
)
```

To make a searchable text copy, run `pdftotext -layout source/paper.pdf source/paper.txt` from the repository root.
