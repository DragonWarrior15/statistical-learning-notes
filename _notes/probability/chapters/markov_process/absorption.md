---
title: "Absorption Probabilities"
---

## Absorption Probabilities

For a fixed absorbing (_final_) state $s$, let $a_{i}$ denote the probability of absorption given the initial state is $i$. Assuming we start from a transient state, we have the following equations to solve for $a_{i}$
\begin{align}
    a_{s} &= 1\newline
    a_{i} &= 0 \quad\text{for all $i \neq s$, $i$ is aborbing state}\newline
    a_{i} &= \sum_{j}a_{j}p_{ij}
\end{align}

The last equation follows from the law of total probability. Let $A$ be the event of absorption to state $s$
\begin{align}
    a_{i} &= P(A \vert X_{0} = i)\newline
    &= \sum_{j}P(A \vert X_{1} = j, X_{0} = i)P(X_{1} = j \vert X_{0} = i)\newline
    &= \sum_{j}a_{j}p_{ij}\quad\text{outflux to the possible states}
\end{align}

Be cognizant of the flow in the last equation. $a_{i}$ denotes the absoption probability into state $s$ given $i$ as the starting state. To utilize the law of total probability, we move 1 step into all the states directly connect with $i$ and assume we will start the absorption cycle again ($a_{j}$).

For multiple absorption states, we can consider them together as a group with a single absorption probability and setup the equations.

Going further, let $\mu_{i}$ denote the expected no of steps until absorption (in a recurrent state) starting from a transient state $i$. Clearly $\mu_{i}$ is zero if $i$ is recurrent since we are already in a recurrent state. The equations thus setup as
\begin{align}
    \mu_{i} &= 0 \quad\text{if $i$ is recurrent}\newline
    \mu_{i} &= 1 + \sum_{j} \mu_{j} p_{ij}
\end{align}
The last equation is derived using law of total probability similar to how we did earlier. The small change that comes now is to account for the 1 step we have taken to move from $i \to j$.

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
