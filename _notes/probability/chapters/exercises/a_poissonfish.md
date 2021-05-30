---
title: "Answer"
---

-   P(fish for $> 2$ hours) = $P(k=0, \tau=2)$ = $e^{-0.6 \times 2}$

-   P(fish for $> 2$ but $< 5$ hours) = P(first catch in $[2,5]$ hours) = $P(k=0,\tau=2)(1-P(k=0,\tau=3)$ which is no fish in $[0,2]$ but at least $1$ fish in the next $3$ hours (which will be independent of first $2$ hours)

-   P(catch at least two fish) = P(at least $2$ catches before $2$ hours) = $1 - P(k=0,\tau=2) - P(k=1,\tau=2)$

-   $E\[fish\]$ has two possibilities, either single fish after $2$ hours, or many fist before $2$ hours.
    \begin{align}
        E\[fish\] &= E\[fish \vert \tau \leq 2\](1-P(\tau > 2)) + E\[fish \vert \tau > 2\] P(\tau > 2)\newline
        &= (0.6 \times 2) \times (1-P(k=0,\tau=2)) + 1 \times P(k=0,\tau=2)
    \end{align}

-   $E\[$Total fishing time$\]$ = $2 + P(k=0,\tau=2)\frac{1}{\lambda}$, since we fish for atlest $2$ hours

-   $E\[$future fishing time $\vert$ fished for two hours$\]$ can be obtained using the memoryless property of Poisson process. The expected time till first arrival is independent of what has happened till now. Thus, $E[T_{1}] = \frac{1}{\lambda}$
