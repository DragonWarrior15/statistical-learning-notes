---
title: "Series Solutions of ODEs"
---

## Series Solutions of ODEs
Here we look at some methods that are useful for solving ODEs with variable coefficients.

### Power Series Method
Here we assume the solution to be a polynomial (a power series) and try to determine the coefficients of the same. We try to compare this series to expansions of common functions to determine the final solution form.

Common series expansions
\begin{align}
    \frac{1}{1 - x} &= 1 + x + x^{2} + \cdots\newline
    e^{x} &= 1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + \cdots\newline
    \sin x &= 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!}\newline
    \cos x &= x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!}
\end{align}

We assume the solution to be
\begin{align}
    y = a_{0} + a_{1}x + a_{2}x^{2} + a_{3}x^{3} + \cdots
\end{align}
and substitute in the equation. Further, we will also insert the power series expansions of the coefficients. This way, the entire equation only contains different powers of $x$ (in the form of power series). Then we can find the values of the coefficients in our solution by equating the coefficients of corresponding powers of $x$.

Refer to exercises for a worked out example.
