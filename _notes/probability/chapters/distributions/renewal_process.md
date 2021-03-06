---
title: "Renewal Process"
---

## Renewal Process

This is a fundamental stochastic process useful in modelling arrivals and interarrival times. Some definitions will make the usage clear.


Let $S_{i}$ denote the $i$th renewal time or the time when the $i$th arrival takes place. By definition, $S_{0} = 0$. We can also define
\begin{align}
        S_{n} &= S_{n-1} + \xi_{n}\newline
        S_{n} &= \xi_{1} + \xi_{2} + \cdots + \xi_{n-1}
    \end{align}
where $\xi_{i}$ are positive ($P(\xi > 0) = 1$) independent identically distributed variables representing the interarrival times. We also define
\begin{align}
        N_{t} &= \argmax_{k} \{ S_{k} \leq t \}\newline
        \{ S_{n} > t \} &= \{ N_{t} < n \}
    \end{align}
or, $N_{t}$ is simply the number of arrivals till the time $t$.


Define the following quantity
\begin{align}
        F^{n\*} &= F_{\xi} * \ldots * F_{\xi} \text{ $n$ times}\newline
        u(t) &= \sum_{i=1}^{\infty} F^{n\*}(t)
    \end{align}
It can be shown that the function $u(t)$ converges. The expectation of $N_{t}$ then becomes
\begin{align}
        E[N_{t}] &= E[\text{number of $n$ such that $S_{n} \leq t$}]\newline
        &= E[\sum_{n=1}^{\infty} I(S_{n} \leq t)] \quad \text{ sum of Indicators will equal $n$}\newline
        &= \sum_{n=1}^{\infty} P(S_{n} \leq t) \quad \text{ since $E[$Indicator$]$ is just the function inside indicator}\newline
        &= \sum_{n=1}^{\infty} F^{n\*}(t) \quad \text{ by defining cumulative as sum of $\xi$s}\newline
        &= u(t)
    \end{align}

### Laplace Transform

For a density function $f$ defined from $\mathbb{R}^{\geq 0} \to \mathbb{R}$, Laplace transform is
\begin{align}
        L_{f}(s) = \int_{\mathbb{R}^{\geq 0}} e^{-sx} f(x) dx
    \end{align}
The following properties hold for this transform

1.  If $f$ is a probability density function, then
    \begin{align}
                E[e^{-sx}] = L_{f}(s)
            \end{align}

2.  if $f_{1}$ and $f_{2}$ are two probability density functions, then
    \begin{align}
                L_{f_{1}\*f_{2}}(s) = L_{f_{1}}(s) L_{f_{2}}(s)
            \end{align}

3.  If $F$ is the cumulative probability distribution for $X$ and $p$ is the probability density function, then
    \begin{align}
                L_{F_{X}}(s) = \frac{L_{p_{X}}(s)}{s}
            \end{align}
    which can be proven using integration by parts as follows
    \begin{align}
                L_{F_{X}}(s) = \int_{\mathbb{R}^{\geq 0}} F_{X}(x) \frac{d(e(-sx))}{s} = 0 + \frac{1}{s} \int_{\mathbb{R}^{\geq 0}} p_{X}(x) e^{-sx} dx
            \end{align}

### Calculating the Expectation

Armed with the concept of a Laplace transform, we make the following observation first
\begin{align}
        u(t) &= \sum_{i=1}^{\infty} F^{n\*}(t) = F(t) + \sum_{i=2}^{\infty} F^{n\*}(t)\newline
        &= F(t) + \big( \sum_{i=1}^{\infty} F^{n\*}(t) \big) * F(t)\newline
        &= F(t) + u(t) * F(t)\newline
       u(t) &= F(t) + u(t) * p(t)
    \end{align}
where $p$ is the probability density function and the last line stems from the fact that $\int u * F = \int u(x-y) dF(y) = \int u(x-y) p(y) dy$. Taking Laplace transform on both sides,

\begin{align}
        L_{u}(s) &= L_{F}(s) + L_{u}(s) L_{p}(s)\newline
        L_{u}(s) &= \frac{L_{p}(s)}{s} + L_{u}(s) L_{p}(s) \text{ from point 3 above}\newline
        L_{u(s)} &= \frac{L_{p}(s)}{s(1-L_{p}(s))}
    \end{align}

The last equation can be used to calculate the laplace transform of $u(t)$ and consecutively guess the functional form of $u(t)$.

### Limit Theorems for Renewal Processes

The following two theorems hold true for Renewal processes

1.  If $E[\xi] = \mu < \infty$, then
    \begin{align}
                \lim_{t \to \infty} \frac{N_{t}}{t} = \frac{1}{\mu}
            \end{align}
    which is analogous to the strong law of large numbers. This can be proven as follows
    \begin{align}
                S_{N_{t}} \leq t \leq S_{N_{t} + 1} \text{ from the definition of $N_{t}$}\newline
                \text{or, } \frac{N_{t}}{S_{N_{t} + 1}} \leq \frac{N_{t}}{t} \leq \frac{N_{t}}{S_{N_{t}}}
            \end{align}
    we can calculate the limits on the two bounds as
    \begin{align}
                \lim_{t \to \infty} \frac{N_{t}}{S_{N_{t}}} = \lim_{n \to \infty} \frac{n}{S_{n}} = \frac{1}{\mu}
            \end{align}
    from the strong law of large numbers applied to $\lim_{n \to \infty} \frac{S_{n}}{n}$. Similarly, one can show
    \begin{align}
                \lim_{t \to \infty} \frac{N_{t}}{S_{N_{t} + 1}} = \lim_{t \to \infty} \frac{N_{t}}{N_{t} + 1} \lim_{t \to \infty} \frac{N_{t} + 1}{S_{N_{t} + 1}} = 1 * \frac{1}{\mu}
            \end{align}

2.  If $Var(\xi) = \sigma^{2} < \infty$, then
    \begin{align}
                \lim_{t \to \infty} \frac{N_{t} - t/\mu}{\sigma \sqrt{t}/\mu^{3/2}} = \mathcal{N}(0,1)
            \end{align}
    which is analogous to the central limit theorem. It can be proven by considering the CLT on $\xi$s
    \begin{align}
                \lim_{n \to \infty} P(\frac{S_{n} - n\mu}{\sigma \sqrt{n}} \leq x) &= \text{CDF of }\mathcal{N}(0,1)\newline
                \text{or, } \lim_{n \to \infty} P(S_{n} \leq n\mu + \sigma \sqrt{n} x) &= \text{CDF of }\mathcal{N}(0,1)\newline
                \text{or, } \lim_{n \to \infty} P(N_{t} \geq n) &= \text{CDF of }\mathcal{N}(0,1) \text{ from definition of $N_{t}$, where $t = n\mu + \sigma \sqrt{n} x$}\newline
            \end{align}
    We substitute $n\mu = t$ for very large value of $n$, since the total time will become total variables into the expected time for one $\xi$ when $n$ is large. Hence,
    \begin{align}
                n &= \frac{t}{\mu} - \frac{\sigma \sqrt{t}}{\mu^{3/2}}x\newline
                \lim_{n \to \infty} P(N_{t} \geq n) &= \lim_{n \to \infty} P(\frac{N_{t} - t/\mu}{\sigma \sqrt{t}/\mu^{3/2}} \leq x) = \text{CDF of }\mathcal{N}(0,1)
            \end{align}
