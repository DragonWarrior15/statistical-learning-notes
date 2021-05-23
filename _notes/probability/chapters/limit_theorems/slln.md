---
title: "Strong Law of Large Numbers"
---

## Strong Law of Large Numbers

This law is similar to the weak law, but deals with the convergence of the mean. Let $X_{i}$ be $n$ independent identically distributed random variables with mean $\mu$. Then the mean $M_{n}$,
\begin{align}
        \lim_{n \to \infty} P(M_{n} = \mu) = 1
    \end{align}

That is, $M_{n}$ converges to $\mu$ with probability $1$ or **almost surely**. Convergence with probability $1$ implies convergence in probability, but the converse is not always true.


There is a subtle differnce between WLLN and SLLN. WLLN states that the probability of deviation of $M_{n}$ from the true mean is always finite, although the probability of deviation converges to $0$ in the limit. On the other hand, SLLN states with absolute certainty that in infinite experiments, the sample mean will converge to the true mean with probability $1$.
