---
title: "Negative Binomial Distribution"
---

## Negative Binomial Distribution

Suppose we run an experiment with independent Bernoulli trials where the experiment stops when $r > 0$ **successes** are observed. Let $p$ be the probability of success, and $k$ **be the number of failures** in the experiment,
\begin{align}
        P(X = k) &= \binom{k + r - 1}{r-1}(1-p)^{k}p^{r} \quad k = 0, 1, 2, \ldots
    \end{align}
since the last trial is by definition a success; we can only choose the failures from the remaining trials. Again, $X$ **is the number of failures** and not the number of trials.

### Moment Generating Function
\begin{align}
    \phi(t) &= \sum_{k=0}^{\infty}e^{tk} \binom{k+r-1}{r-1}\roundbr{1-p}^{k}p^{r}\newline
    \phi(t) &= \sum_{k=0}^{\infty} \binom{k+r-1}{ r-1}\squarebr{\roundbr{1-p}e^{t}}^{k}p^{r}\newline
    \phi(t) &= \sum_{k=0}^{\infty} \binom{k+r-1}{r-1}\squarebr{\roundbr{1-p}e^{t}}^{k}\squarebr{1 - \roundbr{1-p}e^{t}}^{r} \roundbr{\frac{p}{1 - \roundbr{1-p}e^{t}}}^{r}\newline
    \phi(t) &= \roundbr{\frac{p}{1 - \roundbr{1-p}e^{t}}}^{r} \sum_{k=0}^{\infty} \binom{k+r-1}{r-1}\squarebr{\roundbr{1-p}e^{t}}^{k}\squarebr{1 - \roundbr{1-p}e^{t}}^{r}\newline
    &= \roundbr{\frac{p}{1 - \roundbr{1-p}e^{t}}}^{r} \times 1\newline
    &= \roundbr{\frac{p}{1 - \roundbr{1-p}e^{t}}}^{r}
\end{align}

### Mean and Variance

With the moment generating function, mean and variance are easy to calculate
\begin{align}
        E[X] &= \frac{r(1-p)}{p}\newline
        Var(X) &= \frac{r(1-p)}{p^{2}}
    \end{align}

### Relation to Geometric Distribution

Geometric distribution is a special case of Negative binomial distribution with $r = 1$
\begin{align}
        Geom(p) = NB(1, p)
    \end{align}
and can be checked using the mgf of the two.

Further, the sum of $r$ independent geometric random variables is a negative binomial distribution with parameters $r$ and $p$
\begin{align}
        \sum_{r} Geom(p) = NB(r, p)
    \end{align}

### Sum of Negative Binomial Random Variables
If $X_{i}$ are $NB(r_{i}, p)$, then the sum of $n$ such variables is $NB(\sum r_{i}, p)$. That is, the sum of negative binomial random variables is also a negative binomial random variable. This can be readily seen from the mgf.
