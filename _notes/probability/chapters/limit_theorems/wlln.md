---
title: "Weak Law of Large Numbers"
---

## Weak Law of Large Numbers

The weak law of large numbers provides bounds on the error between the true mean of a distribution and its estimated value from a sequence of random variables. Let $X_{1}, X_{2}, \ldots, X_{n}$ be a sequence of $n$ identically distributed random variables with mean $\mu$ and (a finite) variance $\sigma^{2}$, then
\begin{align}
        M_{n} &= \frac{X_{1} + \cdots + X_{n}}{n}\newline
        P(\mid M_{n} - \mu \mid \geq \epsilon) &\leq \frac{\sigma^{2}}{n\epsilon^{2}}\newline
        \lim_{n \to \infty} P(\mid M_{n} - \mu \mid \geq \epsilon) &\to 0
    \end{align}

For a distribution with finite variance, the above follows from Chebychev's inequality on $M_{n}$
\begin{align}
        M_{n} &= \frac{X_{1} + X_{2} + \cdots + X_{n}}{n} \newline
        E[M_{n}] &= \frac{1}{n} \sum_{i=1}^{n} E[X_{i}] = \mu \quad\text{expectation of expectation} \newline
        Var(M_{n}) &= \sum_{i=1}^{n} Var(\frac{X_{i}}{n}) = \frac{\sigma^{2}}{n} \quad\text{since $X_{i}$ are independent} \newline
        P(\mid M_{n} - \mu \mid \geq \epsilon) &\leq \frac{\sigma^{2}}{n\epsilon^{2}}
    \end{align}
The above expression allows us to calculate the probability that $M_{n}$ falls in the interval $[\mu-\epsilon, \mu+\epsilon]$. As the value of $epsilon$ grows smaller, we will require a large value of $n$ to be able to confidently say that $M_{n}$ indeed falls in that range.


In cases where the true variance of the distribution is not known, we can still use the above inequality in the context of an upper bound on the variance. For instance, it can be shown that the variance of a $Bernoulli(p)$ is $p(1-p) \leq 1/4$.
