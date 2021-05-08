---
title: "Polynomial Regression"
---

## Polynomial Regression

This is a simply modification to the original linear regression setting where we incorporate higher powers of the predictor as well. This helps incorporate non linear trends in the data as well while retaining an additive relationship between the variables.
\begin{align}
    \hat{y} &= \hat{\beta_{0}} + \hat{\beta_{1}}x\newline
    \hat{y} &= \hat{\beta_{0}} + \hat{\beta_{1}}x + \hat{\beta_{2}}x^{2} + \cdots + \hat{\beta_{d}}x^{d}
\end{align}

which are linear and polynomial regressions respectively.

Generally, is is **unusual to have $d$ to be greater than $3$ or $4$** because higher degree of polynomial makes the model highly flexible with very curvy shapes. This may reduce bias to a large extent but the variance obtained thus is quite high, expecially near the end values of the range.

\begin{align}
        \hat{C} &= Cov(\hat{\beta}, \hat{\beta})\newline
        l_{i} &= (1, x_{i}, x_{i}^{2}, \ldots, x_{i}^{d})^{T}\newline
        Var[\hat{y_{i}}] &= l_{i}^{T}\hat{C}l_{i}
    \end{align}

The same form of polynomial regression terms works in the context of classification as well for Logistic Regression.
