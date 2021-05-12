---
title: "Dirichlet Distribution"
---

## Dirichlet Distribution

Dirichlet Distribution is an extension of the Beta distribution to multiple random variables and is also called *Multivariate Beta Distribution* (MBD). For $K \geq 2$ it is defined as
\begin{align}
        f(x_{1}, \ldots, x_{K}, \alpha_{1}, \ldots, \alpha_{K}) = \frac{1}{B(\boldsymbol{\alpha})} \prod_{i=1}^{K} x_{i}^{\alpha_{i} - 1}\newline
        \text{with} \quad \sum_{i=1}^{K} x_{i} = 1, \quad x_{i} \geq 0 \; \forall \; i=1,\ldots,K\newline
        B(\boldsymbol{\alpha}) = \frac{\prod_{i=1}^{K}\Gamma(\alpha_{i})}{\Gamma \bigg(\sum_{i=1}^{K} \alpha_{i} \bigg)} \quad \text{with} \; \boldsymbol{\alpha} = (\alpha_{1}, \ldots, \alpha_{K})
    \end{align}
