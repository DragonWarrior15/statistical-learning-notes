---
title: "Generating Discrete Random Variables"
---

## Generating Discrete Random Variables

Suppose we want to generate the random variable $X$ with probability mass function
\begin{align}
        P(X = x_{i}) = p_{i}, i = 1, 2, \ldots, n\; \sum_{i=1}^{n} p_{i} = 1
    \end{align}
Then using a uniform random generator $U$, we can generate the discrete random variable using
\begin{align}
        X = x_{i} \quad \text{if} \quad p_{1} + p_{2} +\cdots + p_{i-1} \leq U < p_{1} + p_{2} +\cdots + p_{i}
    \end{align}
i.e., we divide the number line at points $p_{1}, p_{1}+p_{2}, \ldots, 1$ and choose the $i^{th}$ interval such that $U$ falls in that interval. This algorithm is valid since
\begin{align}
        P(a \leq U < b) = b-a\newline
        P(\sum_{j=1}^{i-1}p_{j} \leq U < \sum_{j=1}^{i}p_{j}) = p_{i}
    \end{align}

This method is known as *discrete inverse transform method*.


### Binomial Random Variable

To generate a Bernoulli random variable, we simply select $X = 1$ if $U < p$ otherwise $X = 0$. Similarly a binomial random variable can be generated using individual Bernoulli variables as described. A more efficient method is to use the inverse transform method. For number of successes $0, 1, 2, \ldots, n$, we must calculate the probability mass function. This can be done efficiently using recursion
\begin{align}
        p_{i} = P(X = i) = \binom{n, i} p^{i} (1-p)^{n-i}\newline
        \frac{p_{i+1}}{p_{i}} = \frac{n-i}{i+1} \frac{p}{1-p}
    \end{align}

The algorithm is then simply

1.  Assign $i = 0, P = p_{0} = (1-p)^{n}, F = P, b = p/(1-p)$

2.  Generate random number $U \in (0, 1)$

3.  if $U \leq F, X = i$, stop else continue

4.  Update $P$ to get $p_{i+1}$, $P = Pb\frac{n-i}{i+1}$

5.  Update the cumulative probability $F = F + P$

6.  increase $i = i + 1$, goto 3

The average number of iterations taken by the algorithm $= E[X + 1] = np + 1$ since total values checked are $n + 1$.
