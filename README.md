# Notes on Machine Learning

A book-length collection of notes written while studying machine learning:
derivations worked out in full, concepts examined from several angles, and
summaries of book chapters — from the statistical foundations of learning to
graph neural networks.

The notes started as ~100 standalone LaTeX documents, Markdown files and
notebooks. They are organised here as a single LaTeX book (11 parts,
90 chapters, ~860 pages), with the accompanying code and notebooks.

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

8. Statistics and Probability for Machine Learning
9. Limit Theorems and Statistical Inference
10. Covariance and Estimation
11. Convergence of Events and Probabilities
12. Bayesian Reasoning
13. Uncertain and Unreliable Evidence
14. Monte Carlo Methods
15. The EM Algorithm

**Part III — Linear Algebra, Geometry and Calculus**

16. The Adjoint Operator and the Dual Space
17. Projections, Adjoints and the Geometry of Least Squares
18. The Singular Value Decomposition
19. Matrix Factorization
20. Principal Component Analysis: Setting and Inertia
21. PCA: Pairwise Distances and Total Inertia
22. PCA and Data Reconstruction
23. PCA through Affine Spaces
24. The Gradient and the Tangent Space
25. The Gradient in Machine Learning

**Part IV — Loss Functions, Likelihood and Output Units**

26. Cross-Entropy
27. Cross-Entropy Minimization and Maximum Likelihood
28. Empirical Distribution, Maximum Likelihood and Cost Functions
29. Bayes Classification and Surrogate Losses
30. The 0–1, Cross-Entropy and Hinge Losses
31. The Multinomial Logistic Loss
32. Any Distribution is a Softmax
33. The Softmax Function and its Numerical Stability
34. Sigmoid, Softmax and Other Output Units

**Part V — Classical Models**

35. The Perceptron Trick
36. Support Vector Machines
37. Support Vector Methods: SVDD, OCSVM and SVR
38. Decision Trees
39. Ensemble Methods
40. A Mathematical Justification of Gradient Boosting
41. Dynamic Time Warping
42. Some Linear Time Series Models
43. Time Series with Multiplicative Seasonality
44. Open-Loop versus Closed-Loop Prediction

**Part VI — Neural Networks: Fundamentals and Training**

45. Deep Learning: An Overview
46. Desirable Properties of Activation Functions
47. A Catalogue of Activation Functions
48. Backpropagation in a Network with Two Hidden Layers
49. Backpropagation: A Worked Example
50. Backpropagation and the Chain Rule
51. Backpropagation as Dynamic Programming
52. Gradient Descent and its Variants
53. Normalization in Neural Networks
54. Dropout as a Regularization Method
55. Dropout: From Theory to Implementation

**Part VII — Convolutional Networks and Computer Vision**

56. Convolution versus Cross-Correlation
57. Convolution in CNNs
58. Image Gradients by Convolution
59. Transpose Convolution
60. Normalization in Convolutional Networks
61. The Evolution of CNNs
62. Instance Segmentation
63. Transfer Learning

**Part VIII — Recurrent Networks**

64. Gradient Computation in RNNs
65. From the Chain Rule to Backpropagation Through Time
66. Long Short-Term Memory

**Part IX — Language Modeling and Structured Prediction**

67. Bigram Language Modeling with Multinomial Logistic Regression
68. Bigram Logistic Regression: Loss and Gradient
69. A One-Hidden-Layer Neural Bigram Model
70. Word Embeddings
71. Hierarchical Softmax and Huffman Trees
72. Noise Contrastive Estimation and Negative Sampling
73. Structured Prediction
74. The Viterbi Algorithm for Part-of-Speech Tagging
75. Conditional Random Fields for Part-of-Speech Tagging

**Part X — Contrastive and Self-Supervised Learning**

76. Contrastive Learning: An Overview
77. Contrastive Learning: A Mathematical Treatment

**Part XI — Machine Learning on Graphs**

78. The Laplacian, Local Averages and Graphs
79. From Harmonic Functions to Graph Laplacians
80. Graph Laplacians and Spectral Methods
81. A Unified View of Spectral Decomposition
82. Fourier Analysis
83. From the DFT to Graph Neural Networks
84. Random-Walk Node Similarity
85. The Leicht–Holme–Newman Similarity
86. Reproducing Kernel Hilbert Spaces
87. Semi-Supervised Learning on Graphs
88. Shallow Graph Embedding Methods
89. Graph Autoencoders

**Appendix**

90. Darboux's Theorem

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
