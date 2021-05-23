---
title: "Central Limit Theorem"
---

## Central Limit Theorem

Chebychev's inequality gives a loose bound. We can do better with CLT. Let $X$ be a random variable with mean $\mu$ and variance $\sigma^{2}$, and let $X_{i}$ be independent identically distributed random variables with the same distribution as $X$. Consider the random variable $S_{n}$ defined below,
\begin{align}
        S_{n} &= X_{1} + X_{2} + \cdots + X_{n}\newline
        Z_{n} &= \frac{S_{n} - E[S_{n}]}{\sigma_{n}} \quad\text{random variable with mean $0$ and variance $1$} \newline
             &= \frac{S_{n} - nE[X]}{\sqrt{n} \sigma}\newline
        \text{Then,}\quad \lim_{n \to \infty} P \bigg(\frac{S_{n} - n\mu}{\sqrt{n} \sigma} \leq c \bigg) &= P(Z \leq c) = \Phi(c)
    \end{align}
Or, the cumulative distribution of the random variable $(S_{n} - n\mu)/\sqrt{n} \sigma$ converges to that of a standard normal.

By defining the confidence on how close we desire $S_{n}$ to the actual mean, we can calculate the required value of the $n$ using standard normal CDF tables. However, we need to have an estimate of variance of the distribution in order to estimate $n$.


As a rule of thumb, $n=30$ gives a very close approximation to the normal distribution.


Similar to the weak law of large numbers, if the variance is not available, but an upper bound on the same can be obtained, the probability of intereset can be calculated using this bound.

### De Moivre-Laplace Approximation to the Binomial

A Binomial random variable $S_{n}$ can be viewed as the sum of $n$ Bernoulli random variables $X_{i}$ with the parameter $p$. We can apply the central limit theorem to obtain the probabiliy of the variable between any two ranges
\begin{align}
        P(k \leq S_{n} \leq l) &= P(\frac{k - np}{\sqrt{n} p(1-p)} \leq \frac{S_{n} - np}{\sqrt{n} p(1-p)} \leq \frac{l - np}{\sqrt{n} p(1-p)})\newline
        &= P(\frac{S_{n} - np}{\sqrt{n} p(1-p)} \leq \frac{l - np}{\sqrt{n} p(1-p)}) - P(\frac{S_{n} - np}{\sqrt{n} p(1-p)} \leq \frac{k - np}{\sqrt{n} p(1-p)})\newline
        &\approx \Phi(\frac{l - np}{\sqrt{n} p(1-p)}) - \Phi(\frac{k - np}{\sqrt{n} p(1-p)}) \; \text{for large $n$}
    \end{align}
Since $S_{n}$ will take discrete values, $P(S_{n} <= k) = P(S_{n} < k+1)$ for any positive integer $k$. A better approximation of the above formula can be obtained by considering the middle point of $k$ and $k+1$ as applicable
\begin{align}
        P(k \leq S_{n} \leq l)&\approx \Phi(\frac{l + \frac{1}{2} - np}{\sqrt{n} p(1-p)}) - \Phi(\frac{k - \frac{1}{2} - np}{\sqrt{n} p(1-p)}) \; \text{for large $n$}
    \end{align}

This correction yields a more closer result to the actual values. With $p$ close to $1/2$, the approximation works well for $n = 40,50$ itself. The distribution is also symmetric at this point which helps the CLT. However, as the $p$ becomes closer to $0$ or $1$, larger values of $n$ are required for the approximation to be valid.


We can also calculate the value of a single point as given below
\begin{align}
        P(S_{n} = k)&\approx \Phi(\frac{k - \frac{1}{2} - np}{\sqrt{n} p(1-p)}) - \Phi(\frac{k + \frac{1}{2} - np}{\sqrt{n} p(1-p)}) \; \text{for large $n$}
    \end{align}
