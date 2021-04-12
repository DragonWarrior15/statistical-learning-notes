---
title: "Subspace"
---

# Subspace

A subset $U$ of vector space $\setv$ is called a subspace if $U$ is also a vector space on the same definitions of addition and scalar multiplication as on $\setv$.


## Conditions for subspace

A subset $U$ of vector space $\setv$ is a subspace of $\setv$ if and only if $U$ satisfies the following three conditions

-   Additive Identity

    The additive identity $0 \in U$

-   Closed under Addition

    If $u,v \in U$, then $u + v \in U$

-   Closed under Multiplication

    If $u \in U$, then $\lambda u \in u$ for all $\lambda \in \field$

With these conditions, empty sets are not a vector subspace of $\setv$ and must contain at least one element to qualify as a vector space. The smalles subspace of $\setv$ is $\{ 0 \}$ and the largest subspace is $\setv$ itself.


It is easy to verify that the subspaces of $\real^{2}$ are $\{ 0\}$, $\real^{2}$ and all lines through the origin ($0$). For $\real^{3}$, the subspaces will be $\{ 0\}$, $\real^{3}$, the set of all lines through origin, and the set of all planes through the origin.

## Sum of Subspaces

For subsets $U_{1}, U_{2}, \ldots U_{m}$ of $\setv$, the sum denoted by $U_{1} + U_{2} + \cdots + U_{m}$ is the set of all possible sums of elements of all the $m$ subsets. More precisely
\begin{align}
    U_{1} + U_{2} + \cdots + U_{m} = \{u_{1} + u_{2} + \cdots + u_{m} | u_{1} \in U_{1}, u_{2} \in U_{2}, \ldots, u_{m} \in U_{m} \}\end{align}

Furthermore, this sum of subspaces is the smallest subspace containing all the subspaces $U_{1}, \ldots, U_{m}$.

## Direct Sum

For subsets $U_{1}, U_{2}, \ldots, U_{m}$, the direct sum is denoted by
\begin{align}
    U_{1} + U_{2} + \cdots + U_{m} = U_{1} \oplus U_{2} \oplus \cdots \oplus U_{m}\end{align}

The sum is a direct sum when any element of the direct sum can be expressed as the sum of elements of the subsets in a unique way.
\begin{align}
    U_{1} \oplus U_{2} \oplus \cdots \oplus U_{m} = u_{1} + u_{2} + \cdots + u_{m}\end{align}
where $u_{i} \in U_{i}$ and there is a unique way to write this sum.


As an example, let
\begin{align}
    U_{1} &= {(x,y,0) | x,y \in \field}\newline
    U_{2} &= {(0,0,z) | z \in \field}\newline
    U_{1}, U_{2} &\in \field^{3}\newline
    \text{Then,} \: \field^{3} &= U_{1} \oplus U_{2}\end{align}

$U_{1} + \cdots + U_{m}$ is a direct sum if and only if there is a way to write $0$ as a sum $u_{1} + \cdots + u_{m}$ such that all the $u_{i}$ are $0$.


The sum of two subspaces is a direct sum if and only if the intersection of those two subspaces is $0$, i.e., for $U, W \in \setv$, we have $U \cap W = \{ 0 \}$
