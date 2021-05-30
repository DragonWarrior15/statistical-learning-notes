---
title: "Vector Space"
---

# Vector Space

We first define addition and multiplication on a set $\setv$.


-   **Addition**

    Addition on set $\setv$ is a function that assigns an element $u + v \in \setv$ for every element $u, v \in \setv$.

-   **Scalar Multiplication**

    Multiplication on set $\setv$ is a function that assigns an element $\lambda v \in \setv$ for every element $\lambda \in \setv$ and $v \in \setv$.

$\field$ is a set of real or complex numbers.


A ***Vector Space*** is a set $\setv$ with addition and multiplication defined on $\setv$ and the following properties hold.

-   **Commutativity**

    $u + v = v + u$ where both $u,v \in \setv$

-   **Associativity**

    $(u + v) + w = u + (v + w)$ and $(ab)v = a(bv)$ for all $u,v,w \in \setv$ and $a,b \in \field$

-   **Additive Identity**

    There exsits an element $0 \in \setv$ such that $v + 0 = v$ for all $v \in \setv$. This element is unique. Mutilication of any element $a \in \field$ by $0$ results in $0$.

-   **Additive Inverse**

    For every element $v \in \setv$ there exists $w \in \setv$ such that $v + w = 0$. This element is unique. Because of the uniqueness, the additive inverse of $v$ is denoted by $-v$ such that $v + (-v) = 0$. Multiplying an element with the scalar $-1$ also results in the additive inverse of that element.

-   **Multiplicative Identity**
    There exists an element $1 \in \field$ such that $1 \times v = v$ for all $v \in \setv$

-   **Distributive Property**

    $a(u + v) = au + av$ and $(a + b)v = av + bv$ for all $u,v \in \setv$ and $a,b \in \setv$

Elements of a vector space are called **vectors** or **points**. As we have noticed in the definitions above, the correct way to describe the vector space is to write vector space over a field $\field$. A vector space over $\real$ is called a real vector space and a vector space over $\comp$ is called a complex vector space.
