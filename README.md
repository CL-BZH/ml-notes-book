# Notes on Machine Learning

A book-length collection of notes written while studying machine learning:
derivations worked out in full, concepts examined from several angles, and
summaries of book chapters — from the statistical foundations of learning to
graph neural networks.

The notes started as ~100 standalone LaTeX documents, Markdown files and
notebooks. They are organised here as a single LaTeX book (11 parts,
78 chapters and three appendices, ~830 pages), with the accompanying code and notebooks.

**[📕 Download the PDF](https://github.com/CL-BZH/ml-notes-book/releases/latest/download/Notes_on_Machine_Learning.pdf)**

## Contents

**Part I — Foundations of Statistical Learning**

1. The Statistical Learning Problem
2. Bayes Decision Theory
3. Empirical Risk Minimization
4. Uniform Convergence and the Symmetrization Lemma
5. Generative and Discriminative Models
6. Lipschitz Continuity
7. Measuring Performance

**Part II — Probability and Statistics**

8. Estimators and Sampling Distributions
9. Limit Theorems and Statistical Inference
10. Covariance and Its Estimation
11. Convergence of Events and Probabilities
12. Bayesian Reasoning
13. Monte Carlo Methods
14. The EM Algorithm

**Part III — Linear Algebra, Geometry and Calculus**

15. Adjoints, Projections and Least Squares
16. The Singular Value Decomposition
17. Principal Component Analysis
18. Matrix Factorization
19. The Geometry of the Gradient

**Part IV — Loss Functions, Likelihood and Output Units**

20. Entropy, Cross-Entropy and Maximum Likelihood
21. Output Distributions and their Losses
22. Sigmoid and Softmax Output Units
23. Surrogate Losses for Classification

**Part V — Classical Models**

24. The Perceptron Trick
25. Support Vector Machines
26. Support Vector Methods: SVDD, OCSVM and SVR
27. Decision Trees
28. Ensemble Methods
29. A Mathematical Justification of Gradient Boosting
30. Dynamic Time Warping
31. Some Linear Time Series Models
32. Time Series with Multiplicative Seasonality
33. Open-Loop versus Closed-Loop Prediction

**Part VI — Neural Networks: Fundamentals and Training**

34. Deep Learning: An Overview
35. Desirable Properties of Activation Functions
36. A Catalogue of Activation Functions
37. Backpropagation in a Network with Two Hidden Layers
38. Backpropagation: A Worked Example
39. Backpropagation and the Chain Rule
40. Backpropagation as Dynamic Programming
41. Gradient Descent and its Variants
42. Normalization in Neural Networks
43. Dropout as a Regularization Method
44. Dropout: From Theory to Implementation

**Part VII — Convolutional Networks and Computer Vision**

45. Convolution versus Cross-Correlation
46. Convolution in CNNs
47. Image Gradients by Convolution
48. Transpose Convolution
49. Normalization in Convolutional Networks
50. The Evolution of CNNs
51. Instance Segmentation
52. Transfer Learning

**Part VIII — Recurrent Networks**

53. Gradient Computation in RNNs
54. From the Chain Rule to Backpropagation Through Time
55. Long Short-Term Memory

**Part IX — Language Modeling and Structured Prediction**

56. Bigram Language Modeling with Multinomial Logistic Regression
57. Bigram Logistic Regression: Loss and Gradient
58. A One-Hidden-Layer Neural Bigram Model
59. Word Embeddings
60. Hierarchical Softmax and Huffman Trees
61. Noise Contrastive Estimation and Negative Sampling
62. Structured Prediction
63. The Viterbi Algorithm for Part-of-Speech Tagging
64. Conditional Random Fields for Part-of-Speech Tagging

**Part X — Contrastive and Self-Supervised Learning**

65. Contrastive Learning: An Overview
66. Contrastive Learning: A Mathematical Treatment

**Part XI — Machine Learning on Graphs**

67. The Laplacian, Local Averages and Graphs
68. From Harmonic Functions to Graph Laplacians
69. Graph Laplacians and Spectral Methods
70. A Unified View of Spectral Decomposition
71. Fourier Analysis
72. From the DFT to Graph Neural Networks
73. Random-Walk Node Similarity
74. The Leicht–Holme–Newman Similarity
75. Reproducing Kernel Hilbert Spaces
76. Semi-Supervised Learning on Graphs
77. Shallow Graph Embedding Methods
78. Graph Autoencoders

**Appendices**

- A. Darboux's Theorem
- B. The Flat Circle ℝ/ℤ
- C. Solutions to the Exercises

## Building the book

Requirements: a TeX Live distribution (2023 or later recommended) with
`latexmk`. The book uses only standard packages (TikZ/PGFPlots, tcolorbox,
nicematrix, witharrows, forest, listings, algorithmicx, cleveref …).

```bash
cd book
make                       # builds main.pdf (≈ 3 latexmk passes)
make chapter CH=chapters/07-cnn-vision/04-transpose-convolution   # one chapter only → chapter.pdf
make clean
```

A GitHub Actions workflow (`.github/workflows/build-book.yml`) builds the PDF
on every push. Pushing a version tag (`git tag v1.1 && git push origin v1.1`)
also publishes it as a release; the latest version is always available
[here](https://github.com/CL-BZH/ml-notes-book/releases/latest/download/Notes_on_Machine_Learning.pdf).

## Repository layout

```
book/
  main.tex              entry point (book class)
  chapters.tex          list of parts and chapters (\include)
  preamble/             packages.tex, common.tex (shared macros, theorem styles)
  frontmatter/          preface
  chapters/<part>/      one .tex file per chapter
  figures/              raster figures
code/
  backpropagation/      a 2-layer network trained with hand-written backprop (+ Adam)
  em-three-coin/        EM for the three-coin model vs. direct maximum likelihood
notebooks/              Bayesian reasoning, Gibbs sampling, SVD, convolutions, bigram model
```

### Writing conventions for chapters

Each chapter file is wrapped in `\begin{notechapter} … \end{notechapter}`,
which opens a TeX group: macros, colours and `tcolorbox` environments defined
at the top of a chapter stay local to that chapter. Labels are prefixed with
the chapter slug (e.g. `\label{svd:eq:rank1}`) so that chapters can be
combined without clashes. Inside a chapter, `\chapterappendix` replaces
`\appendix`.

## Code and notebooks

```bash
pip install -r code/requirements.txt
python code/backpropagation/main.py
python code/em-three-coin/em_eval.py
jupyter lab notebooks/
```

## Licence

No licence has been chosen yet. Until one is added, the default copyright
applies (others may read the repository but not reuse its content). For
written material, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
is a common choice; for the code, MIT.
