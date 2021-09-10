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

### Total Probability Theorem

Let $A_{1}$, $A_{2}$, .. ,$A_{n}$ be n disjoint events that completely cover the event space, and B be another event, then
\begin{align}
        P(B) &= P(B|A_{1})P(A_{1}) + P(B|A_{2})P(A_{2}) + \cdots + P(B|A_{n})P(A_{n})\newline
        \text{or, } P(B) &= \sum_{i=1}^{n} P(B|A_{i})P(A_{i})
    \end{align}

## Independence

Two events A and B are independent iff
\begin{align}
        &P(A \cap B) = P(A) P(B)
    \end{align}
Note that *independence* is not the same as *disjoint*
\begin{align}
    A \cap B = \phi \Rightarrow P(A \cap B) = 0 \text{ but } P(A) \neq P(B) \neq 0
    \end{align}
Multiple events $A_{1}, A_{2}, \ldots , A_{n}$ are independent iff
\begin{align}
        P(A_{i} \cap A_{j} \cap \ldots \cap A_{k}) = P(A_{i}) P(A_{j}) \;..\; P(A_{k}) \;\;\forall\;i,j,\ldots,k \;|\; i,j,\ldots,k \in {1,2,\ldots,n}
    \end{align}
Conditional Independence is similar to the above equation. For an event C,
\begin{align}
        P(A_{i} \cap A_{j} \cap \ldots \cap A_{k} | C) = P(A_{i}|C) P(A_{j}|C) \;..\; P(A_{k}|C) \;\;\forall\;i,j,\ldots,k \;|\; i,j,\ldots,k \in {1,2,\ldots,n}
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
        P_{XYZ}(x,y,z) &= P_{X}(x) P_{Y|X}(y|x) P_{Z|X,Y}(z|x,y) \quad \text{Chain Rule}
    \end{align}

## Expected Value

Before going to expected value, let's define a Random Variable
\begin{align}
        \text{Random Variable } X \text{ is a linear map : } \mathbb{R} \to \mathbb{R} \text{. The value taken by the variable is denoted by } x
    \end{align}

$X$ will have an associated probability distribution, i.e., $P_{X}(X = x)$ . Using these quantities, we have
\begin{align}
        E[X] = \sum_x xP_{X}(X = x) \quad \text{Expected Value}
    \end{align}

Based on this definition, the following theorems for expected value follow
\begin{align}
        E[\alpha] &= \alpha\newline
        E[\alpha X] &= \alpha E[X] \newline
        E[\alpha X + \beta] &= \alpha E[X] + \beta \newline
        E[g(X)] &= \sum_x g(x)P_{X}(X = x) \newline
        E[X^{2}] &= \sum_x x^{2} P_{X}(X = x) \quad \text{Also called \emph{Second Moment}}\newline
        E[X|A] &= \sum_{x} x P_{X|A}(X|A) = f(A)\;\text{and not X}\newline
        E[g(X)|A] &= \sum_{x} g(x) P_{X|A}(X|A) \newline
        E[X + Y + Z] &= E[X] + E[Y] + E[Z] \quad \text{Linearity of Expectation}\newline
        E[XY] &= \sum_{X} \sum_{Y} xy P_{XY}(x,y) \newline
        E[g(X,Y)] &= \sum_{X} \sum_{Y} g(xy) P_{XY}(x,y) \newline
        E[XY] &= E[X]E[Y] \quad \text{if X and Y are $\emph{independent}$}
    \end{align}
where $\alpha, \beta \in \mathbb{R}$, $g(X) : \mathbb{R} \rightarrow \mathbb{R}$, and $A$ is an event, $X, Y, Z$ are Random Variables.


The same formulas are valid in case of random vectors $\mathbf{X}$ and constants $\mathbf{b}$ and $\mathbf{A}$
\begin{align}
        E[\mathbf{X}] &= \begin{bmatrix}
        &E[X_{1}]\newline
        &E[X_{2}]\newline
        &\vdots\newline
        &E[X_{n}]
        \end{bmatrix}\newline
        E[\mathbf{X_{1}} + \mathbf{X_{2}} + \cdots + \mathbf{X_{n}}] &= E[\mathbf{X_{1}}] + E[\mathbf{X_{2}}] + \cdots + E[\mathbf{X_{n}}]\newline
        E[\mathbf{A}\mathbf{X}+\mathbf{b}] &= E[\mathbf{A}\mathbf{X}] + E[\mathbf{b}] = \mathbf{A}E[\mathbf{X}] + \mathbf{b}\newline
    \end{align}

### Total Expectation Theorem

The *Total Expectation Theorem* is the natural extension of the *Total Probability Theorem*
Let $A_{1}, A_{2}, \ldots, A_{n}$ be n disjoint events that completely cover the event space, and X be random variable, then
\begin{align}
        E[X] &= E[X|A_{1}]P(A_{1}) + E[X|A_{2}]P(A_{2}) + \cdots + E[X|A_{n}]P(A_{n})\newline
        \text{or, } E[X] &= \sum_{i=1}^{n} E[X|A_{i}]P(A_{i})
    \end{align}

## Variance

The formal definition of variance is
\begin{align}
        Var(X) = E[(X - \bar{X})^{2}] = E[X^{2}] - E[X]^{2}
    \end{align}
Using this definition, the following theorems follow
\begin{align}
        E[X^{2}] &= E[X]^{2} + Var(X) \newline
        Var(\alpha) &= 0 \newline
        Var(\alpha X + \beta) &= \alpha^{2} Var(X) \newline
        Var(X + Y) &= Var(X) + Var(Y) \text{if $X$ and $Y$ are independent random variables}
    \end{align}

## Cumulative Probability Distribution

Cumulative probability distribution is defined for both discrete and continuous variables
\begin{align}
        F_{x}(X) = P(X \leq x) = \begin{cases} \int_{-\infty}^{x} p_{X}(t) dt &\mbox{$X$ is a discrete random variable}\newline
        \sum_{k <= x} P_{X}(k) &\mbox{$X$ is a continuous random variable} \end{cases}
    \end{align}

## Covariance and Correlation

For any two random variables $X$ and $Y$,
\begin{align}
        Cov(X,Y) &= E[(X - \overline{X})(Y - \overline{Y})] = E[XY] - E[X]E[Y]\newline
        Cov(X,X) &= Var(X)\newline
        Corr(X,Y) &= E[\bigg(\frac{X - \overline{X}}{\sigma_{X}}\bigg) \bigg(\frac{Y - \overline{Y}}{\sigma_{Y}}\bigg)]\newline
        &= \frac{Cov(X,Y)}{\sigma_{X} \sigma_{Y}}
    \end{align}
where the correlation is also known as Pearson Correlation. Key points to note

-   *Independence* $\Rightarrow Cov(X,Y) = Corr(X,Y) = 0$, but the converse is ***not*** true

-   Correlation is dimensionless and $-1 \leq Corr(X,Y) \leq 1$ with value close to $0$ implying minimal relation and values close to $-1, 1$ implying perfect relation

**Spearman's correlation** is similar to Pearson correlation but applied on rank variables. We first rank order the variables $X$ and $Y$ independently and create a new variable $rg_{X}$ and $rg_{Y}$ that are ranks of those variables. In case of same values, the average of the positions is taken (if the order were 1 2 3 4, we would change it to 1 2.5 2.5 4, position 2 and 3 have the same value).
\begin{align}
        \rho = \frac{Cov(rg_{X}, rg_{Y})}{\sigma_{rg_{X}} \sigma_{rg_{Y}}}
    \end{align}
and there is a formula to this in the case when all ranks are distinct
\begin{align}
        d_{i} &= rg_{x,i} - rg_{y,i}\newline
        \rho &= 1 - \frac{6\sum_{i=1}^{n} d_{i}^{2}}{n(n^{2} - 1)}
    \end{align}

In case of vectors, the covariances are defined as follows
\begin{align}
        Var(X) = Cov(\mathbf{X}, \mathbf{X}) &= E[(\mathbf{X} - E[\mathbf{X}])(\mathbf{X} - E[\mathbf{X}])^{T}]\newline
        &= E[\mathbf{X}\mathbf{X}^{T} - \mathbf{X}E[\mathbf{X}]^{T} - E[\mathbf{X}]\mathbf{X}^{T} + E[\mathbf{X}]E[\mathbf{X}]^{T}]\newline
        &= E[\mathbf{X}\mathbf{X}^{T}] - E[\mathbf{X}]E[\mathbf{X}]^{T} - E[\mathbf{X}]E[\mathbf{X}]^{T} + E[\mathbf{X}]E[\mathbf{X}]^{T}\newline
        &= E[\mathbf{X} \mathbf{X}^{T}] - E[\mathbf{X}]E[\mathbf{X}]^{T}\newline
        Cov(\mathbf{X}, \mathbf{Y}) &= E[(\mathbf{X} - E[\mathbf{X}])(\mathbf{Y} - E[\mathbf{Y}])^{T}]\newline
        &= E[\mathbf{X} \mathbf{Y}^{T}] - E[\mathbf{X}]E[\mathbf{Y}]^{T}\newline
    \end{align}

Using the above definitions, we have the following formulae for variance of transformed random vectors
\begin{align}
        \mathbf{Y} &= \mathbf{A}\mathbf{X}+\mathbf{b}\newline
        E[\mathbf{Y}] &= \mathbf{A}E[\mathbf{X}]+\mathbf{b}\newline
        Var(\mathbf{Y}) &= E[(\mathbf{Y}-E[\mathbf{Y}])(\mathbf{Y}-E[\mathbf{Y}])^{T}] = E[\mathbf{Y}\mathbf{Y}^{T}] - E[\mathbf{Y}]E[\mathbf{Y}]^{T}\newline
        &= E[(\mathbf{A}\mathbf{X}+\mathbf{b})(\mathbf{A}\mathbf{X}+\mathbf{b})^T] - (\mathbf{A}E[\mathbf{X}]+\mathbf{b})(\mathbf{A}E[\mathbf{X}]+\mathbf{b})^{T}\newline
        &= E[\mathbf{A}\mathbf{X}\mathbf{X}^{T}\mathbf{A}^{T} + \mathbf{A}\mathbf{X}\mathbf{b})^T + \mathbf{b}\mathbf{X}^{T}\mathbf{A}^{T} + \mathbf{b}\mathbf{b})^T]\newline &- (\mathbf{A}E[\mathbf{X}]E[\mathbf{X}]^{T}\mathbf{A}^{T} + \mathbf{A}E[\mathbf{X}]\mathbf{b})^{T} + \mathbf{b}E[\mathbf{X}]^{T}\mathbf{A}^{T} + \mathbf{b}\mathbf{b})^T)\newline
        &= E[\mathbf{A}\mathbf{X}\mathbf{X}^{T}\mathbf{A}^{T}] - \mathbf{A}E[\mathbf{X}]E[\mathbf{X}]^{T}\mathbf{A}^{T}\newline &= \mathbf{A} (\mathbf{X}\mathbf{X}^{T} - E[\mathbf{X}]E[\mathbf{X}]^{T}) \mathbf{A}^{T}\newline
        Var(\mathbf{A}\mathbf{X}+\mathbf{b}) &= \mathbf{A} Var(\mathbf{X}) \mathbf{A}^{T}\newline
        Var(\mathbf{X} + \mathbf{Y}) &= Var(\mathbf{X}) + Cov(\mathbf{X}, \mathbf{Y}) + Cov(\mathbf{Y}, \mathbf{X}) + Var(\mathbf{Y})\newline
        &= Var(\mathbf{X}) + 2Cov(\mathbf{X}, \mathbf{Y}) + Var(\mathbf{Y})
    \end{align}
