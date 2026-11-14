# Notes on Machine Learning

A book-length collection of notes written while studying machine learning:
derivations worked out in full, concepts examined from several angles, and
summaries of book chapters — from the statistical foundations of learning to
graph neural networks.

The notes started as ~100 standalone LaTeX documents, Markdown files and
notebooks. They are organised here as a single LaTeX book (11 parts,
77 chapters and three appendices, ~800 pages), with the accompanying code and notebooks.

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

24. The Perceptron
25. Support Vector Machines
26. Support Vector Methods for Regression and Novelty Detection
27. Decision Trees
28. Ensembles: Bagging, Random Forests and AdaBoost
29. Gradient Boosting
30. Dynamic Time Warping
31. Linear Time Series Models
32. Decomposition and Forecasting

**Part VI — Neural Networks: Fundamentals and Training**

33. Deep Learning: An Overview
34. Desirable Properties of Activation Functions
35. A Catalogue of Activation Functions
36. Backpropagation in a Network with Two Hidden Layers
37. Backpropagation: A Worked Example
38. Backpropagation and the Chain Rule
39. Backpropagation as Dynamic Programming
40. Gradient Descent and its Variants
41. Normalization in Neural Networks
42. Dropout as a Regularization Method
43. Dropout: From Theory to Implementation

**Part VII — Convolutional Networks and Computer Vision**

44. Convolution versus Cross-Correlation
45. Convolution in CNNs
46. Image Gradients by Convolution
47. Transpose Convolution
48. Normalization in Convolutional Networks
49. The Evolution of CNNs
50. Instance Segmentation
51. Transfer Learning

**Part VIII — Recurrent Networks**

52. Gradient Computation in RNNs
53. From the Chain Rule to Backpropagation Through Time
54. Long Short-Term Memory

**Part IX — Language Modeling and Structured Prediction**

55. Bigram Language Modeling with Multinomial Logistic Regression
56. Bigram Logistic Regression: Loss and Gradient
57. A One-Hidden-Layer Neural Bigram Model
58. Word Embeddings
59. Hierarchical Softmax and Huffman Trees
60. Noise Contrastive Estimation and Negative Sampling
61. Structured Prediction
62. The Viterbi Algorithm for Part-of-Speech Tagging
63. Conditional Random Fields for Part-of-Speech Tagging

**Part X — Contrastive and Self-Supervised Learning**

64. Contrastive Learning: An Overview
65. Contrastive Learning: A Mathematical Treatment

**Part XI — Machine Learning on Graphs**

66. The Laplacian, Local Averages and Graphs
67. From Harmonic Functions to Graph Laplacians
68. Graph Laplacians and Spectral Methods
69. A Unified View of Spectral Decomposition
70. Fourier Analysis
71. From the DFT to Graph Neural Networks
72. Random-Walk Node Similarity
73. The Leicht–Holme–Newman Similarity
74. Reproducing Kernel Hilbert Spaces
75. Semi-Supervised Learning on Graphs
76. Shallow Graph Embedding Methods
77. Graph Autoencoders

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
