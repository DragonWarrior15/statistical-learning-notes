---
title: "Bernoulli Process"
---

## Bernoulli Process

Bernoulli process falls under the family of random processes, which are random variables continuously evolving over time. Bernoulli process can be described as a sequence of independent Bernoulli trials, where each trial has only two outcomes : success with $P(success) = p$ and failure.
\begin{alignat}{2}
        P_{X_{t}}(x_{t}) &= \begin{cases} p &\mbox{if $X_{t} = 1$}\newline
                                        1-p &\mbox{if $X_{t} = 0$} \end{cases}\newline
        E[X_{t}] &= p\newline
        Var(X_{t}) &= p(1-p)
    \end{alignat}

### Mean and Variance

Number of successes S in n time slots
\begin{align}
        P(S=k) &= \binom{n}{k} p^{k}(1-p)^{n-k}\newline
        E[S] &= np\newline
        Var(S) &= np(1-p)
    \end{align}

### Interarrival Times (Geometric Random Variable)

Let $T_{1}$ denote the number of trials till the first success
\begin{align}
        P(T_{1} = t) &= (1-p)^{t-1}p \quad \text{$t \in {1, 2, \ldots}$}\newline
        E[T_{1}] &= \frac{1}{p}\newline
        Var(T_{1}) &= \frac{1-p}{p^{2}}
    \end{align}
This process is memoryless as all future coin flips are independent of whatever has happened till now. Also, the distribution is a **Geometric Random Variable**.

### Sum of Interarrival times

We are interested in the total time till k arrivals. Let this random variable be $Y_{k}$
\begin{align}
        Y_{k} &= T_{1} + T_{2} + \cdots + T_{k} \quad \text{where $T_{i}$'s are i.i.d geometric with parameter $p$}\newline
        P(Y_{k} = t) &= P(\text{$k-1$ arrivals between $t=1$ to $t=t$ and last arrival at time $t$})\newline
           &= \binom{t-1}{k-1}p^{k}(1-p)^{t-k} \quad \text{$\forall\; t \geq k$}\newline
        E[Y_{k}] &= \sum_{i=1}{k}E[T_{i}]\newline
                &= \frac{k}{p}\newline
        Var(Y_{k}) &= \sum_{i=1}^{k}Var(T_{i})\newline
                    &= \frac{k(1-p)}{p^{2}}
    \end{align}
