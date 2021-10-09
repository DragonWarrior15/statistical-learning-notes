---
title: "Probability Theorems"
---

# Probability Theorems

## Set Theorems

For any three sets, the following hold true
\begin{align}
        A &= (A \cap B) \cup (A \cap B^{c}) \;where\;B\;and\;B^{c}\;are\;disjoint \newline
        A \cap (B \cup C) &= (A \cap B) \cup (A \cap C) \newline
        A \cup (B \cap C) &= (A \cup B) \cap (A \cup C)
    \end{align}

## Basic Probability Rules

\begin{align}
        &\text{If } A \cap B = \phi \text{, then } P(A \cup B) = P(A) + P(B)\newline
        &P(A|B)P(B) = P(B|A)P(A) = P(A \cap B) \quad \text{Bayes' Theorem}\newline
        &P(A) = P(A \cap B) + P(A \cap B^{c}) = P(A|B)P(B) + P(A|B^{c})P(B^{c})\newline
        &P(A \cap B \cap C) = P(A) P(B|A) P(C|B,A) \quad \text{Chain Rule}
    \end{align}

**Support** of a random variable is defined as that region of space where the probability distribution is strictly positive.

### Total Probability Theorem

Let $A_{1}$, $A_{2}$, .. ,$A_{n}$ be n disjoint events that completely cover the event space, and B be another event, then
\begin{align}
        P(B) &= P(B|A_{1})P(A_{1}) + P(B|A_{2})P(A_{2}) + \cdots + P(B|A_{n})P(A_{n})\newline
        \text{or, } P(B) &= \sum_{i=1}^{n} P(B|A_{i})P(A_{i})
    \end{align}

## Joint Probability Distributions

*Joint Probability Distributions* are defined for two or more than two variables. In this section, we only consider two variables. The formal definition is

\begin{align}
        P_{XY}(x, y) = P(X = x \;and\; Y = y)
    \end{align}

Based on this definition, the following theorems follow

\begin{align}
        \sum_{x} \sum_{y} P_{XY}(x,y) &= 1 \newline
        P_{X}(x) &= \sum_{y} P_{XY}(x,y) \quad \text{Marginal Probability} \newline
        P_{X|Y}(x|y) &= P_{X|Y}(X=x|Y=y) = \frac{P_{XY}(x,y)}{P_{Y}{y}} \newline
        \sum_{x} P_{X|Y}(x|y) &= 1 \quad \text{Since Y is fixed and we sum over all X's} \newline
        P_{XYZ}(x,y,z) &= P_{X}(x) P_{Y|X}(y|x) P_{Z|X,Y}(z|x,y) \quad \text{Chain Rule}\newline
        \text{where} \quad P_{Z|X,Y}(z|x,y) &= \frac{P_{XYZ}(x,y,z)}{P_{XY}(x,y)} \quad \text{from Bayes rule}
    \end{align}

## Independence

Two events A and B are **independent** iff
\begin{align}
        &P(A \cap B) = P(A) P(B)
    \end{align}
Note that *independence* is not the same as *disjoint*
\begin{align}
    A \cap B = \phi \Rightarrow P(A \cap B) = 0 \text{ but } P(A) \neq P(B) \neq 0
    \end{align}
Multiple events $A_{1}, A_{2}, \ldots , A_{n}$ are **mutually independent** iff
\begin{align}
        P(A_{i} \cap A_{j} \cap \ldots \cap A_{k}) = P(A_{i}) P(A_{j}) \;..\; P(A_{k}) \;\;\forall\;i,j,\ldots,k \;|\; i,j,\ldots,k \in {1,2,\ldots,n}
    \end{align}
If the above is satisfied only for pairs of random variables, then the variables are said to be **pairwise independent**.

Conditional Independence is similar to the above equation. For an event C,
\begin{align}
        P(A_{i} \cap A_{j} \cap \ldots \cap A_{k} | C) = P(A_{i}|C) P(A_{j}|C) \;..\; P(A_{k}|C) \;\;\forall\;i,j,\ldots,k \;|\; i,j,\ldots,k \in {1,2,\ldots,n}
    \end{align}

For two variables with a joint distribution $P(x,y)$, they are independent iff $P(x,y) = P(x)P(y)$ throughout the the support of the variables (where the probabilities are positive). That is, $P(A) = 0$ for all $A$ where the above equality does not hold.

Independence is not only limited to the pdf or pmf of the random variables. Two random variables are independent iff (any of the below will do)
\begin{align}
    F_{XY}(x,y) &= F_{X}(x)F_{Y}(y)\newline
    P(a < X \leq b, c < Y \leq d) &= P(a < X \leq b)P(c \leq d)\newline
    E[u(X)v(Y)] &= E[u(X)]E[v(Y)] \quad \text{if expectations exist}\newline
    M(t_{1}, t_{2}) &= M(t_{1}, 0)M(0, t_{2})
\end{align}

where $E$ is the expected value and $M$ is the mgf (moment generating function).


## Cumulative Probability Distribution

Cumulative probability distribution is defined for both discrete and continuous variables
\begin{align}
        F_{x}(X) = P(X \leq x) = \begin{cases} \int_{-\infty}^{x} p_{X}(t) dt &\mbox{$X$ is a discrete random variable}\newline
        \sum_{k <= x} P_{X}(k) &\mbox{$X$ is a continuous random variable} \end{cases}
    \end{align}

In the multivariate case,
\begin{align}
    F_{X_{1}, \ldots, X_{n}}(x_{1}, \ldots, x_{2}) &= P(X_{1} \leq x_{1}, \ldots, X_{n} \leq x_{n})\newline
\end{align}

Calculating the probability over an interval becomes easy with the cdf
\begin{align}
    P(a < X \leq b) = F_{X}(b) - F_{X}(a)
\end{align}

Every probability distribution is uniquely determined by a cdf and not a pdf/pmf. We can differentiate the cdf to obtain the pdf.
\begin{align}
    \frac{dF_{X}(x)}{dx} &= f_{X}(x)\newline
    \frac{d^{n}F_{\mathbf{X}}(\mathbf{x})}{dx_{1}\cdots dx_{n}} &= f_{\mathbf{X}}(\mathbf{x}) = f(x_{1}\cdots x_{n})\newline
\end{align}

Suppose we transform a random variable using a one-to-one function $g$ such that $Y = g(X)$. To obtain the pdf of this new random variable $Y$, we can start with the cdf.
\begin{align}
    P(Y \leq y) &= P(g(X) \leq y) = P(X \leq g^{-1}(y)) = F_{X}(g^{-1}(y))\newline
    f_{Y}(y) &= \frac{dF_{X}(g^{-1}(y))}{dy} = f_{X}(g^{-1}(y)) \lvert\frac{dg^{-1}(y)}{dy}\rvert = f_{X}(g^{-1}(y)) \lvert\frac{dx}{dy}\rvert
\end{align}

where the last term $\lvert dx/dy \rvert$ is often called **Jacobian** and denoted by **J**.
