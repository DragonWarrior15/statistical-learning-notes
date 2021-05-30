---
title: "Convergence in Probability"
---

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
