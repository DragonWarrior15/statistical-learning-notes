---
title: "Special Solutions to First Order ODE"
---

## Special Solutions to First Order ODE
### Separable ODE
An ODE of the form
\begin{align}
    M(x) + N(y)y^{\prime} = 0
\end{align}

is called a **separable** ODE since the functions of $x$ and $y$ are separated here. Integrating by multiplying with $dx$ and using the knowledge $dy = y^{\prime}dx$

\begin{align}
    \int M(x)dx + \int N(y)y^{\prime}dx &= c\newline
    \int M(x)dx + \int N(y)dy &= c
\end{align}

#### Homogenous ODE
(These equations are reducible to a separable form)

A homogenous function is of the form
\begin{align}
    f(tx_{1}, tx_{2}, \ldots, tx_{n}) = t^{d}f(x_{1}, x_{2}, \ldots, x_{n})
\end{align}

for some $d \in \mathbb{Z}$ called the degree of $f(x_{1}, \ldots x_{n})$. A first order ODE
\begin{align}
    M(x, y) + N(x, y)\frac{dy}{dx} = 0
\end{align}
is called homogenous if $M$ and $N$ are both homogenous of equal degree. We can solve such equations by substituting $y = xv$
\begin{align}
    \frac{dy}{dx} &= x\frac{dv}{dx} + v\newline
    M(x, xv) + N(x, xv)\bigg( x\frac{dv}{dx} + v \bigg) &= 0\newline
    x^{d}M(1, v) + x^{d}N(1, v)\bigg( x\frac{dv}{dx} + v \bigg) &= 0\newline
    M(1, v) + xN(1, v)\frac{dv}{dx} + vN(1,v) &= 0\newline
    \frac{dx}{x} + \frac{N(1,v)}{M(1,v) + N(1,v)v} &= 0
\end{align}

which is a **separable** equation.

As a common case, consider the following equation and the substituition $y=xv$
\begin{align}
    y^{\prime} &= f(\frac{y}{x})\newline
    y &= xv \implies \frac{dy}{dx} = v + x\frac{dv}{dx}\newline
    v + x\frac{dv}{dx} &= f(v)\newline
    \implies \frac{dv}{f(v) - v} &= \frac{dx}{x}
\end{align}

which is a separable equation as shown above.

### Exact ODE
The derivative of a function can be expressed as a sum of its partial derivatives in the following way
\begin{align}
    u &= f(x, y)\newline
    du &= \frac{\partial u}{\partial x}dx + \frac{\partial u}{\partial y}dy
\end{align}

An ODE
\begin{align}
    M(x, y)dx + N(x, y)dy = 0
\end{align}
is exact if there exists a function $u(x,y)$ such that
\begin{align}
    \frac{\partial u}{\partial x} &= u_{x} = M\newline
    \frac{\partial u}{\partial y} &= u_{y} = N\newline
    du &= \frac{\partial u}{\partial x}dx + \frac{\partial u}{\partial y}dy\newline
    \implies du &= Mdx + Ndy = 0
\end{align}

Hence, the solution is simply $u(x,y) = c$ after integrating the above equation.

For doing all of this, we make the assumption that the function is continuous and differentiable (for the partial derivatives). Hence, to check whether we have an exact ODE, the following check can be done
\begin{align}
    M &= \frac{\partial u}{\partial x} \; N = \frac{\partial u}{\partial y}\newline
    \implies \frac{\partial M}{\partial y} &= M_{y} = \frac{\partial^{2} u}{\partial y \partial x}\newline
    \text{and}\; \frac{\partial N}{\partial x} &= N_{x} = \frac{\partial^{2} u}{\partial x \partial y}\newline
    \implies M_{y} &= N_{x}
\end{align}

But, instead of guessing $u(x,y)$, we can use the following steps
1. Integrate $\frac{\partial u}{\partial x} = M(x,y)$ to get
    \begin{align}
        u(x,y) = \int M(x,y) dx + k(y)
    \end{align}
    where $k(y)$ is the constant of integration.
2. Differentiate with respect to $y$
    \begin{align}
        \frac{\partial u}{\partial y} &= \frac{\partial}{\partial y} \int M(x,y) dx + k^{\prime}(y) = N(x,y)
    \end{align}
    since the ODE is exact.
3.  Determine $k(y)$ from this equation to subsequently find $u(x,y)$ completely.

#### Integrating Factors
Suppose the ODE
\begin{align}
    M(x,y)dx + N(x,y)dy = 0
\end{align}
is not exact. One way to solve this ODE is to make it exact by finding a factor $\mu(x, y)$ such that the equation
\begin{align}
    \mu M(x,y)dx + \mu N(x,y)dy = 0
\end{align}
is exact, i.e., $(\mu(x,y) M(x,y))\_{y} = (\mu(x,y) N(x,y))\_{x}$. This function or factor $\mu$ is called **Integrating Factor**.

Using this fact,
\begin{align}
    \mu M_{y} + \mu_{y} M = \mu N_{x} + \mu_{x} N
\end{align}

In practice this can be difficult to solve directly. We can start by making a simplifying assumption that $\mu$ is dependent on a single variable, say $x$. In that case, $\mu_{y}$ will be zero. Substituiting,
\begin{align}
    \mu_{x} &= \frac{d\mu}{dx}\newline
    \mu M_{y} &= \mu N_{x} + \mu_{x} N\newline
    \frac{\mu_{x}}{\mu} &= \frac{M_{y} - N_{x}}{N}\newline
    \ln (\mu) &= \int \frac{M_{y} - N_{x}}{N} dx\newline
    \mu &= \exp \left( \int \frac{M_{y} - N_{x}}{N} dx \right)\newline
    \implies \frac{M_{y} - N_{x}}{N} &= \text{function of $x$ only}
\end{align}

Similarly, if $\mu$ is a function of $y$ only,
\begin{align}
    \mu_{y} &= \frac{d\mu}{dy}\newline
    \mu &= \exp \left( \int \frac{N_{x} - M_{y}}{M} dy \right)\newline
    \implies \frac{N_{x} - M_{y}}{M} &= \text{function of $y$ only}
\end{align}

In both the formulae, we take the difference of the terms $M_{y}$ and $N_{x}$. If the two terms are equal, we have an exact ODE, and the IF will be 1. The denominator in the formula for IF is $N$ if IF is a function of $x$ ($N_{x}$ is used in the check) and $M$ if IF is a function of $y$ ($M_{y}$ is used in the check).

Further, the IF should be a function of only a single variable, and so should be the terms derived above for the formulat of IF. If that does not hold, our assumption is wrong. We need to do the check for both the assumptions that $\mu$ is a function of $x$ or $y$.
