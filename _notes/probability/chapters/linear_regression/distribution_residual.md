---
title: "Distribution of Residual"
---

## Distribution of Residual

Residuals and the $SS_{R}$ are defined as
\begin{align}
        R &= Y - (\hat{\theta}\_{0} + \hat{\theta}\_{1}X)\newline
        SS_{R} &= \sum_{i=1}^{n} R_{i}^{2} = \sum_{i=1}^{n} (Y - \hat{\theta}\_{0} - \hat{\theta}\_{1}X)^{2}\newline
        &= \frac{S_{xx}S_{YY} - S_{xY}^{2}}{S_{xx}}
    \end{align}

$SS_{R}$ is itself a random variable and it can be shown that
\begin{align}
        \frac{SS_{R}}{\sigma^{2}} \sim \chi_{n-2}^{2}\newline
        E[\frac{SS_{R}}{\sigma^{2}}] = n - 2\newline
        E[\frac{SS_{R}}{n-2}] = \sigma^{2}\newline
    \end{align}
since $SS_{R}/\sigma^{2}$ is the sum of squares of normally distributed variables ($E[Y] = \theta_{0} + \theta_{1}X$) and two degrees of freedoms are already taken up by the coefficients. Further, $SS_{R}$ is an unbiased estimator of the variance of the error terms $\sigma^{2}$, and is also independent of the coefficients.
