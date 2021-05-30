---
title: "Differential Equations"
---

# Ordinary Differential Equations
Let $y(x)$ denote a function of $x$. A differential equation is a function that captures the relations between the derivatives of $y$ and the functions of $x$.

\begin{align}
    F(x, y^{1}, y^{2}, \ldots, y^{(n)}) = 0
\end{align}

where $y^{1}, y^{2}, \ldots, y^{(n)}$ denote the various derivates of $y$.

The order of a differential equation is the degree of the highest derivative in the equation. For the above case, the order will be $n$ assumuing that a term containing $y^{(n)}$ exists in the equation.

A differential equation is linear if it can be expressed as follows
\begin{align}
    L(y(x)) &= L(y^{1}, y^{2}, \ldots, y^{(n)}) = f(x)\newline
    a_{0}(x)y^{(n)}+ a_{1}(x)y^{(n-1)} + \cdots + a_{n}(x)y &= f(x)
\end{align}

where $L$ is a linear transformation from the space of functions that are derivatives, to the space of functions. The coefficients part of this linear combination can themselves be functions of $x$, with $a_{0}(x) \neq 0$.

A very simple example of DE in real life is the motion of a pendumlum modelled as
\begin{align}
    \frac{d^{2}\theta}{dt^{2}} + \frac{g}{l}\sin\theta
\end{align}


