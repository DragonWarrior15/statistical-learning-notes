---
title: "Markov Inequality"
---

## Markov Inequality

For any non-negative random variable $X$ and positive $a$,
\begin{align}
        P(X \geq a) \leq \frac{E[X]}{a}
    \end{align}
This means that for a random variable with small mean, the probability of taking large values is small.


This can be proved as follows
\begin{align}
        E[X] &= \int_{0}^{\infty} xp_{X}(x) dx = \int_{0}^{a} xp_{X}(x) dx + \int_{a}^{\infty} xp_{X}(x) dx\newline
        &\geq \int_{a}^{\infty} xp_{X}(x) dx \geq \int_{a}^{\infty} ap_{X}(x) dx = a\int_{a}^{\infty} p_{X}(x) dx\newline
        &\geq aP(X \geq a)
    \end{align}

Based on experiments with simple distributions (like uniform distribution), it can be verified that the bounds provided by this inequality can be quite loose.
