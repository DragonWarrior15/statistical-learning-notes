---
title: "Convolutions"
---

## Convolutions

Convolution operations are defined for both CDF and PDF/PMFs. Let $X$ and $Y$ be random independent variables, then
\begin{alignat}{2}
    F_{X+Y}(x) &= F_{X} * F_{Y} &&= \int_{\mathbb{R}} F_{X}(x-y) dF_{Y}(y)\newline
    p_{X+Y}(x) &= p_{X} * p_{Y} &&= \int_{\mathbb{R}} p_{X}(x-y) p_{Y}(y) dy
\end{align}

We can extend the idea to $n$ independent variables as
\begin{align}
    F_{X}^{n\*} = F_{X} * \cdots * F_{X} \text{ $n$ times}\end{align}
It has the following properties for positive random variable $X_{i}$s

1.  \begin{align}
            F_{X}^{n\*}(x) \leq F_{X}^{n}(x)
        \end{align}
    This can be proven as
    \begin{align}
            P(X_{1} + \cdots + X_{n} \leq x) &\leq P(X_{1} \leq x, \ldots, X_{n} \leq x)\newline
            P(X_{1} + \cdots + X_{n} \leq x) &\leq \prod_{i=1}^{n} P(X \leq x) \text{ by independence}\newline
            \text{or, } F_{X}^{n\*}(x) &\leq F_{X}^{n}(x)
        \end{align}

2.  \begin{align}
            F_{X}^{n\*}(x) \geq F_{X}^{n+1}(x)
        \end{align}
    which follows immediately from the fact that
    \begin{align}
            P(X_{1} + \cdots + X_{n} \leq x) &\geq P(X_{1} \leq x, \ldots, X_{n+1} \leq x)\newline
        \end{align}
    since the volume of the regions denoting the sums will be lower in the higer dimensions. This can be quickly verified by considering $X_{1} \leq 1$ and $X_{1} + X_{2} <= 1$.
