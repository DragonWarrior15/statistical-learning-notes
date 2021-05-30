---
title: "Maximum A Priori (MAP)"
---

## Maximum A Priori (MAP)

Similar to MLE, we have another estimator method which evaluates $\theta$ using the posterior probability of $\theta$ given $X$
\begin{align}
    \hat{\theta}\_{MAP} &= \max_{\theta} P(\theta|X) = \max_{\theta} \frac{P(X|\theta)P(\theta)}{P(X)}\newline
    &= \max_{\theta}P(X|\theta)P(\theta)\end{align}

since $P(X)$ is just a normalization factor and thus constant. However, this sufferes from multiple problems

1.  Not invariant to reparametrization. Hence solution could change with algebraic manipulation.

2.  Can't be used as a prior since we will be looking at delta functions in the prior then.

3.  Finds untypical points (bumps) that are not smooth points in the curve.

4.  Cannot compute confidence intervals since we only get point estimates.

## Conjugate Distributions
Conjugate distributions are really helpful in calculating the posterior, especially in case of complicated distributions. In the context of MAP estimate, the prior is said to be the **conjugate prior** of the likelihood if the **posterior** obtained by multiplying the likelihood **and the prior belong to the same family of distributions**. An example
\begin{gather}
    p(X|\theta) = \mathcal{N}(\alpha_{1}, \beta_{1}^{2}), \quad p(\theta) = \mathcal{N}(\alpha_{2}, \beta_{2}^{2})\newline
    \text{Then,} \quad p(\theta|X) \propto p(X|\theta)p(\theta) = \mathcal{N}(\alpha_{3}, \beta_{3}^{2})
\end{gather}

which stems from the simple fact that multiplication of two normals will sum up the exponential terms, resulting in a constant times a new normal distribution. We ignore the constant since we only need the functional form for optimization.

**Normal distribution is conjugate to the normal distribution*.
