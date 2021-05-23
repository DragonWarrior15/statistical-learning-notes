---
title: "Answer"
---

Note that the required probability distribution is given by the following formula
\begin{align}
    p_{X+Y}(x) = \int_{-\infty}^{\infty} p_{X}(x-y) \times p_{Y}(y) dy\end{align}
However, note that the exponential distribution is not positive everywhere. For values $< 0$, the probability density is 0. Hence, we break the integral into three parts as follows
\begin{align}
    p_{X+Y}(x) = \int_{-\infty}^{0} p_{X}(x-y) \times p_{Y}(y) dy + \int_{0}^{x} p_{X}(x-y) \times p_{Y}(y) dy + \int_{x}^{\infty} p_{X}(x-y) \times p_{Y}(y) dy\end{align}
Carefully note that for $y$ in range $(-\infty,0]$, $p_{Y}(y) = 0$, and in the range $[x,\infty)$, $x-y < 0$, which implies $p_{X}(x) = 0$. Hence,
\begin{align}
    p_{X+Y}(x) &= \int_{0}^{x} p_{X}(x-y) \times p_{Y}(y) dy\newline
    &= \lambda \mu \exp(-\lambda x) \int_{0}^{x} \exp((\lambda - \mu)y) dy\newline
    &= \frac{\lambda \mu}{\lambda - \mu} \exp(-\lambda x) (\exp((\lambda - \mu)x) - 1)\newline
    &= \frac{\lambda \mu}{\lambda - \mu}(\exp(\mu x) - \exp(-\lambda x))\end{align}
