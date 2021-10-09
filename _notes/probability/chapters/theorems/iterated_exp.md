---
title: "Iterated Expectation and Variance"
---

## Iterated Expectation and Variance

The law of iterated expectation tells the following about expectation and variance
\begin{align}
        E[E[X|Y]] &= E[X] \newline
        Var(X) &= E[Var(X|Y)] + Var(E[X|Y])\newline
        &\geq Var(E[X|Y])
    \end{align}
To interpret the above two formulae, notice that we are talking about two random variables $X$ and $E[X \vert Y]$. Both share the same mean $E[X]$ but the latter has lower variance since we have additional information after conditioning on $Y$ (which causes the variance to be lower).


Proof for Iterated Expectation
\begin{align}
        P(X) &= \sum_{y} P(X|Y) P(Y) \newline
        \Rightarrow E[X] &= \sum_{x} xP(X) = \sum_{x} \sum_{y} xP(X|Y)P(Y) \newline
            &= \sum_{y} P(Y) \sum_{x} xP(X|Y) = \sum_{y} P(Y) E[X|Y] \newline
        \text{or, } E[X] &= E[E[X|Y]] \quad \text{($E[X|Y]$ is a function of $Y$ and not $X$)}\newline
        &= E[g(Y)] \quad \text{where $g(Y) = E[X \vert Y]$}
    \end{align}

Proof for Variance
\begin{align}
        Var(X) &= E[X^{2}] - E[X]^{2} \newline
        Var(X|Y) &= E[(X-\overline{X})^{2}|Y] = E[X^{2}|Y] - E[X|Y]^{2} \quad \text{(1)}\newline
        Var[E(X|Y)] &= E[E(X|Y)^{2}] - E[E[X|Y]]^{2}\newline
                    &= E[E[(X|Y)]^{2}] - E[X]^{2} \quad \text{(2)}\newline
        E[Var(X|Y)] &= E[E[X^{2}|Y]] - E[E[X|Y]^{2}] \quad \text{from (1)}\newline
                    &= E[X^{2}] - E[E[X|Y]^{2}] \quad \text{(3)}\newline
        E[Var(X|Y)] + Var(E[X|Y]) &= E[X^{2}] - E[X]^{2} \quad \text{adding (2) and (3)}\newline
                                    &= Var(X)
    \end{align}
