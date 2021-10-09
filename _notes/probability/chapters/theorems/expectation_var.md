---
title: "Expectation, Variance and Covariance"
---
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
        E[X^{2}] &= \sum_x x^{2} P_{X}(X = x) \quad \text{Also called Second Moment}\newline
        E[X|A] &= \sum_{x} x P_{X|A}(X|A) = f(A)\quad \text{and not $X$, and is a random variable in itself}\newline
        E[g(X)|A] &= \sum_{x} g(x) P_{X|A}(X|A) \newline
        E[X + Y + Z] &= E[X] + E[Y] + E[Z] \quad \text{Linearity of Expectation (follows from linearity of integrals)}\newline
        E[XY] &= \sum_{X} \sum_{Y} xy P_{XY}(x,y) \newline
        E[g(X,Y)] &= \sum_{X} \sum_{Y} g(xy) P_{XY}(x,y) \newline
        E[k_{1}g_{1}(X,Y) + k_{2}g_{2}(X,Y)] &= k_{1}E[g_{1}(X,Y)] + k_{2}E[g_{2}(X,Y)]\newline
        E[XY] &= E[X]E[Y] \quad \text{if X and Y are independent}
    \end{align}
where $\alpha, \beta \in \mathbb{R}$, $g(X) : \mathbb{R} \rightarrow \mathbb{R}$, and $A$ is an event, $X, Y, Z$ are Random Variables.

The expected value for a function of the random variable (As stated above)
\begin{align}
    E[g(X)] &= \sum_x g(x)P_{X}(X = x)
\end{align}
is very handy in several places. For instance,
\begin{align}
    g(X) &= \roundbr{X - \mu_{X}}{2}\newline
    Var(X) &= E[g(X)]\newline
    E[X] &= E[g(X, Y)] \quad \text{if $g(X, Y) = X$}
\end{align}
And the last equation can be readily solved using marginal distributions/probabilities. The variance formula shown here extends to the conditional version as well.

The same formulas are valid in case of random vectors $\mathbf{X}$ and constants $\mathbf{b}$ and $\mathbf{A}$
\begin{align}
        E[\mathbf{X}] &= \begin{bmatrix}
        E[X_{1}]\newline
        E[X_{2}]\newline
        \vdots\newline
        E[X_{n}]
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
        Var(X) &= E[(X - \bar{X})^{2}]\newline
        &= E[X^{2}] - E[X]^{2}\newline
        Var(X\vert Y) &= E[X^{2} \vert Y] - E[X\vert Y]^{2}
    \end{align}
Using this definition, the following theorems follow
\begin{align}
        E[X^{2}] &= E[X]^{2} + Var(X) \newline
        Var(\alpha) &= 0 \newline
        Var(\alpha X + \beta) &= \alpha^{2} Var(X) \newline
        Var(X + Y) &= Var(X) + Var(Y) \text{if $X$ and $Y$ are independent random variables}
    \end{align}

### Covariance and Correlation

For any two random variables $X$ and $Y$,
\begin{align}
        Cov(X,Y) &= E[(X - \overline{X})(Y - \overline{Y})] = E[XY] - E[X]E[Y]\newline
        Cov(X,X) &= Var(X)\newline
        Corr(X,Y) &= E[\bigg(\frac{X - \overline{X}}{\sigma_{X}}\bigg) \bigg(\frac{Y - \overline{Y}}{\sigma_{Y}}\bigg)]\newline
        &= \frac{Cov(X,Y)}{\sigma_{X} \sigma_{Y}} = \rho
    \end{align}
where the correlation (denoted by $\rho$) is also known as Pearson Correlation. Key points to note
* **Independence implies** $\Rightarrow Cov(X,Y) = Corr(X,Y) = 0$, **but the converse is not true**
* The contrapositive statement is however true. $\rho \neq 0$ does imply that $X$ and $Y$ are dependent.
* Correlation is dimensionless and $-1 \leq Corr(X,Y) \leq 1$ with value close to $0$ implying minimal relation and values close to $-1, 1$ implying perfect relation. It measures the linearity between $X$ and $Y$.

With the help of covariance, we can calculate the variance of sum of random variables as below
\begin{align}
    Var(X + Y) &= E[(X+Y)^{2}] - E[X+Y]^{2} = (E[X^{2}] - E[X]^{2}) + 2(E[XY] - E[X]E[Y]) + (E[Y^{2}] - E[Y]^{2})\newline
    &= Var(X) + 2Cov(X, Y) + Var(Y)\newline
    Var(\sum_{1}^{n}{X_{i}}) &= \sum_{i=1}^{n}Var(X_{i}) + 2\sum_{i < j}Cov(X_{i}, X_{j})\newline
    Var(\sum_{1}^{n}a_{i}{X_{i}}) &= \sum_{i=1}^{n}a_{i}^{2}Var(X_{i}) + 2\sum_{i < j}a_{i}a_{j}Cov(X_{i}, X_{j})\newline
\end{align}

**Spearman's correlation** is similar to Pearson correlation but applied on rank variables. We first rank order the variables $X$ and $Y$ independently and create a new variable $rg_{X}$ and $rg_{Y}$ that are ranks of those variables. In case of same values, the average of the positions is taken (if the order were 1 2 3 4, we would change it to 1 2.5 2.5 4, position 2 and 3 have the same value).
\begin{align}
        \rho = \frac{Cov(rg_{X}, rg_{Y})}{\sigma_{rg_{X}} \sigma_{rg_{Y}}}
    \end{align}
and there is a formula to this in the case when all ranks are distinct
\begin{align}
        d_{i} &= rg_{x,i} - rg_{y,i}\newline
        \rho &= 1 - \frac{6\sum_{i=1}^{n} d_{i}^{2}}{n(n^{2} - 1)}
    \end{align}

In case of (column) **vectors**, the **Variance-Covariance Matrix** is defined as
\begin{align}
        Var(X) = Cov(\mathbf{X}, \mathbf{X}) &= E[(\mathbf{X} - E[\mathbf{X}])(\mathbf{X} - E[\mathbf{X}])^{T}]\newline
        &= E[\mathbf{X}\mathbf{X}^{T} - \mathbf{X}E[\mathbf{X}]^{T} - E[\mathbf{X}]\mathbf{X}^{T} + E[\mathbf{X}]E[\mathbf{X}]^{T}]\newline
        &= E[\mathbf{X}\mathbf{X}^{T}] - E[\mathbf{X}]E[\mathbf{X}]^{T} - E[\mathbf{X}]E[\mathbf{X}]^{T} + E[\mathbf{X}]E[\mathbf{X}]^{T}\newline
        &= E[\mathbf{X} \mathbf{X}^{T}] - E[\mathbf{X}]E[\mathbf{X}]^{T}\newline
        \text{For the individual elements,} \quad \squarebr{Cov(\mathbf{X}, \mathbf{X})}\_{ij} &= Cov(X_{i}, X_{j})\newline
        \squarebr{Cov(\mathbf{X}, \mathbf{X})}\_{ii} &= Cov(X_{i}, X_{i}) = Var(X_{i})\newline
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
        &= E[\mathbf{A}\mathbf{X}\mathbf{X}^{T}\mathbf{A}^{T}] - \mathbf{A}E[\mathbf{X}]E[\mathbf{X}]^{T}\mathbf{A}^{T}\newline &= \mathbf{A} (E[\mathbf{X}\mathbf{X}^{T}] - E[\mathbf{X}]E[\mathbf{X}]^{T}) \mathbf{A}^{T}\newline
        Var(\mathbf{A}\mathbf{X}+\mathbf{b}) &= \mathbf{A} Var(\mathbf{X}) \mathbf{A}^{T}\newline
        Var(\mathbf{X} + \mathbf{Y}) &= Var(\mathbf{X}) + Cov(\mathbf{X}, \mathbf{Y}) + Cov(\mathbf{Y}, \mathbf{X}) + Var(\mathbf{Y})\newline
        &= Var(\mathbf{X}) + 2Cov(\mathbf{X}, \mathbf{Y}) + Var(\mathbf{Y})
    \end{align}

where $Var(\mathbf{X})$ and $Cov(\mathbf{X}, \mathbf{X})$ are used interchangeably and mean the same thing.
