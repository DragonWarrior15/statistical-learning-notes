---
title: "Bayes Estimator"
---

## Bayes Estimator

The Bayes estimator is the expected value of the parameter given the data. It utilizes the Bayes theorem in order to arrive at the estimator value
\begin{align}
        E[\theta|X_{1} = x_{1}, X_{2} = x_{2}, \ldots, X_{n} = x_{n}] &= \int \theta f(\theta|x_{1}, x_{2}, \ldots, x_{n})\newline
        f(\theta|x_{1}, x_{2}, \ldots, x_{n}) &= \frac{p(\theta) f(x_{1}, x_{2}, \ldots, x_{n} | \theta)}{\int p(\theta) f(x_{1}, x_{2}, \ldots, x_{n} | \theta) d\theta}
    \end{align}
where $p(\theta)$ is the assumed prior distribution on the parameter $\theta$. Based on our knowledge of the process, this can be uniform, normal etc.
