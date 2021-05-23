---
title: "Answer"
---

Let $X_{i}$ denote the random variables with respective parameters $\lambda_{i}$.

Note that
\begin{align}
        P(min(X_{1}, X_{2}, \ldots, X_{n}) > x) &= P(X_{1} > x, X_{2} > x, \ldots, X_{n} > x)\newline
        &= \prod_{i=1}^{n} (1 - P(X \leq x))\newline
        &= \prod_{i=1}^{n} e^{-\lambda_{i}x} = exp(-\sum_{i=1}^{n}\lambda_{i} x)
    \end{align}
which is an exponential random variable with the rates added together.
