---
title: "Linear Regression"
---

# Linear Regression

Linear Regression is a parametric model where we assume a linear relationship between the dependent and independent variables.
\begin{align}
    X &= (X_{1}, X_{2}, \ldots, X_{p})\newline
    Y &= \beta_{0} + \beta_{1}X_{1} + \beta_{2}X_{2} + \cdots + \beta_{p}X_{p} + \epsilon\end{align}
Where $X$ represents a p dimensional input and $\beta$ are the coefficients, and $\epsilon$ is the error which is assumed to have $\mathcal{N}(0, \sigma^{2})$ distribution. Errors are assumed to be independent. We will usually not know the error or it's variance, and hence our estimate is denoted by $\hat{Y}$. Further, the estimted coefficients will also be denoted with a hat since we can never know the true model, but only get estimates of these parameters
\begin{align}
    \hat{Y} &= \hat{\beta}\_{0} + \hat{\beta}\_{1}X_{1} + \hat{\beta}\_{2}X_{2} + \cdots + \hat{\beta}\_{p}X_{p} + \epsilon\end{align}
