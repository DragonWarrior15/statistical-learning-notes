---
title: "Answer"
---

The mgf of exponential variables ($\lambda = 1$) is already known
\begin{align}
    E[e^{tX_{i}}] &= \frac{\lambda}{\lambda - t} = \frac{1}{1 - t}\newline
    E[e^{tY}] &= E[e^{t\sum_{i=1}^{4}X_{i}}] = \prod_{i=1}^{4}E[e^{tX_{i}}]\newline
    &= \roundbr{\frac{1}{1-t}}^{4}
\end{align}
which follows from the independence of the random variables. The mgf obtained is that of a Gamma distribution with parameters $\alpha = 4$ and $\lambda = 1$. It is also a known fact that the sum of independent identically distributed Exponential variables is a Gamma distribution.
