---
title: "Weighted Least Squares"
---

## Weighted Least Squares

Suppose we know that the variance of $Y$ is dependent on $Y$ itself in the form $Var(Y_{i}) \propto \sigma^{2}/w_{i}$, i.e., the weights are known only upto a constant. In this case, we minimize the weighted least squares to obtain the coefficients
\begin{align}
        \minimize_{\theta_{0}, \theta_{1}} \sum_{i=1}^{n} w_{i}(Y_{i} - \theta_{0} - \theta_{1}x_{i})^{2}
    \end{align}
