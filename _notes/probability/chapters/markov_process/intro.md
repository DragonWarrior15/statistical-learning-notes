---
title: "Markov Process"
---

# Markov Process

Markov Process is a discrete time process that is not memoryless. Here the random variable takes several possible states, and the probability distribution is defined in such a way that $P(\text{transition from state 1 to state 2})$ is dependent on state 1.


Let $X_{n}$ be the random variable denoting the state after n transitions and $X_{0}$ will represent the starting state (which can be given or random). Markov assumption states that *Given the current state, past does not matter*. Armed with these,
\begin{align}
        p_{ij} &= P(\text{next state $j$ $|$ current state $i$})\newline
        p_{ij} &= P(X_{n+1}=j|X_{n}=i) = P(X_{n+1}=j|X_{n}=i, X_{n-1}, \ldots, X_{0})\newline
        r_{ij}(n) &= P(X_{n}=j|X_{0}=i) \quad\text{or, in state $j$ after $n$ steps}\newline
        r_{ij}(n) &= \sum_{k=1}^{m} r_{ik}(n-1)p_{kj}
    \end{align}

We can form a transition matrix M such that $M_{ij} = p_{ij}$. To get the probability of transition from state $i \to j$ after $n$ steps, we can refer to the $ij$ entry of the matrix $M^{n}$ (since this multiplication will take summation from all possible routes to reach $j$ from $i$).
