---
title: "Chebychev Inequality"
---

## Chebychev Inequality

For any random variable $X$ with mean $\mu$ and variance $\sigma^{2}$, and a positive $k$,
\begin{align}
        P(\lvert X - \mu \rvert \geq k) \leq \frac{\sigma^{2}}{k^{2}}
    \end{align}
This means that for a random variable with small variance, the probability of taking a value far from the mean is small.


This can be proved using Markov's inequality on the non negative random variable $(X-\mu)^{2}$ and positive $k^{2}$
\begin{align}
        P((X-\mu)^{2} \geq k^{2}) &\leq \frac{E[(X-\mu)^{2}]}{k^{2}}\newline
        \text{or, } \; P(\lvert X - \mu \rvert \geq k) &\leq \frac{\sigma^{2}}{k^{2}}
    \end{align}

Substituiting $k = c\sigma$,
\begin{align}
        P(\lvert X - \mu \rvert \geq c\sigma) \leq \frac{1}{c^{2}}
    \end{align}
