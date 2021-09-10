---
title: "Geometric Distribution"
---

## Geometric Distribution

A geometric distribution represents the probability distribution for the number of trials in Bernoulli trials till the first success.
\begin{align}
        P(X = k) &= (1-p)^{k-1}p \quad k = 1, 2, 3, \ldots
    \end{align}

To be precise, this definition is called the shifted geometric distribution. Another definition is to consider $k$ as the number of trials before the first success. The distribution will then be defined on $k = 0, 1, 2, \ldots$.

### Moment Generating Function

To calculate mean and variance, we first calculate the moment generating function
\begin{align}
        E[e^{tX}] &= \sum_{k=1}^{\infty} (1-p)^{k-1}p e^{tk}\newline
        \phi(k) &= \frac{p}{1-p} \sum_{k=1}^{\infty} ((1-p)e^{t})^{k}\newline
        &= \frac{p}{1-p} \frac{(1-p)e^{t}}{1 - (1-p)e^{t}} = \frac{pe^{t}}{1 - (1-p)e^{t}}\newline
        \diffone{\phi}(t) &= \frac{(1 - (1-p)e^{t})pe^{t} + pe^{t}(1-p)e^{t}}{(1 - (1-p)e^{t})^{2}}\newline
        &= \frac{pe^{t}}{(1 - (1-p)e^{t})^{2}}\newline
        \difftwo{\phi}(t) &= \frac{(1 - (1-p)e^{t})^{2}pe^{t} + pe^{t}2(1 - (1-p)e^{t})(1-p)e^{t}}{(1 - (1-p)e^{t})^{4}}\newline
        &= \frac{pe^{t}(1 + (1-p)e^{t})}{(1 - (1-p)e^{t})^{3}}
    \end{align}

### Mean and Variance

With the moment generating function, mean and variance are easy to calculate
\begin{align}
        E[X] &= \diffone{\phi}(0) = \frac{1}{p}\newline
        E[X^{2}] &= \difftwo{\phi}(0) = \frac{2-p}{p^{2}}\newline
        Var(X) &= \frac{2-p}{p^{2}} - \frac{1}{p^{2}} = \frac{1-p}{p^{2}}
    \end{align}
