---
title: "Special Solutions to First Order ODE"
---

## Special Solutions to First Order ODE
### Separable ODE
An ODE of the form
\begin{align}
    M(x) + N(y)\diffone{y} = 0
\end{align}

is called a **separable** ODE since the functions of $x$ and $y$ are separated here. Integrating by multiplying with $dx$ and using the knowledge $dy = \diffone{y}dx$

\begin{align}
    \int M(x)dx + \int N(y)\diffone{y}dx &= c\newline
    \int M(x)dx + \int N(y)dy &= c
\end{align}

The constant $c$ can be determined using an initial condition (and will decide the direction of $y$).

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
    \diffone{y} &= f(\frac{y}{x})\newline
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
        \frac{\partial u}{\partial y} &= \frac{\partial}{\partial y} \int M(x,y) dx + \diffone{k}(y) = N(x,y)
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
    \mu &= \exp \roundbr{\int \frac{M_{y} - N_{x}}{N} dx}\newline
    \implies \frac{M_{y} - N_{x}}{N} &= \text{function of $x$ only}
\end{align}

Similarly, if $\mu$ is a function of $y$ only,
\begin{align}
    \mu_{y} &= \frac{d\mu}{dy}\newline
    \mu &= \exp \roundbr{\int \frac{N_{x} - M_{y}}{M} dy}\newline
    \implies \frac{N_{x} - M_{y}}{M} &= \text{function of $y$ only}
\end{align}

In both the formulae, we take the difference of the terms $M_{y}$ and $N_{x}$. If the two terms are equal, we have an exact ODE, and the IF will be 1. The denominator in the formula for IF is $N$ if IF is a function of $x$ ($N_{x}$ is used in the check) and $M$ if IF is a function of $y$ ($M_{y}$ is used in the check).

Further, the IF should be a function of only a single variable, and so should be the terms derived above for the formulat of IF. If that does not hold, our assumption is wrong. We need to do the check for both the assumptions that $\mu$ is a function of $x$ or $y$.

#### Another common version of IF
For equation of the form
\begin{align}
    \frac{dy}{dx} + P(x)y = Q(x)
\end{align}

The intgrating factor is
\begin{align}
    IF &= \exp\roundbr{\int P(x)dx}\newline
    \implies e^{\int P(x)dx}\frac{dy}{dx} + e^{\int P(x)dx}P(x)y &= e^{\int P(x)dx}Q(x)\newline
    \frac{d}{dx}\roundbr{e^{\int P(x)dx}y} &= e^{\int P(x)dx}Q(x)
\end{align}

which is readily solvable if the right hand side integral can be evaluated without much trouble.

### Linear ODE
Any ODE that is expresible in the form
\begin{align}
    \diffone{y} + p(x)y = r(x)
\end{align}
is called a **linear ODE**. Both $p(x)$ and $r(x)$ are functions of $x$. Such equations are common in engineering, where $r(x)$ is often called the _input_ and $y$ the _output_.

If $\diffone{y}$ has a coefficient $f(x)$, it can be converted to the standard form by dividing throughout by $f(x)$.

if $r(x) = 0$, then the equation is termed as a **linear homogenous** equation. Otherwise its called linear non-homogenous equation.

If the input or $r(x)$ is zero everywhere, the equation is simple to solve due to a separable form.
\begin{align}
    \diffone{y} + p(x)y &= 0\newline
    \frac{\diffone{y}}{y} &= -p(x)\newline
    y &= c \exp \roundbr{-\int p(x) dx}
\end{align}

If the input or $r(x)$ is not zero everywhere, we can use an integrating factor $\exp \roundbr{\int p(x) dx}$
\begin{align}
    \diffone{y}e^{\int p(x) dx} + p(x)e^{\int p(x) dx} y &= r(x)e^{\int p(x) dx}\newline
    d \roundbr{y e^{\int p(x) dx}} &= r(x)e^{\int p(x) dx}\newline
    y &= e^{-\int p(x) dx} \roundbr{\int r(x)e^{\int p(x) dx} dx + c}
\end{align}

#### Bernoulli Equation
A differential equation of the form
\begin{align}
    \diffone{y} + p(x)y = g(x) y^{a}
\end{align}
where $a$ is any real number is called **Bernoulli Equation**. This is a non linear equation seen frequently in various applications, and can be reduced to a linear form by making the substituition $y^{1-a} = v$

\begin{align}
    (1-a)y^{-a}\diffone{y} &= \diffone{v}\newline
    \diffone{y} &= \frac{1}{1-a}y^{a}\diffone{v}\newline
    \implies \frac{1}{1-a}y^{a}\diffone{v} + p(x)y &= g(x) y^{a}\newline
    \frac{1}{1-a}\diffone{v} + p(x)y^{1-a} &= g(x)\newline
    \implies \diffone{v} + (1-a)p(x)v &= (1-a)g(x)\newline
\end{align}

which is a linear ODE and can be solved by introducing the integrating factor $\exp \roundbr{\int (1-a)p(x) dx}$.

### Existence of solution in IVP
A given IVP can have no solution, exactly one solution or more than one solutions.
* $\detm{\diffone{y}} + \detm{y} = 0$, $y(0) = 1$ has no solution since the only solution to ODE is $y = 0$.
* $\diffone{y} = 2x$, $y(0) = 1$ has a single unique solution $y = x^{2} + 1$.
* $x\diffone{y} = y - 1$, $y(0) = 1$ has infinite solutions $y = 1 + cx$.

**Uniqueness Theorem** and **Existence Theorem** help check whether a given IVP has a solution at all, or if it has exactly one solution.

**Existence Theorem**
Consider the IVP $y = f(x,y)$ and $y(x_{0}) = y_{0}$. Suppose that $f(x,y)$ is continuous in the rectangular region $R$ given by $\vert x - x_{0} \vert < a$ and $\vert y - y_{0} \vert < b$ and is bounded in $R$ by a constant $K$ ($f(x,y) \leq K$ for $x,y \in R$).

The IVP will have at least one solution in the rectangular region $R$. The solution exists for at least all $x$ in the subinterval $\vert x - x_{0} \vert < \alpha$ where $\alpha$ is the minimum of $a, b/K$.

**Uniqueness Theorem**
If we add one more condition to the above IVP that the partial derivative with respect to y $f_{y}(x,y)$ is also bounded in the region by $M$, i.e., $f_{y}(x,y) \leq M$ for $x,y \in R$. Then, the IVP has at most one solution. By the existence theorem, the IVP will have exactly one solution in the subinterval $\vert x - x_{0} \vert < \alpha$
