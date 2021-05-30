---
title: "Comparison of Classifiers"
---

## Comparison of Classifiers

Logistic Regression and LDA are similar in the sense that they produce linear decision boundaries.

-   Logistic Regression estimates coefficients using Maximum Likelihood Estimate

-   LDA estimates parameters using the sample mean and variance

For both the models, $\log {odds}$ takes a linear form. LDA adds a strong assumption of normal distribution of the predictor variables.


Comparison of models

-   Logistic Regression is the simplest classifier one can build. It assumes linearly separated decision boundaries. It is usually used as a binary classifier. The decision boundary can be made non linear by adding transformed version of the predictors like second powers, interaction terms etc.

-   LDA is also a linear classifier, but works under the assumptions that the decision boundaries are linear and all the classes share the same covariance matrix. It works well with multiple classes. The performance can be quite bad if the underlying variables are not normally distributed.

-   QDA is a natural extension of LDA that relaxes the assumption of shared covariance matrix and allows each class to have a separate covariance matrix. This causes QDA to work well when decision boundaries have non linearity

-   KNN is a non parametric model that is the most flexible. However, we can get no indication of which predictor is important, and the model can suffer from high variance.
