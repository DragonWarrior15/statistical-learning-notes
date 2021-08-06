---
title: "Differential Equations"
---

# Ordinary Differential Equations
Let $y(x)$ denote a function of $x$. A differential equation is a function that captures the relations between the derivatives of $y$ and the functions of $x$. An ordinary differential equation will contain $y$ as only the function of $x$ (independent variable). An equation containing the partial derivatives will be call a _partial differential equation_.

\begin{align}
    F(x, y^{1}, y^{2}, \ldots, y^{(n)}) = 0
\end{align}

where $y^{1}, y^{2}, \ldots, y^{(n)}$ denote the various derivates of $y$.

The **order** of a differential equation is the highest derivative in the equation. For the above case, the order will be $n$ assuming that a term containing $y^{(n)}$ exists in the equation with non-zero coefficient.

Similarly, the **degree** of a differential equation is the power to which the highest derivative is raised in the equation. Suppose a term $(y^{(n)})^{m}$ existed in the equation where $n$ is the order, then the degree will be $m$.

A differential equation is linear if it can be expressed as follows
\begin{align}
    L(y(x)) &= L(y^{1}, y^{2}, \ldots, y^{(n)}) = f(x)\newline
    a_{0}(x)y^{(n)}+ a_{1}(x)y^{(n-1)} + \cdots + a_{n}(x)y &= f(x)
\end{align}

where $L$ is a linear transformation from the space of functions that are derivatives, to the space of functions. The coefficients in this linear combination can themselves be functions of $x$, with $a_{0}(x) \neq 0$.

A simple example of DE in real life is the motion of a pendumlum modeled as
\begin{align}
    \frac{d^{2}\theta}{dt^{2}} + \frac{g}{l}\sin\theta
\end{align}

## Particular solution
Suppose we have a differential equation of the form $y^{1} = f(x,y)$ and the solution to this equation is $y = g(x) + c$, where $c$ is an arbitrary constant. Then, this solution is called a **general solution** since it represents a family of curves. The solution can also be of the form $y = cg(x)$, or anything else depending on the differential equation itself.

If we choose a specific value of the constant, we get a **particular solution** to the problem. The constant can be determined using an initial condition like $y(x_{0}) = y_{0}$. An ODE together with the initial condition is called an **initial value problem**.

### Note:
* We will be using the notations $y^{1}$, $y^{(1)}$ and $y^{\prime}$ interchangeably over the next sections
* Reference: [Advanced Engineering Mathematics](https://www.amazon.in/Advanced-Engineering-Mathematics-10ed-ISV/dp/8126554231)
