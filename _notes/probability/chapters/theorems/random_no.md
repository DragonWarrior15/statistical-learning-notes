---
title: "Random number of Random Variables"
---

## Random number of Random Variables

Let $X_{i}$ be independent identically distributed Random Variables and let $Y = \sum_{i=1}^{N} X_{i}$ be the sum of $N$ such random variables where $N$ itself is a random variable. Then,
\begin{align}
        Y &= X_{1} + X_{2} + \cdots + X_{N}\newline
        E[Y|N=n] &= \sum_{i=1}^{n}E[X_{i}]\newline
                &= NE[X]\newline
        E[Y] &= E[E[Y|N]] = E[NE[X]]\newline
            &= E[N]E[X] \quad \text{since $E[X]$ will be a number}\newline
        Var(Y) &= E[Var(Y|N)] + Var(E[Y|N])\newline
            &= E[NVar(X)] + Var(NE[X])\newline
            &= E[N]Var(X) + E[X]^{2}Var(N)
    \end{align}
