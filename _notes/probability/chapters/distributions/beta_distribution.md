---
title: "Beta Distribution"
---

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
