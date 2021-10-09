---
title: "Geometric Distribution"
---

## Geometric Distribution

A geometric distribution represents the probability distribution for the number of failures in Bernoulli trials till the first success.
\begin{align}
        P(X = k) &= (1-p)^{k}p \quad k = 0, 1, 2, \ldots
    \end{align}

Another definition is to consider $k$ as the number of trials before the first success. The distribution will then be defined on $k = 1, 2, \ldots$ and is often called the shifted distribution.

### Moment Generating Function

To calculate mean and variance, we first calculate the moment generating function
\begin{align}
        E[e^{tX}] &= \sum_{k=0}^{\infty} (1-p)^{k}p e^{tk}\newline
        \phi(k) &= p \sum_{k=0}^{\infty} ((1-p)e^{t})^{k}\newline
        &= p \frac{1}{1 - (1-p)e^{t}}\newline
        \diffone{\phi}(t) &= \frac{p(1-p)e^{t}}{(1 - (1-p)e^{t})^{2}}\newline
        \difftwo{\phi}(t) &= \frac{p(1-p)e^{t}\squarebr{1 + (1-p)e^{t}}}{(1 - (1-p)e^{t})^{3}}
    \end{align}

Expected number of failures will be $1/p - 1 = (1-p)/p$ (since $1/p$ is the total expected trials and we subtract the last trial which is a success).

### Mean and Variance

With the moment generating function, mean and variance are easy to calculate
\begin{align}
        E[X] &= \diffone{\phi}(0) = \frac{1-p}{p}\newline
        E[X^{2}] &= \difftwo{\phi}(0) = \frac{(1-p)(2-p)}{p^{2}}\newline
        Var(X) &= \frac{(1-p)(2-p)}{p^{2}} - \frac{(1-p)^{2}}{p^{2}} = \frac{1-p}{p^{2}}
    \end{align}

If $X$ denoted the total trials till first success, $E[X]$ would be $(1-p)/p + 1 = 1/p$ and variance would be same since its only a shifted distribution.
