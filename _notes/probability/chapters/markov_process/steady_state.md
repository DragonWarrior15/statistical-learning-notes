---
title: "Steady State Probabilities"
---

## Steady State Probabilities

Do $r_{ij}(n)$ converge to some $\pi_{j}$ (independent of i) ?

Yes if,

-   recurrent states are all in a single class

-   single recurrent class is not periodic (otherwise oscillations are possible)

Assuming yes,
\begin{align}
        r_{ij}(n) &= \sum_{k} r_{ik}(n-1)p_{kj}\newline
        \lim_{n \to \infty} r_{ij}(n) &= \sum_{k} r_{ik}(n-1)p_{kj}\newline
        \pi_{ij} &= \sum_{k} \pi_{ik} p_{kj} \quad\text{balance equations} \newline
        \sum_{i} \pi_{i} &= 1 \newline
        \text{frequency of transitions $k \rightarrow j$} &= \pi_{k} p_{kj} \quad\text{in one step}\newline
        \text{frequency of transitions into $j$} &= \sum_{k} \pi_{k} p_{kj} \quad\text{influx from all connected states}
    \end{align}
