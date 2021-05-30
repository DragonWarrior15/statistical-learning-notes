---
title: "Chi-Square Distribution"
---

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

We say that a Gamma distributed random variable with $\lambda = 1/2$ and $\alpha$ can be considered equivalent to a $\chi^{2}\_{2\alpha}$ variable. Here, $\lambda$ is contrained to be $1/2$. By transforming the variables appropriately, we can extend the idea to a sum of exponentially distributed random variables.


Consider $n$ independent and identically exponentially distributed random variables $X_{i}$ with parameter $\lambda$. Consider for any of those random variables $X_{i}$,
\begin{align}
        Y &= 2\lambda X\newline
        F_{Y}(y) &= P(Y \leq y) = P(X <\leq \frac{y}{2\lambda})\newline
        &= F_{X}(\frac{y}{2\lambda}) = 1 - \exp \bigg( \frac{y}{2} \bigg)\newline
        f_{Y}(y) &= \frac{d}{dy} 1 - \exp \bigg( -\frac{y}{2} \bigg)\newline
        &= \frac{1}{2}\exp \bigg( \frac{y}{2} \bigg)\newline
        &= Exp(\frac{1}{2})
    \end{align}
i.e., $\frac{2}{\lambda}Exp(\lambda) \sim Exp(\frac{1}{2})$. Now, consider the sum of these transformed random variables
\begin{align}
        \frac{2}{\lambda}\bigg( X_{1} + \cdots X_{n} \bigg) &\sim Gamma(n, 1/2) \sim \chi_{2n}^{2}
    \end{align}

Hence, we can convert the sum of $n$ exponentially distributed random variables with parameter $\lambda$, to a $\chi^{2}\_{n}$ variable by multiplying the individual variables by $2/\lambda$.

### Mean and Variance

Since the distribution of a chi-square variable is identical to a $Gamma(n/2, 1/2)$ distribution,
\begin{align}
        E[X] &= n\newline
        Var(x) &= 2n
    \end{align}
