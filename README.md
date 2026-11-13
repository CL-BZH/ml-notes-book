# Notes on Machine Learning

A book-length collection of notes written while studying machine learning:
derivations worked out in full, concepts examined from several angles, and
summaries of book chapters — from the statistical foundations of learning to
graph neural networks.

The notes started as ~100 standalone LaTeX documents, Markdown files and
notebooks. They are organised here as a single LaTeX book (11 parts,
84 chapters, ~840 pages), with the accompanying code and notebooks.

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

20. Cross-Entropy
21. Cross-Entropy Minimization and Maximum Likelihood
22. Empirical Distribution, Maximum Likelihood and Cost Functions
23. Bayes Classification and Surrogate Losses
24. The 0–1, Cross-Entropy and Hinge Losses
25. The Multinomial Logistic Loss
26. Any Distribution is a Softmax
27. The Softmax Function and its Numerical Stability
28. Sigmoid, Softmax and Other Output Units

**Part V — Classical Models**

29. The Perceptron Trick
30. Support Vector Machines
31. Support Vector Methods: SVDD, OCSVM and SVR
32. Decision Trees
33. Ensemble Methods
34. A Mathematical Justification of Gradient Boosting
35. Dynamic Time Warping
36. Some Linear Time Series Models
37. Time Series with Multiplicative Seasonality
38. Open-Loop versus Closed-Loop Prediction

**Part VI — Neural Networks: Fundamentals and Training**

39. Deep Learning: An Overview
40. Desirable Properties of Activation Functions
41. A Catalogue of Activation Functions
42. Backpropagation in a Network with Two Hidden Layers
43. Backpropagation: A Worked Example
44. Backpropagation and the Chain Rule
45. Backpropagation as Dynamic Programming
46. Gradient Descent and its Variants
47. Normalization in Neural Networks
48. Dropout as a Regularization Method
49. Dropout: From Theory to Implementation

**Part VII — Convolutional Networks and Computer Vision**

50. Convolution versus Cross-Correlation
51. Convolution in CNNs
52. Image Gradients by Convolution
53. Transpose Convolution
54. Normalization in Convolutional Networks
55. The Evolution of CNNs
56. Instance Segmentation
57. Transfer Learning

**Part VIII — Recurrent Networks**

58. Gradient Computation in RNNs
59. From the Chain Rule to Backpropagation Through Time
60. Long Short-Term Memory

**Part IX — Language Modeling and Structured Prediction**

61. Bigram Language Modeling with Multinomial Logistic Regression
62. Bigram Logistic Regression: Loss and Gradient
63. A One-Hidden-Layer Neural Bigram Model
64. Word Embeddings
65. Hierarchical Softmax and Huffman Trees
66. Noise Contrastive Estimation and Negative Sampling
67. Structured Prediction
68. The Viterbi Algorithm for Part-of-Speech Tagging
69. Conditional Random Fields for Part-of-Speech Tagging

**Part X — Contrastive and Self-Supervised Learning**

70. Contrastive Learning: An Overview
71. Contrastive Learning: A Mathematical Treatment

**Part XI — Machine Learning on Graphs**

72. The Laplacian, Local Averages and Graphs
73. From Harmonic Functions to Graph Laplacians
74. Graph Laplacians and Spectral Methods
75. A Unified View of Spectral Decomposition
76. Fourier Analysis
77. From the DFT to Graph Neural Networks
78. Random-Walk Node Similarity
79. The Leicht–Holme–Newman Similarity
80. Reproducing Kernel Hilbert Spaces
81. Semi-Supervised Learning on Graphs
82. Shallow Graph Embedding Methods
83. Graph Autoencoders

**Appendix**

84. Darboux's Theorem

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
