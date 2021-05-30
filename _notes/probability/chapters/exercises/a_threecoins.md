---
title: "Answer"
---

Define $X$ as the following random variable
\begin{alignat}{1}
            X = \begin{cases} 1, p = \frac{1}{4} &\mbox{$HHH$ or $TTT$}\newline
                             0, p = \frac{3}{4} &\mbox{otherwise} \end{cases}\newline
        \end{alignat}

1.  $K$ is simply a binomial distribution, where we want the $2^{nd}$ success to happen at the $K+1$th trial.
    \begin{align}
                    p_{K}(k) = \binom{k}{1}\frac{1}{4}^{2}\frac{3}{4}^{k-1} \quad\text{since the last trial is success}
                \end{align}

2.  $M$ = number of tails before first success. Let the success be at $N+1$. Defin $Y$ as
    \begin{alignat}{2}
                    Y &= \begin{cases} 1 \quad p=\frac{1}{2} &\mbox{$HHT$, $HTH$, or $THH$}\newline
                                     2 \quad p=\frac{1}{2} &\mbox{$HTT$, $THT$, or $TTH$} \end{cases}\newline
                    E[Y] &= 1 \times \frac{1}{2} + 2 \times \frac{1}{2}\newline
                    Var(Y) &= (1 - \frac{3}{2})^{2} \times \frac{1}{2} + (2 - \frac{3}{2})^{2} \times \frac{1}{2}\newline
                    E[N+1] &= \frac{1}{p} = 4\newline
                    Var(N+1) &= Var(N) = \frac{1-p}{p^{2}} = \frac{1 - \frac{1}{4}}{\frac{1}{4}^{2}}\newline
                    M &= Y_{1} + Y_{2} + \cdots Y_{N}\newline
                    E[M] &= E[Y_{1} + Y_{2} + \cdots Y_{N}]\newline
                    Var(M) &= Var(Y_{1} + Y_{2} + \cdots Y_{N})\newline
                \end{alignat}
    Note that both $Y$ and $N$ are random variables here. Using the formulae for random number of random variables,
    \begin{align}
                    E[M] &= E[E[M|N]] = E[NE[Y]] = E[N]E[Y] = (4-1) \times \frac{3}{2} = \frac{9}{2}\newline
                    Var(M) &= Var(E[M|N]) + E[Var(M|N)] = Var(NE[Y]) + E[NVar(Y)]\newline
                        &= E[Y]^{2}Var(N) + E[N]Var(Y) = \frac{9}{4} \times 12 + 3 \times \frac{1}{4} = \frac{111}{4}
                \end{align}
