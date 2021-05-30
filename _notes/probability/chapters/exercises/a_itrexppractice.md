---
title: "Answer"
---

We use the formulae from iterated expectation to calculate these.
\begin{alignat}{2}
            P_{Y}(y) &= \begin{cases} \frac{1}{3} &y = 1\newline
                                    \frac{2}{3} &y = 2 \end{cases}\newline
            E[X] &= E[E[X \vert Y]] = \sum_{y}E[X \vert Y]P(Y)\newline
                &= 90 \times \frac{1}{3} + 60 \times \frac{2}{3}\newline
            Var(X) &= E[Var(X \vert Y)] + Var(E[X \vert Y])\newline
                  &= \sum_{y}Var(X \vert Y)P(Y) + ((90-E[E[X \vert Y])^{2}\frac{1}{3} + (60-E[E[X \vert Y]])^{2}\frac{2}{3})\newline
                  &= \frac{650}{3}
        \end{alignat}
