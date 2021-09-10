---
title: "Exponential Distribution"
---

## Exponential Distribution

Exponential distribution is characterized by the parameter $\lambda$ and has the following probability distribution
\begin{align}
        f_{X}(x) = \begin{cases} 0 &\mbox{if $x < 0$}\newline
                                \lambda e^{-\lambda x} &\mbox{otherwise} \end{cases}
    \end{align}

Exponential distribution is used to represent the interarrival time probability distribution in the context of Poisson Process. The cumulative distribution is given by
\begin{align}
        F_{X}(x) &= \begin{cases} 0 &\mbox{if $x < 0$}\newline
                                1 - e^{-\lambda x} &\mbox{otherwise} \end{cases}\newline
        P(X > x) &= \int_{x}^{\infty} \lambda e^{-\lambda x} dx\newline
        &= e^{-\lambda x}
    \end{align}

### Mean and Variance

The mean of the distribution is given by
\begin{align}
        E[x] &= \int_{0}^{\infty} \lambda x e^{-\lambda x} dx\newline
        &= [-x e^{-\lambda x}]\_{0}^{\infty} + \int_{0}^{\infty} e^{-\lambda x} dx = \frac{1}{\lambda}\newline
        E[X] &= \frac{1}{\lambda}
    \end{align}
where we used integration by parts, $\int uv' = uv - \int u'v$ and substituted $u = x$ and $v = -e^{-\lambda x}/\lambda$.


For variance, we first calculate the value of $E[x^{2}]$
\begin{align}
        E[x^{2}] &= \int_{0}^{\infty} \lambda x^{2} e^{-\lambda x} dx\newline
        &= [-x^{2} e^{-\lambda x}]\_{0}^{\infty} + \int_{0}^{\infty} 2x e^{-\lambda x} dx\newline
        &= [\frac{-2x e^{-\lambda x}}{\lambda}]\_{0}^{\infty} - [\frac{2e^{-\lambda x}}{\lambda^{2}}]\_{0}^{\infty}\newline
        &= \frac{2}{\lambda^{2}}\newline
        Var(X) &= E[X^{2}] - E[X]^{2}\newline
        Var(X) &= \frac{1}{\lambda^{2}}
    \end{align}
The above property can be generalized for the $n$th power as well
\begin{align}
        E[X^{n}] = \frac{n!}{\lambda^{n}}
    \end{align}

### Moment Generating Function

The moment generating function of an exponential distribution can be derived as follows
\begin{align}
        E[e^{tX}] &= \int_{0}^{\infty} e^{tx} \lambda e^{-\lambda x} dx = \frac{\lambda}{\lambda - t} \int_{0}^{\infty} (\lambda - t) e^{-(\lambda - t)x} dx\newline
        &= \frac{\lambda}{\lambda - t}
    \end{align}
since quantity under the integral is an exponential distribution with the parameter $\lambda - t$.

### Memoryless Property

A fundamental mathematical property of the exponential distribution is the memoryless property. In summary, this means that whatever has transpired till now will not affect the future distribution. Mathematically $P(T > t+s)$ is independent of t
\begin{align}
        P(T > t+s | T>t) &= \frac{P(T> t+s \text{ and }T > t)}{P(T > t)}\newline
        &= \frac{P(T > t + s)}{P(T > t)}\newline
        &= \frac{e^{-\lambda(t+s)}}{e^{-\lambda t}}\newline
        &= e^{-\lambda s}\newline
        P(T > t+s | T>t) &= P(T > s)
    \end{align}

### Minimum of Exponential Variables

If $X_{1}, \ldots X_{n}$ are $n$ independent exponentially distributed random variables with $X_{i} \sim Exponential(\lambda_{i})$, then the distribution of the minima is also Exponential.
\begin{align}
        P(min(X_{1}, \ldots, X_{n}) > x) &= P(X_{1} > x, \ldots, X_{n} > x)\newline
        &= P(X_{1} > x) P(X_{2} > x) \ldots P(X_{n} > x) \; \text{by independence}\newline
        &= \prod_{i=1}^{n} e^{-\lambda_{i} x}\newline
        &= \exp(-\sum_{i=1}^{n} \lambda_{i} x)\newline
        \implies min(X_{1}, \ldots, X_{n}) &\sim Exponential(\lambda_{1} + \cdots + \lambda_{n})
    \end{align}
