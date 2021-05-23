---
title: "Sample Mean"
---

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

