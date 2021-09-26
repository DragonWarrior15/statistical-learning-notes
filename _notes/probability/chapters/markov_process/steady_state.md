---
title: "Steady State Probabilities"
---

## Steady State Probabilities

Do $r_{ij}(n)$ converge to some $\pi_{j}$ (independent of i) ? where $\pi_{j}$ denotes the steady state probability of occupancy of state $j$, or $P(X_{n} = j)$ for large $n$.

Yes if,
* recurrent states are all in a single class
* single recurrent class is not periodic (otherwise oscillations are possible)

Assuming yes,
\begin{align}
        r_{ij}(n) &= \sum_{k} r_{ik}(n-1)p_{kj}\newline
        \lim_{n \to \infty} r_{ij}(n) &= \lim_{n \to \infty} \sum_{k} r_{ik}(n-1)p_{kj}\newline
        \pi_{j} &= \sum_{k} \pi_{k} p_{kj} \quad\text{balance equations} \newline
        \mbox{and,} \sum_{i} \pi_{i} &= 1 \newline
        \text{frequency of transitions $k \rightarrow j$} &= \pi_{k} p_{kj} \quad\text{in one step}\newline
        \text{frequency of transitions into $j$} &= \sum_{k} \pi_{k} p_{kj} \quad\text{influx from all connected states}
    \end{align}

The $pi_{j}$ sum up to 1 and form a probability distribution called the **stationary distribution** of the chain (because if the initial distribution $P(X_{0} = j) = \pi_{j}$, the occupancy distribution of the states is constant for all steps and can be verified using total probability theorem on any of the nodes).

In the steady state,
* $\pi_{j} = 0$ for transient states
* $\pi_{j} > 0$ for recurrent states
(note that any state that is absorbing is actually recurrent since its only connected to itself and hence _accessible_ to itself from itself)
