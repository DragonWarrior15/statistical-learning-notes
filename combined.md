---
title: "Combined Notes"
layout: default_wo_nav
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
        E[X^{2}] &= \sum_x x^{2} P_{X}(X = x) \quad \text{Also called Second Moment}\newline
        E[X|A] &= \sum_{x} x P_{X|A}(X|A) = f(A)\;\text{and not X}\newline
        E[g(X)|A] &= \sum_{x} g(x) P_{X|A}(X|A) \newline
        E[X + Y + Z] &= E[X] + E[Y] + E[Z] \quad \text{Linearity of Expectation}\newline
        E[XY] &= \sum_{X} \sum_{Y} xy P_{XY}(x,y) \newline
        E[g(X,Y)] &= \sum_{X} \sum_{Y} g(xy) P_{XY}(x,y) \newline
        E[XY] &= E[X]E[Y] \quad \text{if X and Y are independent}
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


## Iterated Expectation and Variance

The law of iterated expectation tells the following about expectation and variance
\begin{align}
        E[E[X|Y]] &= E[X] \newline
        Var(X) &= E[Var(X|Y)] + Var(E[X|Y])\newline
    \end{align}

Proof for Iterated Expectation
\begin{align}
        P(X) &= \sum_{y} P(X|Y) P(Y) \newline
        \Rightarrow E[X] &= \sum_{x} xP(X) = \sum_{x} \sum_{y} xP(X|Y)P(Y) \newline
            &= \sum_{y} P(Y) \sum_{x} xP(X|Y) = \sum_{y} P(Y) E[X|Y] \newline
        \text{or, } E[X] &= E[E[X|Y]] \quad \text{($E[X|Y]$ is a function of $Y$ and not $X$)}
    \end{align}

Proof for Variance
\begin{align}
        Var(X) &= E[X^{2}] - E[X]^{2} \newline
        Var(X|Y) &= E[(X-\overline{X})^{2}|Y] = E[X^{2}|Y] - E[X|Y]^{2} \quad \text{(1)}\newline
        Var[E(X|Y)] &= E[E(X|Y)^{2}] - E[E[X|Y]]^{2}\newline
                    &= E[E[(X|Y)]^{2}] - E[X]^{2} \quad \text{(2)}\newline
        E[Var(X|Y)] &= E[E[X^{2}|Y]] - E[E[X|Y]^{2}] \quad \text{from (1)}\newline
                    &= E[X^{2}] - E[E[X|Y]^{2}] \quad \text{(3)}\newline
        E[Var(X|Y)] + Var(E[X|Y]) &= E[X^{2}] - E[X]^{2} \quad \text{adding (2) and (3)}\newline
                                    &= Var(X)
    \end{align}


## Random number of Random Variables

Let $X_{i}$ be independent identically distributed Random Variables and let $Y = \sum_{i=1}^{N} X_{i}$ be the sum of $N$ such random variables where $N$ itself is a random variable. Then,
\begin{align}
        Y &= X_{1} + X_{2} + \cdots + X_{N}\newline
        E[Y|N=n] &= \sum_{i=1}^{n}E[X_{i}]\newline
                &= NE[X]\newline
        E[Y] &= E[E[Y|N]] = E[NE[X]]\newline
            &= E[N]E[X] \quad \text{since $E[X]$ will be a number}\newline
        Var(Y) &= E[Var(Y|N)] + Var(E[Y|N])\newline
            &= E[NVar(X)] + Var(NE[X])\newline
            &= E[N]Var(X) + E[X]^{2}Var(N)
    \end{align}


## Moment Generating Function

Moment generating function is defined as the following for all values of $t$
\begin{align}
        \phi (t) = E[e^{tX}] = \begin{cases} \sum_{x} e^{tx} p_{X}(x) &\mbox{for discrete case}\newline
        \int_{-\infty}^{\infty} e^{tx} f_{X}(x) &\mbox{for continuous case} \end{cases}
    \end{align}
This function is called the moment generating function because all the moments of the random variable $X$ can be obtained by successively differentiating the function $\phi(t)$.


\begin{align}
        \phi^{\prime}(t) &= \frac{d}{dt} E[e^{tX}]\newline
        &= E[\frac{d}{dt} e^{tX}]\newline
        &= E[Xe^{tX}]\newline
        \text{mean} &= E[X]\newline
        &= \phi^{\prime}(0)
    \end{align}

Continuing in a similar fashion,
\begin{align}
        \phi^{\prime\prime}(t) &= \frac{d}{dt} E[Xe^{tX}]\newline
        &= E[\frac{d}{dt}Xe^{tX}]\newline
        &= E[X^{2}e^{tX}]\newline
        \text{variance} &= \phi^{\prime\prime}(0)\newline
        &= E[X^{2}]
    \end{align}
In general, for any $n > 0$, the $n^{th}$ derivative will give the $n^{th}$ moment
\begin{align}
        \phi^{n}(0) = E[X^{n}]
    \end{align}

There exists a **one to one correspondence between the moment generating function and the distribution function of a random variable**, similar to Lagrangian multipliers.

## Moment Generating Function for Sum of Independent RV

An important property is in the context of sum of two or more random variables. The **moment generating of sum of two independent random variables is simply the product of the moment generating functions of the two individual random variables**
\begin{align}
        \phi_{X+Y}(t) &= E[e^{t(X+Y)}]\newline
        &= E[e^{tX} e^{tY}]\newline
        &= E[e^{tX}] E[e^{tY}]\newline
        \phi_{X+Y}(t) &= \phi_{X}(t) \phi_{Y}(t) \quad \text{for independent random variables}
    \end{align}


## Convolutions

Convolution operations are defined for both CDF and PDF/PMFs. Let $X$ and $Y$ be random independent variables, then
\begin{align}
{2}
    F_{X+Y}(x) &= F_{X} * F_{Y} &= \int_{\mathbb{R}} F_{X}(x-y) dF_{Y}(y)\newline
    p_{X+Y}(x) &= p_{X} * p_{Y} &= \int_{\mathbb{R}} p_{X}(x-y) p_{Y}(y) dy\end{align}

We can extend the idea to $n$ independent variables as
\begin{align}
    F_{X}^{n\*} = F_{X} * \cdots * F_{X} \text{ $n$ times}\end{align}
It has the following properties for positive random variable $X_{i}$s

1.  \begin{align}
            F_{X}^{n\*}(x) \leq F_{X}^{n}(x)
        \end{align}
    This can be proven as
    \begin{align}
            P(X_{1} + \cdots + X_{n} \leq x) &\leq P(X_{1} \leq x, \ldots, X_{n} \leq x)\newline
            P(X_{1} + \cdots + X_{n} \leq x) &\leq \prod_{i=1}^{n} P(X \leq x) \text{ by independence}\newline
            \text{or, } F_{X}^{n\*}(x) &\leq F_{X}^{n}(x)
        \end{align}

2.  \begin{align}
            F_{X}^{n\*}(x) \geq F_{X}^{n+1}(x)
        \end{align}
    which follows immediately from the fact that
    \begin{align}
            P(X_{1} + \cdots + X_{n} \leq x) &\geq P(X_{1} \leq x, \ldots, X_{n+1} \leq x)\newline
        \end{align}
    since the volume of the regions denoting the sums will be lower in the higer dimensions. This can be quickly verified by considering $X_{1} \leq 1$ and $X_{1} + X_{2} <= 1$.


## Continuous Uniform Random Variable

A uniform random variable has the following distribution function
\begin{align}
        f_{X}(x) = \begin{cases} \frac{1}{b-a} &\mbox{$if a \leq x \leq b$}\newline
                                    0 &\mbox{otherwise} \end{cases}
    \end{align}

### Mean and Variance

\begin{align}
        E[X] &= \int_{a}^{b} x \frac{1}{b-a} dx = [\frac{x^{2}}{2(b-a)}]\_{a}^{b}\newline
            &= \frac{a+b}{2}\newline
        Var(X) &= \int_{a}^{b} (x - \frac{a+b}{2})^{2} \frac{1}{b-a} dx \newline
            &= \frac{(b-a)^{2}}{12}
    \end{align}

### Moment Generating Function

\begin{align}
        E[e^{tX}] &= \int_{a}^{b} e^{tx} \frac{1}{b-a} dx\newline
        &= \frac{e^{tb} - e^{ta}}{t(b-a)}
    \end{align}


## Bernoulli and Binomial Random Variable

*Binomial Random Variable* $X$ is defined as the number of successes in an experiment with $n$ independent trials, where each trial can only have two outcomes, *success* or *failure*.
Each trial is also known as a Bernoulli random variable or a Bernoulli trial.
Let $X_{i}$ denote the Random Variable corresponding to the individual trials, with probability of success $p$. Then we have the following

\begin{alignat}{2}
        X_{i} &= \begin{cases} 1 &\mbox{if success in trial i}\newline
                                0 &\mbox{otherwise} \end{cases} \quad \text{indicator variable} \newline
        X &= X_{1} + X_{2} + \cdots + X_{n} = \sum_{i=1}^{n} X_{i} \newline
        P(X=k) &= \binom{n}{k} p^{k} (1 - p)^{n-k}
    \end{alignat}

where $X$ denotes the Binomial random variable.

### Mean and Variance

First let's calculate the mean and variance for a Bernoulli trial $X_{i}$
\begin{alignat}{2}
        E[X_{i}] &= 1 * p + 0 * (1 - p) &&= p\newline
        Var(X_{i}) &= (1 - p)^{2}p + (0-p)^{2}(1-p) &&= p(1-p)
    \end{alignat}

We know that all $X_{i}'s$ are independent. Hence, the mean and variance for X become
\begin{alignat}{3}
        E[X] &= E[\sum_{i=1}^{n} X_{i}] &&= \sum_{i=1}^{n}E[X_{i}] &&= np \newline
        Var(X) &= Var(\sum_{i=1}^{n} X_{i}) &&= \sum_{i=1}^{n} Var(X_{i}) &&= np(1-p)
    \end{alignat}

### Sum of Binomial Random Variables

Suppose two random variables $X_{1} \sim binmomial(n_{1},p)$ and $X_{2} \sim binomial(n_{2},p)$, then
\begin{align}
        X_{1} + X_{2} \sim binomial(n_{1} + n_{2}, p)
    \end{align}
which follows from the fact that the sum of the two random variables represents an experiment with $n_{1} + n_{2}$ trials where the probability of success of any trial still remains the same at $p$.

### Moment Generating Functions

#### Bernoulli Trial

\begin{align}
        E[e^{tX}] &= pe^{t} + (1-p)e^{0} = pe^{t} + 1-p
    \end{align}

#### Binomial Variable

A binomial variable is a sum of $n$ Bernoulli trials
\begin{align}
        X &= X_{1} + \cdots + X_{n}\newline
        E[e^{tX}] &=E[e^{t(X_{1} + \cdots + X_{n})}] = E[e^{tX_{1}} e^{tX_{2}} \cdots e^{tX_{n}}]\newline
        &= E[e^{tX_{1}}] E[e^{tX_{2}}] \cdots E[e^{tX_{n}}] = \prod_{i=1}^{n} (pe^{t} + 1-p)\newline
        &= (pe^{t} + 1-p)^{n}
    \end{align}


## Geometric Distribution

A geometric distribution represents the probability distribution for the number of trials in Bernoulli trials till the first success.
\begin{align}
        P(X = k) &= (1-p)^{k-1}p \quad k = 1, 2, 3, \ldots
    \end{align}

To be precise, this definition is called the shifted geometric distribution. Another definition is to consider $k$ as the number of trials before the first success. The distribution will then be defined on $k = 0, 1, 2, \ldots$.

### Moment Generating Function

To calculate mean and variance, we first calculate the moment generating function
\begin{align}
        E[e^{tX}] &= \sum_{k=1}^{\infty} (1-p)^{k-1}p e^{tk}\newline
        \phi(k) &= \frac{p}{1-p} \sum_{k=1}^{\infty} ((1-p)e^{t})^{k}\newline
        &= \frac{p}{1-p} \frac{(1-p)e^{t}}{1 - (1-p)e^{t}} = \frac{pe^{t}}{1 - (1-p)e^{t}}\newline
        \diffone{\phi}(t) &= \frac{(1 - (1-p)e^{t})pe^{t} + pe^{t}(1-p)e^{t}}{(1 - (1-p)e^{t})^{2}}\newline
        &= \frac{pe^{t}}{(1 - (1-p)e^{t})^{2}}\newline
        \difftwo{\phi}(t) &= \frac{(1 - (1-p)e^{t})^{2}pe^{t} + pe^{t}2(1 - (1-p)e^{t})(1-p)e^{t}}{(1 - (1-p)e^{t})^{4}}\newline
        &= \frac{pe^{t}(1 + (1-p)e^{t})}{(1 - (1-p)e^{t})^{3}}
    \end{align}

### Mean and Variance

With the moment generating function, mean and variance are easy to calculate
\begin{align}
        E[X] &= \diffone{\phi}(0) = \frac{1}{p}\newline
        E[X^{2}] &= \difftwo{\phi}(0) = \frac{2-p}{p^{2}}\newline
        Var(X) &= \frac{2-p}{p^{2}} - \frac{1}{p^{2}} = \frac{1-p}{p^{2}}
    \end{align}


## Negative Binomial Distribution

Suppose we run an experiment with independent Bernoulli trials where the experiment stops when $r > 0$ successes are observed. Let $p$ be the probability of success, and $k$ be the number of failures in the experiment,
\begin{align}
        P(X = k) &= \binom{k + r - 1}{r-1}(1-p)^{k}p^{r} \quad k = 0, 1, 2, \ldots
    \end{align}
since the last trial is by definition a success; we can only choose the failures from the remaining trials.

### Mean and Variance

With the moment generating function, mean and variance are easy to calculate
\begin{align}
        E[X] &= \frac{rp}{1-p}\newline
        Var(X) &= \frac{r(1-p)}{p^{2}}
    \end{align}

### Relation to Geometric Distribution

Geometric distribution is a special case of Negative binomial distribution with $r = 1$
\begin{align}
        Geom(p) = NB(1, p)
    \end{align}

Further, the sum of $r$ independent geometric random variables (defined on $0,1,2,\ldots$) is a negative binomial distribution with parameters $r$ and $p$
\begin{align}
        \sum_{r} Geom(p) = NB(r, p)
    \end{align}


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


## Exponential Distribution

Exponential distribution is characterized by the parameter $\lambda$ and has the following probability distribution
\begin{align}
        f_{X}(x) = \begin{cases} 0 &\mbox{if $x < 0$}\newline
                                \lambda e^{-\lambda x} &\mbox{otherwise} \end{cases}
    \end{align}

Exponential distribution is used to represent the interarrival time probability distribution in the context of Poisson Process. The cumulative distribution is given by
\begin{align}
        F_{X}(x) &= \begin{cases} 0 &\mbox{if $x < 0$}\newline
                                1 - e^{-\lambda x} &\mbox{otherwise} \end{cases}\newline
        P(X > x) &= \int_{x}^{\infty} \lambda e^{-\lambda x} dx\newline
        &= e^{-\lambda x}
    \end{align}

### Mean and Variance

The mean of the distribution is given by
\begin{align}
        E[x] &= \int_{0}^{\infty} \lambda x e^{-\lambda x} dx\newline
        &= [-x e^{-\lambda x}]\_{0}^{\infty} + \int_{0}^{\infty} e^{-\lambda x} dx = \frac{1}{\lambda}\newline
        E[X] &= \frac{1}{\lambda}
    \end{align}
where we used integration by parts, $\int uv' = uv - \int u'v$ and substituted $u = x$ and $v = -e^{-\lambda x}/\lambda$.


For variance, we first calculate the value of $E[x^{2}]$
\begin{align}
        E[x^{2}] &= \int_{0}^{\infty} \lambda x^{2} e^{-\lambda x} dx\newline
        &= [-x^{2} e^{-\lambda x}]\_{0}^{\infty} + \int_{0}^{\infty} 2x e^{-\lambda x} dx\newline
        &= [\frac{-2x e^{-\lambda x}}{\lambda}]\_{0}^{\infty} - [\frac{2e^{-\lambda x}}{\lambda^{2}}]\_{0}^{\infty}\newline
        &= \frac{2}{\lambda^{2}}\newline
        Var(X) &= E[X^{2}] - E[X]^{2}\newline
        Var(X) &= \frac{1}{\lambda^{2}}
    \end{align}
The above property can be generalized for the $n$th power as well
\begin{align}
        E[X^{n}] = \frac{n!}{\lambda^{n}}
    \end{align}

### Moment Generating Function

The moment generating function of an exponential distribution can be derived as follows
\begin{align}
        E[e^{tX}] &= \int_{0}^{\infty} e^{tx} \lambda e^{-\lambda x} dx = \frac{\lambda}{\lambda - t} \int_{0}^{\infty} (\lambda - t) e^{-(\lambda - t)x} dx\newline
        &= \frac{\lambda}{\lambda - t}
    \end{align}
since quantity under the integral is an exponential distribution with the parameter $\lambda - t$.

### Memoryless Property

A fundamental mathematical property of the exponential distribution is the memoryless property. In summary, this means that whatever has transpired till now will not affect the future distribution. Mathematically $P(T > t+s)$ is independent of t
\begin{align}
        P(T > t+s | T>t) &= \frac{P(T> t+s \text{ and }T > t)}{P(T > t)}\newline
        &= \frac{P(T > t + s)}{P(T > t)}\newline
        &= \frac{e^{-\lambda(t+s)}}{e^{-\lambda t}}\newline
        &= e^{-\lambda s}\newline
        P(T > t+s | T>t) &= P(T > s)
    \end{align}

### Minimum of Exponential Variables

If $X_{1}, \ldots X_{n}$ are $n$ independent exponentially distributed random variables with $X_{i} \sim Exponential(\lambda_{i})$, then the distribution of the minima is also Exponential.
\begin{align}
        P(min(X_{1}, \ldots, X_{n}) > x) &= P(X_{1} > x, \ldots, X_{n} > x)\newline
        &= P(X_{1} > x) P(X_{2} > x) \ldots P(X_{n} > x) \; \text{by independence}\newline
        &= \prod_{i=1}^{n} e^{-\lambda_{i} x}\newline
        &= \exp(-\sum_{i=1}^{n} \lambda_{i} x)\newline
        \implies min(X_{1}, \ldots, X_{n}) &\sim Exponential(\lambda_{1} + \cdots + \lambda_{n})
    \end{align}


## Poisson Process

### Poisson Random Variable

A random variable $X$ is said to be $Poisson(\lambda)$ if it has the following probability distribution
\begin{align}
        p_{X}(x = k) = \begin{cases} e^{-\lambda} \frac{\lambda^{k}}{k!} &\text{ for all } x = \{ 0,\;1,\;2, \cdots \}\newline
                                    0 &\text{ otherwise} \end{cases}
    \end{align}

The sum of $n$ independent Poisson variables is also Poisson
\begin{align}
        X_{1} + X_{2} + \cdots + X_{n} \sim Poisson(\lambda_{1} + \lambda_{2} + \cdots + \lambda_{n})
    \end{align}

### Mean and Variance

Expected value is calculated as follows
\begin{align}
        E[X] &= \sum_{k=0}^{\infty} ke^{-\lambda} \frac{\lambda^{k}}{k!} = \lambda e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!}\newline
        &= \lambda e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^{k}}{k!}\newline
        E[X] &= \lambda
    \end{align}

Variance can be calculated using $Var(X) = E[X^{2}] - E[X]^{2}$
\begin{align}
        E[X^{2}] &= \sum_{k=0}^{\infty} k^{2} e^{-\lambda} \frac{\lambda^{k}}{k!} = \lambda e^{-\lambda} \sum_{k=1}^{\infty} k\frac{\lambda^{k-1}}{(k-1)!}\newline
        &= \lambda e^{-\lambda} \sum_{k=0}^{\infty} (k+1) \frac{\lambda^{k}}{k!}\newline
        &= \lambda e^{-\lambda} \big( \lambda \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!} + \sum_{k=0}^{\infty} \frac{\lambda^{k}}{k!} \big)\newline
        &= \lambda e^{-\lambda} (\lambda e^{\lambda} + e^{\lambda})\newline
        Var(X) &= E[X^{2}] - E[X]^{2}\newline
        Var(X) &= \lambda
    \end{align}

Thus, mean and variance is the same for a Poisson variable.

### Moment Generating Function

The mean and variance are easy to derive with the moment generating function of the Poisson distribution
\begin{align}
        E[e^{tX}] &= \sum_{k=0}^{\infty} e^{tk} e^{-\lambda} \frac{\lambda^{k}}{k!} = e^{-\lambda} \sum_{k=0}^{\infty} \frac{(\lambda e^{t})^{k}}{k!}\newline
        \phi(t) &= e^{-\lambda} e^{\lambda e^{t}} = e^{-\lambda(1-e^{t})}
    \end{align}

Now, we can use the derivates of this function to derive the expectations
\begin{alignat}{3}
        E[X] &= \phi^{\prime}(0) &&= e^{-\lambda(1-e^{t})} \lambda e^{t} &&= \lambda\newline
        E[X^{2}] &= \phi^{\prime\prime}(0) &&= \lambda e^{-\lambda(1-e^{t}) + t} (1+\lambda e^{t}) &&= \lambda^{2} + \lambda
    \end{alignat}

### Sum of Poisson Variables

The sum of two independent random variables $X_{1} \sim Poisson(\lambda_{1})$ and $X_{2} \sim Poisson(\lambda_{2})$ is also Poisson. This can be derived with their moment generating functions
\begin{align}
        E[e^{t(X_{1} + X_{2})}] &= E[e^{tX_{1}} e^{tX_{2}}] = E[e^{tX_{1}}]E[e^{tX_{2}}] \;\text{by independence}\newline
        &= e^{-\lambda_{1}(1-e^{t})} e^{-\lambda_{2}(1-e^{t})} = e^{-(\lambda_{1} + \lambda_{2})(1-e^{t})}\newline
        \implies X_{1} + X_{2} &\sim Poisson(\lambda_{1} + \lambda_{2})
    \end{align}

### Approximation of a Binomial Random Variable

Recall the probability distribution for a binomial random variable with parameters $n$ and $p$
\begin{align}
        P(X = i) = \binom{n}{i} p^{i} (1-p)^{n-i}
    \end{align}

Let $\lambda = np$ and $n$ be large while $p$ is very small (i.e., the probability of occurrence of the event is small with a large number of trials)
\begin{align}
        P(X = i) &= \frac{n!}{(n-i)!i!} (\frac{\lambda}{n})^{i} (1-\frac{\lambda}{n})^{n-i}\newline
        &= \frac{n(n-1) \ldots (n-i + 1)}{n^{i}} \frac{\lambda^{i}}{i!} \frac{(1-\lambda / n)^{n}}{(1 - \lambda / n)^{i}}\newline
        &\approx 1 \frac{\lambda^{i}}{i!} \frac{e^{-\lambda}}{1}\newline
        P(X = i) &\approx e^{-\lambda}\frac{\lambda^{i}}{i!}
    \end{align}

where have used the limit definition of $e$, $\lim_{n \to \infty}(1 + x/n)^{n} = e$. Examples where this approximation is valid include number of misprints on a page (the probability of a word being misprinted is small, and there are a large number of words on a page), number of transistors failing on first day of use (probability of failure is small, with extremely large number of transistors being used on any day). All these examples can be assumed to follow the Poisson distribution with mean $\lambda = np$.

### Poisson Process

Poisson process also falls in the realm of random processes but is different from Bernoulli process as it is a continuous time process. This process is very commonly used to model arrival times and number of arrivals in a given time interval.
\begin{align}
        P(k, \tau) &= \text{Probability of $k$ arrivals in interval of duration $\tau$}\newline
        \sum_{k} P(k, \tau) &= 1 \; \text{for a given $\tau$}
    \end{align}
Assumptions

-   The Probability is dependent only on the length of the interval $\tau$ and not the *location* of the interval

-   Number of arrivals in disjoint time intervals are *independent*

### A Special Counting Process

A counting process $N_{t}:t \in [0,\infty)$ is a Poisson process with rate $\lambda$ if

1.  $N_{0} = 0$

2.  $N_{t}$ is composed of independent and stationary increments

3.  The number of arrivals in any time interval $\tau > 0$ has $Possion(\lambda \tau)$ distribution

Hence, for a Poisson process, the number of arrivals in any interval is dependent only on the length of that interval and not the location. Further, the number of arrivals in the interval will follow a Poisson distribution.

### Derivation from Bernoulli Process

For a very small interval $\delta$,
\begin{align}
        P(k, \delta) &= \begin{cases} 1-\lambda \delta &\mbox{$k = 0$}\newline
                                     \lambda \delta &\mbox{$k = 1$}\newline
                                     0 &\mbox{$k > 2$} \end{cases} + O(\delta^{2})\newline
        \lambda &= \lim_{\delta \to 0}\frac{P(1,\delta)}{\delta} \quad \text{arrival rate per unit time}\newline
        E[k] &= (\lambda \delta) * 1 + (1-\lambda \delta) * 0\newline
            &= \lambda \delta \newline
        \tau &= n \delta
    \end{align}

The last equation clearly implies that we can approximate the whole process as a bernoulli process where we have $n$ miniscule time intervals with at most one arrival per interval.
\begin{align}
        P(k\; \text{arrivals}) &= \binom{n}{k} p^{k} (1-p)^{n-k} \newline
            &= \binom{n}{k} (\frac{\lambda \delta}{n})^{k} (1 - \frac{\lambda \delta}{n})^{n-k}\newline
        \lambda \tau &= np \quad \text{or, arrival rate * time = E[arrivals]}\newline
        Poisson &= \lim_{\delta \to 0, n \to \infty} Bernoulli\newline
        or,\; P(k, \tau) &= \frac{(\lambda \tau)^{k} e^{-\lambda \tau}}{k!} \quad \text{$k = 0,1, \cdots$, for a given $\tau$}\newline
        where,\; \sum_{k} P(k, \tau) &= 1 \quad \text{for a given $\tau$}
    \end{align}

Let $N_{t}$ denote the no of arrivals till time t, then
\begin{align}
        E[N_{t}] &= \lambda t\newline
        Var(N_{t}) &= \lambda t\newline
        P(N(t) = k) &= e^{-\lambda t} \frac{(\lambda t)^{k}}{k!}, \; \text{for $k=0,1,2,\ldots$}
    \end{align}

### Time till kth arrival

Suppose the $k^{th}$ arrival happens at a time $t$. Then we are saying that there have been $k-1$ arrivals till time $t$ and the $k^{th}$ arrival happens at time $t$ (precisely in an interval of $[t, t+\delta]$). Let $Y_{k}$ be the required time,
\begin{align}
        f_{Y_{k}}(t)\delta &= P(t \leq Y_{k} \leq t+\delta)\newline
                    &= P(\text{$k-1$ arrivals  in $[0,t]$}) (\lambda \delta)\newline
                    &= \frac{(\lambda t)^{k-1}}{(k-1)!}e^{-\lambda t}(\lambda \delta)\newline
        f_{Y_{k}}(t) &= \frac{\lambda^{k} t^{k-1}}{(k-1)!}e^{-\lambda t} \quad \text{Erlang Distribution}
    \end{align}

### Time of 1st Arrival

Using the Erlang Distribution described above, we have
\begin{align}
        f_{Y_{1}}(t) = \lambda e^{-\lambda t}
    \end{align}
$Y_{k} = T_{1} + T_{2} + \cdots + T_{k}$ where all $T_{i}$ are independent and exponential distributions.

### Renewal Process

Poisson process can be seen as a special case of a renewal process, when the interarrival times are all exponentially distributed.
\begin{alignat}{3}
        \text{Interarrival time }& \xi_{i}&& = \lambda e^{-\lambda t}\newline
        \text{Number of arrivals }& P(N_{t} = n)&& = \frac{(\lambda t)^{n}}{n!} e^{-\lambda t}\newline
        \text{Time till $n$th arrival }& P(S_{n} = t)&& = \lambda \frac{(\lambda t)^{n-1}}{(n-1)!} e^{-\lambda x} \text{ for $t > 0$}\newline
        \text{Cumulative distribution }& P(S_{n} \leq t)&& = \begin{cases} 1 - e^{-\lambda t} \sum_{k=1}^{n-1} \frac{(\lambda t)^{k}}{k!} &\mbox{if $t > 0$}\newline
        0 &\mbox{otherwise} \end{cases}
    \end{alignat}

### Merging of Poisson Processes

Merging of two Poisson processes is also a Poisson process. Consider two flasbulbs of Red and Green colours, flashing as Possion processes with rates $\lambda_{1}$ and $\lambda_{2}$. Then the process denoting the combined flashing of the two bulbs is also Poisson.

Consider a very small interval of time $\delta$. In this small interval, any of the individual bulbs can have at most one flashes (since we ignore higher order terms). Thus, the following four possibilities arise


| . | $Red$ | $\overline{Red}$ |
| - | ----- | ---------------- |
| $Green$ | $\lambda_{1} \delta \lambda_{2} \delta$ | $(1-\lambda_{1}\delta)  \lambda_{2} \delta$ |
| $\overline{Green}$ | $\lambda_{1} \delta (1-\lambda_{2}\delta)$ | $(1-\lambda_{1}\delta) (1-\lambda_{2}\delta)$ |


| . | $Red$ | $\overline{Red}$ |
| - | ----- | ---------------- |
| $Green$ | $0$ | $\lambda_{2} \delta$ |
| $\overline{Green}$ | $\lambda_{1} \delta$ | $(1-(\lambda_{1} + \lambda_{2}) \delta)$ |

The combined process (of at least one bulb flashing) $\sim Poisson(\lambda_{1} + \lambda_{2})$

\begin{align}
    P(\text{arrival happened from first process}) = \frac{\lambda_{1} \delta}{\lambda_{1} \delta + \lambda_2 \delta} = \frac{\lambda_{1}}{\lambda_{1} + \lambda_{2}}
    \end{align}

### Splitting of Poisson Process

Suppose we have a Poisson process with parameter $\lambda$ which we split into two processes up and down, with probabilities $p$ and $1-p$. The two resulting processes are also Poisson with different parameters.

Consider a small time slot of length $\delta$. Then,
\begin{align}
        P(\text{arrival in this time slot}) &= \lambda \delta\newline
        P(\text{arrival in up slot}) &= \lambda \delta p\newline
        P(\text{arrival in down slot}) &= \lambda \delta (1-p)
    \end{align}
Thus, up and down are themselves Poisson with parameters $\lambda p$ and $\lambda (1-p)$ respectively.

### Random Indcidence for Poisson

Suppose we have a Poisson process with parameter $\lambda$ running forever. We show up at a random time instant. What is the length of the chosen interarrival time (the total of the time from the last arrival to the next arrival).

Let $T_{1}^{\prime}$ denote the time that has elapsed since the last arrival and $T_{1}$ be the time till the next arrival. Note that the reverse process is also Poisson with the same parameter. Thus,
\begin{align}
        E[\text{interarrival time}] = E[T_{1}^{\prime} + T_{1}] = \frac{1}{\lambda} + \frac{1}{\lambda} = \frac{2}{\lambda}
    \end{align}

This may seem paradoxical since the time difference between any two arrivals in a Poisson process is same and it's expected length is $\frac{1}{\lambda}$, whereas we got an interval twice this length. The paradox is resolved by considering the fact that when we choose a random point in time, it is more likely to fall in an interval of larger size than the smaller ones (since probability will be proportional to the length of the interval).


Consider a separate example where we want to compare two values $E[\text{size of a family}]$ and $E[\text{size of a family of a given person}]$.

The two value will be different due to the underlying nature of the way experiment is conducted. For the first, we randomly choose families and average their sizes. Here, family of any size is equally likely to be picked. In the second case, we first pick a person from the population, get their family size, and then average the sizes of the families. Note that, this experiment is biased since the we are more likely to select people from larger families (or equivalently, it is more likely that we pick a person from a large family since the probability of picking is proportional to the family size). Hence, the second value will likely be larger and the two quantities are not equal.

### Non Homogenous Poisson Process

Sometimes, it may not be accurate to use a simple Poisson process to model arrival. For example, a restaurant will not have the same rate of influx throughout the day. This rate itself is a function of time. In such cases, we model the arrivals as Non Homogenous Poisson Process.


For such a process, we have $\lambda(t): [0,\infty) \to [0, \infty)$ and the counting process $N_{t}$ is non homogenous if the following hold

1.  $N_{0} = 0$

2.  The increments to $N_{t}$ are **independent but not stationary**

3.  For any small time interval $\delta$, the probability of more than 1 arrival in the interval is zero

The distribution of arrivals in a time interval is still Poisson, but the Poisson parameter is now dependent on the location of the interval itself (since the process does not have stationary increments)
\begin{align}
        N_{t+s} - N_{t} \sim Poisson(\int_{t}^{t+s} \lambda(\alpha) d\alpha)
    \end{align}


## Gamma Distribution

A random variable is said to have a Gamma distribution if for parameters $(\alpha, \lambda)$ with $\lambda > 0, \alpha > 0$, it has the following probability distribution
\begin{align}
        p_{X}(x) = \begin{cases}
            \frac{\lambda e^{-\lambda x} (\lambda x)^{\alpha - 1}}{\Gamma(\alpha)} &\mbox{if $x \geq 0$}\newline
            0 &\mbox{otherwise}
        \end{cases}
    \end{align}
The denominator in the above fomula acts as nothing but a normalization constant and is defined as
\begin{align}
        \Gamma (\alpha) &= \int_{0}^{\infty} e^{-x} x^{\alpha - 1}\newline
        &= (\alpha - 1) \int_{0}^{\infty} e^{-x} x^{\alpha - 2} dy \:\text{using integration by parts}\newline
        &= (\alpha - 1) \Gamma (\alpha - 1)
    \end{align}

Note that at $\alpha = 1$, $\Gamma (1) = \int_{0}^{\infty} e^{-x} = 1$. Hence, if $\alpha$ is an integer, $\Gamma(\alpha) = (\alpha-1) !$ using the recursion relation derived above.


For a fixed $\lambda$, as the value of $\alpha$ becomes large, the distribution takes the form of a normal distribution.

{% include image.html url="notes/probability/images/gamma_1.png" description="Gamma distribution for $\lambda = 1$ and different values of $\alpha$" img_classes="notes-img gamma_1" %}
{% include image.html url="notes/probability/images/gamma_2.png" description="distribution for $\alpha = 50$" img_classes="notes-img gamma_1" %}

### Mean, Variance and Moment Generating Function

Mean and variance are easily obtainable for this using the moment generating function. Recall
\begin{align}
        \phi(t) &= E[e^{tX}]\newline
        \phi^{n}(t) &= E[X^{n}]
    \end{align}

For the current distribution,
\begin{align}
        \phi(t) &= \frac{\lambda^{\alpha}}{\Gamma(\alpha)} \int_{0}^{\infty} e^{tx} e^{-\lambda x} x^{\alpha - 1} dx\newline
        &= \bigg(\frac{\lambda}{\lambda - t}\bigg)^{\alpha}
    \end{align}
by rearranging the terms to complete an integral of a Gamma distribution with parameters $(\alpha, \lambda - t)$. Differentiating,
\begin{align}
        \phi^{\prime}(t) &= \frac{\alpha \lambda^{\alpha}}{(\lambda - t)^{\alpha + 1}}\newline
        \phi^{\prime \prime}(t) &= \frac{\alpha(\alpha + 1)\lambda^{\alpha}}{(\lambda - t)^{\alpha + 2}}\newline
        E[X] &= \phi^{\prime}(0) = \frac{\alpha}{\lambda}\newline
        Var(X) &= \phi^{\prime \prime}(0) = \frac{\alpha}{\lambda^{2}}
    \end{align}

### Sum of Gamma Distributions

Let $X_{1}, X_{2}, \ldots, X_{n}$ be $n$ independent random variables that are gamma distributed with parameters
$(\alpha_{1}, \lambda), (\alpha_{2}, \lambda), \ldots, (\alpha_{n}, \lambda)$. Then the distribution of the sum of these random variables is itself a gamma distribution with the parameters $\alpha^{\prime} = \sum_{i=1}^{n} \alpha_{i}$ and $\lambda^{\prime} = \lambda$.


This follows from the moment generating function of the sum of variables
\begin{align}
        E[e^{t(X_{1} + \cdots + X_{n})}] &= \prod_{i=1}^{n} E[e^{tX_{i}}] \; \text{by independence}\newline
        &= \prod_{i=1}^{n} \bigg(\frac{\lambda}{\lambda - t}\bigg)^{\alpha} = \bigg(\frac{\lambda}{\lambda - t}\bigg)^{\sum_{i=1}^{n} \alpha_{i}}
    \end{align}
which is the moment generating function of $Gamma(\sum_{i=1}^{n} \alpha_{i}, \lambda)$.

### Relation with Exponential Distribution

With $\alpha = 1$, the Gamma distribution becomes an Exponential distribution with parameter $\lambda$. Based on the previous theorem, the sum of $n$ independent Gamma distributed random variables with parameters $(1, \lambda)$ or equivalently, $n$ independent Exponentially distributed random variables with parameter $\lambda$ is a Gamma distribution with parameters $(n, \lambda)$.


## Beta Distribution

Recall the definition of a gamma function
\begin{align}
        \Gamma(\alpha) = \int_{0}^{\infty} x^{\alpha - 1}e^{-x}dx
    \end{align}

Beta function is defined on $\alpha (Re(\alpha) > 0)$ and $\beta (Re(\beta) > 0)$ as
\begin{align}
        B(\alpha, \beta) &= \int_{0}^{1} t^{\alpha-1} (1-t)^{\beta - 1} dt\newline
        \Gamma(\alpha)\Gamma(\beta) &= \int_{0}^{\infty} x^{\alpha - 1}e^{-x}dx \int_{0}^{\infty} y^{\beta - 1}e^{-y}dy = \int_{0}^{\infty}\int_{0}^{\infty}x^{\alpha - 1}y^{\beta - 1}e^{-(x+y)} dxdy\newline
        &= \int_{z=0}^{\infty}\int_{t=0}^{1} (zt)^{\alpha - 1} (z(1-t))^{\beta - 1} e^{-z} zdtdz\newline
        &= \int_{z=0}^{\infty} z^{\alpha + \beta - 1} e^{-z} \int_{t=0}^{1} t^{\alpha - 1} (1-t)^{\beta - 1}\newline
        \Gamma(\alpha)\Gamma(\beta) &= \Gamma(\alpha+\beta) B(\alpha, \beta)
    \end{align}

A Beta distribution is a continuous probability distribution defined in the interval $[0,1]$ with parameters $\alpha >0, \beta >0$ and has the following pdf
\begin{align}
        f(x;\alpha, \beta) &= \frac{x^{\alpha - 1}(1-x)^{\beta - 1}}{\int_{0}^{1} u^{\alpha - 1}(1-u)^{\beta - 1} du}\newline
        &= \frac{1}{B(\alpha, \beta)} x^{\alpha - 1}(1-x)^{\beta - 1}\newline
        &= \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)} x^{\alpha - 1}(1-x)^{\beta - 1}
    \end{align}

### Mean and Variance

\begin{align}
        \mu &= E[X] = \int_{0}^{1} x \frac{x^{\alpha - 1}(1-x)^{\beta - 1}}{B(\alpha, \beta)}\newline
        &= \frac{B(\alpha+1, \beta)}{B(\alpha, \beta)} \int_{0}^{1} \frac{x^{(\alpha + 1)-1}(1-x)^{\beta - 1}}{B(\alpha+1, \beta)}\newline
        &= \frac{B(\alpha+1, \beta)}{B(\alpha, \beta)} = \frac{\Gamma(\alpha+1)\Gamma(\beta)}{\Gamma(\alpha+\beta+1)} \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\newline
        &= \frac{\alpha \Gamma(\alpha) \Gamma(\beta)}{(\alpha+\beta)\Gamma(\alpha+\beta)}  \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)} \; \text{using}\; \Gamma(\alpha)=(\alpha - 1) \Gamma (\alpha - 1)\newline
        E[X] &= \frac{\alpha}{\alpha + \beta}\newline
        E[X^{2}] &= \int_{0}^{1} x \frac{x^{\alpha + 1}(1-x)^{\beta - 1}}{B(\alpha, \beta)} = \frac{B(\alpha + 2, \beta)}{B(\alpha, \beta)}\newline
        &= \frac{\alpha(\alpha + 1)}{(\alpha + \beta)(\alpha + \beta + 1)}\newline
        Var(X) &= E[X^{2}] - E[X]^{2} = \frac{\alpha(\alpha + 1)}{(\alpha + \beta)(\alpha + \beta + 1)} - \frac{\alpha^{2}}{(\alpha + \beta)^{2}}\newline
        &= \frac{\alpha \beta}{(\alpha + \beta)^{2}(\alpha + \beta + 1)}
    \end{align}

### Relation between Gamma and Beta Distributions

\begin{align}
        X_{1} &\sim Gamma(\alpha_{1}, \beta_{1})\newline
        X_{2} &\sim Gamma(\alpha_{2}, \beta_{2})\newline
        \frac{\beta_{2} X_{1}}{\beta_{2}X_{1} + \beta_{1}X_{2}} &\sim Beta(\alpha_{1}, \alpha_{2})\newline
    \end{align}


## Dirichlet Distribution

Dirichlet Distribution is an extension of the Beta distribution to multiple random variables and is also called *Multivariate Beta Distribution* (MBD). For $K \geq 2$ it is defined as
\begin{align}
        f(x_{1}, \ldots, x_{K}, \alpha_{1}, \ldots, \alpha_{K}) = \frac{1}{B(\boldsymbol{\alpha})} \prod_{i=1}^{K} x_{i}^{\alpha_{i} - 1}\newline
        \text{with} \quad \sum_{i=1}^{K} x_{i} = 1, \quad x_{i} \geq 0 \; \forall \; i=1,\ldots,K\newline
        B(\boldsymbol{\alpha}) = \frac{\prod_{i=1}^{K}\Gamma(\alpha_{i})}{\Gamma \bigg(\sum_{i=1}^{K} \alpha_{i} \bigg)} \quad \text{with} \; \boldsymbol{\alpha} = (\alpha_{1}, \ldots, \alpha_{K})
    \end{align}


## Normal Distribution

The Normal distribution (or gaussian distribution) is defined between $-\infty$ and $\infty$. It is parametrized by mean $\mu$ and variance $\sigma$, $X \sim \mathcal{N}(\mu, \sigma^{2})$
\begin{align}
        f_{X}(x) = \frac{1}{\sqrt{2\pi \sigma^{2}}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}
    \end{align}
As already described,
\begin{align}
        E[X] &= \mu\newline
        Var(X) &= \sigma^{2}
    \end{align}

### Standard Normal Distribution

A *Standard Normal* is defined as a normal distribution with $\mu = 0$ and $\sigma^{2} = 1$
Any normal distribution can be converted to a standard normal as $X = \frac{X - \mu}{\sigma}$
If $Y = aX + b$, then $Y \sim \mathcal{N}(a \mu + b, a^{2}\sigma^{2})$.


For a standard normal variable $Z$, it is standard to denote
\begin{align}
        P(Z \leq z) = \Phi(z) \quad P(Z = z) = \phi(z) = \mathcal{N}(0,1)
    \end{align}

Further, for a given $\alpha \in (0,1)$, define $z_{\alpha}$ by
\begin{align}
        P(Z > z_{\alpha}) = \alpha = 1-\Phi(z_{\alpha})s
    \end{align}
Some standard values of $\alpha$ can be useful

-   $z_{0.01} = 1.2816$

-   $z_{0.05} = 1.645$

-   $z_{0.025} = 1.96$

-   $z_{0.01} = 2.33$

The 68–95–99.7 rule is also useful which states that
* Probability of $X$ lying between 1 standard deviation on either side of mean is 68%
* Probability of $X$ lying between 2 standard deviation on either side of mean is 95%
* Probability of $X$ lying between 3 standard deviation on either side of mean is 99.7%

### Moment Generating Function

\begin{align}
        E[e^{tX}] = \int_{-\infty}^{\infty} e^{tx} \frac{1}{\sqrt{2\pi \sigma^{2}}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}
    \end{align}
We will rearrange the terms to form a perfect square in the exponent part with a changed mean.
\begin{align}
        E[e^{tX}] &= \int_{-\infty}^{\infty} e^{tx} \frac{1}{\sqrt{2\pi \sigma^{2}}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}\newline
        &= \int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi \sigma^{2}}}\exp \bigg( -\frac{(x-(\mu+\sigma^{2}t))^{2} - (\mu+\sigma^{2}t)^{2} + \mu^{2}}{2 \sigma^{2}} \bigg)\newline
        &= \int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi \sigma^{2}}} \exp \bigg(-\frac{(x-(\mu+\sigma^{2}t)^{2}}{2 \sigma^{2}} \bigg) \exp \bigg(\mu t + \frac{\sigma^{2} t^{2}}{2} \bigg)\newline
        E[e^{tX}] &= \exp \bigg(\mu t + \frac{\sigma^{2} t^{2}}{2}\bigg)
    \end{align}
Since the total integral of a normal distribution is 1 (the total probability).

### Sum of Normal Distributions

With the help of moment generating functions, this calculation becomes easier. Let $X_{1}, \ldots X_{n}$ be $n$ independent normal distributions with $X_{i} \sim \mathcal{N}(\mu_{i}, \sigma^{2}\_{i})$.
\begin{align}
        E[e^{t(X_{1} + X_{2} + \cdots + X_{n})}] &= \prod_{i=1}^{n} E[e^{tX_{i}}] = \prod_{i=1}^{n} e^{\mu_{i} t + \frac{\sigma_{i}^{2} t^{2}}{2}}\newline
        &= \exp(\sum_{i=1}^{n} \mu_{i} t+ \sum_{i=1}^{n}\sigma^{2} \frac{t^{2}}{2})\newline
        \implies X_{1} + X_{2} + \cdots + X_{n} &\sim \mathcal{N}(\mu_{1} + \cdots + \mu_{2}, \sigma_{1}^{2} + \cdots + \sigma_{2}^{2})
    \end{align}

### Multivariate Normal Distribution

Multivariate normal distribution is an extension of a normal distribution into multiple dimensions
\begin{align}
        f_{\mathbf{X}}(\boldsymbol{x}) = \frac{1}{\sqrt{(2\pi)^{d} \lvert \Sigma \rvert}} exp(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})\Sigma^{-1}(\mathbf{x} - \boldsymbol{\mu})^{T})
    \end{align}
for $d$ dimensional vector $\mathbf{x}$ with mean vector $\boldsymbol{\mu}$ and covriance matrix $\Sigma$.


## Chi-Square Distribution

If $Z_{1}, Z_{2}, \ldots, Z_{n}$ are $n$ independent standard normal variables, then the random variable $X$
\begin{align}
        X &= Z_{1}^{2} + Z_{2}^{2} + \cdots + Z_{n}^{2}\newline
        \text{then,} \quad X &\sim \chi_{n}^{2}
    \end{align}
i.e., $X$ follows the chi-square distribution with $n$ degrees of freedom.


If we add two chi-square distributed variables with degrees of freedom $n_{1}$ and $n_{2}$, then the resultant variable itself is chi-square distributed with $n_{1} + n_{2}$ degrees of freedom. This simply follows from the fact that the sum of the two random variables is nothing but sum of $n_{1} + n_{2}$ standard normal squared variables which is nothing but a chi-square variable with $n_{1} + n_{2}$ degrees of freedom.


If $X \sim \chi_{n}^{2}$, then $\chi_{\alpha, n}^{2}$ is
\begin{align}
        P(X \geq \chi_{\alpha, n}^{2}) = \alpha
    \end{align}
This quantity is usually listed in mathematical tables since they are heavily used in hypothesis testing.


### Relation between Chi-Square and Gamma Distribution

Consider the moment generating function for a chi-square random variable with $n=1$ degrees of freedom
\begin{align}
        E[e^{tX}] &= E[e^{tZ^{2}}] \quad\text{$Z \sim \mathcal{N}(0, 1)$}\newline
        &= \int_{-\infty}^{\infty} e^{tx^{2}} f_{Z}(x) dx \quad\text{since $E[g(x)] = \int_{x} g(x)p(x)$}\newline
        &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{tx^{2}} e^{-x^{2}/2}\newline
        &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-x^{2}(1/2 - t)}\newline
        \text{Using}\quad \int_{-\infty}^{\infty} e^{-a(x+b)^{2}} &= \sqrt{\frac{\pi}{a}}\newline
        E[e^{tX}] &= \frac{1}{\sqrt{2\pi}} \sqrt{\frac{\pi}{1/2 - t}}\newline
        &= \frac{1}{\sqrt{1 - 2t}}
    \end{align}

Extending this idea to the case of $n$ degrees of freedom,
\begin{align}
        E[e^{tX}] &= E[e^{t(Z_{1}^{2} + Z_{2}^{2} + \cdots + Z_{n}^{2})}]\newline
        &= E[\prod_{i=1}^{n} e^{t Z_{i}^{2}}]\newline
        &= \prod_{i=1}^{n} E[e^{t Z_{i}^{2}}] \quad\text{since $Z_{i}$ are independent}\newline
        &= (1 - 2t)^{-n/2} \quad\text{from the derivation above}
    \end{align}

But, the quantity just derived is nothing but the moment generating function of the Gamma distribution with parameters $(n/2, 1/2)$. Hence, by the uniqueness of the moment generating function, we are forced to conclude that the **probability density function of a chi-square variable with n degrees is same as that of a Gamma distribution with parameters (n/2, 1/2)**.

Thus,
\begin{align}
        f_{X}(x) = \frac{\frac{1}{2} e^{-x/2} (\frac{x}{2})^{(n/2) - 1}}{\Gamma(\frac{n}{2})} \quad\text{$x > 0$}
    \end{align}

#### Sum of Exponentially Distributed Random Variables to Chi-Square Distribution

We say that a Gamma distributed random variable with $\lambda = 1/2$ and $\alpha$ can be considered equivalent to a $\chi^{2}\_{2\alpha}$ variable. Here, $\lambda$ is constrained to be $1/2$. By transforming the variables appropriately, we can extend the idea to a sum of exponentially distributed random variables.


Consider $n$ independent and identically exponentially distributed random variables $X_{i}$ with parameter $\lambda$. Consider for any of those random variables $X_{i}$,
\begin{align}
        Y &= 2\lambda X\newline
        F_{Y}(y) &= P(Y \leq y) = P(X \leq \frac{y}{2\lambda})\newline
        &= F_{X}(\frac{y}{2\lambda}) = 1 - \exp \bigg( -\frac{y}{2} \bigg)\newline
        f_{Y}(y) &= \frac{d}{dy} 1 - \exp \bigg( -\frac{y}{2} \bigg)\newline
        &= \frac{1}{2}\exp \bigg( -\frac{y}{2} \bigg)\newline
        &= Exp(\frac{1}{2})
    \end{align}
i.e., $2\lambda Exp(\lambda) \sim Exp(\frac{1}{2})$. Now, consider the sum of these transformed random variables
\begin{align}
        2\lambda\bigg( X_{1} + \cdots X_{n} \bigg) &\sim Gamma(n, 1/2) \sim \chi_{2n}^{2}
    \end{align}

Hence, we can convert the sum of $n$ exponentially distributed random variables with parameter $\lambda$, to a $\chi^{2}\_{n}$ variable by multiplying the individual variables by $2/\lambda$.

### Mean and Variance

Since the distribution of a chi-square variable is identical to a $Gamma(n/2, 1/2)$ distribution,
\begin{align}
        E[X] &= n\newline
        Var(x) &= 2n
    \end{align}


## t-Distribution

Let $Z$ be a standard normal random variable and let $\chi_{n}^{2}$ be a chi-square random variable. Assuming these two random variables are independent, the random variable $T_{n}$ is
\begin{align}
        T_{n} = \frac{Z}{\sqrt{\chi_{n}^{2}/n}}
    \end{align}
is said to have a t-distribution with $n$ degrees of freedom.

This distribution is symmetric around the normal, and as $n$ increases, the distribution becomes more and more like the standard normal distribution.

{% include image.html url="notes/probability/images/t_1.png" description="t-distribution for different degrees of freedom" img_classes="notes-img t_1" %}
{% include image.html url="notes/probability/images/t_2.png" description="Comparison with standard normal" img_classes="notes-img t_1" %}

From the above figure , we see that t-distribution is heavier tailed than a standard normal. Translation, this means that a larger value is more likely to occur under a t-distribution than a standard normal. Furthermore, the heavy tails imply more variance than the standard normal.


For $\alpha$ between $0$ and $1$, let $t_{\alpha, n}$ be such that
\begin{align}
        P(T_{n} \geq t_{\alpha, n}) = \alpha
    \end{align}
By symmetry around the origin,
\begin{align}
        P(T_{n} \leq -t_{\alpha, n}) &= \alpha\newline
        \text{or} \quad P(T_{n} \geq -t_{\alpha, n}) &= 1 - \alpha\newline
        \text{and,} \quad -t_{\alpha, n} &= t_{1 - \alpha, n}
    \end{align}

These standard values are available in math charts since they form the basis of the t test.

{% include image.html url="notes/probability/images/t_3.png" description="visual representation of $t_{\alpha,n}$" img_classes="notes-img" %}

### Mean and Variance

The following are stated without proof
\begin{align}
        E[T_{n}] &= 0\newline
        Var(T_{n}) &= \frac{n}{n-2}\newline
    \end{align}

In the limit of large $n$, the variance is close to $1$, which is consistent with the fact that the distribution resembles a standard normal in that limit.


## F-Distribution

If $\chi_{n}^{2}$ and $\chi_{m}^{2}$ are two independent chi-squared distributions with $n$ and $m$ degrees of freedom respectively, then the variable $F_{n,m}$ defined as
\begin{align}
        F_{n,m} = \frac{\chi_{n}^{2}/n}{\chi_{m}^{2}/m}
    \end{align}
is said to have an F-distribution with n and m degrees of freedom.

For any $\alpha$ between $0$ and $1$, we define $F_{\alpha, n, m}$ as
\begin{align}
        P(F_{n,m} \geq F_{\alpha, n, m}) = \alpha
    \end{align}
These values are available in standard tables for different combinations of $\alpha, n$ and $m$.


Consider
\begin{align}
        \alpha &= P(\frac{\chi_{n}^{2}/n}{\chi_{m}^{2}/m} > F_{\alpha, n, m})\newline
        &= P(\frac{\chi_{m}^{2}/m}{\chi_{n}^{2}/n} < \frac{1}{F_{\alpha, n, m}})\newline
        &= 1 - P(\frac{\chi_{m}^{2}/m}{\chi_{n}^{2}/n} \geq \frac{1}{F_{\alpha, n, m}})\newline
        \text{or} \quad P(\frac{\chi_{m}^{2}/m}{\chi_{n}^{2}/n} \geq \frac{1}{F_{\alpha, n, m}}) &= 1 - \alpha\newline
        \text{but} \quad P(F_{m,n} \geq F_{1 - \alpha, m, n}) &= 1 - \alpha\newline
        \text{From the last two equations} \quad \frac{1}{F_{\alpha, n, m}} &= F_{1-\alpha, m, n}
    \end{align}

### Mean and Variance

We state the following without proof for $X \sim F(n,m)$
\begin{align}
        E[X] &= \frac{m}{m - 2} \: m > 2\newline
        Var(x) &= \frac{2 m^{2}(m + n - 2)}{n(m - 2)^{2}(m - 4)} \: m > 4
    \end{align}


## Logistics Distribution

A random variable $X$ is said to have a logistics distribution with parameters $\mu$ and $v$ if its cumulative density function is of the form
\begin{align}
        F_{X}(x) = \frac{e^{(x-\mu)/ v}}{1 + e^{(x-\mu)/ v}}, \quad \text{ $\forall - \infty < x < \infty$}
    \end{align}
Differentiating to get the density function
\begin{align}
        f_{x}(x) = \frac{e^{(x-\mu)/v}}{v(1 + e^{(x-\mu)/v})^{2}}, \quad \text{ $\forall -\infty < x < \infty$}
    \end{align}

### Mean

\begin{align}
        E[X] &= \mu\newline
        v &= \text{dispersion parameter}
    \end{align}


## Renewal Process

This is a fundamental stochastic process useful in modelling arrivals and interarrival times. Some definitions will make the usage clear.


Let $S_{i}$ denote the $i$th renewal time or the time when the $i$th arrival takes place. By definition, $S_{0} = 0$. We can also define
\begin{align}
        S_{n} &= S_{n-1} + \xi_{n}\newline
        S_{n} &= \xi_{1} + \xi_{2} + \cdots + \xi_{n-1}
    \end{align}
where $\xi_{i}$ are positive ($P(\xi > 0) = 1$) independent identically distributed variables representing the interarrival times. We also define
\begin{align}
        N_{t} &= \argmax_{k} \{ S_{k} \leq t \}\newline
        \{ S_{n} > t \} &= \{ N_{t} < n \}
    \end{align}
or, $N_{t}$ is simply the number of arrivals till the time $t$.


Define the following quantity
\begin{align}
        F^{n\*} &= F_{\xi} * \ldots * F_{\xi} \text{ $n$ times}\newline
        u(t) &= \sum_{i=1}^{\infty} F^{n\*}(t)
    \end{align}
It can be shown that the function $u(t)$ converges. The expectation of $N_{t}$ then becomes
\begin{align}
        E[N_{t}] &= E[\text{number of $n$ such that $S_{n} \leq t$}]\newline
        &= E[\sum_{n=1}^{\infty} I(S_{n} \leq t)] \quad \text{ sum of Indicators will equal $n$}\newline
        &= \sum_{n=1}^{\infty} P(S_{n} \leq t) \quad \text{ since $E[$Indicator$]$ is just the function inside indicator}\newline
        &= \sum_{n=1}^{\infty} F^{n\*}(t) \quad \text{ by defining cumulative as sum of $\xi$s}\newline
        &= u(t)
    \end{align}

### Laplace Transform

For a density function $f$ defined from $\mathbb{R}^{\geq 0} \to \mathbb{R}$, Laplace transform is
\begin{align}
        L_{f}(s) = \int_{\mathbb{R}^{\geq 0}} e^{-sx} f(x) dx
    \end{align}
The following properties hold for this transform

1.  If $f$ is a probability density function, then
    \begin{align}
                E[e^{-sx}] = L_{f}(s)
            \end{align}

2.  if $f_{1}$ and $f_{2}$ are two probability density functions, then
    \begin{align}
                L_{f_{1}\*f_{2}}(s) = L_{f_{1}}(s) L_{f_{2}}(s)
            \end{align}

3.  If $F$ is the cumulative probability distribution for $X$ and $p$ is the probability density function, then
    \begin{align}
                L_{F_{X}}(s) = \frac{L_{p_{X}}(s)}{s}
            \end{align}
    which can be proven using integration by parts as follows
    \begin{align}
                L_{F_{X}}(s) = \int_{\mathbb{R}^{\geq 0}} F_{X}(x) \frac{d(e(-sx))}{s} = 0 + \frac{1}{s} \int_{\mathbb{R}^{\geq 0}} p_{X}(x) e^{-sx} dx
            \end{align}

### Calculating the Expectation

Armed with the concept of a Laplace transform, we make the following observation first
\begin{align}
        u(t) &= \sum_{i=1}^{\infty} F^{n\*}(t) = F(t) + \sum_{i=2}^{\infty} F^{n\*}(t)\newline
        &= F(t) + \big( \sum_{i=1}^{\infty} F^{n\*}(t) \big) * F(t)\newline
        &= F(t) + u(t) * F(t)\newline
       u(t) &= F(t) + u(t) * p(t)
    \end{align}
where $p$ is the probability density function and the last line stems from the fact that $\int u * F = \int u(x-y) dF(y) = \int u(x-y) p(y) dy$. Taking Laplace transform on both sides,

\begin{align}
        L_{u}(s) &= L_{F}(s) + L_{u}(s) L_{p}(s)\newline
        L_{u}(s) &= \frac{L_{p}(s)}{s} + L_{u}(s) L_{p}(s) \text{ from point 3 above}\newline
        L_{u(s)} &= \frac{L_{p}(s)}{s(1-L_{p}(s))}
    \end{align}

The last equation can be used to calculate the laplace transform of $u(t)$ and consecutively guess the functional form of $u(t)$.

### Limit Theorems for Renewal Processes

The following two theorems hold true for Renewal processes

1.  If $E[\xi] = \mu < \infty$, then
    \begin{align}
                \lim_{t \to \infty} \frac{N_{t}}{t} = \frac{1}{\mu}
            \end{align}
    which is analogous to the strong law of large numbers. This can be proven as follows
    \begin{align}
                S_{N_{t}} \leq t \leq S_{N_{t} + 1} \text{ from the definition of $N_{t}$}\newline
                \text{or, } \frac{N_{t}}{S_{N_{t} + 1}} \leq \frac{N_{t}}{t} \leq \frac{N_{t}}{S_{N_{t}}}
            \end{align}
    we can calculate the limits on the two bounds as
    \begin{align}
                \lim_{t \to \infty} \frac{N_{t}}{S_{N_{t}}} = \lim_{n \to \infty} \frac{n}{S_{n}} = \frac{1}{\mu}
            \end{align}
    from the strong law of large numbers applied to $\lim_{n \to \infty} \frac{S_{n}}{n}$. Similarly, one can show
    \begin{align}
                \lim_{t \to \infty} \frac{N_{t}}{S_{N_{t} + 1}} = \lim_{t \to \infty} \frac{N_{t}}{N_{t} + 1} \lim_{t \to \infty} \frac{N_{t} + 1}{S_{N_{t} + 1}} = 1 * \frac{1}{\mu}
            \end{align}

2.  If $Var(\xi) = \sigma^{2} < \infty$, then
    \begin{align}
                \lim_{t \to \infty} \frac{N_{t} - t/\mu}{\sigma \sqrt{t}/\mu^{3/2}} = \mathcal{N}(0,1)
            \end{align}
    which is analogous to the central limit theorem. It can be proven by considering the CLT on $\xi$s
    \begin{align}
                \lim_{n \to \infty} P(\frac{S_{n} - n\mu}{\sigma \sqrt{n}} \leq x) &= \text{CDF of }\mathcal{N}(0,1)\newline
                \text{or, } \lim_{n \to \infty} P(S_{n} \leq n\mu + \sigma \sqrt{n} x) &= \text{CDF of }\mathcal{N}(0,1)\newline
                \text{or, } \lim_{n \to \infty} P(N_{t} \geq n) &= \text{CDF of }\mathcal{N}(0,1) \text{ from definition of $N_{t}$, where $t = n\mu + \sigma \sqrt{n} x$}\newline
            \end{align}
    We substitute $n\mu = t$ for very large value of $n$, since the total time will become total variables into the expected time for one $\xi$ when $n$ is large. Hence,
    \begin{align}
                n &= \frac{t}{\mu} - \frac{\sigma \sqrt{t}}{\mu^{3/2}}x\newline
                \lim_{n \to \infty} P(N_{t} \geq n) &= \lim_{n \to \infty} P(\frac{N_{t} - t/\mu}{\sigma \sqrt{t}/\mu^{3/2}} \leq x) = \text{CDF of }\mathcal{N}(0,1)
            \end{align}


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


## Recurring and Transient States
First lets define **accessible** states. A state $j$ is accessible from $i$ if $r_{ij}(n)$ is positive for sufficiently large $n$. This means even after running the chain for a long time, its possible to reach $j$ from $i$.

A state $i$ is called **recurrent** if, starting from $i$, and travelling anywhere, it is always possible to return to $i$. Using the concept of _accessibility_ defined above, let $A(j)$ denote the set of states accessible from $j$. Then, for every state $i \in A(j)$, $j \in A(i)$. Meaning that we can wander to any accessible state of $j$ and expect to return back to $j$ with finite probability.

If a state is not recurrent, it is **transient**. This means that there exists at least one $i \in A(j)$ such that $j \notin A(i)$.

All these definitions only depend on the sign of the transition probabilities (whether they are positive or not), and not on the values.

In the below figure, we see examples of different types of states.
* State 1 is recurrent since only 1 is accessible from 1.
* 2 is transient since all other states are accessible from 2, but 2 is not accessible from either of those.
* 3 and 4 are accessible only from each other and are thus recurrent.

{% include image.html url="notes/probability/images/markov_3.png" description="Sample Markov chain with transient and recurrent states" img_classes="notes-img markov_3" %}

Any set of states such that they are all accessible from each other form a _recurrent class_. In the figure above, states 3,4 from one recurrent class while state 1 is a recurrent class in itself.

### Markov Chain Decomposition
* A Markov chain can be decomposed into one or more recurrent classes, plus a few transient states.
* A recurrent state is accessible from all other recurrent states in its class, but is not accessible from states in other recurrent classes.
* A transient state is not accessible from any recurrent state.
* At least one, possibly more, recurrent states are accessible from a given transient state.

Decomposing a Markov chain and understanding the recurrent and transient components is a great way to reason out the behaviour of the chain. We note the following two observations
* If a chain enters or starts in a class of recurrent states, it stays within the class since by definition they are all accessible from each other and are visited an infinite number of times.
* If the initial state is transient, the chain first goes through a set of transient states before finally settling down in a class of recurrent states.

States in a recurrent class are **periodic** if they can be grouped into $d > 1$ groups such that all transitions from one group lead to the next group (in a fixed order). A recurrent class is **aperiodic** if it is not periodic.


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

The $pi_{j}$ sum up to 1 and form a probability distribution called the **stationary distribution** of the chain (because if the initial distribution $P(X_{0} = j) = \pi_{j}, the occupancy distribution of the states is constant for all steps and can be verified using total probability theorem on any of the nodes).

In the steady state,
* $\pi_{j} = 0$ for transient states
* $\pi_{j} > 0$ for recurrent states
(note that any state that is absorbing is actually recurrent since its only connected to itself and hence _accessible_ to itself from itself)


## Birth Death Process

Consider the checkout counter example. The states are represented by the number of people currently being processed, and we always move $n$ to $[n-1, n, n+1]$, i.e., either the people in the queue decrease by one, remain same or increase by one. Let the probability for moving up be $p$ and moving down be $q$.

{% include image.html url="notes/probability/images/markov_1.png" description="" img_classes="notes-img" %}

Let's estimate the steady state probabilities. Consider the following diagram splitting the chain into two parts through the two adjacent states

{% include image.html url="notes/probability/images/markov_2.png" description="" img_classes="notes-img markov_1" %}

In this case, to maintain steady state, long term frequency of left-right transition should be same as right left transition, i.e., $\pi_{i}p_{i} = \pi_{i+1}q_{i}$ because between any two transitions of type $i \to i + 1$, exactly one transition $i + 1 \to i$ must have occurred due to the structure of the chain.

In the special case of $p_{i} = p$ and $q_{i} = q \;\forall\; i$,
\begin{align}
        \rho &= \frac{p}{q} \quad\text{load factor}\newline
        \pi_{i+1} &= \pi_{i} \frac{p}{q} = \pi_{i} \rho \newline
        \pi_{i} &= \pi_{0} \rho^{i} \quad\text{$i = 0,\ldots,m$} \newline
        \text{Using } \sum_{i=0}^{m} \pi_{0}\rho^{i} &= 1,\newline
        \pi_{0} &= \frac{1}{\sum_{i=0}^{m} \rho^{i}}\newline
        \text{if $p < q$ and $m \rightarrow \infty,$}\newline
        \pi_{0} &= 1 - \rho \newline
        \pi_{i} &= (1-\rho)\rho^{i}\newline
        E[X_{n}] &= \frac{\rho}{1-\rho} \quad\text{Exponential Distribution}
    \end{align}
When $\rho = 1$ or $p = q$, then all states are equally likely - symmetric random walk.



## Absorption Probabilities

For a fixed absorbing (_final_) state $s$, let $a_{i}$ denote the probability of absorption given the initial state is $i$. Assuming we start from a transient state, we have the following equations to solve for $a_{i}$
\begin{align}
    a_{s} &= 1\newline
    a_{i} &= 0 \quad\text{for all $i \neq s$, $i$ is aborbing state}\newline
    a_{i} &= \sum_{j}a_{j}p_{ij}
\end{align}

The last equation follows from the law of total probability. Let $A$ be the event of absorption to state $s$
\begin{align}
    a_{i} &= P(A \vert X_{0} = i)\newline
    &= \sum_{j}P(A \vert X_{1} = j, X_{0} = i)P(X_{1} = j \vert X_{0} = i)\newline
    &= \sum_{j}a_{j}p_{ij}\quad\text{outflux to the possible states}
\end{align}

Be cognizant of the flow in the last equation. $a_{i}$ denotes the absoption probability into state $s$ given $i$ as the starting state. To utilize the law of total probability, we move 1 step into all the states directly connect with $i$ and assume we will start the absorption cycle again ($a_{j}$).

For multiple absorption states, we can consider them together as a group with a single absorption probability and setup the equations.

Going further, let $\mu_{i}$ denote the expected no of steps until absorption (in a recurrent state) starting from a transient state $i$. Clearly $\mu_{i}$ is zero if $i$ is recurrent since we are already in a recurrent state. The equations thus setup as
\begin{align}
    \mu_{i} &= 0 \quad\text{if $i$ is recurrent}\newline
    \mu_{i} &= 1 + \sum_{j} \mu_{j} p_{ij}
\end{align}
The last equation is derived using law of total probability similar to how we did earlier. The small change that comes now is to account for the 1 step we have taken to move from $i \to j$.

For a given state $s$,
\begin{align}
        E[\text{steps to first time reach $s$ from $i$}] &= t_{i} \newline
        t_{i} &= E[min (n \geq 0 \text{ such that } X_{n} = s)] \newline
        t_{s} &= 0 \newline
        t_{i} &= 1 + \sum_{j} t_{j}p_{ij} \quad\text{outflux to all possible states}
    \end{align}

Mean recurrence time (mean time to reach back a state) for $s$
\begin{align}
        t_{s}^{\*} &= E[min (n \geq 1 \text{ such that } X_{n}=s) | X_{0} = s] \newline
        t_{s}^{\*} &= 1 + \sum_{j} t_{j} p_{ij}
    \end{align}


# Limit Theorems

Here we look at inequalities around the mean (and variance) of random variables and try to get bounds on probabilities of certain associated events. These are especially useful when either the distribution of the random variable is not available, or calculating it may be difficult.


## Markov Inequality

For any non-negative random variable $X$ and positive $a$,
\begin{align}
        P(X \geq a) \leq \frac{E[X]}{a}
    \end{align}
This means that for a random variable with small mean, the probability of taking large values is small.


This can be proved as follows
\begin{align}
        E[X] &= \int_{0}^{\infty} xp_{X}(x) dx = \int_{0}^{a} xp_{X}(x) dx + \int_{a}^{\infty} xp_{X}(x) dx\newline
        &\geq \int_{a}^{\infty} xp_{X}(x) dx \geq \int_{a}^{\infty} ap_{X}(x) dx = a\int_{a}^{\infty} p_{X}(x) dx\newline
        &\geq aP(X \geq a)
    \end{align}

Based on experiments with simple distributions (like uniform distribution), it can be verified that the bounds provided this inequality can be quite loose.


## Chebychev Inequality

For any random variable $X$ with mean $\mu$ and variance $\sigma^{2}$, and a positive $k$,
\begin{align}
        P(\lvert X - \mu \rvert \geq k) \leq \frac{\sigma^{2}}{k^{2}}
    \end{align}
This means that for a random variable with small variance, the probability of taking a value far from the mean is small.


This can be proved using Markov's inequality on the non negative random variable $(X-\mu)^{2}$ and positive $k^{2}$
\begin{align}
        P((X-\mu)^{2} \geq k^{2}) &\leq \frac{E[(X-\mu)^{2}]}{k^{2}}\newline
        \text{or, } \; P(\lvert X - \mu \rvert \geq k) &\leq \frac{\sigma^{2}}{k^{2}}
    \end{align}

Substituiting $k = c\sigma$,
\begin{align}
        P(\lvert X - \mu \rvert \geq c\sigma) \leq \frac{1}{c^{2}}
    \end{align}


## Weak Law of Large Numbers

The weak law of large numbers provides bounds on the error between the true mean of a distribution and its estimated value from a sequence of random variables. Let $X_{1}, X_{2}, \ldots, X_{n}$ be a sequence of $n$ identically distributed random variables with mean $\mu$ and (a finite) variance $\sigma^{2}$, then
\begin{align}
        M_{n} &= \frac{X_{1} + \cdots + X_{n}}{n}\newline
        P(\mid M_{n} - \mu \mid \geq \epsilon) &\leq \frac{\sigma^{2}}{n\epsilon^{2}}\newline
        \lim_{n \to \infty} P(\mid M_{n} - \mu \mid \geq \epsilon) &\to 0
    \end{align}

For a distribution with finite variance, the above follows from Chebychev's inequality on $M_{n}$
\begin{align}
        M_{n} &= \frac{X_{1} + X_{2} + \cdots + X_{n}}{n} \newline
        E[M_{n}] &= \frac{1}{n} \sum_{i=1}^{n} E[X_{i}] = \mu \quad\text{expectation of expectation} \newline
        Var(M_{n}) &= \sum_{i=1}^{n} Var(\frac{X_{i}}{n}) = \frac{\sigma^{2}}{n} \quad\text{since $X_{i}$ are independent} \newline
        P(\mid M_{n} - \mu \mid \geq \epsilon) &\leq \frac{\sigma^{2}}{n\epsilon^{2}}
    \end{align}
The above expression allows us to calculate the probability that $M_{n}$ falls in the interval $[\mu-\epsilon, \mu+\epsilon]$. As the value of $epsilon$ grows smaller, we will require a large value of $n$ to be able to confidently say that $M_{n}$ indeed falls in that range.


In cases where the true variance of the distribution is not known, we can still use the above inequality in the context of an upper bound on the variance. For instance, it can be shown that the variance of a $Bernoulli(p)$ is $p(1-p) \leq 1/4$.


## Convergence in Probability

First, we consider convergence in the context of a sequence of real numbers. A sequence of real numbers $a_{1}, a_{2}, \ldots$ converges to $a$ if for every $\epsilon > 0$, there exists $n_{0}$ such that $\lvert a_{n} - a \rvert \leq \epsilon$ for all $n \geq n_{0}$.


### Sequence of Random Variables

Before jumping to convergence in probability, lets review what a sequence of random variables represents. Consider a sample space $S = \{s_{1}, s_{2}, \ldots\}$. A random variable $X$ maps every outcome of the sample space to a real number and associates a probability to those real numbers: $X(s_{i}) = x_{i}$.


A sequence of random numbers will provide a different mapping that will be dependent on n: $X_{n}(s_{i}) = x_{n,i}$. When discussing convergence of a sequence of random variables, we will refer to a sequence of such kind. A basic example of such a sequence can be on a coin toss
\begin{align}
        X_{n} = \begin{cases} 1/(n+1) &\mbox{if Heads}\newline 1 &\mbox{if Tails} \end{cases}
    \end{align}

### Types of Convergence

There are different types of convergences. Some are stronger and others weaker. Stronger convergence can imply the weaker ones, but not the other way around.

The diagram below summarizes the relation between the different types of convergence. The convergences are arranged in decreasing order of strength from top to bottom.

#### Convergence in Distribution

This is the weakest type of convergence and only deals with the CDF. There is no requirement for $X_{n}$ to converge to $X$. Mathematically, A sequence of random variables $X_{i}$ converges in distribution to $X$ if for $\lim_{n \to \infty} P(X_{n} \leq x) = P(X \leq x)$ for all $x$ where $F_{X}(x) = P(X \leq x)$ is continuous. This is denoted as $X_{n} \overset{d}\rightarrow X$.


If $X_{i}$ and $X$ are both discrete distributions with non-negative integral values, then $X_{n} \overset{d}\rightarrow X$ if and only if $\lim_{n \to \infty} P_{X_{n}}(x) = P_{X}(x)$. This can be proved by first assuming LHS to be true to derive RHS and vice versa. With this, we can prove that a Bernoulli random variable converges to Poisson in the limit $n \to \infty$. CLT is a famous example of convergence in distribution and is discussed in subsequent sections.

#### Convergence in Probability

Convergence in probability is stronger than convergence in distribution. A sequence of random variables $X_{i}$ converges in probability to $X$ if for $\lim_{n \to \infty} P(\lvert X_{n} - X \rvert \geq \epsilon) = 0$ for every $\epsilon > 0$. This is denoted as $X_{n} \overset{p}\rightarrow X$.


We can also write this in similar terms as the convergence of a sequence of real numbers by changing the formulation. A sequence of random variables $X_{n}$ converges to $X$ if for every $\epsilon > 0$, there exists $n_{0}$ such that $P(\lvert X_{n} - X \rvert \geq \epsilon) \leq \delta$ for all $n \geq n_{0}$.


A famous example of this type of convergence is the weak law of large numbers discussed earlier.

#### Convergence in Mean

For a fixed $r \geq 1$, a sequence of random variables $X_{i}$ is said to converge to $X$ in the $r^{th}$ mean or in the $L^{r}$ norm if $\lim_{n \to \infty} E[\lvert X_{n} - X \rvert^{r}] = 0$. This is denoted by $X_{n} \overset{L^{r}}\rightarrow X$. For $r=2$ this is called mean-square convergence and is denoted by $X_{n} \overset{m.s.}\rightarrow X$.


Mean convergence is stronger than convergence in probability, i.e., convergence in $L^{r}$ norm implies convergence in probability as well.

#### Almost Sure Convergence

Consider a sequence of random variables $X_{1}, X_{2}, X_{3}, \ldots$ defined on a sample space $S$ (assume finite for the moment) $= \{s_{1}, s_{2}, \ldots s_{k}\}$. Since a random variable $X_{n}$ is a mapping from an outcome in sample space to the set of real numbers, $X_{n}(s_{i}) = x_{ni}$ for $i=1,2,\ldots,k$.


After performing the random experiment, one of the $s_{i}$ś will be the outcome of the experiment and we will know the value for all the $X_{n}$ś. For $s_{j}$ as the outcome, we observe the sequence $x_{1j}, x_{2j}, \ldots$. Almost surely convergence is defined based on the convergence of this sequence of numbers.


A sequence of random variables $X_{1}, X_{2}, \ldots$ converges almost surely to a random variable $X$ if $P(\{s \in S:\lim_{n \to \infty} X_{n}(s) = X(s)\}) = 1$ and is denoted by $X_{n} \overset{a.s.}\rightarrow X$.


There is a useful set of results to show almost convergence. If for the sequence of random variables and all $\epsilon > 0$, we have
\begin{align}
        \sum_{n=1}^{\infty}P(\lvert X_{n} - X \rvert > \epsilon) &< \infty\newline
        \implies X_{n}(s) &= X(s)
    \end{align}
This is only a sufficient condition. Below is a condition that is both necessary and sufficient
\begin{align}
        A_{m} = \{\lvert X_{n} - X \rvert < \epsilon \;\text{for all}\; n \geq m \}\newline
        \text{Then, }\; X_{n} \overset{a.s.}\rightarrow X \;\text{if and only if for any $\epsilon > 0$}\newline
        \lim_{m \to \infty} P(A_{m}) = 1
    \end{align}
A famous theorem in almost surely convergence is the strong law of large numbers, which states that for a set of independent identically distributed random with a finite mean, the expected value of the average of the random numbers almost surely converges to the mean.

#### Continuous Mapping Theorems

Let $X_{1}, X_{2}, X_{3}, \ldots$ be a sequence of random variables, and let $h: \mathcal{R} \rightarrow \mathcal{R}$, then
\begin{align}
        \text{If}\; X_{n} \overset{d}\rightarrow X \; &\text{then} \; h(X_{n}) \overset{d}\rightarrow h(X)\newline
        \text{If}\; X_{n} \overset{p}\rightarrow X \; &\text{then} \; h(X_{n}) \overset{p}\rightarrow h(X)\newline
        \text{If}\; X_{n} \overset{a.s.}\rightarrow X \; &\text{then} \; h(X_{n}) \overset{a.s.}\rightarrow h(X)
    \end{align}


## Central Limit Theorem

Chebychev's inequality gives a loose bound. We can do better with CLT. Let $X$ be a random variable with mean $\mu$ and variance $\sigma^{2}$, and let $X_{i}$ be independent identically distributed random variables with the same distribution as $X$. Consider the random variable $S_{n}$ defined below,
\begin{align}
        S_{n} &= X_{1} + X_{2} + \cdots + X_{n}\newline
        Z_{n} &= \frac{S_{n} - E[S_{n}]}{\sigma_{n}} \quad\text{random variable with mean $0$ and variance $1$} \newline
             &= \frac{S_{n} - nE[X]}{\sqrt{n} \sigma}\newline
        \text{Then,}\quad \lim_{n \to \infty} P \bigg(\frac{S_{n} - n\mu}{\sqrt{n} \sigma} \leq c \bigg) &= P(Z \leq c) = \Phi(c)
    \end{align}
Or, the cumulative distribution of the random variable $(S_{n} - n\mu)/\sqrt{n} \sigma$ converges to that of a standard normal.

By defining the confidence on how close we desire $S_{n}$ to the actual mean, we can calculate the required value of the $n$ using standard normal CDF tables. However, we need to have an estimate of variance of the distribution in order to estimate $n$.


As a rule of thumb, $n=30$ gives a very close approximation to the normal distribution.


Similar to the weak law of large numbers, if the variance is not available, but an upper bound on the same can be obtained, the probability of intereset can be calculated using this bound.

### De Moivre-Laplace Approximation to the Binomial

A Binomial random variable $S_{n}$ can be viewed as the sum of $n$ Bernoulli random variables $X_{i}$ with the parameter $p$. We can apply the central limit theorem to obtain the probabiliy of the variable between any two ranges
\begin{align}
        P(k \leq S_{n} \leq l) &= P(\frac{k - np}{\sqrt{n} p(1-p)} \leq \frac{S_{n} - np}{\sqrt{n} p(1-p)} \leq \frac{l - np}{\sqrt{n} p(1-p)})\newline
        &= P(\frac{S_{n} - np}{\sqrt{n} p(1-p)} \leq \frac{l - np}{\sqrt{n} p(1-p)}) - P(\frac{S_{n} - np}{\sqrt{n} p(1-p)} \leq \frac{k - np}{\sqrt{n} p(1-p)})\newline
        &\approx \Phi(\frac{l - np}{\sqrt{n} p(1-p)}) - \Phi(\frac{k - np}{\sqrt{n} p(1-p)}) \; \text{for large $n$}
    \end{align}
Since $S_{n}$ will take discrete values, $P(S_{n} <= k) = P(S_{n} < k+1)$ for any positive integer $k$. A better approximation of the above formula can be obtained by considering the middle point of $k$ and $k+1$ as applicable
\begin{align}
        P(k \leq S_{n} \leq l)&\approx \Phi(\frac{l + \frac{1}{2} - np}{\sqrt{n} p(1-p)}) - \Phi(\frac{k - \frac{1}{2} - np}{\sqrt{n} p(1-p)}) \; \text{for large $n$}
    \end{align}

This correction yields a more closer result to the actual values. With $p$ close to $1/2$, the approximation works well for $n = 40,50$ itself. The distribution is also symmetric at this point which helps the CLT. However, as the $p$ becomes closer to $0$ or $1$, larger values of $n$ are required for the approximation to be valid.


We can also calculate the value of a single point as given below
\begin{align}
        P(S_{n} = k)&\approx \Phi(\frac{k - \frac{1}{2} - np}{\sqrt{n} p(1-p)}) - \Phi(\frac{k + \frac{1}{2} - np}{\sqrt{n} p(1-p)}) \; \text{for large $n$}
    \end{align}


## Strong Law of Large Numbers

This law is similar to the weak law, but deals with the convergence of the mean. Let $X_{i}$ be $n$ independent identically distributed random variables with mean $\mu$. Then the mean $M_{n}$,
\begin{align}
        \lim_{n \to \infty} P(M_{n} = \mu) = 1
    \end{align}

That is, $M_{n}$ converges to $\mu$ with probability $1$ or **almost surely**. Convergence with probability $1$ implies convergence in probability, but the converse is not always true.


There is a subtle differnce between WLLN and SLLN. WLLN states that the probability of deviation of $M_{n}$ from the true mean is always finite, although the probability of deviation converges to $0$ in the limit. On the other hand, SLLN states with absolute certainty that in infinite experiments, the sample mean will converge to the true mean with probability $1$.


# Distribution of Sample Mean and Variance

Let $X_{1}, X_{2}, \ldots, X_{n}$ be independent random variables from a distribution having mean $\mu$ and variance $\sigma^{2}$. From the central limit theorem,
\begin{align}
        \frac{X_{1} + X_{2} + \cdots + X_{n} - n\mu}{\sigma \sqrt{n}} \sim \mathcal{N}(0, 1)
    \end{align}
or, the sum of the random variables follows the distribution of a standard normal as the value of $n$ becomes large. Typically, the property starts to manifest as soon as $n$ becomes around 30.


## Sample Mean

Let the random variable $\overline{X}$ denote the sample mean and is defined as
\begin{align}
        \overline{X} = \frac{X_{1} + X_{2} + \cdots + X_{n}}{n}
    \end{align}
Note that any scaled version of a normal distribution is also normal. Thus, **The mean of n independent random variables coming from the same distribution also follows a normal distribution for sufficiently large n**.


Note that sample mean is itself a random variable and thus has a distribution. This happens because the quantity itself is the average of several random variables, which are instances of the same probability distribution.
\begin{align}
        E[\overline{X}] &= E[\frac{X_{1} + X_{2} + \cdots + X_{n}}{n}]\newline
        &= \frac{1}{n} \sum_{i=1}^{n} E[X_{i}]\newline
        E[\overline{X}] &= \mu
    \end{align}

Similiarly, the variance of the sample mean can be computed as follows
\begin{align}
        Var(\overline{X}) &= Var(\frac{X_{1} + X_{2} + \cdots + X_{n}}{n})\newline
        &= Var(\frac{X_{1}}{n}) + Var(\frac{X_{2}}{n}) + \cdots + Var(\frac{X_{n}}{n}) \quad\text{using independence}\newline
        &= n \frac{\sigma^{2}}{n^{2}} \quad\text{using $Var(aX) = a^{2}Var(X)$}\newline
        Var(\overline{X}) &= \frac{\sigma^{2}}{n}
    \end{align}

Hence, for a population of mean $\mu$ and variance $\sigma^{2}$, the $E[$sample mean$]$ is still $\mu$ but the variance of the sample mean shrinks by a factor of $n$. Stated in a different manner, this means that the spread of the sample mean reduces as we take the mean from more and more observations. This directly translates into the fact that our confidence on the estimate of the sample mean increases with more observations.



## Sample Variance

The sample variance is defined as
\begin{align}
        S^{2} = \frac{\sum_{i=1}^{n} (X_{i} - \overline{X})^{2}}{n - 1}
    \end{align}
where $\overline{X}$ is the sample mean. Similar to the sample mean, this is also a random variable. We divide by $n-1$ so that the estimator is unbiased, as shown below by calculating the mean of the estimator
\begin{align}
        E[S^{2}] &= E[\frac{\sum_{i=1}^{n} (X_{i} - \overline{X})^{2}}{n - 1}]\newline
        &= \frac{1}{n-1} \sum_{i=1}^{n} E[(X_{i} - \overline{X})^{2}]
        = \frac{1}{n-1} \sum_{i=1}^{n} E[X_{i}^{2} - 2X_{i} \overline{X} + \overline{X}^{2}]\newline
        &= \frac{1}{n-1} \big( \sum_{i=1}^{n} E[X_{i}^{2}] - E[2\overline{X} \sum_{i=1}^{n}X_{i}] + \sum_{i=1}^{n}E[\overline{X}^{2}] \big)\newline
        &= \frac{1}{n-1} \big( \sum_{i=1}^{n} E[X_{i}^{2}] - E[2n\overline{X}^{2}] + nE[\overline{X}^{2}] \big)\newline
        \text{Using}\quad E[X^{2}] &= Var(X) + E[X]^{2},\newline
        E[S^{2}] &= \frac{1}{n-1} \big( \sum_{i=1}^{n} E[Var(X_{i}) + E[X_{i}]^{2}] - nE[\overline{X}^{2}] \big)\newline
        &= \frac{1}{n-1}(n\sigma^{2} + n\mu^{2} - n(\frac{\sigma^{2}}{n} + \mu^{2}))\newline
        E[S^{2}] &= \sigma^{2}
    \end{align}
i.e., the mean of the sample variance is same as the variance of the distribution (population variance). Further, the division by $n-1$ to calculate sample variance comes from the fact that we are already using $\overline{X}$ as an estimate for sample mean which takes away one degree of freedom.


## Distributions for a Normal Population

Consider $X_{1}, X_{2}, \ldots, X_{n}$ be independently derived from a normal population with mean $\mu$ and variance $\sigma^{2}$

i.e., $X_{i} \sim \mathcal{N}(\mu, \sigma^{2}) \forall i = 1, 2, \ldots, n$


Based on the derivations above,
\begin{align}
        E[\overline{X}] &= \mu\newline
        Var(\overline{X}) &= \frac{\sigma^{2}}{n}
    \end{align}

And since the sum of normal random variables is also normal,
\begin{align}
        \frac{\overline{X} - \mu}{\sigma/\sqrt{n}} \sim \mathcal{N}(0, 1)
    \end{align}
which is similar to the central limit theorem.


From the derivation above for the sample variance,
\begin{align}
        E[S^{2}] = \sigma^{2}
    \end{align}

Now let's calcluate the distribution of $S^{2}$
\begin{align}
        S^{2} &= \frac{\sum_{i=1}^{n} (X_{i} - \overline{X})^{2}}{n-1}\newline
        (n-1)S^{2} &= \sum_{i=1}^{n} (X_{i} - \overline{X})^{2}\newline
        &= \sum_{i=1}^{n} ((X_{i} - \mu) - (\overline{X} - \mu))^{2}\newline
        &= \sum_{i=1}^{n} ((X_{i} - \mu)^{2} + (\overline{X} - \mu)^{2} - 2(X_{i} - \mu)(\overline{X} - \mu))\newline
        &= \sum_{i=1}^{n} (X_{i} - \mu)^{2} + n(\overline{X} - \mu)^{2} - 2(\overline{X} - \mu)\sum_{i=1}^{n}(X_{i} - \mu)\newline
        &= \sum_{i=1}^{n} (X_{i} - \mu)^{2} + n(\overline{X} - \mu)^{2} - 2n(\overline{X} - \mu)^{2}\newline
        &= \sum_{i=1}^{n} (X_{i} - \mu)^{2} - n(\overline{X} - \mu)^{2}\newline
        \frac{(n-1)S^{2}}{\sigma^{2}} &= \sum_{i=1}^{n} (\frac{X_{i} - \mu}{\sigma})^{2} - (\frac{\overline{X} - \mu}{\sigma/\sqrt{n}})^{2} \quad\text{to make standard normals}\newline
        \text{or,}\quad \frac{(n-1)S^{2}}{\sigma^{2}} + (\frac{\overline{X} - \mu}{\sigma/\sqrt{n}})^{2} &= \sum_{i=1}^{n} (\frac{X_{i} - \mu}{\sigma})^{2}
    \end{align}

The right hand side is a chi-square variable with $n$ degrees of freedom and the second part of the left hand side is a chi-square variable with $1$ degree of freedom. We know that sum of independent chi-square variables is also a chi-square variable with degrees of freedom equal to the sum of individual degrees of freedom. Hence, it follows that
\begin{align}
        \frac{(n-1)S^{2}}{\sigma^{2}} \sim \chi_{n-1}^{2}
    \end{align}
and also the fact that **for a normal population, the sample mean and sample variance are independent variables with normal and chi-square distributions respectively**. This independence is a unique property for a normal distribution and is useful in parameter estimation and hypothesis testing.


Another interesting observation from the above derivations is
\begin{align}
        \sqrt{n}\frac{\overline{X} - \mu}{S} &\sim t_{n-1}\newline
        \text{whereas}\quad \sqrt{n}\frac{\overline{X} - \mu}{\sigma} &\sim \mathcal{N}(0,1)
    \end{align}
Note that the denominator is in the first equation is sample variance. The derivation is
\begin{align}
        \frac{Z}{\sqrt{\chi_{n}^{2}/n}} &\sim t_{n} \quad\text{definition}\newline
        \text{or,}\quad \frac{\frac{\overline{X} - \mu}{\sigma / \sqrt{n}}}{\sqrt{\frac{(n-1)S^{2}}{\sigma^{2}} \frac{1}{n-1}}} &\sim t_{n-1}\newline
        \text{or,}\quad \sqrt{n}\frac{\overline{X} - \mu}{S} &\sim t_{n-1}
    \end{align}


# Parameter Estimation

In probability theory, we usually have the distribution known to us and we try to use this information to obtain theoretical results applicable on population of this distribution. However, in statistics, we are given the samples drawn from the population, and we are interested in estimating the parameters of this population. For instance, it can be known that the samples are drawn from a normal distribution and the objective is to use the samples to obtain the mean and variance of the normal distribution. It is possible to partially know the parameters in some cases, for example mean is unknown but the variance is known. Following are some methods to obtain the *estimates* of these parameters.


## Maximum Likelihood Estimator

Maximum Likelihood Estimator or MLE is based on the idea to **find that value of $\theta$ that maximizes the probability of observing the given set of samples of the population**. Alternately, let $x_{i}$ for $i=1,2,\ldots,n$ be $n$ samples drawn from a population whose distribution is parametrized by $\theta$ (can be a vector as well). Then we define the likelihood function as
\begin{align}
        \text{likelihood}\quad = f(x_{1}, x_{2}, \ldots, x_{n}|\theta)
    \end{align}
i.e., the joint probability (or density) of occurrence of all the samples under the given distribution for some value of $\theta$. We aim to maximize this likelihood to get the estimate of $\theta$. It is often the case that taking logarithm of both sides allows for an easy way of estimation. Note that both likelihood an log likelihood are maximized by the same value of estimator.


### MLE for Bernoulli Variable

Suppose we observe $n$ independent samples from a Bernoulli process and the aim is to find the MLE for the probability of success.

Let $p$ denote the probability of success. Then,
\begin{align}
        P(X_{i} = x) &= p^{x}(1-p)^{1-x} \quad\text{where $x$ is $0$ or $1$}\newline
        \text{or,}\quad P(X_{i} = x_{i}) &= p^{x_{i}}(1-p)^{1-x_{i}}
    \end{align}
Since all the samples are independent, the joint probability or likelihood is simply the product of all the probabilities
\begin{align}
        f(x_{1}, x_{2}, \ldots, x_{n}|p) &= p^{x_{1}}(1-p)^{1-x_{1}} \ldots p^{x_{n}}(1-p)^{1-x_{n}}\newline
        &= p^{\sum_{i=1}^{x_{i}}} (1-p)^{n-\sum_{i=1}^{x_{i}}}\newline
        log(f(x_{1}, x_{2}, \ldots, x_{n}|p)) &= {\sum_{i=1}^{x_{i}}}log(p) + (n-{\sum_{i=1}^{x_{i}}})log(1-p)
    \end{align}
Taking the derivative with respect to $p$ to maximize,
\begin{align}
        \frac{d}{dp}log(f(x_{1}, x_{2}, \ldots, x_{n}|p)) &= {\sum_{i=1}^{x_{i}}}\frac{1}{p} - (n-{\sum_{i=1}^{x_{i}}})\frac{1}{1-p} = 0\newline
        \text{or,}\quad \hat{p} &= \frac{\sum_{i=1}^{n}x_{i}}{n}
    \end{align}
which is the proportion of successful trials in the sample.

### MLE for Poisson Variable

Suppose that we observe $n$ random samples obtained from a poisson process. Recall
\begin{align}
        P(X = k) = \frac{e^{-\lambda} \lambda^{k}}{k!}
    \end{align}
Hence, the joint distribution can be written as
\begin{align}
        f(x_{1}, x_{2}, \ldots, x_{n}|p) &= \prod_{i=1}^{n} \frac{e^{-\lambda} \lambda^{x_{i}}}{x_{i}!}\newline
        f(x_{1}, x_{2}, \ldots, x_{n}|p) &= \frac{e^{-n\lambda} \lambda^{\sum_{i=1}^{n} x_{i}}}{\prod_{i=1}^{n} x_{i}!}\newline
        log(f(x_{1}, x_{2}, \ldots, x_{n}|p)) &= -n\lambda + (\sum_{i=1}^{n} x_{i})log(\lambda) - \sum_{i=1}^{n} log(x_{i}!)\newline
        \frac{d}{dp}(f(x_{1}, x_{2}, \ldots, x_{n}|p)) &= -n + (\sum_{i=1}^{n} x_{i})\frac{1}{\lambda}\newline
        &= 0\newline
        \text{or,}\quad \hat{\lambda} &= \frac{\sum_{i=1}^{n} x_{i}}{n}
    \end{align}
i.e., the average rate is simply the average of all the observed arrivals.

### MLE for Normal Variable

Suppose we observe $n$ samples from a normal population whose mean is $\mu$ and variance is $\sigma^{2}$. We will aim to obtain MLE estimates for both the mean and variance. Recall
\begin{align}
         P(X = x) = \frac{1}{\sqrt{2 \pi \sigma^{2}}} exp(-\frac{(x-\mu)^{2}}{2\sigma^{2}})
    \end{align}

Hence, the likelihood will be
\begin{align}
        f(x_{1}, x_{2}, \ldots, x_{n}|\mu, \sigma^{2}) &= \prod_{i=1}^{n} \frac{1}{\sqrt{2 \pi \sigma^{2}}} exp(-\frac{(x-\mu)^{2}}{2\sigma^{2}})\newline
        log(f(x_{1}, x_{2}, \ldots, x_{n}|\mu, \sigma^{2})) &= -\frac{n}{2}\log(2\pi) - n\log(\sigma) - \frac{1}{2\sigma^{2}}(\sum_{i=1}^{n} (x_{i} - \mu)^{2})\newline
        \frac{d}{d\mu}(log(f(x_{1}, x_{2}, \ldots, x_{n}|\mu, \sigma^{2}))) &= -\frac{1}{\sigma^{2}}(\sum_{i=1}^{n} (x_{i} - \mu))\newline
        &= 0\newline
        \text{or,}\quad \hat{\mu} &= \frac{\sum_{i=1}^{n} x_{i}}{n}\newline
        \frac{d}{d\sigma}(log(f(x_{1}, x_{2}, \ldots, x_{n}|\mu, \sigma^{2}))) &= - \frac{n}{\sigma} - \frac{1}{2\sigma^{2}}(\sum_{i=1}^{n} (x_{i} - \mu)^{2})\newline
        &= 0\newline
        \text{or,}\quad \hat{\sigma}^{2} &= \frac{\sum_{i=1}^{n}(x_{i} - \mu)^2}{n}\newline
        &= \frac{\sum_{i=1}^{n}(x_{i} - \overline{x})^2}{n}\newline
        \text{where}\quad \overline{x} &= \frac{\sum_{i=1}^{n} x_{i}}{n}
    \end{align}
Note that the estimator for variance is different from the sample variance
\begin{align}
        \text{MLE}\quad \sigma^{2} &= \frac{\sum_{i=1}^{n}(x_{i} - \overline{x})^2}{n}\newline
        S^{2} &= \frac{\sum_{i=1}^{n}(x_{i} - \overline{x})^2}{n - 1}
    \end{align}

### MLE for Uniform Random Variable

Consider oberving $n$ samples from a uniform distribution with the parameter $\theta$. Then,
\begin{align}
        f(x_{1}, x_{2}, \ldots, x_{n}|\theta) = \frac{1}{\theta^{n}}
    \end{align}
which is clearly maximized when $\theta$ is minimum. But since $\theta$ has to be at least as large as the maximum observed value,
\begin{align}
        \hat{\theta} = max(x_{1}, x_{2}, \ldots, x_{n})
    \end{align}


## Method of Moments Estimate

For this method, we calculate expected value of powers of the random variable to get $d$ equations for estimating $d$ parameters (if the solutions exist). For instance, consider $f_{X}(x) = f(x \lvert \theta, \sigma)$. We can estimate the values of the parameters by solving the two equations
\begin{align}
        E[X] &= \frac{\sum_{i=1}^{n} X_{i}}{n} = \int xf(x \lvert \theta, \sigma) dx\newline
        E[X^{2}] &= \frac{\sum_{i=1}^{n} X_{i}^{2}}{n} = \int x^{2}f(x \lvert \theta, \sigma) dx
    \end{align}
with the solutions to these equations denoted as $\theta_{MME}$ and $\sigma_{MME}$. Depending on the distribution, calculation of expected values can be done using moment generating functions. The above estimation is valid when we have a large number of samples, since by the law of large numbers, the sample mean will converge to the true mean.


## Interval Estimates

The MLE estimates calculated above are estimates and do not reflect the true value. We expect the true value of the parameter to be close to the estimate, but not exactly equal to it. Hence, it makes sense to give an interval instead of a single estimate to reflect our confidence in the estimated value of the parameter.


Note that the below confidence intervals imply that $\alpha$ percent of times, the constructed interval will contain the true mean $\mu$, when the same calculation is repeated with multiple samples. The calculations of intervals do not imply that $\mu$ is contained in the interval with $\alpha$ confidence. We calculate an interval that falls on $\mu$ rather than telling the interval that $\mu$ falls in.


### Confidence interval for Mean of Normal Distribution when Variance is Known

Consider the problem of estimation of the mean of a normal distribution with known variance $\sigma^{2}$. Since we know that the MLE for mean is just the sample mean, and the sample mean follows a normal distribution,
\begin{align}
        P(-1.96 < \frac{\overline{X} - \mu}{\sigma / \sqrt{n}} < 1.96) &= 0.95 \quad\text{using standard normal tables}\newline
        \text{or,}\quad P(overline{X} - 1.96\frac{\sigma}{\sqrt{n}}< \mu < \overline{X} + 1.96\frac{\sigma}{\sqrt{n}}) &= 0.95
    \end{align}
Thus, we are 95% confident that the true value of the mean lies in the range
\begin{align}
        (\overline{X} - 1.96\frac{\sigma}{\sqrt{n}}, \overline{X} + 1.96\frac{\sigma}{\sqrt{n}})
    \end{align}

This trick to calculate the confidence interval can be generalized for any value of confidence. Recall that
\begin{align}
        P(Z > z_{\alpha}) = \alpha\newline
        P(Z < -z_{\alpha}) = \alpha
    \end{align}

Hence, for a given confidence level $\alpha$, the two sided confidence interval is
\begin{align}
        P(-z_{\alpha /2} < Z < z_{\alpha /2}) &= 1 - \alpha\newline
        P(-z_{\alpha /2} < \sqrt{n}\frac{\overline{X} - \mu}{\sigma} < z_{\alpha /2}) &= 1 - \alpha\newline
        P(\overline{x}-z_{\alpha /2}\frac{\sigma}{\sqrt{n}} < \mu < \overline{x}-z_{\alpha /2}\frac{\sigma}{\sqrt{n}}) &= 1 - \alpha\newline
        \text{two sided $1 - \alpha$ confidence interval} &= (\overline{x}-z_{\alpha /2}\frac{\sigma}{\sqrt{n}}, \overline{x}+z_{\alpha /2}\frac{\sigma}{\sqrt{n}})\newline
    \end{align}
where $\overline{x}$ is the observed value of $\overline{X}$.

{% include image.html url="notes/probability/images/conf_1.png" description="Visualization of the double sided confidence interval on standard normal." img_classes="notes-img" %}

In a very similar manner, we can calculate the one sided confidence interval. Here, we are only interested in the lower or upper bound of the said interval. The other side is $\infty$ or $-\infty$.
\begin{align}
        P(Z > z_{\alpha}) &= \alpha\newline
        P(\sqrt{n}\frac{\overline{X} - \mu}{\sigma} > z_{\alpha}) &= \alpha\newline
        P(\mu < \overline{x} + z_{\alpha}\frac{\sigma}{\sqrt{n}}) &= \alpha\newline
        \text{Lower $1-\alpha$ confidence interval} &= (-\infty, \overline{x} + z_{\alpha}\frac{\sigma}{\sqrt{n}})\newline
        \newline
        P(Z < -z_{\alpha}) &= \alpha\newline
        P(\sqrt{n}\frac{\overline{X} - \mu}{\sigma} < -z_{\alpha}) &= \alpha\newline
        P(\overline{x} - z_{\alpha}\frac{\sigma}{\sqrt{n}} < \mu) &= \alpha\newline
        \text{Upper $1-\alpha$ confidence interval} &= (\overline{x} - z_{\alpha}\frac{\sigma}{\sqrt{n}}, \infty)
    \end{align}

The interpretation of the right sided confidence interval is that we are $1-\alpha$ confident that the value of the mean is more than the lower end of the interval. In a similar way, the left side interval gives the upper bound on the value of mean with the desired confidence.

### Confidence interval for Mean of Normal Distribution when Variance is Unknown

The derivation of confidence intervals in this case is similar to the above, with the only difference of using a t-distribution. Recall
\begin{align}
        \sqrt{n} \frac{\overline{X} - \mu}{S} \sim t_{n-1}
    \end{align}
where $S$ is the sample variance. Following similar derivation to the known variance case,
\begin{align}
        \text{two sided $1 - \alpha$ confidence interval} &= (\overline{x}-t_{\alpha /2, n-1}\frac{s}{\sqrt{n}}, \overline{x}+t_{\alpha /2, n-1}\frac{s}{\sqrt{n}})\newline
        \text{Lower $1-\alpha$ confidence interval} &= (-\infty, \overline{x} + t_{\alpha, n-1}\frac{s}{\sqrt{n}})\newline
        \text{Upper $1-\alpha$ confidence interval} &= (\overline{x} - t_{\alpha, n-1}\frac{s}{\sqrt{n}}, \infty)
    \end{align}
where $s$ is the observed value of the sample variance $S$. However, notice that the intervals calculated will usually be larger than those when the variance is known because t-distribution is heavier tailed than a standard normal and thus has higher variance.

{% include image.html url="notes/probability/images/conf_2.png" description="Visualization of the double sided confidence interval on t-distribution." img_classes="notes-img" %}

### Confidence interval for Variance of Normal Distribution when Mean is Unknown

Recall that
\begin{align}
        (n-1)\frac{S^{2}}{\sigma^{2}} \sim \chi_{n-1}^{2}
    \end{align}
By noting that $\sigma^{2}$ is always positive, we have the following
\begin{align}
        \text{two sided $1 - \alpha$ confidence interval} &= (\frac{(n-1)s^{2}}{\chi_{\alpha/2, n-1}^{2}}, \frac{(n-1)s^{2}}{\chi_{1 - \alpha/2, n-1}^{2}})\newline
        \text{Lower $1-\alpha$ confidence interval} &= (0, \frac{(n-1)s^{2}}{\chi_{1 - \alpha, n-1}^{2}})\newline
        \text{Upper $1-\alpha$ confidence interval} &= (\frac{(n-1)s^{2}}{\chi_{\alpha, n-1}^{2}}, \infty)
    \end{align}

### Estimating Difference in Means of Two Normal Populations

Suppose the following two independent sets of random variables
\begin{align}
        X_{1}, X_{2}, \ldots, X_{n} &\sim \mathcal{N}(\mu_{1}, \sigma_{1}^{2})\newline
        Y_{1}, Y_{2}, \ldots, Y_{m} &\sim \mathcal{N}(\mu_{1}, \sigma_{1}^{2})
    \end{align}

Then, we are interseted in the distribution of $\mu_{1} - \mu_{2}$. It is intuitive to see that the MLE estimator of this quantity is nothing but $\overline{X} - \overline{Y}$. Also, since $\overline{X}$ and $\overline{Y}$ are both normally distributed,
\begin{align}
        \overline{X} - \overline{Y} \sim \mathcal{N}(\mu_{1} - \mu_{2}, \frac{\sigma_{1}^{2}}{n} + \frac{\sigma_{2}^{2}}{m})
    \end{align}

Consequently, using the confidence intervals derived for the case of a mean of a single normal distribution, we have the following intervals when the standard deviations are known
\begin{align}
        \text{two sided $1 - \alpha$ confidence interval} &= (\overline{x} - \overline{y}-z_{\alpha /2}\sqrt{\frac{\sigma_{1}^{2}}{n} + \frac{\sigma_{2}^{2}}{m}}, \overline{x} - \overline{y}+z_{\alpha /2}\sqrt{\frac{\sigma_{1}^{2}}{n} + \frac{\sigma_{2}^{2}}{m}})\newline
        \text{Lower $1-\alpha$ confidence interval} &= (-\infty, \overline{x} - \overline{y}+z_{\alpha /2}\sqrt{\frac{\sigma_{1}^{2}}{n} + \frac{\sigma_{2}^{2}}{m}})\newline
        \text{Upper $1-\alpha$ confidence interval} &= (\overline{x} - \overline{y}-z_{\alpha /2}\sqrt{\frac{\sigma_{1}^{2}}{n} + \frac{\sigma_{2}^{2}}{m}}, \infty)
    \end{align}
where $\overline{x}$ and $\overline{y}$ are estimates of $\overline{X}$ and $\overline{Y}$ respectively.

A more challenging scenario arises when the variances are not known. In that case, it is only logical to try to estimate the intervals using sample variances (themselves random variables)
\begin{align}
        S_{1}^{2} &= \frac{\sum_{i=1}^{n} (X_{i} - \overline{X})^{2}}{n-1}\newline
        S_{2}^{2} &= \frac{\sum_{i=1}^{m} (Y_{i} - \overline{Y})^{2}}{m-1}
    \end{align}

However, the distribution useful for deriving the confidence intervals
\begin{align}
        \frac{\overline{X} - \overline{Y} - (\mu_{1} - \mu_{2})}{\sqrt{\frac{S_{1}^{2}}{n} + \frac{S_{2}^{2}}{m}}}
    \end{align}
is complicated and depends on the unknown variances. The variable is friendly if we assume that the two unknown variances are both same.


Assuming $\sigma_{1} = \sigma_{2} = \sigma$, it follows
\begin{align}
        (n-1)\frac{S_{1}^{2}}{\sigma^{2}} &\sim \chi_{n-1}^{2}\newline
        (m-1)\frac{S_{2}^{2}}{\sigma^{2}} &\sim \chi_{m-1}^{2}\newline
        (n-1)\frac{S_{1}^{2}}{\sigma^{2}} + (m-1)\frac{S_{2}^{2}}{\sigma^{2}} &\sim \chi_{n+m-2}^{2}\newline
    \end{align}
since $S_{1}^{2}$ and $S_{2}^{2}$ are independent chi-square random variables and from [section]({{ "/notes/probability/chapters/distributions/chi_square.html" | relative_url}}) that the sum of such variables is also chi-square.

We already know
\begin{align}
        \frac{\overline{X} - \overline{Y} - (\mu_{1} - \mu_{2})}{\sqrt{\frac{\sigma^{2}}{n} + \frac{\sigma^{2}}{m}}} \sim \mathcal{N}(0, 1)
    \end{align}
and we also know that the ratio of a standard normal and the square root of a chi-square divided by it's degrees of freedom is a t-distribution
\begin{align}
        \frac{\overline{X} - \overline{Y} - (\mu_{1} - \mu_{2})}{\sqrt{\frac{\sigma^{2}}{n} + \frac{\sigma^{2}}{m}}} \div \sqrt{\frac{(n-1)\frac{S_{1}^{2}}{\sigma^{2}} + (m-1)\frac{S_{2}^{2}}{\sigma^{2}}}{n+m-2}} &\sim t_{n+m-2}
    \end{align}
Let
\begin{align}
        S_{p}^{2} &= \frac{(n-1)S_{1}^{2} + (m-1)S_{2}^{2}}{n + m - 2}
    \end{align}
Then,
\begin{align}
        P(-t_{\alpha/2, n+m-2} \leq \frac{\overline{X} - \overline{Y} - (\mu_{1} - \mu_{2})}{S_{p}\sqrt{\frac{1}{n} + \frac{1}{m}}} \leq t_{\alpha/2, n+m-2}) &= 1 - \alpha
    \end{align}
\begin{align}
        \text{Two sided $1 - \alpha$ confidence interval} &= (\overline{x} - \overline{y}-t_{\alpha /2, n+m-2}s_{p}\sqrt{\frac{1}{n} + \frac{1}{m}}, \overline{x} - \overline{y}+t_{\alpha /2, n+m-2}s_{p}\sqrt{\frac{1}{n} + \frac{1}{m}})
    \end{align}
where $s_{p}$ is the sample estimate for $S_{p}$. Lower confidence interval is derived in a similar fashion to the previous derivations, but the upper confidence interval is the lower confidence interval of $\mu_{2} - \mu_{1}$.

### Confidence Interval for Mean of Bernoulli Random Variable

Suppose we obtain a sample of $n$ independent Bernoulli random variables, where the probability of success is $p$. Let $X$ denote the no of successes. Using the CLT for large $n$,
\begin{align}
        \frac{X - np}{\sqrt{np(1-p)}} \sim \mathcal{N}(0, 1)
    \end{align}
It is not tractable to calculate the confidence intervals from this formulation. Let $\hat{p} = X/n$ denote the MLE of the mean $p$. Substituiting in the denominator of above,
\begin{align}
        P(-z_{\alpha/2} \leq \frac{X - np}{\sqrt{n\hat{p}(1-\hat{p})}} \leq z_{\alpha/2}) &\approx 1-\alpha\newline
        \text{Two sided $1-\alpha$ confidence interval} &\approx (\hat{p} - z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}, \hat{p} + z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}})
    \end{align}
and one sided confidence intervals can be obtained in similar manner to previous derivations.


## Evaluating an Estimator

Let $\boldsymbol{X} = (X_{1}, X_{2}, \ldots, X_{n})$ be the set of random variables sampled from a population whose parameters are defined by $\theta$. Let $d(\boldsymbol{X})$ denote an estimator of $\theta$. Then
\begin{align}
        r(d, \theta) = E[(d(\boldsymbol{X}) - \theta)^{2}]
    \end{align}
denotes the mean squared estimator of $\boldsymbol{X}$. Although it is rare to find an estimator that minimizes this error, we can certainly find the minima under the set of estimators satisfying a certain criteria.

The bias of an estimator is defined as
\begin{align}
        b_{\theta}(d) = E[d(\boldsymbol{X})] - \theta
    \end{align}
If the bias is zero, then the estimator is called an **unbiased estimator**. That is, the expected value of the estimator is same as the parameter being estimated.


For an unbiased estimator, the mean square error is
\begin{align}
        r(d, \theta) &= E[(d(\boldsymbol{X}) - \theta)^{2}]\newline
        &= E[(d(\boldsymbol{X}) - E[d(\boldsymbol{X})])^{2}]\newline
        &= Var(d(\boldsymbol{X}))
    \end{align}
i.e., the mean squared error of an unbiased estimator is equal to its variance.


Let $X_{1}, X_{2}, \ldots, X_{n}$ be sampled from a distribution whose mean is $\theta$. Then,
\begin{align}
        d(\boldsymbol{X}) &= \sum_{i=1}^{n} \lambda_{i} X_{i}\newline
        \text{and}\quad \sum_{i=1}^{n}\lambda_{i} &= 1
    \end{align}
is also an unbiased estimator because
\begin{align}
        E[\sum_{i=1}^{n} \lambda_{i} X_{i}] &= \sum_{i=1}^{n} \lambda_{i} E[X_{i}]\newline
        &= \theta \sum_{i=1}^{n}\lambda_{i}\newline
        &= \theta
    \end{align}

### Combining Unbiased Estimators

Suppose we have $n$ unbiased estimators $d_{1}, \ldots, d_{n}$ for a parameter $\theta$ with different independent variances
\begin{align}
        E[d_{i}] = \theta \quad Var(d_{i}) = \sigma_{i}^{2}
    \end{align}
Then, a weighted combination of these estimators is also an unbiased estimator of $\theta$ (assuming that the weights sum up to 1). Suppose we wish to find a set of weights that minimize the mean squared error to get the best estimator, then
\begin{align}
        d &= \sum_{i=1}^{n} w_{i} d_{i} \quad\text{where $\sum_{i=1}^{n} w_{i} = 1$}\newline
        r(d, \theta) &= Var(d) \quad\text{(derived above)}\newline
        &= Var(\sum_{i=1}^{n} w_{i} d_{i})
        = \sum_{i=1}^{n} w_{i}^{2} Var(d_{i}) \quad\text{by independence}\newline
        &= \sum_{i=1}^{n} w_{i}^{2} \sigma_{i}^{2}
    \end{align}
\begin{align}
        \text{So we minimize}\quad \sum_{i=1}^{n} w_{i}^{2} \sigma_{i}^{2} - \lambda(\sum_{i=1}^{n} w_{i}-1) \quad \text{ssing $\lambda$ as Lagrange multiplier}\newline
        \text{Taking the derivative for any $i$,}\quad 0 = 2\sigma_{i}^{2} w_{i} - \lambda \newline
        \text{Using}\quad \sum_{i=1}^{n} w_{i} = 1, \quad
        w_{i} = \frac{1/\sigma_{i}^{2}}{1/\sigma_{1}^{2} + 1/\sigma_{2}^{2} + \cdots + 1/\sigma_{n}^{2}}
    \end{align}
or, the weights for the estimators are inversely proportional to their individual variances. This is useful in situations when we have $n$ independent results for evaluation of a parameter, and we want to increase our confidence in the estimator by combining all these independent results.


### Relation between Bias and Variance

The result obtained above that the mean squared error of an unbiased estimator is it's variance can be generalized for the case of any estimator as follows
\begin{align}
        r(d, \theta) &= E[(d - \theta)^{2}]\newline
        &= E[(d - E[d] + E[d] -\theta)^{2}]\newline
        &= E[(d - E[d])^{2} + (E[d] - \theta)^{2} + 2(d - E[d])(E[d] - \theta)]\newline
        &= E[(d - E[d])^{2}] + E[(E[d] - \theta)^{2}] + 2(E[d] - \theta)E[d - E[d]]\newline
        &= E[(d - E[d])^{2}] + (E[d] - \theta)^{2}\newline
        r(d, \theta) &= Var(d) + b_{\theta}^{2}(d)\newline
    \end{align}
where we have noted that $E[d - E[d]] = E[d] - E[d] = 0$ and $E[d] - \theta$ is a constant since $E[d]$ itself is a constant.

### Minimum Variance Unbiased Estimator (MVUE)

For an unbiased estimator, the MSE derived above is only dependent on the variance of the estimator. Hence, the MVUE is the one for which the variance is the minimum.

#### Cramer Rao Lower Bound (CRLB) & Related Theorems

The CRLB sets a lower bound on the variance of any unbiased estimator. If this lower bound is known,

-   If the variance of an unbiased estimator equals this lower bound, we know that we have found the MVUE

-   The lower bound provides a benchmark against which to compare different estimators

-   The bound can be used to rule out impossible estimators

##### Fisher Information

To calculate the CRLB, we first define Fisher Information (FI). For any distribution with the density function $f_{X}(x \vert \theta)$ and a random variable $X$, the FI measures a kind of variance of $X$ with respect to $\theta$. If the density function has peaks, knowing $X$ can provide a lot of information about $\theta$. On the other hand, a flat distribution will require many samples of $X$ to find out a good estimate of $\theta$. Mathemtically, for a single random variable $X$, FI is defined as
\begin{align}
        \mathcal{I}(\theta) = E \bigg[ \bigg(\frac{\partial}{\partial \theta} \ln f_{X}(X; \theta)\bigg)^{2} \bigg \vert \theta \bigg]
    \end{align}
and if the density is twice differentiable,
\begin{align}
        \mathcal{I}(\theta) = -E \bigg[ \frac{\partial^{2}}{\partial \theta^{2}} \ln f_{X}(X; \theta) \bigg \vert \theta \bigg]
    \end{align}

Fisher information is additive. The total Fisher information for a set of $n$ independent random variables from the same distribution will simply be $n\mathcal{I}(\theta)$ where $\mathcal{I}(\theta)$ has been derived above.

##### Sufficient Statistic

Another important definition is a sufficient statistic. Any statistic of the population $t = T(X)$ (for instance, sample mean is a population statistic, and so is sample variance) is called a sufficient statistic for the parameter $\theta$ if the conditional probability distribution of the data (or sample) $X$ given $t$ does not depend on parameter $\theta$. That is, once $t$ is known, the data will provide no additional information about $\theta$.
\begin{align}
        t = T(X) \quad \text{is sufficient statistic if} \quad P(X \vert t) \perp \theta
    \end{align}

##### Fisher Neyman Factorization Theorem

The theorem states that a given statistic $T(X)$ is sufficient if and only if
\begin{align}
        f_{X}(x;\theta) = h(X)g(T(X), \theta)
    \end{align}
where $h$ depends on the data while $g$ depends on $\theta$ and on the data $X$ only through $T(X)$.

Then, for an unbiased estimator $\hat{\theta}$ and Fisher information $\mathcal{I}(\theta)$ for a single observation, the CRLB is
\begin{align}
        Var(\hat{\theta}) \geq \frac{1}{n\mathcal{I}(\theta)}
    \end{align}

The above is a universal bound for unbiased estimators. The lower bound is slightly differently for biased estimators. Let $b(\theta)$ denote the bias for estimator $T(X)$, then
\begin{align}
        Var(T(X)) \geq \frac{(1 + b'(\theta))^{2}}{n\mathcal{I}(\theta)}
    \end{align}

##### Complete Statistic

A statistic $T$ is called complete if $E_{\theta}[g(T)] = 0$ for all $\theta$ and some function $g$ implies that $P(g(T) = 0) = 1$ for all $\theta$.

##### Lehmann--Scheffe Theorem

The theorem states that any unbiased estimator of an unknown quantity that depends on the data only through a complete sufficient statistic is the unique best unbiased estimator of that quantity.

##### Rao-Blackwell Theorem

If $g(X)$ is any kind of estimator of an unknown $\theta$, the the conditional expectation of $g(X)$ given $T(X)$ (a sufficient statistic) is typically a better estimate of $\theta$ and never worse. Often, one can start off with a crude estimator $g(X)$ and compute the expected value to get an estimator that is optimal in various senses.


## Bayes Estimator

The Bayes estimator is the expected value of the parameter given the data. It utilizes the Bayes theorem in order to arrive at the estimator value
\begin{align}
        E[\theta|X_{1} = x_{1}, X_{2} = x_{2}, \ldots, X_{n} = x_{n}] &= \int \theta f(\theta|x_{1}, x_{2}, \ldots, x_{n})\newline
        f(\theta|x_{1}, x_{2}, \ldots, x_{n}) &= \frac{p(\theta) f(x_{1}, x_{2}, \ldots, x_{n} | \theta)}{\int p(\theta) f(x_{1}, x_{2}, \ldots, x_{n} | \theta) d\theta}
    \end{align}
where $p(\theta)$ is the assumed prior distribution on the parameter $\theta$. Based on our knowledge of the process, this can be uniform, normal etc.


# Bayesian Inference

We have a signal $S$ that goes through a \"model\" $a$ through which we observe $X$ (with sum added noise $N$). The aim of Bayesian Inference is to try to infer $S$ given the observed $X$.


Hypothesis testing is done on an unknown that takes some possible values, and the aim is to arrive at a value that gives a small probability of incorrect decision (e.g. - Radar)


Estimation is aimed at finding the value of a quantity with a small estimation error (e.g. poll estimation)


Bayes Rule
\begin{align}
        p_{\Theta|X}(\theta|x) &= \frac{p_{\Theta}(\theta)p_{X|\Theta}(x|\theta)}{p_{X}(x)} \quad\text{$\theta$ and $X$ are both discrete}\newline
        \text{or,}\quad Posterior &= \frac{Prior * Model}{Data}\newline
        p_{\Theta|X}(\theta|x) &= \frac{p_{\Theta}(\theta)f_{X|\Theta}(x|\theta)}{f_{X}(x)} \quad\text{$\theta$ is discrete and $X$ is continuous}\newline
    \end{align}
Note that Bayesian inference will give us a distribution over the possible values, but it is often desirable to get an estimate.

## Maximum a Posteriori (MAP)

MAP is a point estimate of the unknown quantity and is defined as follows
\begin{align}
        p_{\Theta|X}(\theta|x) = \max_{\theta}p_{\Theta|X}(\theta|x) \quad\text{$\theta$ with maximum posterior probability}\newline
    \end{align}
In continuous case, expected value can be a better estimate

## Maximum Likelihood Estimation

This is another method to give estimates from the Bayesian Inference. We assume the random variable of interest to be generated through a model with some parameters, i.e. $X \sim p_{X}(x;\theta)$ and we pick the $\theta$ that makes the data most likely
\begin{align}
        \hat{\theta}\_{MLE} &= \argmax_{\theta} p_{X|\Theta}(x|\theta)\newline
        \hat{\theta}\_{MAP} &= \argmax_{\theta} p_{\Theta|X}(\theta|x)\newline
        &= \argmax_{\theta} p_{X|\Theta}(x|\theta)p_{\Theta}(\theta)
    \end{align}

Thus, we can see that if we assume a uniform prior on $\theta$, MAP and MLE estimates are the same. MLE estimates tha maximum through cosideration of multiple probabilistic models. We can get different estimates for different priors.

## Least Mean Square Estimate

Here, we aim to find an estimate such that
\begin{align}
        \theta^{\*} &= \min_{c} E[(\Theta - c)^{2}]\newline
        E[(\Theta - c)^{2}] &= E[\Theta^{2}] - 2cE[\Theta] + c^{2}\newline
        \text{Taking derivative,}\quad \frac{dE}{dc} &= 0\newline
        c &= E[\Theta]\newline
        \text{In general,}\quad c &= E[\Theta|X] \quad\text{minimizes $E[(\Theta - g(X))^{2}]$ over all estimators $g(X)$ }
    \end{align}
$E[\Theta]$ minimizes the least squares estimate


When $X$ is observed, the best estimate simply becomes $E[\Theta \vert X]$.


# Hypothesis Testing

Hypothesis testing is a set of procedures used to test a hypothesis about statistical parameters. Based on the results of the procedure, we decide whether to accept or reject the hypothesis. This can be as simple as deciding whether the mean of a population is more than 1 or not.


Whenever a hypothesis is accepted, it does not mean that the hypothesis is true, but rather that the data is consistent with it.


Suppose we have a population that is characterized by the distribution $F_{\theta}$ and we are interested in making statistical comments about the value of the parameters $\theta$. **The hypothesis that specifies the statement that we are going to test about the parameter is called the null hypothesis** and is denoted by $H_{0}$. Note that the statement of the null hypothesis can either comment on the exact value of the parameter, or comment on an inequality satisfied by the parameter. When the hypothesis completely specifies the distribution, it is called a *simple hypothesis* and in the other case, it is called *composite hypothesis*.


To test the hypothesis, suppose we have available with us $n$ independent samples from the population. Based on these samples, we must define a $n$ dimensional region $C$ such that if the sample falls in this region, we reject the null hypothesis and vice versa. This region $C$ is called the critical region (or the rejection region).
\begin{align}
        \text{Reject}\quad H_{0} \quad\text{if}\quad (X_{1}, X_{2}, \ldots, X_{n}) \in C\newline
        \text{Acecpt}\quad H_{0} \quad\text{if}\quad (X_{1}, X_{2}, \ldots, X_{n}) \notin C
    \end{align}

Two types of errors can result when checking a hypothesis

-   *type* $I$ *error*: Reject $H_{0}$ when it is correct

-   *type* $II$ *error*: Accept $H_{0}$ when it is incorrect

Since hypothesis testing is about checking if the given data is consistent with the hypothesis, the error we make on rejecting the hypothesis when it is correct should be low. This is consistent with the confidence intervals discussed earlier. We denote *type I error* by $\alpha$ meaning that there is only $\alpha$ chance that the hypothesis will be incorrectly rejected by the test, and is called the level of significance of the test.


**A lower significance level or lower $\alpha$ implies that we require stronger evidence against the null hypothesis to reject it.**

A classical approach while testing the parameters of a population will be to first determine a point estimator of the parameter and then determine the distribution of the said estimator. Hypothesis test will usually involve checking whether the estimator lies in a selcted region, for which we can determine the relevant confidence intervals through the distribution of the estimator.


The maximum probability of type $I$ error is also called the **size of the test**. For a simple hypothesis test
\begin{align}
        \alpha &= P(\text{Reject}\; H_{0}\; \text{when it is correct})\newline
        &= P((X_{1}, X_{2}, \ldots, X_{n}) \in C \vert H_{0})\newline
        &= \text{size of the test}
    \end{align}
For a composite hypothesis test
\begin{align}
        \alpha = sup_{h \in H_{0}} P(\text{Reject}\; H_{0} \vert h)
    \end{align}
or, the size of the test is the worst case scenario probability of a type $I$ error (we intend to minimize the type $I$ error).

Finally, the power of a test and any related measure will be defined based on the set of observables $(X_{1}, X_{2}, \ldots, X_{n})$ since the hypothesis tests depend on determining the critical region $C$ for these set of observables.



## Test around Mean of Normal Population

### Known Variance

Consider $n$ samples $X_{1}, X_{2}, \ldots, X_{n}$ drawn from a normal distribution with unknown mean $\mu$ and known variance $\sigma^{2}$. We have the following hypothesis
\begin{align}
        \text{null hypothesis} \quad H_{0}&: \mu = \mu_{0}\newline
        \text{alternate hypothesis} \quad H_{1}&: \mu \neq \mu_{0}
    \end{align}

The sample mean $\overline{X}$ is clearly a natural choice for the estimator of the mean. It is intuitive to define the critical region in such a manner that we reject $H_{0}$ if the estimator is far off from $\mu_{0}$ and vice versa
\begin{align}
        C = \{ X_{1}, X_{2}, \ldots X_{n}: \vert\overline{X} - \mu_{0}\vert > c\}
    \end{align}
for some suitably chosen $c$. We also know that the mean of a normal population has a normal distribution. Hence for some significance level $\alpha$ (*type I error*),
\begin{align}
        P_{\mu_{0}}(\vert\overline{X} - \mu_{0}\vert > c) = \alpha
    \end{align}
where the subscript denotes the fact that the probability is being calculated under the assumption of $\mu = \mu_{0}$. Under this assumption, $\overline{X}$ is normally distributed with mean $\mu_{0}$.
\begin{align}
        P_{\mu_{0}}(\vert\frac{\overline{X} - \mu_{0}}{\sigma/\sqrt{n}}\vert > \frac{c\sqrt{n}}{\sigma}) &= \alpha\newline
        2P_{\mu_{0}}(\frac{\overline{X} - \mu_{0}}{\sigma/\sqrt{n}} > \frac{c\sqrt{n}}{\sigma}) &= \alpha
    \end{align}
but we know that these are tabulated values
\begin{align}
        P(Z > z_{\alpha/2}) &= \alpha/2\newline
        \text{or,}\quad \frac{c\sqrt{n}}{\sigma} &= z_{\alpha/2}\newline
        \text{or,}\quad c &= \frac{\sigma z_{\alpha/2}}{\sqrt{n}}
    \end{align}
or simply put in terms of the hypothesis test,
\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &\bigg\lvert \frac{\sqrt{n}}{\sigma}(\overline{X} - \mu_{0}) \big\rvert &> &z_{\alpha/2}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &\big\lvert \frac{\sqrt{n}}{\sigma}(\overline{X} - \mu_{0}) \big\rvert &\leq &z_{\alpha/2}\newline
    \end{alignat}
where $\alpha$ is the *type I error* and should ideally be low.

{% include image.html url="notes/probability/images/hypo_1.png" description="Acceptance Region for Hypothesis $\mu=\mu_{0}$" img_classes="notes-img" %}

### p-value

*p-value* denotes the probability of observing a test-statistic at least as large as the observed test-statistic under the assumption that the null hypothesis is true. Mathemtically,
\begin{align}
        P(Z > \frac{\sqrt{n}}{\sigma}(\overline{X} - \mu_{0})) = \text{p-value}
    \end{align}
where $Z$ is the random variable denoting the test-statistic while right-hand side of the inequality is the observed test-statistic. For the above formula, we have assumed the test statistic to be derived from a normal distribution. However, the definition is applicable to any distribution.


A very small *p-value* means that either the null hypothesis is incorrect, or the observed test statistic must be very unlikely. We can use *p-value* to compare against already defined significance levels to accept or reject the null hypothesis.

{% include image.html url="notes/probability/images/pvalue_1.png" description="*p-value* and significance levels on a standard normal distribution" img_classes="notes-img" %}

Furthermore, if we have a predefined value of the significance level, any *p-value* lower than this level implies it is very likely for the mean to be different, calling for rejecting $H_{0}$. This is visually represented in figure above (note that the figure compares different significance levels for a fixed value of *p-value*).


Thus, a small *p-value* denotes strong evidence in favor of observing an effect. For an analogy, consider the hypothesis test concerning the weights of a linear regression model. The usual $H_{0}$ refers to the coefficient being $0$. Thus, a small *p-value* strongly rejects the null hypothesis, meaning that the corresponding regressor has non-zero impact on the target variable.

### Power of a test and Type II error

We have not yet invoked the *type II error*. Consider $\beta(\mu)$ as probability of accepting $H_{0}$ when the mean is $\mu$
\begin{align}
        \beta(\mu) &= P_{\mu}(\text{accepting $H_{0}$ when the mean is $\mu$})\newline
        &= P(\text{statistic is}\quad \leq z_{\alpha/2})\newline
        &= P(\vert\frac{\sqrt{n}}{\sigma}(\overline{X} - \mu_{0})\vert \leq z_{\alpha/2})\newline
        &= P(-z_{\alpha/2} \leq \frac{\sqrt{n}}{\sigma}(\overline{X} - \mu_{0}) \leq z_{\alpha/2})
    \end{align}
We also define **effect size** here. It is defined as
\begin{align}
        \text{effect size} &= \text{True value} - \text{Hypothesize value}\newline
        &= \mu - \mu_{0}
    \end{align}
But, under the premise that $\mu$ is the correct mean (and $H_{0}$ is false),
\begin{align}
        \frac{\overline{X} - \mu}{\sigma/\sqrt{n}} \sim \mathcal{N}(0, 1)
    \end{align}
Thus,
\begin{align}
        \beta(\mu) &= P(-z_{\alpha/2} - \frac{\sqrt{n}}{\sigma}\mu \leq \frac{\sqrt{n}}{\sigma}(\overline{X} - \mu_{0}) - \frac{\sqrt{n}}{\sigma}\mu \leq z_{\alpha/2} - \frac{\sqrt{n}}{\sigma}\mu)\newline
        &= P(-z_{\alpha/2} - \frac{\sqrt{n}}{\sigma}(\mu + \mu_{0}) \leq \frac{\sqrt{n}}{\sigma}(\overline{X} - \mu) \leq z_{\alpha/2} - \frac{\sqrt{n}}{\sigma}(\mu + \mu_{0}))\newline
        &= \Phi(z_{\alpha/2} - \frac{\sqrt{n}}{\sigma}(\mu - \mu_{0})) - \Phi(-z_{\alpha/2} - \frac{\sqrt{n}}{\sigma}(\mu - \mu_{0}))\newline
        &= \Phi(\frac{\sqrt{n}}{\sigma}(\mu_{0} - \mu) +z_{\alpha/2}) - \Phi(\frac{\sqrt{n}}{\sigma}(\mu_{0} - \mu) -z_{\alpha/2})\newline
    \end{align}
where $\Phi$ is the standard normal cumulative distribution function.

$\beta(\mu)$ is called the Operating Charectistic. The value of this function is only dependent on the gap between $\mu_{0}$ and $\mu$. For a fix $\alpha$, as the gap grows, we move away from the centre of the standard normal. As such, the difference in the two terms of $\beta(\mu)$ keeps decreasing. It is maximum when $\mu = \mu_{0}$.

{% include image.html url="notes/probability/images/hypo_2.png" description="Curve of $\beta(\mu)$ for a fixed $\alpha$" img_classes="notes-img" %}

The function $1 - \beta(\mu)$ is called the **power function** and is the probability of rejection of $H_{0}$ when it is false. This function is useful in calculating the value of the sample size so that the probability of accepting $H_{0}: \mu = \mu_{0}$ when the true mean is $\mu_{1}$ is $\beta$. We solve the equation $\beta(\mu_{1}) = \beta$ and try to guess the value of $n$ because analytical solution is not possible.

\begin{align}
         n \approx \frac{(z_{\alpha/2} + z_{\beta})^{2} \sigma^{2}}{(\mu_{1} - \mu_{0})^{2}}
    \end{align}
is the approximate solution assuming $\alpha$ is negligible.


The power of a test is dependent on

1.  Sample size $n$: Other things being constant, the power of a test is higher the larger the sample size.

2.  Significance level $\alpha$: The smaller the value of $\alpha$, the larger is the acceptance region making it more likely to accept $H_{0} (\mu = \mu_{0})$ when the true mean is different.

3.  Effect size: The greater the effect size (difference between the hypothesized value and the true value), the higher the power of the test.

### Neyman-Pearson Lemma

Consider a test with two competing hypothesis $H_{0} = \theta_{0}$ and $H_{1} = \theta_{1}$ where the probability density (or mass) function is given by $f(\mathbf{x} \vert \theta_{i})$ for $i \in \{0, 1\}$. Denoting the critical region (rejection region) by $C$, the Neyman-Pearson Lemma states that the **Most Powerful (MP) test** statisfies the below for some $\eta \geq 0$

-   $\mathbf{x} \in C \; \text{if} \; f(\mathbf{x}\vert\theta_{1}) > \eta f(\mathbf{x}\vert\theta_{0})$

-   $\mathbf{x} \in C^{c} \; \text{if} \; f(\mathbf{x}\vert\theta_{1}) < \eta f(\mathbf{x}\vert\theta_{0})$

-   $P_{\theta_{0}}(\mathbf{X} \in C) = \alpha$ for some prefixed significance level $\alpha$

In practice, the likelihood ratio is often used to construct the tests and determine the relation between the effect size and the likelihood ratio.

### One Sided Test

In one sided test, we test the equality of the mean with a fixed value vs a single sided inequality of the mean being larger than, or smaller than that fixed value.
\begin{align}
        \text{null hypothesis}\quad H_{0}&: \mu = \mu_{0}\newline
        \text{alternate hypothesis}\quad H_{1}&: \mu > \mu_{0}
    \end{align}

Note that the variance of the distribution is known in this case. Clearly, the critical region (rejection region) is one where the large values of $\mu$ are unlikely
\begin{align}
        C = {X_{1}, \ldots, X_{n}: \overline{X} - \mu_{0} > c}
    \end{align}
for some constant $c$ chosen based on the significance level $\alpha$. Equivalently,
\begin{align}
        P(\frac{\overline{X} - \mu_{0}}{\sigma/\sqrt{n}} > z_{\alpha}) &= \alpha\newline
        \text{or,}\quad \overline{X} &> z_{\alpha}\frac{\sigma}{\sqrt{n}} + \mu_{0}
    \end{align}

is the rejection region based on the sample mean.

\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &\frac{\sqrt{n}}{\sigma}(\overline{X} - \mu_{0}) &> &z_{\alpha}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &\frac{\sqrt{n}}{\sigma}(\overline{X} - \mu_{0}) &\leq &z_{\alpha}\newline
    \end{alignat}

The *p-value* is similarly calculated as the probability that the standard normal is at least as large as this test statistic. Similar to the two sided test, operating characteristic curve can be defined
\begin{align}
        \beta(\mu) &= P(\text{Accepting}\quad H_{0})\newline
        &= P(\overline{X} \leq z_{\alpha}\frac{\sigma}{\sqrt{n}} + \mu_{0})\newline
        &= P(\frac{\overline{X} - \mu}{\sigma/\sqrt{n}} \leq z_{\alpha} + \frac{\mu_{0} - \mu}{\sigma/\sqrt{n}})\newline
        &= P(Z \leq z_{\alpha} + \frac{\mu_{0} - \mu}{\sigma/\sqrt{n}})
    \end{align}
where $Z$ is the standard normal.


##### Special Note

The tests discussed above have been derived under the assumption that the sample mean has a normal distribution. But, by central limit theorem, the sample mean of any large population will tend towards a normal distribution. Hence, the hypothesis tests will remain valid provided the population has known variance $\sigma^{2}$.

### Unknown Variance

We proceed in a manner similar to the known variance case but use sample variance instead. Recall
\begin{align}
        \sqrt{n} \frac{\overline{X} - \mu_{0}}{S} \sim T_{n-1}
    \end{align}
which is a t-distributed random variable with $n-1$ degrees of freedom. Since t-distribution also has specially defined values $t_{\alpha, n-1}$ similar to $z_{\alpha}$, we can simply use the following 2-sided tests at significance level $\alpha$
\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &\bigg \lvert\frac{\sqrt{n}}{S}(\overline{X} - \mu_{0}) \bigg\rvert &> &t_{\alpha/2, n-1}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &\bigg \lvert\frac{\sqrt{n}}{S}(\overline{X} - \mu_{0}) \bigg\rvert &\leq &t_{\alpha/2, n-1}\newline
    \end{alignat}

Further, *p-values* are defined using the same statistic $\sqrt{n}(\overline{X} - \mu_{0})/S$ and for any significance level which is less than the *p-value* probability that the t-statistic is greater than this statistic $\sqrt{n}(\overline{X} - \mu_{0})/S$, we will reject $H_{0}: \mu = \mu_{0}$. We accept the null hypothesis when the significance level is larger than the *p-value*.


Similar to the known variance case, we have the one sided tests defined as below
\begin{align}
        H_{0}: \mu \leq \mu_{0} \quad \text{versus} \quad H_{1}: \mu > \mu_{0}
    \end{align}
\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &\frac{\sqrt{n}}{S}(\overline{X} - \mu_{0}) &> &t_{\alpha, n-1}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &\frac{\sqrt{n}}{S}(\overline{X} - \mu_{0}) &\leq &t_{\alpha, n-1}\newline
    \end{alignat}
and the other side
\begin{align}
        H_{0}: \mu \geq \mu_{0} \quad \text{versus} \quad H_{1}: \mu < \mu_{0}
    \end{align}
\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &\frac{\sqrt{n}}{S}(\overline{X} - \mu_{0}) &< &-t_{\alpha, n-1}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &\frac{\sqrt{n}}{S}(\overline{X} - \mu_{0}) &\geq &-t_{\alpha, n-1}\newline
    \end{alignat}
and we can calculate the *p-value* as well in the above cases using the test statistic.


## Testing Equality of Means of Two Normal Populations

### Known Variances

Consider the two populations as
\begin{align}
        X_{1}, X_{2}, \ldots, X_{n} &\sim \mathcal{N}(\mu_{x}, \sigma_{x}^{2})\newline
        Y_{1}, Y_{2}, \ldots, Y_{m} &\sim \mathcal{N}(\mu_{y}, \sigma_{y}^{2})
    \end{align}

Then, the difference in the sample means will itself be a normal distribution (since it is the difference of two normals), and the test statistic can be defined as below
\begin{align}
        \overline{X} - \overline{Y} \sim \mathcal{N}(\mu_{x} - \mu_{y}, \sqrt{\frac{\sigma_{x}^{2}}{n} + \frac{\sigma_{y}^{2}}{m}})\newline
        T = \frac{(\overline{X} - \overline{Y}) - (\mu_{x} - \mu_{y})}{\sqrt{\frac{\sigma_{x}^{2}}{n} + \frac{\sigma_{y}^{2}}{m}}} \sim \mathcal{N}(0, 1)
    \end{align}

when $H_{0}$ is true,
\begin{align}
        T = \frac{(\overline{X} - \overline{Y})}{\sqrt{\frac{\sigma_{x}^{2}}{n} + \frac{\sigma_{y}^{2}}{m}}} \sim \mathcal{N}(0, 1)
    \end{align}
and we compare the following hypotheses
\begin{alignat}{3}
        &H_{0}: \mu_{x} = \mu_{y} \quad &\text{versus} \quad &H_{1}: \mu_{x} \neq \mu_{y}\newline
        \text{or,} \quad &H_{0}: \mu_{x} - \mu_{y} = 0 \quad &\text{versus} \quad &H_{1}: \mu_{x} - \mu_{y} \neq 0
    \end{alignat}
we reject $H_{0}$ when the difference between the means is large, i.e., $H_{0}$ is testing whether the test statistic is close to zero or not

\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &T &> &z_{\alpha/2}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &T &\leq &z_{\alpha/2}
    \end{alignat}
where the variances of both the populations are known.


In a very similar fashion, the hypthesis testing rules for one sided test can be derived.

For
\begin{align}
        H_{0}: \mu_{x} \leq \mu_{y} \quad \text{versus} \quad H_{1}: \mu_{x} > \mu_{y}
    \end{align}
We reject $H_{0}$ when the difference $\mu_{x} - \mu_{y}$ is highly positive
\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &\frac{(\overline{X} - \overline{Y})}{\sqrt{\frac{\sigma_{x}^{2}}{n} + \frac{\sigma_{y}^{2}}{m}}} &> &z_{\alpha}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &\frac{(\overline{X} - \overline{Y})}{\sqrt{\frac{\sigma_{x}^{2}}{n} + \frac{\sigma_{y}^{2}}{m}}} &\leq &z_{\alpha}
    \end{alignat}

For the other side of the test, we use the same criteria as above, but switching the sets $X$ and $Y$.

### Unknown but Equal Variances

We consider the same two populations of $Xs$ and $Ys$, but this time the variances are unknown. for simplicity of analysis, we assume that the unknown variances are same
\begin{align}
        \sigma_{x} = \sigma_{y} = \sigma
    \end{align}

From [section]({{ "/notes/probability/chapters/parameter_estimation/interval_estimates.html#estimating-difference-in-means-of-two-normal-populations" | relative_url }}), we know
\begin{align}
        S_{p}^{2} = \frac{(n-1)S_{1}^{2} + (m-1)S_{2}^{2}}{n + m - 2}\newline
        \frac{(\overline{X} - \overline{Y}) - (\mu_{x} - \mu_{y})}{\sqrt{\frac{\sigma_{x}^{2}}{n} + \frac{\sigma_{y}^{2}}{m}}} \div \frac{S_{p}}{\sigma} \sim t_{n+m-2}
    \end{align}

If $H_{0}$ is true, $\mu_{x} = \mu_{y}$ and we have
\begin{align}
        T = \frac{(\overline{X} - \overline{Y})}{S_{p}\sqrt{\frac{1}{m} + \frac{1}{n}}} \sim t_{n+m-2}
    \end{align}

and we have the critical region defined as
\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &T &> &t_{\alpha/2, n+m-2}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &T &\leq &t_{\alpha/2, n+m-2}
    \end{alignat}

and for the one sided hypothesis
\begin{align}
        H_{0}: \mu_{x} \leq \mu_{y} \quad \text{versus} \quad H_{1}: \mu_{x} > \mu_{y}
    \end{align}
We reject $H_{0}$ when the difference $\mu_{x} - \mu_{y}$ is highly positive
\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &T &> &t_{\alpha, n+m-2}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &T &\leq &z_{\alpha, n+m-2}
    \end{alignat}

### Unknown and Unequal Variances

We consider the natural test statistic as follows
\begin{align}
        \frac{(\overline{X} - \overline{Y}) - (\mu_{x} - \mu_{y})}{\sqrt{\frac{S_{x}^{2}}{n} + \frac{S_{y}^{2}}{m}}}
    \end{align}
Even when $H_{0}$ is true, the above is not a simple distribution to solve for. If we make the additional assumption that $n$ and $m$ are large, then
\begin{align}
        \frac{(\overline{X} - \overline{Y})}{\sqrt{\frac{S_{x}^{2}}{n} + \frac{S_{y}^{2}}{m}}} \sim \mathcal{N}(0, 1)
    \end{align}
and the same criteria for accepting and rejecting $H_{0}$ discussed [above](#known-variances) are applicable, but after replacing population variances with sample variances.


### Unknown and Unequal Variances

Suppose we want to observe the change in a quantity in a sample, after some kind of intervention. A simple example can be change in the mileage of a car after installation of a catalytic converter. Suppose we have $n$ samples with us, and for each of the sample, we associate $X_{i}$ with the measurement of the quantity before intervention and $Y_{i}$ with the quantity post intervention. Note that $X_{i}$ is not independent of $Y_{i}$ because they come from the same $i^{th}$ sample. Hence, the test discussed in [section](#known-variances) is not applicable.


Instead, we consider the quantity $W = X - Y$ and assume that $W_{i}$ come from a normal population. We can then consider the hypothesis
\begin{align}
        H_{0}: \mu_{w} = 0 \quad \text{versus} \quad H_{1}: \mu_{w} \neq 0
    \end{align}

Using the results derived in [section]({{ "/notes/probability/chapters/hypothesis_testing/mean_normal.html#unknown-variance" | relative_url }}), we have
\begin{alignat}{4}
        \text{Reject}\quad &H_{0} \quad\text{if}\quad &\sqrt{n}\frac{\overline{W}}{S_{w}} &> &t_{\alpha/2, n-1}\newline
        \text{Accept}\quad &H_{0} \quad\text{if}\quad &\sqrt{n}\frac{\overline{W}}{S_{w}} &\leq &t_{\alpha/2, n-1}
    \end{alignat}

One sided tests can be derived in exactly the same manner as [section]({{ "/notes/probability/chapters/hypothesis_testing/mean_normal.html#unknown-variance" | relative_url }}) and the concepts discussed in [section]({{ "/notes/probability/chapters/hypothesis_testing/mean_normal.html#p-value" | relative_url }}) still hold true.


## Tests around Variance of Normal Population

For a $n$ sized sample of independent observations from a normal population, we are interested in checking
\begin{align}
        H_{0}: \sigma^{2} = \sigma_{0}^{2} \quad \text{versus} \quad \sigma^{2} \neq \sigma_{0}^{2}
    \end{align}

Recall from [section]({{ "/notes/probability/chapters/sample_mean_var/normal.html#distributions-for-a-normal-population" | relative_url }})
\begin{align}
        \frac{(n-1)S^{2}}{\sigma^{2}} \sim \chi_{n-1}^{2}
    \end{align}

Then if $H_{0}$ is true, our test statistic
\begin{align}
        TS = \frac{(n-1)S^{2}}{\sigma_{0}^{2}} \sim \chi_{n-1}^{2}
    \end{align}

and from the test simply becomes
\begin{alignat}{2}
        \text{Accept} \quad &H_{0} \quad &&\text{if} \quad \chi_{1-\alpha/2, n-1}^{2} \leq TS \leq \chi_{\alpha/2, n-1}^{2}\newline
        \text{Reject} \quad &H_{0} \quad &&\text{otherwise}
    \end{alignat}

One sided test can be done in a similar manner, comparing with $\chi_{1-\alpha, n-1}^{2}$ or $\chi_{\alpha, n-1}^{2}$ based on which side we want to reject $H_{0}$.


### Comparing Variance of Two Normal Populations

We are interested in comparing
\begin{align}
        H_{0}: \sigma_{x}^{2} = \sigma_{y}^{2} \quad \text{versus} \quad \sigma_{x}^{2} \neq \sigma_{y}^{2}
    \end{align}

Recall that the ratio of sample variance with population variance is $\chi^{2}$-distributed, and the ratio of two $\chi^{2}$-distributed variables has an F-distribution. Hence, when $H_{0}$ is true,
\begin{align}
        TS = \frac{S_{x}^{2}}{S_{y}^{2}} \sim F_{n-1, m-1}
    \end{align}

Noting that F-distribution is always positive, the region for accepting $H_{0}$ simply become
\begin{alignat}{2}
        \text{Accept}\quad &H_{0} \quad &&\text{if} \quad F_{1-\alpha/2, n-1, m-1} \leq TS \leq F_{\alpha/2, n-1, m-1}\newline
        \text{Reject}\quad &H_{0} \quad &&\text{otherwise}
    \end{alignat}


## Tests around Bernoulli Population

Suppose we have a set of $n$ samples and we want to test how many of them satisfy a property (or equivalently, success). Let $p$ be the fraction of population satisfying he property and we want to check if this equals $p_{0}$
\begin{align}
        H_{0}: p \leq p_{0} \quad \text{versus} \quad p > p_{0}
    \end{align}

i.e., we reject this batch if the size of sample not satisfying the property (defective) is more than some predefined quantity/significance $p_{0}$.


We reject when the defectives in the sample ($X$) are more than a threshold $k$
\begin{align}
        P(X \geq k) = \sum_{i=k}^{n} \binom{n}{i} = \sum_{i=k}^{n} p^{i}(1-p)^{n-i}
    \end{align}

which is an increasing function in $p$. Hence, when $H_{0}$ is true,
\begin{align}
        P(X \geq k) \leq \sum_{i=k}^{n} p_{0}^{i}(1-p_{0})^{n-i}
    \end{align}

and we reject when $X \geq k^{\*}$ depending on the significance level $\alpha$
\begin{align}
        k^{\*} = \text{minimum}\quad k \quad \text{where} \quad \sum_{i=k}^{n} p_{0}^{i}(1-p_{0})^{n-i} \leq \alpha
    \end{align}
because there can be multiple $k$ which satisfy the above equation, and we want to reject $H_{0}$ as soon as the number of defectives in sample $X$ is more than the minimum $k$.


The test can also be done using *p-value*
\begin{align}
        \text{p-value} &= P(Bin(n, p_{0}) \geq x)\newline
        &= \sum_{i=x}^{n}p_{0}^{i}(1-p_{0})^{n-i}
    \end{align}

where $x$ is the count of defects in the sample. We reject $H_{0}$ at any $\alpha >$ *p-value* since in that situation the number of defects required will be much less than $x$.

For large $n$, $X$ will behave like a normal distribution and when $H_{0}$ is true,
\begin{align}
        \frac{X - np_{0}}{\sqrt{np_{0}(1-p_{0})}} \sim \mathcal{N}(0,1)
    \end{align}

and criteria discussed in [section]({{ "/notes/probability/chapters/hypothesis_testing/mean_normal.html#known-variance" | relative_url }}) hold.


# Linear Regression

We are given pairs of data $(x_{1},y_{1}), (x_{2},y_{2}), \ldots, (x_{n},y_{n})$ (all independent) where we assume that $x$ and $y$ are governed by the linear relation
\begin{align}
        y \approx \theta_{0} + \theta_{1}x
    \end{align}
The aim is to determine the model which is parametric consisting of two parameters $\theta_{0}$ and $\theta_{1}$. We find it using the least squares estimate, i.e., minimizing
\begin{align}
        \minimize_{\theta_{0}, \theta_{1}} \sum_{i=1}^{n} (y_{i} - \theta_{0} - \theta_{1}x)^{2}
    \end{align}
The true model also includes noise and is given by
\begin{align}
        Y_{i} = \theta_{0} + \theta_{1}X_{i} + W_{i}
    \end{align}
where we assume the noise $W_{i} \sim \mathcal{N}(0, \sigma^{2})$ and is independently and identically distributed. Observing some $X$ and $Y$ is same as observing the noise.
\begin{align}
        P(X=x,Y=y) &= P(W=y-\theta_{0}-\theta_{1}x) = \frac{1}{\sqrt{2\pi \sigma_{2}}} \exp\bigg(-\frac{(y-\theta_{0}-\theta_{1}x)^{2}}{2 \sigma^{2}}\bigg)\newline
        P(X_{1}=x_{1},Y_{1}=y_{1}, \ldots, X_{n}=x_{n},Y_{n}=y_{n}) &= \prod_{i=1}^{n} P(X_{1}=x_{i},Y_{i}=y_{i})\newline
        &= \prod_{i=1}^{n} W_{i} = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma_{2}}} \exp\bigg(-\frac{(y_{i}-\theta_{0}-\theta_{1}x_{i})^{2}}{2\sigma^{2}}\bigg)
    \end{align}
Maximizing the above product is maximizing the likelihood of the occurrence of the data under the model parameters $\theta_{0}$ and $\theta_{1}$. Since taking log will not change the maxima, we usually maximize the log likelihood
\begin{align}
        \maximize_{\theta_{0}, \theta_{1}} \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^{2}}} \exp(-\frac{(y_{i}-\theta_{0}-\theta_{1}x_{i})^{2}}{2\sigma^{2}}) = \minimize_{\theta_{0}, \theta_{1}} \sum_{i=1}^{n} (y_{i}-\theta_{0}-\theta_{1}x_{i})^{2}
    \end{align}

We can take derivatives with respect to the parameters of the above function to get the estimate for the parameters as
\begin{align}
        \bar{x} &= \frac{1}{n} \sum_{i=1}^{n} x_{i} \text{,}\quad \bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_{i}\newline
        \hat{\theta}\_{1} &= \frac{\sum_{i=1}^{n} (x_{i} - \bar{x}) (y_{i} - \bar{y})}{\sum_{i=1}^{n}(x_{i} - \bar{x})^{2}} = \frac{E[(X-\overline{X})(Y-\overline{Y})]}{E[(X-\overline{X})^{2}]} = \frac{Cov(X,Y)}{Var(X)}\newline
        \hat{\theta}\_{0} &= \bar{y} - \hat{\theta_{1}} \bar{x}
    \end{align}

The above formulae can also be derived if the additives are a function of $X$. Since the linear relationship will still be respected and the loglikelihood can be maximized to get the estimates of the parameters.


Some useful notation
\begin{align}
{2}
        S_{xY} &= \sum_{i=1}^{n} (x_{i} - \bar{x})(Y_{i} - \overline{Y}) &= (\sum_{i=1}^{n}x_{i}Y_{i}) - n\bar{x}\overline{Y}\newline
        S_{xx} &= \sum_{i=1}^{n} (x_{i} - \bar{x})^{2} &= (\sum_{i=1}^{n} x_{i}^{2}) - n\bar{x}^{2}\newline
        S_{YY} &= \sum_{i=1}^{n} (Y_{i} - \overline{Y})^{2} &= (\sum_{i=1}^{n} Y_{i}^{2}) - n\overline{Y}^{2}
    \end{align}


## Mean and Variance of Coefficients

First note that
\begin{align}
        E[Y_{i}] = E[\theta_{0} + \theta_{1}X_{i} + W_{i}] = \theta_{0} + \theta_{1}X_{i}\newline
        E[\overline{Y}] = (\sum_{i=1}^{n} E[Y_{i}])/n = \theta_{0} + \theta_{1}\overline{X}\newline
        Var(Y_{i}) = \sigma_{2}
    \end{align}
Thus,
\begin{align}
        E[\hat{\theta}\_{1}] &= E\bigg[ \frac{\sum_{i=1}^{n} (x_{i} - \overline{x}) (Y_{i} - \overline{Y})}{\sum_{i=1}^{n}(x_{i} - \overline{x})^{2}} \bigg]\newline
        &= E\bigg[ \frac{\sum_{i=1}^{n} (x_{i} - \overline{x}) (E[Y_{i}] - E[\overline{Y}])}{\sum_{i=1}^{n}(x_{i} - \overline{x})^{2}} \bigg]\newline
        &= \theta_{1}\newline
        E[\hat{\theta}\_{0}] &= E[\overline{Y} - \hat{\theta_{1}} \bar{x}] = \theta_{0}
    \end{align}
meaning that our estimates of the parameters are unbiased and their error will equal the variance
\begin{align}
        Var(\hat{\theta}\_{1}) &= Var \bigg( \frac{\sum_{i=1}^{n} (x_{i} - \overline{x}) (Y_{i} - \overline{Y})}{\sum_{i=1}^{n}(x_{i} - \overline{x})^{2}} \bigg)
        = Var \bigg( \frac{\sum_{i=1}^{n} (x_{i} - \overline{x})Y_{i}}{\sum_{i=1}^{n}(x_{i} - \overline{x})^{2}} \bigg)\newline
        &= \frac{1}{(\sum_{i=1}^{n}(x_{i} - \overline{x})^{2})^{2}} \sum_{i=1}^{n} (x_{i} - \overline{x})^{2} Var(Y_{i})
        = \frac{\sigma^{2}}{\sum_{i=1}^{n}(x_{i} - \overline{x})^{2}}\newline
        Var(\hat{\theta}\_{0}) &= Var(\overline{Y} - \hat{\theta_{1}} \bar{x})
        = Var \bigg( \sum_{i=1}^{n} \bigg( \frac{1}{n} - \frac{\bar{x}(x_{i} - \bar{x})}{\sum_{i=1}^{n}(x_{i} - \bar{x})^{2}} \bigg) \bigg)\newline
        &= \frac{\sigma^{2}}{n^{2}} \bigg( \sum_{i=1}^{n} \bigg( \frac{\sum_{i=1}^{n}x_{i}^{2} - n\bar{x}x_{i}}{\sum_{i=1}^{n}x_{i}^{2} - n\bar{x}^{2}} \bigg)^{2} \bigg)
        = \frac{\sigma^{2}}{n^{2} (\sum_{i=1}^{n}x_{i}^{2} - n\bar{x}^{2})^{2}} (n(\sum_{i=1}^{n})^{2} - n^{2}\bar{x}^{2}(\sum_{i=1}^{n})^{2})\newline
        &= \sigma^{2} \frac{\sum_{i=1}^{n} x_{i}^{2}}{n\big((\sum_{i=1}^{n} x_{i}^{2}) - n\bar{x}^{2} \big)}
    \end{align}
because both the estimators are linear combinations of independent identically distributed normal random variables $Y_{i}s$, and the variance of linear combination of independent random variables is simply the sum of variances multiplied by squares of coefficients.


Thus, **$\hat{\theta_{0}}$ and $\hat{\theta}\_{1}$ are both normally distributed random variables.** with the following distributions

\begin{align}
        \hat{\theta}\_{1} &\sim \mathcal{N}\bigg(\theta_{1}, \frac{\sigma^{2}}{\sum_{i=1}^{n}(x_{i} - \overline{x})^{2}} \bigg)\newline
        \hat{\theta}\_{0} &\sim \mathcal{N}\bigg(\theta_{0}, \sigma^{2} \frac{\sum_{i=1}^{n} x_{i}^{2}}{n\big((\sum_{i=1}^{n} x_{i}^{2}) - n\bar{x}^{2} \big)} \bigg)
    \end{align}


## Distribution of Residual

Residuals and the $SS_{R}$ are defined as
\begin{align}
        R &= Y - (\hat{\theta}\_{0} + \hat{\theta}\_{1}X)\newline
        SS_{R} &= \sum_{i=1}^{n} R_{i}^{2} = \sum_{i=1}^{n} (Y - \hat{\theta}\_{0} - \hat{\theta}\_{1}X)^{2}\newline
        &= \frac{S_{xx}S_{YY} - S_{xY}^{2}}{S_{xx}}
    \end{align}

$SS_{R}$ is itself a random variable and it can be shown that
\begin{align}
        \frac{SS_{R}}{\sigma^{2}} \sim \chi_{n-2}^{2}\newline
        E[\frac{SS_{R}}{\sigma^{2}}] = n - 2\newline
        E[\frac{SS_{R}}{n-2}] = \sigma^{2}\newline
    \end{align}
since $SS_{R}/\sigma^{2}$ is the sum of squares of normally distributed variables ($E[Y] = \theta_{0} + \theta_{1}X$) and two degrees of freedoms are already taken up by the coefficients. Further, $SS_{R}$ is an unbiased estimator of the variance of the error terms $\sigma^{2}$, and is also independent of the coefficients.


## Inferences Concerning Coefficients

We are most interseted in checking whether a coefficient has an effect or not
\begin{align}
        H_{0}: \theta_{1} = 0 \quad \text{versus} \quad H_{1}: \theta_{1} \neq 0
    \end{align}

We know from above derivations that
\begin{align}
        \frac{\hat{\theta}\_{1} - \theta_{1}}{\sigma^{2} / S_{xx}} \sim \mathcal{N}(0, 1)\newline
        \frac{SS_{R}}{\sigma^{2}} \sim \chi_{n-2}^{2}
    \end{align}
and both the random variables are independent of each other. Hence their division is t-distributed random variable and when $H_{0}$ is true, $\theta_{1} = 0$
\begin{align}
        \frac{\sqrt{S_{xx}}\hat{\theta}\_{1}/\sigma}{\sqrt{\frac{SS_{R}}{\sigma^{2} (n-2)}}} = \hat{\theta}\_{1}\sqrt{\frac{(n-2)S_{xx}}{SS_{R}}} = TS \sim t_{n-2}
    \end{align}
We do this since we do not know the exact value of $\sigma^{2}$ and need to eliminate it with a sample derived version. The hypothesis test at significance level $\alpha$ simply becomes
\begin{align}
{4}
        \text{Reject\quad} &H_{0} \text{\quad if \quad} &\lvert TS \rvert &> &t_{\alpha/2, n-2}\newline
        \text{Accept\quad} &H_{0} \text{\quad if\quad} &\vert TS \rvert &\leq &t_{\alpha/2, n-2}
    \end{align}
which can be converted to a *p-value* using the $TS$ and t-distribution. A small *p-value* will lead to rejection of $H_{0}$ meaning that the data provides evidence of a relationship between dependent and independent variables.


A confidence interval for $\theta_{1}$ at $1-\alpha$ confidence can be obtained as follows
\begin{align}
        P(-t_{\alpha/2, n-2} < (\hat{\theta}\_{1} - \theta_{1})\sqrt{\frac{(n-2)S_{xx}}{SS_{R}}} < t_{\alpha/2, n-2}) = 1-\alpha\newline
        \text{Confidence Interval is} \quad \bigg(\hat{\theta}\_{1} - t_{\alpha/2, n-2}\sqrt{\frac{SS_{R}}{(n-2)S_{xx}}} < \theta_{1} < \hat{\theta}\_{1} + t_{\alpha/2, n-2}\sqrt{\frac{SS_{R}}{(n-2)S_{xx}}} \bigg)
    \end{align}

The hypothesis test for $\theta_{0}$ can be done in the exact same manner as $\theta_{1}$ by considering the following test statistic
\begin{align}
        TS = (\hat{\theta}\_{1} - \theta_{1})\sqrt{\frac{n(n-2)S_{xx}}{(\sum_{i=1}^{n} x_{i}^{2})SS_{R}}} \sim t_{n-2}
    \end{align}



## Inferences Concerning Mean Response

For any new point $x_{0}$, the unbiased estimator for the response is
\begin{align}
        y_{0} &= \hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0}\newline
        E[y_{0}] &= E[\hat{\theta}\_{0}] + E[\hat{\theta}\_{1}]E[x_{0}] = \theta_{0} + \theta_{1}x_{0}
    \end{align}
To get the distribution of this mean response, note that
\begin{align}
        Y_{0} &= \hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0} = \overline{Y} - \hat{\theta}\_{1}\bar{x} + \hat{\theta}\_{1}x_{0}\newline
        &= \frac{1}{n}\sum_{i=1}^{n} Y_{i} + (x_{0} - \bar{x})\frac{\sum_{i=1}^{n} (x_{i} - \bar{x})Y_{i}}{\sum_{i=1}^{n} (x-\bar{x})^{2}}\newline
        &= \sum_{i=1}^{n} \bigg( \frac{1}{n} + \frac{(x_{i} - \bar{x})(x_{0} - \bar{x})}{S_{xx}} \bigg)Y_{i}
    \end{align}
which is a linear combination of independent normally distributed random variables $Y_{i}s$. Thus, the mean response is also a normally distributed random variable and we can get the confidence intervals by considering the mean and variance of this random variable
\begin{align}
        Var(\hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0}) &= \sum_{i=1}^{n} \bigg( \frac{1}{n} + \frac{(x_{i} - \bar{x})(x_{0} - \bar{x})}{S_{xx}} \bigg)^{2}Var(Y_{i})\newline
        \hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0} &\sim \mathcal{N}\bigg(\theta_{0} + \theta_{1}x_{0}, \sigma^{2} \bigg[ \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}} \bigg]\bigg)
    \end{align}
To eliminate $\sigma^{2}$,
\begin{align}
        SS_{R}/\sigma^{2} \sim \chi_{n-2}^{2}\newline
        \frac{(\hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0}) - (\theta_{0} + \theta_{1}x_{0})}{\sigma^{2} \bigg[ \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}} \bigg]} \div \sqrt{\frac{SS_{R}}{(n-2)\sigma^{2}}} \sim t_{n-2}
    \end{align}
and the confidence intervals for confidence $1-\alpha$ become
\begin{align}
        (\hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0}) \pm t_{\alpha/2, n-2} \sqrt{\bigg( \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}} \bigg) \bigg( \frac{SS_{R}}{n-2}\bigg)}
    \end{align}


## Inferences Concerning Future Response

The above section [1.4](#sec:infer_mean_resp){reference-type="ref" reference="sec:infer_mean_resp"} discussed the distribution of the mean response. In many scenarios, we are interested in the distribution of the actual response $Y$ at input $x_{0}$, which takes the noise into account as well. We note
\begin{align}
        Y_{0} &\sim \mathcal{N}(\theta_{0} + \theta_{1}x_{0}, \sigma^{2})\newline
        \hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0} &\sim \mathcal{N}\bigg(\theta_{0} + \theta_{1}x_{0}, \sigma^{2} \bigg[ \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}} \bigg]\bigg)\newline
        Y_{0} - \hat{\theta}\_{0} - \hat{\theta}\_{1}x_{0} &\sim \mathcal{N}\bigg(0, \sigma^{2}\bigg( 1 + \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}} \bigg)\bigg)
    \end{align}

Now we utilise the distribution of $SS_{R}$ to eliminate $\sigma^{2}$ and get to the t-distribution
\begin{align}
        \frac{Y_{0} - \hat{\theta}\_{0} - \hat{\theta}\_{1}x_{0}}{\sigma\sqrt{1 + \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}}}} \div \sqrt{\frac{SS_{R}}{(n-2)\sigma^{2}}} \sim t_{n-2}
    \end{align}
and the **prediction** interval for the response (not mean response is) at $1-\alpha$ confidence
\begin{align}
        (\hat{\theta}\_{0} + \hat{\theta}\_{1}x_{0}) \pm t_{\alpha/2, n-2} \sqrt{\bigg( 1+ \frac{1}{n} + \frac{(x_{0} - \bar{x})^{2}}{S_{xx}} \bigg) \bigg( \frac{SS_{R}}{n-2}\bigg)}
    \end{align}

Note that **prediction interval is the interval where we expect the value of a random variable to lie, whereas the confidence interval is the one where the value of a parameter estimate to lie.**



## Coefficient of Determination

Let's consider the variation in respone Y
\begin{align}
        S_{Y} = \sum_{i=1}^{n} (Y_{i} - \overline{Y})^{2}
    \end{align}
and the variation in the response after removing the effect of inputs
\begin{align}
        SS_{R} = \sum_{i=1}^{n} (Y_{i} - \theta_{0} - \theta_{1}x_{0})^{2}
    \end{align}
and thus,
\begin{align}
        S_{YY} - SS_{R}
    \end{align}
is the variation explained by the inputs. We define $R^{2}$ as
\begin{align}
        R^{2} = \frac{S_{YY} - SS_{R}}{S_{YY}} = 1 - \frac{SS_{R}}{S_{YY}}
    \end{align}
**$R^{2}$ is the proportion of total variance explained by the inputs. A value close to 1 implies most of the variance is explained by the inputs whereas 0 means little variance is explained by inputs.**


It can also be shown that the absolute value of correlation coefficient between $x$ and $Y$ equals the coefficient of determination. Thus, we know the value of $R^{2}$ for simple linear regression directly by $r$.


## Weighted Least Squares

Suppose we know that the variance of $Y$ is dependent on $Y$ itself in the form $Var(Y_{i}) \propto \sigma^{2}/w_{i}$, i.e., the weights are known only upto a constant. In this case, we minimize the weighted least squares to obtain the coefficients
\begin{align}
        \minimize_{\theta_{0}, \theta_{1}} \sum_{i=1}^{n} w_{i}(Y_{i} - \theta_{0} - \theta_{1}x_{i})^{2}
    \end{align}


# Life Testing

This section develops statistical methods around estimtating distribution of variables indicating the lifetime of a particular object. For instance, if the lifetime has an exponential distribution, we utilise the sample to obtain the parameters of the exponential distribution.


Let $X$ be a continuous random variable denoting lifetime of an item, having cumulative distribution $F$ and density function $f$, then
\begin{align}
        \text{hazard function or failure rate,} \quad \lambda(t) &= \frac{f(t)}{1 - F(t)}\newline
        P(X \in (t, t+dt)|X > t) &= \frac{P(X \in (t, t+dt), X > t)}{P(X > t)} = \frac{P(X \in (t, t+dt))}{P(X > t)}\newline
        &\approx \frac{f(t)}{1 - F(t)} dt
    \end{align}

**$\lambda(t)$ denotes the conditional probability that an item of age t will fail in the next moment.**


For exponential distribution, $\lambda(t) = (\lambda e^{-\lambda x})/e^{-\lambda x} = \lambda$ because of the memoryless propoerty.


Hazard function uniquely determines the cumulative distribution $F$
\begin{align}
        \lambda(s) &= \frac{\frac{d}{ds} F(s)}{1 - F(s)} = \frac{d}{ds} (-log(1 - F(s)))\newline
        F(t) &= 1 - exp\left(-\int_{0}^{s} \lambda(s) ds \right)
    \end{align}

## Exponential Distribution: Stopping at rth failure

Suppose we have $n$ items with exponentially distributed lifetime with unknown parameter and we wish to estimate the mean $\theta (note \lambda = 1/\theta)$. We observe the items until $r$ failures and try to estimate $\theta$. Let $X_{i}$ denote the lifetime of the $i^{th}$ item with the following notation
\begin{align}
        x_{1} \leq x_{2} \leq \ldots \leq x_{r} \quad \text{for} \quad i_{1}, i_{2}, \ldots, i_{n}
    \end{align}
i.e., $X_{i_{j}} = x_{j}$. Then the joint likelihood becomes
\begin{align}
        L &= \left(\prod_{i=1}^{r} \frac{1}{\theta}e^{-x_{i}/\theta}\right) \left(\prod_{j=r+1}^{n} e^{-x_{r}/\theta}\right)\newline
        &= \frac{1}{\theta^{r}}exp \left\\{-\frac{1}{\theta} \left(\sum_{i=1}^{r} x_{i} + (n-r)x_{r} \right) \right\\}\newline
        \log(L) &= -r\log(\theta) - \frac{\sum_{i=1}^{r} x_{i}}{\theta} - \frac{(n-r)x_{r}}{\theta}\newline
        \frac{d}{d\theta}\log(L) &= -\frac{r}{\theta} + \frac{\sum_{i=1}^{r} x_{i}}{\theta^{2}} + \frac{(n-r)x_{r}}{\theta^{2}}\newline
        \hat{\theta} &= \frac{\sum_{i=1}^{r} x_{i} + (n-r)x_{r}}{r} = \frac{\tau}{r}
    \end{align}
where we note that for $n-r$ items, the lifetime is known only to be more than $x_{r}$ and thus we use the cumulative probability of lifetime $> x_{r}$ in the likelihood equation. We can replace the values with random variables in above equations.


$\tau$ is the total time on test, i.e. the total time of survival of each item for the duration the test ran ($X_{r}$). Now, we can rewrite $\tau$ using the differences between consecutive times of failures. Note than all items survive for $X_{1}$ time, $n-1$ items survive for at least $X_{2} - X_{1}$ time, and so on till $n-r+1$ items survive for additional $X_{r} - X_{r-1}$ time. Thus,
\begin{align}
        \tau = nX_{1} + (n-1)(X_{2} - X_{1}) + \cdots + (n-r+1)(X_{r} - X_{r-1})
    \end{align}
and from [answer]({{ "/notes/probability/chapters/exercises/a_minexp.html" | relative_url }}), we know that $X_{1}$ is exponential with mean $\theta/n$ and thus, $nX_{1}$ has mean $\theta$. By memoryless property, $X_{2} - X_{1}$ is also exponential with mean $\theta/(n-1)$ and so $(n-1)(X_{2} - X_{1})$ has mean $\theta$. Thus, $\tau$ is the sum of independent exponential variables and is a Gamma distribution with parameters $(r, 1/\theta)$. Since Gamma distribution is related to a $\chi^{2}$ distribution (see [here]({{ "/notes/probability/chapters/distributions/chi_square.html#relation-between-chi-square-and-gamma-distribution" | relative_url }}))
\begin{align}
        \frac{2\tau}{\theta} &\sim \chi_{2r}^{2}\newline
        P(\chi_{1-\alpha/2, 2r}^{2} &< \frac{2\tau}{\theta} < \chi_{\alpha/2, 2r}^{2}) = 1-\alpha\newline
        \theta &\in \left(\frac{2\tau}{\chi_{\alpha/2, 2r}^{2}}, \frac{2\tau}{\chi_{1-\alpha/2, 2r}^{2}} \right) \quad \text{with confidence $1-\alpha$}
    \end{align}


## Random Numbers

We can generate random numbers using the following equation
\begin{align}
        x_{n+1} = (ax_{n} + c) mod(m)
    \end{align}
$x_{n}$ takes the values $1,2,\ldots, m-1$ and we take $x_{n}/m$ as the pseudo random number, which is uniformly distributed between $(0,1)$ for suitable choice of $a, c, m$.


### Permutation of Integers

Suppose we want to generate a permutation of integers from $1, 2, \ldots, n$ such that each of the permutations is equally likely. Assuming we have a uniform random generator $U$ with us,
\begin{align}
        P(Int(kU) + 1 = i) &= P(Int(kU) = i-1) = P(i-1 \leq kU < i)\newline
        &= P(\frac{i-1}{k} \leq U < \frac{i}{k}) = \frac{1}{k}
    \end{align}
which gives us randomly generated random integers between $1$ and $k$ with equal probability. An easy way to generate permutation is

1.  Choose a permutation $r_{1}, r_{2}, \ldots, r_{n}$ which can just be $r_{j} = j$

2.  Let $k = n$

3.  Choose a random number $U$ and let $I = Int(kU) + 1$

4.  Interchange numbers at position $k$ and $I$

5.  $k = k-1$

6.  if $k > 1$ goto step 3 else return permutation

The above algorithm can also be used to get a random subset of size $r$ from a set $1, \dots, k$ by simply running the algorithm till $k = r$ since the elements in the last $r$ positions can be selected. For $r > n/2$, we find the $k=n-r$ elements not in the subset.


## Generating Discrete Random Variables

Suppose we want to generate the random variable $X$ with probability mass function
\begin{align}
        P(X = x_{i}) = p_{i}, i = 1, 2, \ldots, n\; \sum_{i=1}^{n} p_{i} = 1
    \end{align}
Then using a uniform random generator $U$, we can generate the discrete random variable using
\begin{align}
        X = x_{i} \quad \text{if} \quad p_{1} + p_{2} +\cdots + p_{i-1} \leq U < p_{1} + p_{2} +\cdots + p_{i}
    \end{align}
i.e., we divide the number line at points $p_{1}, p_{1}+p_{2}, \ldots, 1$ and choose the $i^{th}$ interval such that $U$ falls in that interval. This algorithm is valid since
\begin{align}
        P(a \leq U < b) = b-a\newline
        P(\sum_{j=1}^{i-1}p_{j} \leq U < \sum_{j=1}^{i}p_{j}) = p_{i}
    \end{align}

This method is known as *discrete inverse transform method*.


### Binomial Random Variable

To generate a Bernoulli random variable, we simply select $X = 1$ if $U < p$ otherwise $X = 0$. Similarly a binomial random variable can be generated using individual Bernoulli variables as described. A more efficient method is to use the inverse transform method. For number of successes $0, 1, 2, \ldots, n$, we must calculate the probability mass function. This can be done efficiently using recursion
\begin{align}
        p_{i} = P(X = i) = \binom{n, i} p^{i} (1-p)^{n-i}\newline
        \frac{p_{i+1}}{p_{i}} = \frac{n-i}{i+1} \frac{p}{1-p}
    \end{align}

The algorithm is then simply

1.  Assign $i = 0, P = p_{0} = (1-p)^{n}, F = P, b = p/(1-p)$

2.  Generate random number $U \in (0, 1)$

3.  if $U \leq F, X = i$, stop else continue

4.  Update $P$ to get $p_{i+1}$, $P = Pb\frac{n-i}{i+1}$

5.  Update the cumulative probability $F = F + P$

6.  increase $i = i + 1$, goto 3

The average number of iterations taken by the algorithm $= E[X + 1] = np + 1$ since total values checked are $n + 1$.


## Generating Continuous Random Variables

To generate a random variable $X$, We utilise it's cumulative distribution function $F$. Note that $F$ is strictly increasing from $0$ to $1$ and the probability density $f$ and $F$ have a one to one mapping, i.e., $F$ has an inverse $F^{-1}$. So, to get $X$, we first generate $U \in (0, 1)$ and then $X = F^{-1}(U)$.


### Exponential Random Variable

The distribution function $F = 1 - exp(-\lambda x)$. Then, the inverse is
\begin{align}
        x &= -\frac{1}{\lambda}log(1 - F)\newline
        \text{or, }\quad X &= \frac{1}{\lambda}log(1 - U)
    \end{align}
and $X$ will follow the exponential distribution. Further, replacing $U$ with $1-U$ will still remain a uniform distribution, meaning $X$ will still be exponential.

### Normal Random Variable

Consider $X, Y \sim \mathcal{N}(0, 1)$. Then,
\begin{align}
        f_{XY}(x,y) = \frac{1}{2\pi}exp(-\frac{x^{2}+y^{2}}{2})
    \end{align}
is the joint distribution. $(X, Y)$ is a point on the cartesian plane and thus, will have an equivalent polar coordinate $(R, \Theta)$ implying $R^{2} = X^{2} + Y^{2}$ which is a $\chi_{2}^{2}$ variable. From section [\[sec:rel_gamma_chi\]](#sec:rel_gamma_chi){reference-type="ref" reference="sec:rel_gamma_chi"},
\begin{align}
       f_{R^{2}}(r) &= \frac{1}{2}exp(-\frac{r}{2})\newline
       \text{and} \quad f_{XY}(x,y) &= \frac{1}{2\pi} exp(-\frac{r}{2}) \quad \text{when} \quad x^{2} + y^{2} = r
    \end{align}

Now, $R$ and $\Theta$ are independent variables and can be used to generate $X$ and $Y$. $\Theta$ is uniformly distributed in $[0, 2\pi]$. Taking the inverse of cumulative distribution of $R^{2}$ (Note that $f_{R^{2}}(r)$ is a distribution on $R^{2}$ and not $R$),
\begin{align}
        R^{2} &= -2log(1 - U_{1})\newline
        \Theta &= 2\pi U_{2}
    \end{align}
where $U_{1}$ and $U_{2}$ are uniform random variables. Using the transformation back to cartesian coordinates from polar ones,
\begin{align}
        X &= \sqrt{-2log(1 - U_{1})}cos(2\pi U_{2})\newline
        Y &= \sqrt{-2log(1 - U_{1})}sin(2\pi U_{2})
    \end{align}
This approach is called *Box-Muller method*. To generate standard normals with mean $\mu$ and variance $\sigma^{2}$, we simply return $\mu + \sigma X, \mu+\sigma Y$.

### Normal Random Variable from Uniform Distribution

Using the central limit theorem, we can add up multiple uniform distributions to get a normal random variable.
\begin{align}
        Y = \bigg(\sum_{i=1}^{12}X_{i} \bigg) - 6 \sim \mathcal{N}(0,1)
    \end{align}
because the mean of 12 uniform random variables is $12 * 0.5 = 6$ and the variance of sum of 12 independent random variables is $12 \times (1-0)^{2}/12 = 1$. The same equation with 30 uniform distributions will become
\begin{align}
        Y = \sqrt{\frac{2}{5}}\bigg[\bigg(\sum_{i=1}^{30}X_{i} \bigg) - 15\bigg] \sim \mathcal{N}(0,1)
    \end{align}
and combining more variables will increase the accuracy of the approximation, but also increase computational time.


## Exercises

1.  **Independence in Complements**

    Given $A \perp B$, show $A \perp B^{c}$ and $A^{c} \perp B^{c}$. [Solution]({{ "/notes/probability/chapters/exercises/a_indcomp.html" | relative_url }})

1.  **Conditional Independence**

    $A,B,$ and $C$ are independent with $P(C) > 0$. Show that $A\perp B \vert C$. [Solution]({{ "/notes/probability/chapters/exercises/a_conind.html" | relative_url }})

1.  **Geometry of Meeting**

    R and J have to meet at a given place and each will arrive at the given place independent of each other with a delay of 0 to 1hr uniformly distributed. The pairs of delays are all equally likely. The first to arrive waits for 15 minutes and leaves. What is the probability of meeting ? [Solution]({{ "/notes/probability/chapters/exercises/a_geomeet.html" | relative_url }})

1.  **Expectation of Function**

    Let $X$ and $Y$ be random variables with $Y = g(X)$. Show $E[Y] = \sum_{x}g(x)p_{X}(x)$. [Solution]({{ "/notes/probability/chapters/exercises/a_expfn.html" | relative_url }})

1.  **Cumulative Distribution Function**

    A random variable X is a combination of a continuous and discrete distribution as follows
    \begin{align}
            f_{X}(x) = \begin{cases} 0.5 &\mbox{$a \leq x \leq b$}\newline
                                     0.5 &\mbox{x = 0.5}\newline
                                     0 &\mbox{otherwise} \end{cases}
        \end{align}
    Find the Cumulative Distribution of X. [Solution]({{ "/notes/probability/chapters/exercises/a_cumuldistfn.html" | relative_url }})

1.  **Number of tosses till first head**

    When tossing a fair coin, what is the $E[$\# tosses till the first H$]$. [Solution]({{ "/notes/probability/chapters/exercises/a_tossh.html" | relative_url }})

1.  **Iterated Expectation Proof**

    For discrete variables, show $E[X] = E[E[X \vert Y]]$. [Solution]({{ "/notes/probability/chapters/exercises/a_itrexpproof.html" | relative_url }})

1.  **Iterated Expectation for three variables**

    For three random variables $X$, $Y$ and $Z$, show $E[Z \vert X] = E[E[Z \vert X,Y] \vert X]$. [Solution]({{ "/notes/probability/chapters/exercises/a_itrexpthree.html" | relative_url }})

1.  **Iterated Expectation practice**

    A class has two sections denoted by the random variable $Y$. Let $X$ denote the quiz score of a student. Given that section 1 has 10 students, section 2 has 20 students, $E[X \vert Y=1] = 90, E[X \vert Y=2] = 60, Var(X \vert Y=1) = 10, Var(X \vert Y=2) = 20$, find $E[X]$ and $Var(X)$. [Solution]({{ "/notes/probability/chapters/exercises/a_itrexppractice.html" | relative_url }})

1.  **Hat Problem**

    $n$ people throw their hats in a box and then pick a hat at random. What is the expected number of people who pick their own hat ? [Solution]({{ "/notes/probability/chapters/exercises/a_hatproblem.html" | relative_url }})

1.  **Breaking a stick**

    A stick of length $l$ is broken first at $X$ uniformly chosen between $[0,l]$, and then at $Y$, uniformly chosen between $[0,X]$. Find the expected length of the shorter part. [Solution]({{ "/notes/probability/chapters/exercises/a_breakstick.html" | relative_url }})

1.  **Convolution of Exponentials**

    Suppose $X \sim exp(\lambda)$ and $Y \sim exp(\mu)$, find the probability distribution $p_{X+Y}(x)$. [Solution]({{ "/notes/probability/chapters/exercises/a_convexp.html" | relative_url }})

1.  **Triangles from a Stick**

    We have a stick of length 1. We randomly choose two points on the stick and break the stick at those points. Calculate the probability that the three pieces form a triangle. [Solution]({{ "/notes/probability/chapters/exercises/a_trianglestick.html" | relative_url }})

1.  **PMF of g(X)**

    Let $X$ be uniform in $[0, 2]$, then find the PMF of $Y = X^{3}$. [Solution]({{ "/notes/probability/chapters/exercises/a_pmffn.html" | relative_url }})

1.  **Waiting for Taxi**

    A taxi stand and bus stop near Al's home are at the same location. Al goes there and if a taxi is waiting $P=\frac{2}{3}$, he boards it. Otherwise, he waits for a taxi or bus to come, whichever is first. Taxi takes anywhere between $0$ to $10$ mins (uniform) while a bus arrives in exactly 5 mins. He boards whichever is first. Find CDF and $E$\[wait time\]. [Solution]({{ "/notes/probability/chapters/exercises/a_waittaxi.html" | relative_url }})

1.  **Bayes Theorem**

    Let $Q$ be a continuous random variable with PDF
    \begin{align}
            f_{Q}(q) = \begin{cases} 6q(1-q) &\mbox{ $0 \leq q \leq 1$}\newline
                                     0 &\mbox{ otherwise} \end{cases}
        \end{align}
    where $Q$ represents $P(success)$ for a Bernoulli $X$, i.e., $P(X=1|Q=q) = q$. Find $f_{Q|X}(q|x) \forall x \in [0,1]$ and $q$. [Solution]({{ "/notes/probability/chapters/exercises/a_bayes.html" | relative_url }})

1.  **A Normal Transformation**

    Let $X \sim \mathcal{N}(0,1)$ and $Y = g(X)$. Find $p_{Y}(y)$.
    \begin{align}
            g(t) = \begin{cases} -t &\mbox{$t \leq 0$}\newline
                                \sqrt{t} &\mbox{$t > 0$} \end{cases}
        \end{align}
    [Solution]({{ "/notes/probability/chapters/exercises/a_normaltr.html" | relative_url }})

1.  **Binomial Shooter**

    A shooter takes 10 hits in a shooting range and each shot has $p=0.2$ of hitting target independent of each other. Let $X =$ number of hits. Find

    1.  PMF of $X$

    2.  $P(\text{no hits})$

    3.  $P(\text{scoring more than misses})$

    4.  $E[X]$ and $Var(X)$

    5.  Suppose the entry is \\$3 and each shot fetches \\$2. Let $Y$ = profit. Find $E[Y]$ and $Var(Y)$.

    6.  Suppose entry is free and total reward is square of number of hits. Let $Z$ be profit. Find $E[Z]$.

    [Solution]({{ "/notes/probability/chapters/exercises/a_binshoot.html" | relative_url }})

1.  **Mosquito and Tick**

    Every second, a mosquito lands with $P = 0.5$. Once it lands, it bites with $P=0.2$. Let $X$ be the time between successive mosquito bites. Find $E[X]$ and $Var(X)$.

    Now suppose a tick comes into play independent of mosquito. It lands with $P=0.1$ and once landed, bites with $)=0.7$. Let $Y$ be the time between successive bug bites. Find $E[Y]$ and $Var(Y)$. [Solution]({{ "/notes/probability/chapters/exercises/a_mosquito.html" | relative_url }})

1.  **HH or TT**

    Given a coin with $P(H) = p$, find the $E$\[number of tosses till $HH$ or $TT$\]. [Solution]({{ "/notes/probability/chapters/exercises/a_hhtt.html" | relative_url }})

1.  **A Three Coin Game**

    Let $3$ fair coins be tossed at every turn. Given all coins and turns are independent, calculate the following (assuming success is defined as all three coins landing the same side up))

    1.  PMF of $K$, no of trials upto but not including the $2^{nd}$ success

    2.  $E$ and $Var$ of $M$, the $E[$number of tails$]$ before first success.

    [Solution]({{ "/notes/probability/chapters/exercises/a_threecoins.html" | relative_url }})

1.  **Linear Expectations**

    Bob conducts trials in a similar manner to previous problem (**A Three Coin Game**) , but with four coins. He repeatedly removes a coin at success until just a single coin remains. Calculate the Expected number of tosses till the finish of experiment. [Solution]({{ "/notes/probability/chapters/exercises/a_linexp.html" | relative_url }})

1.  **Papers Drawn with Replacement**

    Suppose there are $n$ papers in a drawer. We take one paper, sign it, and then put it back into the drawer. We take one more paper out and if it is not signed, we sign it and put it back in the drawer. If the paper is already signed, we simply put it back in the drawer. We repeat this process until all the papers are signed. Find the $E[$papers drawn till all papers are signed$]$. What is the value of this quantity as $n \to large$. [Solution]({{ "/notes/probability/chapters/exercises/a_papers.html" | relative_url }})

1.  **A Three Variable Inequality**

    Let $X$, $Y$, $Z$ be three exponentially distributed random variables with parameters $\lambda, \mu,$ and $\nu$ respectively. Find $P(X < Y < Z)$. [Solution]({{ "/notes/probability/chapters/exercises/a_threevar.html" | relative_url }})

1.  **Poisson Emails**
    You get emails according to a Poisson process at the rate of 5 messages/hour. You check email every 30 minutes. Find

    -   P(no new message)

    -   P(one new message)

    [Solution]({{ "/notes/probability/chapters/exercises/a_poissonemails.html" | relative_url }})

1.  **Poisson Fishing**

    We go fishing where we catch fishes at the rate of $0.6/hour$. We fish for two hours. If we do not catch a fish in the first two hours, we fist until the first catch. Find the following

    -   P(fish for $> 2$ hours)

    -   P(fish for $> 2$ but $< 5$ hours)

    -   P(catch at least two fish)

    -   E\[fish\]

    -   E\[Total fishing time\]

    -   $E\[\text{future fishing time} \vert \text{fished for two hours}\]$

    [Solution]({{ "/notes/probability/chapters/exercises/a_poissonfish.html" | relative_url }})

1.  **Poisson Lightbulbs**

    We have three identical but independent lightbulbs whose lifetimes are modelled by a Poisson process with parameter $\lambda$. Given that we start all the three bulbs together, find the $E[\text{time until last bulb dies out}]$. [Solution]({{ "/notes/probability/chapters/exercises/a_poissonbulb.html" | relative_url }})

1.  **Two Poisson Lightbulbs**

    Beginning at $t=0$, we begin using bulbs one at a time until failure. Any broken bulb is immediately replaced. Each new bulb is selected independently and equally likely from type A(exponential life with $\lambda = 1$) or type B(exponential life with $\lambda = 3$). Lifetimes of all bulbs are independent.

    1.  Find $E[$time until first failure$]$.

    2.  $P($no bulb failure before time $t)$.

    3.  Given that there are no failures until time t, determine the conditional probability that the first bulb used is of type A.

    4.  Find the probability that the total illumination by two type B bulbs $>$ one type A.

    5.  Suppose the process terminates after 12 bulbs fail. Determine the expected value and variance of the total illumination provided by type B bulbs while the process is in operation.

    6.  Given there are no failures until time $t$, find the expected value of time until first failure.

    [Solution]({{ "/notes/probability/chapters/exercises/a_poissonbulb2.html" | relative_url }})

1.  **Minimum of Exponentials**

    Given $n$ independent exponential random variables with different parameters, find the distribution for their minimum. [Solution]({{ "/notes/probability/chapters/exercises/a_minexp.html" | relative_url }})

1.  **A Similar Trick**

    Calculate
    \begin{align}
             \lim_{n \to \infty} \bigg[ \frac{1}{2^{n/2}\Gamma(n/2)} \int_{n + \sqrt{2n}}^{\infty} \exp \bigg( -\frac{t}{2} \bigg) t^{n/2 - 1} dt \bigg]
        \end{align}

    [Solution]({{ "/notes/probability/chapters/exercises/a_gamma_chi.html" | relative_url }})

1.  **Steady State Markov Process**

    Find the steady state probabilites of the following Markov Process [Solution]({{ "/notes/probability/chapters/exercises/a_steadymarkov.html" | relative_url }}){% include image.html url="notes/probability/images/exercises_1.png" img_classes="notes-img exercises_1" indent=true %}


1.  **Absorption Probabilities**

    Calculate the absorption probabilites for state $4$ and expected time to absortion from all states. (for absorption time, assume $p_{35} = 0$ and $p_{32} = 0.5$) [Solution]({{ "/notes/probability/chapters/exercises/a_absorbmarkov.html" | relative_url }})
    {% include image.html url="notes/probability/images/exercises_2.png" description="" img_classes="notes-img exercises_2" indent=true %}


1.  **Selecting Courses with Markov Process**
    {% include image.html url="notes/probability/images/exercises_3.png" description="" img_classes="notes-img exercises_3" indent=true %}

    Consider the above markov process for changing courses. The probability being in some course tomorrow given a course today is mentioned along the edges. Suppose we start with course 6-1 (Note that course 6 is the combination of courses 6-1, 6-2 and 6-3). Calculate the following

    1.  $P($eventually leaving course 6$)$.

    2.  $P($eventually landing in course 15$)$.

    3.  $E[$number of days till leaving course 6$]$.

    4.  At every switch for 6-2 to 6-1 or 6-3 to 6-1, we buy an ice cream (but a maximum of two). Calculate the $E[$number of ice creams before leaving course 6$]$.

    5.  Suppose we end up in 15. What is the $E[$number of steps to reach 15$]$.

    6.  Suppose we don't want to take course 15. Accordingly, when in 6-1, we stay there with probability $1/2$ while other three options have equal probabilities. If we are in 6-2, probability of going to 6-1 and 6-3 are in the same ratio as before. Calculate the $E[$number of days until we enter course 9$]$.

    7.  Assuming
        \begin{align}
            P(X_{n+1}=15 \vert X_{n}=9) &= P(X_{n+1}=9 \vert X_{n}=15) = P(X_{n+1}=15 \vert X_{n}=15)\newline
            &= P(X_{n+1}=9 \vert X_{n}=9) = 1/2
        \end{align}
        what is $P(X_{n}=15)$ and $P(X_{n}=9)$ far into the future.

    8.  Suppose
        \begin{align}
            P(X_{n+1}=6-1 \vert X_{n}=9) &= 1/8 \newline
            P(X_{n+1}=9 \vert X_{n}=9) &= P(X_{n+1}=15 \vert X_{n}=15) = 7/8
        \end{align}
        what is the $E[$number of days till return to 6-1$]$.

    [Solution]({{ "/notes/probability/chapters/exercises/a_markovcourse.html" | relative_url }})

1.  **Estimating Binomial with CLT, 1/2 correction**

    Given a Bernoulli Process with $n = 36$ and $p = 0.5$, find $P(S_{n} \leq 21)$. [Solution]({{ "/notes/probability/chapters/exercises/a_binclt.html" | relative_url }})

1.  **Sample Variance for Normal Distribution**

    The time it takes a central processing unit to process a certain type of job is normally distributed with mean 20 seconds and standard deviation 3 seconds. If a sample of 15 such jobs is observed, what is the probability that the sample variance will exceed 12 ? [Solution]({{ "/notes/probability/chapters/exercises/a_samplevar.html" | relative_url }})

1.  **MLE Estimate**

    Suppose we observe $n$ independent and identically distributed samples $x_{1}, x_{2}, \ldots, x_{n}$ from an exponential distribution. Estimate the parameter of the exponential. [Solution]({{ "/notes/probability/chapters/exercises/a_mleestimate.html" | relative_url }})

1.  **CRLB for an exponential**

    Let $X_{1}, \ldots, X_{n}$ be a random sample from an eponential distribution with the probability density
    \begin{align}
            f_{X}(x;\theta) = \begin{cases} \frac{1}{\theta} \exp \big(-\frac{x}{\theta} \big) &\mbox{$x > 0$}\newline 0 &\mbox{otherwise} \end{cases}
        \end{align}
    where $\theta > 0$. Derive the Cramer-Rao lower bound for the variance of any unbiased estimator of $\theta$. Also prove that $T = \frac{1}{n} \sum_{i=1}^{n} X_{i}$ is the minimum variance unbiased estimator of $\theta$. [Solution]({{ "/notes/probability/chapters/exercises/a_crlb_exp.html" | relative_url }})

1.  **MLE and Proving Sufficient Statistic**

    Suppose $X_{1}, X_{2}, \ldots, X_{n}$ are from a distribution with the following distribution
    \begin{align}
            f_{X}(x) = \begin{cases} \frac{2x}{\lambda} \exp \big(-\frac{x^{2}}{\lambda} \big) &\mbox{if $x > 0$}\newline 0 &\mbox{otherwise} \end{cases}
        \end{align}
    Find the MLE estimate of $\lambda$ and show that it is unbiased and a sufficient statistic of $\lambda$.
    [Solution]({{ "/notes/probability/chapters/exercises/a_mle_sufficient_statistic.html" | relative_url }})

1.  **Bayes Estimator for Normal Distribution**

    Suppose $X_{1}, X_{2}, \ldots, X_{n}$ are from a normal distribution with unknown mean $\theta$ and known variance $\sigma_{0}^{2}$, and suppose the mean has a prior normal ditribution with mean $\mu$ and variance $\sigma^{2}$. Calculate the Bayes estimator for the mean $\theta$.
    [Solution]({{ "/notes/probability/chapters/exercises/a_bayesnormal.html" | relative_url }})

1.  **LMS Estimate**

    Given the prior $f_{\Theta \vert (\theta)}$, uniform in $[4,10]$, and $f_{X \vert \Theta}(x \vert \theta)$ is uniform in $\[\theta-1, \theta+1 \]$, estimate the posterior of $\theta$. [Solution]({{ "/notes/probability/chapters/exercises/a_lmsestimate.html" | relative_url }})

1.  **Probability Convergence**

    Let $X$ be uniformly distributed between $[-1,1]$. Let $X_{1}, X_{2},\ldots,X_{n}$ be independently and identically distributed with the same distribution as $X$. Find whether the following sequences are convergent in probability and also find the limit.

    1.  $X_{i}$

    2.  $Y_{i} = X_{i}/i$

    3.  $Z_{i} = (X_{i})^{i}$

    [Solution]({{ "/notes/probability/chapters/exercises/a_convergence.html" | relative_url }})

1.  **Age of Smokers vs Non Smokers**

    One often hears that the death rate of a person who smokes is, at each age, twice that of a nonsmoker. What does this mean? Does it mean that a nonsmoker has twice the probability of surviving a given number of years as does a smoker of the same age? [Solution]({{ "/notes/probability/chapters/exercises/a_lifesmoker.html" | relative_url }})

1.  **Simple Hypothesis Test**

    Let $X_{1}, \ldots, X_{10}$ be a random sample of heights from a $\mathcal{N}(\mu, 20^{2})$ distribution where we want to test the hypothesis $H_{0}: \mu = 30$ vs $H_{a}: \mu \neq 30$. For a significance level of $0.05$ and mean of the $10$ samples as $27$, determine if $H_{0}$ is accepted or not. [Solution]({{ "/notes/probability/chapters/exercises/a_hypothesis_test.html" | relative_url }})

1.  **Most Powerful Test for Variance**

    Let $X_{1}, \ldots, X_{5}$ be a random sample from a $\mathcal{N}(2, \sigma^{2})$ distribution where $\sigma^{2}$ is unknown. Derive the most powerful test of size $\alpha = 0.05$ for testing $H_{0}: \sigma^{2} = 4$ against $H_{1}: \sigma^{2} = 1$. [Solution]({{ "/notes/probability/chapters/exercises/a_most_powerful_test.html" | relative_url }})
