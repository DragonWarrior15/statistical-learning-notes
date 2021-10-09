---
title: "Moment Generating Function"
---

## Moment Generating Function

Moment generating function (mgf) is defined as the following for all values of $t \in (-h, h)$ where $h > 0$ (important thing is that the function exists at $t = 0$)
\begin{align}
        \phi (t) = E[e^{tX}] = \begin{cases} \sum_{x} e^{tx} p_{X}(x) &\mbox{for discrete case}\newline
        \int_{-\infty}^{\infty} e^{tx} f_{X}(x) &\mbox{for continuous case} \end{cases}
    \end{align}
if it exists. This function is called the moment generating function because all the moments of the random variable $X$ can be obtained by differentiating the function $\phi(t)$.


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

Another handy property of the mgf is that $E[e^{ktX}]$ where $k$ is a constant is $E[e^{(kt)X}] = \phi(kt)$.

### MGF for Multivariate Distributions
Let $\mathbf{X} = (X_{1}, \ldots, X_{n})$ be a multivariate distribution. Then the mgf is
\begin{align}
    E[e^{\mathbf{t}^{T}\mathbf{X}}] &= E[e^{t_{1}X_{1} + \cdots + t_{n}X_{n}}] = E[e^{\sum_{i=1}^{n}t_{i}X_{i}}]
\end{align}

For further discussion, let's assume $\mathbf{X} = (X_{1}, X_{2})$ (although the below derivations work with multivariate distributions in a similar manner). To get the moments, we calculate the partial derivatives of $\phi(t)$.
\begin{align}
    \frac{\partial E[e^{t_{1}X_{1} + t_{2}X_{2}}]}{\partial t_{1}} &= E[X_{1}e^{t_{1}X_{1} + t_{2}X_{2}}]\newline
    \text{Continuing} \quad \frac{\partial^{k} E[e^{t_{1}X_{1} + t_{2}X_{2}}]}{\partial t_{1}^{k}} &= E[X_{1}^{k}e^{t_{1}X_{1} + t_{2}X_{2}}]\newline
    \frac{\partial^{m} E[e^{t_{1}X_{1} + t_{2}X_{2}}]}{\partial t_{2}^{m}} &= E[X_{2}^{m}e^{t_{1}X_{1} + t_{2}X_{2}}]\newline
    \frac{\partial^{k+m} E[e^{t_{1}X_{1} + t_{2}X_{2}}]}{\partial t_{1}^{k}\partial t_{2}^{m}} &= E[X_{1}^{k}X_{2}^{m}e^{t_{1}X_{1} + t_{2}X_{2}}]\newline
    \implies \left.\frac{\partial^{k+m} \phi(t_{1}, t_{2})}{\partial t_{1}^{k}\partial t_{2}^{m}} \right\rvert_{t_{1}=0, t_{2}=0} &=  E[X_{1}^{k}X_{2}^{m}]\newline
\end{align}

Similar to how we obtained moments in the univariate case. The following immediately follow from the last expression ($m$ and $k$ can be zero as well in that expression meaning we dont take any derivatives)
\begin{align}
    \mu_{1} &= E[X_{1}] = \left.\frac{\partial \phi(t_{1}, t_{2})}{\partial t_{1}}\right\rvert_{t_{1}=0, t_{2}=0}\newline
    \mu_{2} &= E[X_{2}] = \left.\frac{\partial \phi(t_{1}, t_{2})}{\partial t_{2}}\right\rvert_{t_{1}=0, t_{2}=0}\newline
    \sigma_{1}^{2} &= E[X_{1}^{2}] - E[X_{1}]^{2} = \left.\frac{\partial^{2} \phi(t_{1}, t_{2})}{\partial t_{1}^{2}}\right\rvert_{t_{1}=0, t_{2}=0} - \mu_{1}^{2}\newline
    \sigma_{12} &= E[X_{1}X_{2}] - E[X_{1}]E[X_{2}] = \left.\frac{\partial^{2} \phi(t_{1}, t_{2})}{\partial t_{1}\partial t_{2}} \right\rvert_{t_{1}=0, t_{2}=0} - \mu_{1}\mu_{2}
\end{align}

### MGF for Sum of Independent RV

An important property is in the context of sum of two or more random variables. The **moment generating function of sum of independent random variables is simply the product of the moment generating functions of the individual random variables**
\begin{align}
        \phi_{X+Y}(t) &= E[e^{t(X+Y)}]\newline
        &= E[e^{tX} e^{tY}]\newline
        &= E[e^{tX}] E[e^{tY}]\newline
        \phi_{X+Y}(t) &= \phi_{X}(t) \phi_{Y}(t) \quad \text{for independent random variables}
    \end{align}

In several cases, the mgf can be useful for calculating the distribution of say the sum of independent variables. See exercises for an illustration.
