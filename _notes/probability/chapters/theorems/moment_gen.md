---
title: "Moment Generating Function"
---

## Moment Generating Function

Moment generating function (mgf) is defined as the following for all values of $t \in (-h, h)$ where $h > 0$ (important thing is that the function exists at $t = 0$)
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
