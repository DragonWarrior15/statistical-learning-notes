---
title: "Counting Process"
---

## Counting Process

Counting process is used in scenarios when we want to count the occurrence of a certain event. $N_{t}$ denotes the number of events till time $t$ starting from 0. It is assumed that $N_{0} = 0$. Formal definition is


A random process $\{N_{t}, t \in [0, \infty)\}$ is said to be a counting process if $N_{t}$ is the number of events from time $t=0$ upto time $t$. For a counting process, we assume

1.  $N_{0} = 0$

2.  $N_{t} \in \{0, 1, 2, \cdots\}$ for all $t \in [0, \infty)$

3.  for $0 \leq s < t, N_{t} - N_{s}$ shows the number of events that occur in the interval $(s,t]$

### Independent Increments

We say that a continuous time counting process $N_{t}$ has independent increments if for all $0 \leq t_{1} < t_{2} < \cdots < t_{n}$, the random variables
\begin{align}
         N_{t_{2}} - N_{t_{1}}, \;N_{t_{3}} - N_{t_{2}}, \ldots, \;N_{t_{n}} - N_{t_{n-1}}
    \end{align}
are independent.


Note that these differences are nothing but the number of arrivals in a given time interval. Thus, we are equivalently saying that **the number of arrivals in any two disjoint intervals are independent**.


A very simple consequence of this property is:

Suppose we wise to find the probability of 2 arrivals in the interval $(1,2]$ and 3 arrivals in the interval $(3,5]$. Then,
\begin{align}
        P(2 \text{ arrivals in } (1,2] \text{ and } 3 \text{ arrivals in } (3,5]) = P(2 \text{ arrivals in } (1,2]) P(3 \text{ arrivals in } (3,5]))
    \end{align}
since the arrivals in disjoint intervals are independent.

### Stationary Increments

We say that a continuous time counting process $N_{t}$ has stationary increments if for all $t_{2} > t_{1} \geq 0$ and for all $r > 0$, $N_{t_{2}} - N_{t_{1}}$ and $N_{t_{2} + r}$ and $N_{t_{1} + r}$ are independent.


In other words, **the number of arrivals in a given time interval is invariant to it's location**. Note that the number of arrivals in the time interval between $t_{1}$ and $t_{2}$ is nothing but $N_{t_{2}} - N_{t_{1}}$. By the above statement, if the process has stationary increments, then this quantity is same as $N_{t_{2} - t_{1}}$, which is the distribution of the counting process itself.
