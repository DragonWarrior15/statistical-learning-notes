---
title: "Answer"
---

This quantity can be calculated using the law of total expectation
\begin{align}
            E[X] = E[X \vert A_{1}]P(A_{1}) + E[X \vert A_{2}]P(A_{2}) + \cdots + E[X \vert A_{n}]P(A_{n}) \quad\text{where $A_{i}$ are disjoint}
        \end{align}
Let $H_{1}$ denote heads at first toss, $H_{2}$ denote heads at the second toss, $T_{1}$ denote tails at first toss and $T_{2}$ denote tails at the second toss. Then,
\begin{align}
            E[X] &= E[X \vert H_{1}]P(H_{1}) + E[X \vert T_{1}]P(T_{1})\newline
            E[X \vert H_{1}] &= E[X \vert H_{1}H_{2}]P(H_{2} \vert H_{1}) + E[X \vert H_{1}T_{2}]P(T_{2} \vert H_{1})\newline
                    &= 2p + (1 + E[X \vert T_{1}])(1-p)\newline
            E[X \vert T_{1}] &= E[X \vert T_{1}T_{2}]P(T_{2} \vert T_{1}) + E[X \vert T_{1}H_{2}]P(H_{2} \vert T_{1})\newline
                    &= 2(1-p) + (1 + E[X \vert H_{1}])p\newline
        \end{align}
$E[X \vert H_{1}T_{2}] = 1 + E[X \vert T_{1}]$ because the tails after the first heads implies the first heads is now irrelevant and we have wasted one toss on the heads. The remaining process is same as starting from the first coin toss as tails.

Solving for the conditional expectations,
\begin{align}
            E[X \vert H_{1}] &= \frac{3 - 2p + p^{2}}{1 - p + p^{2}}\newline
            E[X \vert T_{1}] &= \frac{2 + p^{2}}{1 - p + p^{2}}\newline
            E[X] &= \frac{2 + p - p^{2}}{1 - p + p^{2}}
        \end{align}
