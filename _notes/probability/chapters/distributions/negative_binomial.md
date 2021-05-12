---
title: "Negative Binomial Distribution"
---

## Negative Binomial Distribution

Suppose we run an experiment with independent Bernoulli trials where the experiment stops when $r > 0$ successes are observed. Let $p$ be the probability of success, and $k$ be the number of failures in the experiment,
\begin{align}
        P(X = k) &= \binom{k + r - 1}{r-1}(1-p)^{k}p^{r} \quad k = 0, 1, 2, \ldots
    \end{align}
since the last trial is by definition a success; we can only choose the failures from the remaining trials.

### Mean and Variance

With the moment generating function, mean and variance are easy to calculate
\begin{align}
        E[X] &= \frac{rp}{1-p}\newline
        Var(X) &= \frac{r(1-p)}{p^{2}}
    \end{align}

### Relation to Geometric Distribution

Geometric distribution is a special case of Negative binomial distribution with $r = 1$
\begin{align}
        Geom(p) = NB(1, p)
    \end{align}

Further, the sum of $r$ independent geometric random variables (defined on $0,1,2,\ldots$) is a negative binomial distribution with parameters $r$ and $p$
\begin{align}
        \sum_{r} Geom(p) = NB(r, p)
    \end{align}
