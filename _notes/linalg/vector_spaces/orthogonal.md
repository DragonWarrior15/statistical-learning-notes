---
title: "Orthogonal and Orthonormal Vectors"
---

# Orthogonal and Orthonormal Vectors

A collection of vectors $v_{1}, \ldots, v_{m}$ is said to be **orthogonal** or **mutually orthogonal** if any pair of vectors in that collection is perpendicular to each other.
\begin{align}
    \text{orthogonal if } v_{i}^{T}v_{j} = 0 \text{ for all } i \neq j, i,j = 1,2,\ldots, m\end{align}

Extending this definition, a collection of orthogonal vectors is said to be **orthonormal** or **mutually orthonormal** if they all have norm as $1$
\begin{align}
    \text{orthogonal if } v_{i}^{T}v_{j} = \begin{cases} 1 &\mbox{$i = j$}\newline 0 &\mbox{otherwise} \end{cases} \: i,j = 1,2,\ldots, m\end{align}

Any set of orthonormal vectors is linearly independent. This can be shown as
\begin{align}
    0 &= \alpha_{1}v_{1} + \cdots + \alpha_{m}v_{m}\newline
    0 &= v_{i}^{T}(\alpha_{1}v_{1} + \cdots + \alpha_{m}v_{m})\newline
    0 &= \alpha_{i}v_{i}^{T}v_{i} = \alpha_{i}\newline
    \Rightarrow 0 &= \alpha_{i}\end{align}
because all the vectors in the collection have a norm $1$.


To express any vector as a linear combination of orthonormal vectors, we can use the following formula to derive the coefficients
\begin{align}
    v &= \alpha_{1}v_{1} + \cdots + \alpha_{m}v_{m}\newline
    v_{i}^{T}v &= v_{i}^{T}(\alpha_{1}v_{1} + \cdots + \alpha_{m}v_{m})\newline
    v_{i}^{T}v &= \alpha_{i}\newline
    \Rightarrow v &= (v_{1}^{T}v)v_{1} + \cdots + (v_{m}^{T}v)v_{m}\end{align}

Since a collection of orthonormal vectors is linearly independent, they are also a **basis**, and they are also known as an **orthonormal basis**. The previous equation can be used to derive the expression to express any vector as a linear combination of the orthonormal basis.

## Gram-Schmidt Algorithm

This algorithm can be used to determine if a collection of vectors is linearly independent. For a collection of vectors $v_{1}, \ldots, v_{m}$ the algorithm terminates if it finds $v_{j}$ can be expressed as a linear combination of $v_{1}, \ldots, v_{j-1}$. In other words, the algorithm attempts to find the first vector that is linearly dependent on the previous vectors.


The algorithm produces sequentially a collection of orthonormal vectors and stops when it encounters a zero vector.

for $i = 1, \ldots, m$ :

-   Orthogonalization: $\tilde{q}\_{i} = v_{i} - (q_{1}^{T}v_{i})q_{1} - \cdots - (q_{i-1}^{T}v_{i})q_{i-1}$

-   Test for Linear Independence: if $\tilde{q}\_{i} = 0$, quit

-   Normalization: $q_{i} = \tilde{q}\_{i}/ \lvert\lvert \tilde{q}\_{i} \rvert\rvert$

If the algorithm terminates with exiting in between, we indeed have a collection of linearly depenent vectors with us.


To show why the algorithm works, consider $i = 1$, the first iteration. $\tilde{q}\_{1} = v_{1}$ and $q_{1} = v_{1}/\lvert\lvert v_{1} \rvert\rvert$. In the second iteration, $\tilde{q}\_{2} = v_{2} - (q_{1}^{T}v_{2})q_{1}$. $q_{1}^{T}\tilde{q}\_{2} = 0$ showing that $\tilde{q}\_{2} \perp q_{1}$. We can show a similar argument $\tilde{q}\_{i} \perp q_{i-1}$ using induction and the orthogonalization step. Furthermore, $v$ are linear combinations of $q$ and vice versa. Hence, if $\tilde{q}\_{i} = 0$ for some $i$, $v_{i}$ is a linear combination of all the previous $v$.
