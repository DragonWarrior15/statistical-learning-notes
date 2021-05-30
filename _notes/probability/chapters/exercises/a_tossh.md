---
title: "Answer"
---

Let $X$ be the \# of tosses till first *H*. Then, $(X = 1) \cap (X > 1) = \phi$.
Using *Total Expectation Theorem*
\begin{align}
            E[X] &= P(X = 1)E[X|X = 1] + P(X > 1)E[X|X > 1] \newline
            &= 0.5 * 1 + 0.5 E[X] \newline
            \Rightarrow E[X] &= 2
        \end{align}
$P(X = 1) = 0.5$ because then we get the head in the first toss itself. Since $P(X = 1) + P(X > 1) = 1$, we have $P(X > 1) = 0.5$. $E[X] = E[X|X > 1]$ because the tosses are *independent* and thus memoryless.
