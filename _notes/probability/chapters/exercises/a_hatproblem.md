---
title: "Answer"
---

Let $X$ denote the number of people who pick their own hat. We have been asked $E[X]$.
Let $X_{i}$ be a binary random variable denoting whether the $i^{th}$ person picked their own hat, i.e.,
\begin{alignat}{2}
            X_{i} &= \begin{cases} 1 &\mbox{if $i^{th}$ person picks their own hat}\newline
                                    0 &\mbox{otherwise} \end{cases} \newline
            P(X_{i} = 1) &= \frac{1}{n} \newline
            E[X_{i}] &= 1 \times \frac{1}{n} + 0 \times (1 - \frac{1}{n}) = \frac{1}{n}\newline
        \end{alignat}
Consequently
\begin{align}
            E[X] = E[\sum_{i=1}^{n} X_{i}] = \sum_{n=1}^{n}E[X_{i}] = 1
        \end{align}

It is interesting to see the variance of X. Note that the formula for variance is $E[X^{2}] - E[X]^{2}$. Thus,
\begin{align}
            X^{2} = (\sum_{i=1}^{n} X_{i})^{2} = \sum_{i=1}^{n} X_{i}^{2} + \sum_{i=1}^{n} \sum_{j=1, j\neq i}^{n} X_{i}X_{j} \newline
            E[X^{2}] = \sum_{i=1}^{n}E[X_{i}^{2}] + \sum_{i=1}^{n} \sum_{j=1, j\neq i}^{n} E[X_{i}X_{j}]
        \end{align}
Note that $X_{i}$ and $X_{j}$ are not independent since after the first person has picked the hat, only $n-1$ hats remain
\begin{align}
{3}
            X_{i}X_{j} &= \begin{cases} 1 &\mbox{if $X_{i} = X_{j} = 1$}\newline
                                       0 &\mbox{otherwise} \end{cases} \newline
            P(X_{i}X_{j} = 1) &= P(X_{i} = 1) P(X_{j} = 1 \vert X_{i} = 1) &&= \frac{1}{n} \times \frac{1}{n-1}\newline
            E[X_{i}X_{j}] &= 1 \times (\frac{1}{n} \times \frac{1}{n-1}) + 0 \times (1 - \frac{1}{n} \times \frac{1}{n-1}) &&= \frac{1}{n(n-1)}\newline
            E[X_{i}^2] &= 1^{2} \frac{1}{n} + 0^{2} (1-\frac{1}{n}) &&= \frac{1}{n}
        \end{align}
Putting these values in the original equation for variance
\begin{align}
{2}
            E[X_{2}] &= n \frac{1}{n} + \frac{1}{n} \frac{1}{n-1} (\frac{n(n-1)}{2} \times 2) &&= 2\newline
            Var(X) &= 2 - 1^{2} &&= 1
        \end{align}
