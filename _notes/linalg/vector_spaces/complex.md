---
title: "Complex Field"
---

# Vector Fields
## Complex Field
A complex number is of the form $a + bi \in \comp$ where $a, b \in \real$ and $i^{2} = -1$. Additon and multiplication is performed as

\begin{align}
     (a + bi) + (c + di) &= (a + c) + (b + d)i\newline
     (a + bi) \times (c + di) &= a \times (c + di) + bi \times (c + di)
     = ac + adi + bci + bd \times (-1)\newline
     &= (ac - bd) + (ad + bc)i
\end{align}

Complex arithmetic satisfies the following properties
* **Commutativity**

    $\alpha + \beta = \beta + \alpha$ and $\alpha \beta = \beta \alpha \quad \forall \; \alpha, \beta \in \comp$
* **Associavity**

    $(\alpha + \beta) + \lambda = \alpha + (\beta + \lambda)$ and $(\alpha \beta)\lambda = \alpha(\beta \lambda) \quad \forall \alpha, \beta, \lambda \in \comp$
* **Identity Elements**

    There exist identity elements $0$ and $1$ such that
    $\alpha + 0 = \alpha$ and $\alpha \times 1 = \alpha \quad \forall \alpha \in \comp$
* **Additive inverse**

    For every $\alpha \in \comp, \; \exists \beta \in \comp$ which is unique with $\alpha + \beta = 0$
* **Multiplicative Inverse**

    For every $\alpha \in \comp, \; \exists \beta \in \comp$ which is unique with $\alpha \beta = 1$
* **Distributive Property**

    $\lambda(\alpha + \beta) = \lambda \alpha + \lambda \beta \quad \forall \lambda, \alpha, \beta \in \comp$

Subtraction and Division are also defined for complex numbers

\begin{align}
    \alpha - \beta &= \alpha + (-\beta)\newline
    \alpha \div \beta &= \alpha * (\frac{1}{\beta}) \quad \text{where $1/\beta$ is the multiplicative inverse of $\beta$}
\end{align}

