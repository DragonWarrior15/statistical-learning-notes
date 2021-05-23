---
title: "Absorption Probabilities"
---

## Absorption Probabilities

let $a_{i}$ denote the probability of absorption and $\mu_{i}$ denote the expected no of steps until absorption starting from state $i$. Then,
\begin{align}
        a_{i} &= \sum_{j} a_{j}p_{ij} \quad\text{outflux to the possible states}\newline
        \mu_{i} &= 1 + \sum_{j} \mu_{j} p_{ij}
    \end{align}
For multipe absorption states, we can possibly consider them together as a group and calculate the relevant quantities.

For a given state $s$,
\begin{align}
        E[\text{steps to first time reach $s$ from $i$}] &= t_{i} \newline
        t_{i} &= E[min (n \geq 0 \text{ such that } X_{n} = s)] \newline
        t_{s} &= 0 \newline
        t_{i} &= 1 + \sum_{j} t_{j}p_{ij} \quad\text{outflux to all possible states}
    \end{align}

Mean recurrence time (mean time to reach back a state) for $s$
\begin{align}
        t_{s}^{\*} &= E[min (n \geq 1 \text{ such that } X_{n}=s) | X_{0} = s] \newline
        t_{s}^{\*} &= 1 + \sum_{j} t_{j} p_{ij}
    \end{align}
