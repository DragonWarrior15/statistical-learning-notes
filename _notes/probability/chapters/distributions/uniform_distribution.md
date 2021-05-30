---
title: "Continuous Uniform Random Variable"
---

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
