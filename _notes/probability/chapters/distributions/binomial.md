---
title: "Bernoulli and Binomial Random Variable"
---

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

### Sum of Binomial Random Variables

Suppose we have $k$ independent variables $X_{i} \sim binmomial(n_{i},p)$, then their sum also has a binomial distribution
\begin{align}
        X_{1} + \cdots + X_{k} \sim binomial(n_{1} + \cdots + n_{k}, p)
    \end{align}
which follows from the fact that the sum of the random variables represents an experiment with $n_{1} + \cdots + n_{k}$ trials where the probability of success of any trial still remains the same at $p$. The same can also be derived from the moment generating function.
