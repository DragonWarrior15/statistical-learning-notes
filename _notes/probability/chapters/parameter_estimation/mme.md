---
title: "Method of Moments Estimate"
---

## Method of Moments Estimate

For this method, we calculate expected value of powers of the random variable to get $d$ equations for estimating $d$ parameters (if the solutions exist). For instance, consider $f_{X}(x) = f(x \lvert \theta, \sigma)$. We can estimate the values of the parameters by solving the two equations
\begin{align}
        E[X] &= \frac{\sum_{i=1}^{n} X_{i}}{n} = \int xf(x \lvert \theta, \sigma) dx\newline
        E[X^{2}] &= \frac{\sum_{i=1}^{n} X_{i}^{2}}{n} = \int x^{2}f(x \lvert \theta, \sigma) dx
    \end{align}
with the solutions to these equations denoted as $\theta_{MME}$ and $\sigma_{MME}$. Depending on the distribution, calculation of expected values can be done using moment generating functions. The above estimation is valid when we have a large number of samples, since by the law of large numbers, the sample mean will converge to the true mean.
