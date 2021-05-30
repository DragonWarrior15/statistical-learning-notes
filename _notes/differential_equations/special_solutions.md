---
title: "Special Solutions to ODE"
---

## Special Solutions to ODE
### Separable ODE
An ODE of the form
\begin{align}
    M(x) + N(y)y^{1} = 0
\end{align}

is called a separable ODE since the functions of $x$ and $y$ are separated here. Integrating by multiplying with $dx$ and using the knowledge $dy = y^{1}dx$

\begin{align}
    \int M(x)dx + \int N(y)y^{1}dx &= c\newline
    \int M(x)dx + \int N(y)dy &= c
\end{align}

### Homogenous ODE
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

which is a separable equation.

### Exact ODE
An ODE
\begin{align}
    M(x, y) + N(x, y)\frac{dy}{dx} = 0
\end{align}
is exact if there exists a function $u(x,y)$ such that
\begin{align}
    \frac{\partial u}{\partial x} &= M\newline
    \frac{\partial u}{\partial y} &= N\newline
    du &= \frac{\partial u}{\partial x}dx + \frac{\partial u}{\partial y}dy\newline
    \implies du = Mdx + Ndy &= 0
\end{align}

Hence, the solution is simply $u(x,y) = c$ after integrating the above equation.

But, instead of guessing $u(x,y)$, we can use the following steps
1. Integrate $\frac{\partial u}{\partial x} = M(x,y)$ to get
    \begin{align}
        u(x,y) = \int M(x,y) dx + k(y)
    \end{align}
    where $k(y)$ is the constant of integration.
2. Differentiate with respect to $y$
    \begin{align}
        \frac{\partial u}{\partial y} &= \frac{\partial}{\partial y} \int M(x,y) dx + k'(y) = N(x,y)
    \end{align}
    since the ODE is exact.
3.  Determine $k(y)$ from this equation to subsequently find $u(x,y)$ completely.

#### Closed Form
The differential form $M(x,y)dx + N(x,y)dy$ is called closed if
\begin{align}
    \frac{\partial M}{\partial y} &= \frac{\partial N}{\partial x}\newline
    M_{y} &= N_{x}
\end{align}

If $M,N$ are continuous on a region $D$, then if $D$ is convex, any closed form is exact. We can then find the solution $u(x,y)$ using the steps discussed earlier.

### Integrating Factors
Suppose the ODE
\begin{align}
    M(x,y) + N(x,y)\frac{dy}{dx}
\end{align}
is not exact, then we find factors $\mu$ such that the equation
\begin{align}
    \mu M(x,y) + \mu N(x,y)\frac{dy}{dx}
\end{align}
is exact, i.e., $(\mu(x,y) M(x,y))\_{y} = \mu(x,y) N(x,y)\_{x}$. In practice, we can start by finding a function $\mu$ that is dependent on a single variable, say $x$. In that case, $\mu_{y}$ will be zero.

