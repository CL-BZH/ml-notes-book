# Notes on Machine Learning

A book-length collection of notes written while studying machine learning:
derivations worked out in full, concepts examined from several angles, and
summaries of book chapters — from the statistical foundations of learning to
graph neural networks.

The notes started as ~100 standalone LaTeX documents, Markdown files and
notebooks. They are organised here as a single LaTeX book (11 parts,
93 chapters, ~860 pages), with the accompanying code and notebooks.

## Contents

**Part I — Foundations of Statistical Learning**

1. Introduction to Machine Learning
2. Empirical Risk Minimization
3. A Unified View of Risk
4. The Symmetrization Lemma
5. The Optimal Predictor under Squared Loss
6. Mean Integrated Squared Error
7. The Product Structure in Machine Learning
8. Lipschitz Continuity in Machine Learning
9. The Coefficient of Determination R²
10. Class Encoding, Precision and Recall

**Part II — Probability and Statistics**

11. Statistics and Probability for Machine Learning
12. Limit Theorems and Statistical Inference
13. Covariance and Estimation
14. Convergence of Events and Probabilities
15. Bayesian Reasoning
16. Uncertain and Unreliable Evidence
17. Monte Carlo Methods
18. The EM Algorithm

**Part III — Linear Algebra, Geometry and Calculus**

19. The Adjoint Operator and the Dual Space
20. Projections, Adjoints and the Geometry of Least Squares
21. The Singular Value Decomposition
22. Matrix Factorization
23. Principal Component Analysis: Setting and Inertia
24. PCA: Pairwise Distances and Total Inertia
25. PCA and Data Reconstruction
26. PCA through Affine Spaces
27. The Gradient and the Tangent Space
28. The Gradient in Machine Learning

**Part IV — Loss Functions, Likelihood and Output Units**

29. Cross-Entropy
30. Cross-Entropy Minimization and Maximum Likelihood
31. Empirical Distribution, Maximum Likelihood and Cost Functions
32. Bayes Classification and Surrogate Losses
33. The 0–1, Cross-Entropy and Hinge Losses
34. The Multinomial Logistic Loss
35. Any Distribution is a Softmax
36. The Softmax Function and its Numerical Stability
37. Sigmoid, Softmax and Other Output Units

**Part V — Classical Models**

38. The Perceptron Trick
39. Support Vector Machines
40. Support Vector Methods: SVDD, OCSVM and SVR
41. Decision Trees
42. Ensemble Methods
43. A Mathematical Justification of Gradient Boosting
44. Dynamic Time Warping
45. Some Linear Time Series Models
46. Time Series with Multiplicative Seasonality
47. Open-Loop versus Closed-Loop Prediction

**Part VI — Neural Networks: Fundamentals and Training**

48. Deep Learning: An Overview
49. Desirable Properties of Activation Functions
50. A Catalogue of Activation Functions
51. Backpropagation in a Network with Two Hidden Layers
52. Backpropagation: A Worked Example
53. Backpropagation and the Chain Rule
54. Backpropagation as Dynamic Programming
55. Gradient Descent and its Variants
56. Normalization in Neural Networks
57. Dropout as a Regularization Method
58. Dropout: From Theory to Implementation

**Part VII — Convolutional Networks and Computer Vision**

59. Convolution versus Cross-Correlation
60. Convolution in CNNs
61. Image Gradients by Convolution
62. Transpose Convolution
63. Normalization in Convolutional Networks
64. The Evolution of CNNs
65. Instance Segmentation
66. Transfer Learning

**Part VIII — Recurrent Networks**

67. Gradient Computation in RNNs
68. From the Chain Rule to Backpropagation Through Time
69. Long Short-Term Memory

**Part IX — Language Modeling and Structured Prediction**

70. Bigram Language Modeling with Multinomial Logistic Regression
71. Bigram Logistic Regression: Loss and Gradient
72. A One-Hidden-Layer Neural Bigram Model
73. Word Embeddings
74. Hierarchical Softmax and Huffman Trees
75. Noise Contrastive Estimation and Negative Sampling
76. Structured Prediction
77. The Viterbi Algorithm for Part-of-Speech Tagging
78. Conditional Random Fields for Part-of-Speech Tagging

**Part X — Contrastive and Self-Supervised Learning**

79. Contrastive Learning: An Overview
80. Contrastive Learning: A Mathematical Treatment

**Part XI — Machine Learning on Graphs**

81. The Laplacian, Local Averages and Graphs
82. From Harmonic Functions to Graph Laplacians
83. Graph Laplacians and Spectral Methods
84. A Unified View of Spectral Decomposition
85. Fourier Analysis
86. From the DFT to Graph Neural Networks
87. Random-Walk Node Similarity
88. The Leicht–Holme–Newman Similarity
89. Reproducing Kernel Hilbert Spaces
90. Semi-Supervised Learning on Graphs
91. Shallow Graph Embedding Methods
92. Graph Autoencoders

**Appendix**

93. Darboux's Theorem

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
on every push and uploads it as a build artifact.

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
