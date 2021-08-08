---
title: "Second Order Linear ODEs"
---

### Second Order Linear ODE
A second order linear ODE is of the form
\begin{align}
    \difftwo{y} + p(x)\diffone{y} + q(x)y = r(x)
\end{align}

Any second order ODE not expressible in this form will be non-linear.

* If $\difftwo{y}$ also has a coefficient $f(x)$, we can convert it to the standard form by dividing throughout by $f(x)$.
* Similar to the first order linear ODEs, if $r(x) = 0$, the equation is homogenous, and non-homogenous otherwise.
* The functions of $x$: $p(x)$ and $q(x)$ are also called the **coefficients** of the ODE.

#### Superposition Principle
**For any _homogenous_ second order linear ODE, any linear combination of two solutions is also a solution.** In particular, this means that sums, and sums after multiplying with constants are also solutions of the ODE. This result is only valid for _linear homogenous equations_ and not non-homogenous ones.

This can be verified by first assuming two solutions $y_{1}$ and $y_{2}$, and then substituiting a linear combination $c_{1}y_{1} + c_{2}y_{2}$ in the same homogenous equation. This linear combination is called the _general solution_ to the ODE.

Hence, while evaluating $y_{1}$ and $y_{2}$, we will not keep any constants, since they will automatically appear when preparing the general solution.

The two solutions $y_{1}$ and $y_{2}$ form the **basis** or a **fundamental system** of solutions of the ODE, and must be _linearly independent_. That is, the two functions must satisfy
\begin{align}
    k_{1}y_{1} + k_{2}y_{2} = 0 \forall x \in I \implies k_{1} = 0 \;\text{and}\; k_{2} = 0
\end{align}
where $I$ is the solution interval under consideration.

If the solutions were linearly dependent, there would be a non-trivial solution for the above equation, implying that the two solutions are linearly dependent.
The two functions $y_{1}$ and $y_{2}$ are called the basis as the general solution is the set of all functions that are linear combinations of the two bases.

The linear independence of two solutions can also be verified by checking that their ratio is not a constant (but a function of the independent variable).

#### IVP
Similar to linear ODEs, second order linear homogenous equations have an IVP that can be stated with two initial values, one on the function $y$ itself, and the other on its derivative: $y(x_{0}) = K_{0}$ and $\diffone{y}(x_{0}) = K_{1}$. The two conditions can be used to determine the two constants in a genral solution: $y = c_{1}y_{1} + c_{2}y_{2}$.

The unique solution will pass through the point $(x_{0}, K_{0})$ with the tangent $K_{1}$, and is called a _particular solution_.

#### Reduction of Order
This method for second order linear homogenous equations relies on already knowing one solution of the equation. Then, we determine the second using the fact that the two solutions will be linearly independent.

Suppose $y_{1}$ is one solution, then $y_{2} = uy_{1}$ where $u$ is a function of $x$ (and not a constant), is the second solution. Substituiting in our ODE,
\begin{align}
    \difftwo{y} + p(x)\diffone{y} + q(x)y &= 0\newline
    \difftwo{y_{1}} + p(x)\diffone{y_{1}} + q(x)y_{1} &= 0\newline
    \difftwo{y_{2}} + p(x)\diffone{y_{2}} + q(x)y_{2} &= 0\newline
    \implies \difftwo{(uy_{1})} + p(x)\diffone{(uy_{1})} + q(x)(uy_{1}) &= 0\newline
    \diffone{(uy_{1})} &= \diffone{u}y_{1} + u\diffone{y_{1}}\newline
    \difftwo{(uy_{1})} &= \difftwo{u}y_{1} + 2\diffone{u}\diffone{y_{1}} + u\difftwo{y_{1}}\newline
    \implies \difftwo{u}y_{1} + 2\diffone{u}\diffone{y_{1}} + u\difftwo{y_{1}} + p(x)(\diffone{u}y_{1} + u\diffone{y_{1}}) + q(x)uy_{1} &= 0\newline
    \text{Rearranging,}\: \difftwo{u}y_{1} + \diffone{u} \roundbr{2\diffone{y_{1}} + p(x)y_{1}} + u \roundbr{\difftwo{y_{1}} + p(x)\diffone{y_{1}} + q(x)y_{1}} = 0\newline
    \implies \difftwo{u}y_{1} + \diffone{u} \roundbr{2\diffone{y_{1}} + p(x)y_{1}} = 0\newline
\end{align}

The last equation follows since $y_{1}$ is a solution. Rearranging,
\begin{align}
    \frac{\difftwo{u}}{\diffone{u}} &= -\frac{2\diffone{y_{1}} + p(x)y_{1}}{y_{1}} = -2\frac{\diffone{y_{1}}}{y_{1}} + p(x)\newline
    \implies \int \frac{d\roundbr{\diffone{u}}}{\diffone{u}} &= -2\int \frac{d\roundbr{y_{1}}}{y_{1}} - \int p(x) dx\newline
    \ln \diffone{u} &= -2 \ln y_{1} - \int p(x) dx\newline
    \diffone{u} &= \frac{e^{-\int p(x) dx}}{y_{1}^{2}}\newline
    u &= \int \frac{e^{-\int p(x) dx}}{y_{1}^{2}} dx
\end{align}

which must not be a constant since $y_{1}$ and $y_{2}$ are linearly independent. Now, $y_{2}$ is simply $uy_{1}$.

#### Second Order Linear ODE with Constant Coefficients
We consider equations of the form $\difftwo{y} + a\diffone{y} + by = 0$.

We know that the first order linear equation $\diffone{y} + ay = 0$ has a solution of the form $e^{-ax}$. We can try to substitute a similar solution $e^{\lambda x}$ in the equation above to get
\begin{align}
    e^{\lambda x}\roundbr{\lambda^{2} + a\lambda + b} = 0
\end{align}

Since the exponent is non-zero, the second part of the above equation must be zero. This equation is called the **characteristic equation**. This is a quadratic in $\lambda$ and the roots are
\begin{align}
    \lambda = -\frac{-a \pm \sqrt{a^{2} - 4b}}{2}
\end{align}
has the following three possibilities for the roots:
* **The two roots are real and distinct**
    which happens when $b^{2} - 4a > 0$. Let the two roots be $\lambda_{1}$ and $\lambda_{2}$. Then, the solution of the ODE is
    \begin{align}
        y = c_{1}e^{\lambda_{1} x} + c_{2}e^{\lambda_{2} x}
    \end{align}
* **The two roots are real and equal**
    which happens when $b^{2} - 4a = 0$. Let the root be $\lambda$. We also know that $\lambda = -a/2$. The first solution is $y_{1} = e^{\lambda x}$. The second solution cannot be the same since the ratio of the two solutions must be a function of $x$. Assuming $y_{2} = u(x)y_{1}$ and using reduction of order method,
    \begin{align}
        u &= \int \frac{e^{-\int p(x) dx}}{y_{1}^{2}} dx = \int \frac{e^{-\int a dx}}{\roundbr{e^{\lambda x}}}^{2} dx\newline
        &= \int \frac{e^{-ax}}{e^{2\lambda x}} dx = \int \frac{e^{-ax}}{e^{-ax}} dx\newline
        &= \int 1 dx = x\newline
        y_{2} &= uy_{1} = xe^{x}
    \end{align}
    Clearly, $u$ is not a constant. Hence, the general solution can be written as
    \begin{align}
        y = c_{1}xe^{x} + c_{2}e^{x} = e^{x}(c_{1}x + c_{2})
    \end{align}
* **The two roots are complex**
    Recall Euler's theorem
    \begin{align}
        e^{ix} = \cos x + i\sin x
    \end{align}
    The two complex roots of the quadratic equation will be
    \begin{align}
        \lambda = -\frac{-a \pm i\sqrt{4b - a^{2}}}{2}
    \end{align}
    Let $\sqrt{4b - a^{2}}/2 = \omega$. Similar to the real and distinct roots case, we can write the two solutions as
    \begin{align}
        y_{1} &= e^{\lambda_{1}x} = e^{-ax/2}\roundbr{\cos \omega x + i\sin \omega x}\newline
        y_{2} &= e^{\lambda_{2}x} = e^{-ax/2}\roundbr{\cos \omega x - i\sin \omega x}
    \end{align}

    We can take a linear combination of the above two roots to get a new basis set (whose ratio will not be a constant) by
    * adding the two equations and multiplying the result by $1/2$
    * subtracting the two equations and multiplying the result by $1/2i$
    \begin{align}
        y_{1} &= e^{-ax/2}\cos \omega x\newline
        y_{2} &= e^{-ax/2}\sin \omega x\newline
    \end{align}
    The general solution can then be written as
    \begin{align}
        \omega &= \frac{\sqrt{4b - a^{2}}}{2}\newline
        y &= e^{-ax/2}\roundbr{c_{1}\cos \omega x + c_{2}\sin \omega x}
    \end{align}
