---
title: "F-Distribution"
---

## F-Distribution

If $\chi_{n}^{2}$ and $\chi_{m}^{2}$ are two independent chi-squared distributions with $n$ and $m$ degrees of freedom respectively, then the variable $F_{n,m}$ defined as
\begin{align}
        F_{n,m} = \frac{\chi_{n}^{2}/n}{\chi_{m}^{2}/m}
    \end{align}
is said to have an F-distribution with n and m degrees of freedom.

For any $\alpha$ between $0$ and $1$, we define $F_{\alpha, n, m}$ as
\begin{align}
        P(F_{n,m} \geq F_{\alpha, n, m}) = \alpha
    \end{align}
These values are available in standard tables for different combinations of $\alpha, n$ and $m$.


Consider
\begin{align}
        \alpha &= P(\frac{\chi_{n}^{2}/n}{\chi_{m}^{2}/m} > F_{\alpha, n, m})\newline
        &= P(\frac{\chi_{m}^{2}/m}{\chi_{n}^{2}/n} < \frac{1}{F_{\alpha, n, m}})\newline
        &= 1 - P(\frac{\chi_{m}^{2}/m}{\chi_{n}^{2}/n} \geq \frac{1}{F_{\alpha, n, m}})\newline
        \text{or} \quad P(\frac{\chi_{m}^{2}/m}{\chi_{n}^{2}/n} \geq \frac{1}{F_{\alpha, n, m}}) &= 1 - \alpha\newline
        \text{but} \quad P(F_{m,n} \geq F_{1 - \alpha, m, n}) &= 1 - \alpha\newline
        \text{From the last two equations} \quad \frac{1}{F_{\alpha, n, m}} &= F_{1-\alpha, m, n}
    \end{align}

### Mean and Variance

We state the following without proof for $X \sim F(n,m)$
\begin{align}
        E[X] &= \frac{m}{m - 2} \: m > 2\newline
        Var(x) &= \frac{2 m^{2}(m + n - 2)}{n(m - 2)^{2}(m - 4)} \: m > 4
    \end{align}
