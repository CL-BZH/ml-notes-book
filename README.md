# Notes on Machine Learning

A book-length collection of notes written while studying machine learning:
derivations worked out in full, concepts examined from several angles, and
summaries of book chapters — from the statistical foundations of learning to
graph neural networks.

The notes started as ~100 standalone LaTeX documents, Markdown files and
notebooks. They are organised here as a single LaTeX book (11 parts,
89 chapters, ~860 pages), with the accompanying code and notebooks.

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

15. The Adjoint Operator and the Dual Space
16. Projections, Adjoints and the Geometry of Least Squares
17. The Singular Value Decomposition
18. Matrix Factorization
19. Principal Component Analysis: Setting and Inertia
20. PCA: Pairwise Distances and Total Inertia
21. PCA and Data Reconstruction
22. PCA through Affine Spaces
23. The Gradient and the Tangent Space
24. The Gradient in Machine Learning

**Part IV — Loss Functions, Likelihood and Output Units**

25. Cross-Entropy
26. Cross-Entropy Minimization and Maximum Likelihood
27. Empirical Distribution, Maximum Likelihood and Cost Functions
28. Bayes Classification and Surrogate Losses
29. The 0–1, Cross-Entropy and Hinge Losses
30. The Multinomial Logistic Loss
31. Any Distribution is a Softmax
32. The Softmax Function and its Numerical Stability
33. Sigmoid, Softmax and Other Output Units

**Part V — Classical Models**

34. The Perceptron Trick
35. Support Vector Machines
36. Support Vector Methods: SVDD, OCSVM and SVR
37. Decision Trees
38. Ensemble Methods
39. A Mathematical Justification of Gradient Boosting
40. Dynamic Time Warping
41. Some Linear Time Series Models
42. Time Series with Multiplicative Seasonality
43. Open-Loop versus Closed-Loop Prediction

**Part VI — Neural Networks: Fundamentals and Training**

44. Deep Learning: An Overview
45. Desirable Properties of Activation Functions
46. A Catalogue of Activation Functions
47. Backpropagation in a Network with Two Hidden Layers
48. Backpropagation: A Worked Example
49. Backpropagation and the Chain Rule
50. Backpropagation as Dynamic Programming
51. Gradient Descent and its Variants
52. Normalization in Neural Networks
53. Dropout as a Regularization Method
54. Dropout: From Theory to Implementation

**Part VII — Convolutional Networks and Computer Vision**

55. Convolution versus Cross-Correlation
56. Convolution in CNNs
57. Image Gradients by Convolution
58. Transpose Convolution
59. Normalization in Convolutional Networks
60. The Evolution of CNNs
61. Instance Segmentation
62. Transfer Learning

**Part VIII — Recurrent Networks**

63. Gradient Computation in RNNs
64. From the Chain Rule to Backpropagation Through Time
65. Long Short-Term Memory

**Part IX — Language Modeling and Structured Prediction**

66. Bigram Language Modeling with Multinomial Logistic Regression
67. Bigram Logistic Regression: Loss and Gradient
68. A One-Hidden-Layer Neural Bigram Model
69. Word Embeddings
70. Hierarchical Softmax and Huffman Trees
71. Noise Contrastive Estimation and Negative Sampling
72. Structured Prediction
73. The Viterbi Algorithm for Part-of-Speech Tagging
74. Conditional Random Fields for Part-of-Speech Tagging

**Part X — Contrastive and Self-Supervised Learning**

75. Contrastive Learning: An Overview
76. Contrastive Learning: A Mathematical Treatment

**Part XI — Machine Learning on Graphs**

77. The Laplacian, Local Averages and Graphs
78. From Harmonic Functions to Graph Laplacians
79. Graph Laplacians and Spectral Methods
80. A Unified View of Spectral Decomposition
81. Fourier Analysis
82. From the DFT to Graph Neural Networks
83. Random-Walk Node Similarity
84. The Leicht–Holme–Newman Similarity
85. Reproducing Kernel Hilbert Spaces
86. Semi-Supervised Learning on Graphs
87. Shallow Graph Embedding Methods
88. Graph Autoencoders

**Appendix**

89. Darboux's Theorem

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
