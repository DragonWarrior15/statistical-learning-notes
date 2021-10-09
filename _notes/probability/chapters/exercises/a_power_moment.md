---
title: "Answer"
---

Since the two random variables are independent
\begin{align}
    E[e^{tY}] &= E[e^{t(2X_{1} + 6X_{2})}] = E[e^{(2t)X_{1}}]E[e^{(6t)X_{2}}]\newline
    &= \phi_{1}(2t)\phi_{2}(6t)
\end{align}

For a $Gamma(\alpha, \lambda)$, the mgf is
\begin{align}
    mgf = \roundbr{\frac{\lambda}{\lambda - t}}^{\alpha}
\end{align}

Hence,
\begin{align}
    E[e^{tY}] &= \roundbr{\frac{1/3}{1/3 - (2t)}}^{3}\roundbr{\frac{1}{1 - (6t)}}^{5}\newline
    &= \roundbr{\frac{1}{1 - 6t}}^{8} = \roundbr{\frac{1/6}{1/6 - t}}^{8}
\end{align}

which is the mgf of $Gamma(8, 1/6)$
