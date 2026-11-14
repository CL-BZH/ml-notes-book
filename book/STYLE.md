# Style guide

The book's visual and pedagogical conventions. All definitions are in
`preamble/style.tex`; chapters use only the environments listed here and
define no boxes of their own.

## Structure of a chapter

```latex
\begin{notechapter}
\chapter{Title}\label{ch:slug}
\chaptersubtitle{One-line subtitle}

\begin{chapterintro}
  One paragraph of motivation, then "You will learn" + itemize of goals.
  \prerequisites{chapters or topics the reader needs}
\end{chapterintro}

\section{...}   % sections of explanation, derivation, worked examples

\begin{chaptersummary} itemize of the key results \end{chaptersummary}

\section*{Exercises}
\addcontentsline{toc}{section}{Exercises}
\begin{exercise} ... \hint{...} \end{exercise}
\end{notechapter}
```

Every exercise has a label `slug:exr:N` and ends with `\solutionlink{slug:exr:N}`.
Its solution goes in `backmatter/solutions.tex`, in the section of its chapter,
introduced by `\solution{slug:exr:N}` (which links back to the statement).

Labels are prefixed with the chapter slug: `slug:sec:...`, `slug:thm:...`,
`slug:eq:...`, `slug:fig:...`. Cross-references use `\cref`.

## Environments

| Environment | Use | Look |
|---|---|---|
| `theorem`, `proposition`, `lemma`, `corollary` | results that are proved | blue left bar |
| `definition`, `assumption` | definitions | green left bar |
| `example` | worked examples with numbers | orange left bar |
| `remark` | side comments | unboxed |
| `intuition` | the idea behind a result, before or after the formal version | blue titled box |
| `keyidea` | the one thing to remember from a section | purple titled box |
| `pitfall` | common mistakes and misreadings | red titled box |
| `chapterintro`, `chaptersummary` | chapter frame | shaded / grey box |
| `exercise` (+ `\hint`, `\solutionlink{label}`) | exercises, numbered per chapter; each ends with a link to its solution | plain |

Boxes take an optional title: `\begin{pitfall}[Zero counts]`.

## Notation

| Symbol | Meaning |
|---|---|
| `X, Y` / `x, y` | random variables / their values |
| `\Xs`, `\Ys` | input and output spaces |
| `P` | distribution of `(X, Y)`; `\Prob`, `\E`, `\Var`, `\Cov` |
| `D_n`, `d_n` | random sample / observed dataset of size `n` |
| `\ell(\hat y, y)` | loss |
| `\Risk(f)` = `R(f)` | population risk |
| `\ERisk(f)` = `\widehat R_n(f)` | empirical risk on `n` points |
| `f^*`, `R^*` | Bayes predictor, Bayes risk |
| `\Hs` = `\mathcal F`, `f_\Hs`, `\hat f_n` | hypothesis class, best in class, ERM solution |
| `\eta(x)` | `P(Y = 1 | X = x)`; `\eta_k(x)` in the multiclass case |
| `\bbone[A]` | indicator of the statement `A` |

## Writing

- Explain before formalizing: motivation, then definition, then result and
  proof, then a worked example with numbers.
- Prose over bullet lists; lists only for genuinely parallel items.
- Every claim is either proved, derived, or attributed to a reference.
- Figures are drawn in TikZ/pgfplots; data for plots are computed, not
  sketched by hand, when they are meant to be read quantitatively.
- Network architectures are drawn with the macros of `preamble/nndraw.tex`:
  `\nnbox{name}{x}{w}{h}{d}{colour}{label}` draws a feature map as a box
  (thickness for channels, height and depth for the spatial size) and
  `\nnarrow{from}{to}` connects two boxes.
