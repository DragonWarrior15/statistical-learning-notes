---
title: "Laplace Transforms"
---

## Laplace Transforms
Solving ODEs through Laplace Transforms consists of the following steps
1. The ODE is transformed to an algebraic equation called **subsidiary equation**
1. The subsidiary equation is solved through purely algebraic manipulations
1. The solution is transformed back to get the solution to the original ODE

The main advantages of this method are
1. Problems are solved directly: IVPs can be solved without determining the general solution, and nonhomogenous problems are solved without solving the homogenous equation first.
1. The use of Unit step functions and the Dirac Delta function make this method easy to use with inputs containing discontinuities or periodicities.

### s-shifting
Laplace transform for a function $f$ whose domain is $t > 0$ is defined as
\begin{align}
    F(s) &= L(f) = \int_{t = 0}^{\infty}e^{-st}f(t)dt\newline
    f &= L^{-1}(F)
\end{align}
The assumption is that the integral exists, which is usually the case in most of the engineering applications.

List of useful transforms

| Function | Transform |
| -------- | --------- |
| $f(t) = c$ | $F(f) = \int_{t = 0}^{\infty}e^{-st}c dt = \frac{c}{s}$ |
| $f(t) = e^{at}$ | $F(f) = \int_{t = 0}^{\infty}e^{-st}e^{at} dt = \frac{1}{s-a}$ |
| $h(t) = af(t) + bg(t)$ | $F(h) = aF(f) + bF(g)$ |
| $f(t) = \cos \omega t$ | $F(f) = \int_{t = 0}^{\infty}e^{-st}\cos \omega t dt = \frac{s}{s^{2} + \omega^{2}}$ |
| $f(t) = \sin \omega t$ | $F(f) = \int_{t = 0}^{\infty}e^{-st}\cos \omega t dt = \frac{\omega}{s^{2} + \omega^{2}}$ |
| $f(t) = t^{n}$ n is integer $\geq 0$ | $F(f) = \frac{n!}{s^{n+1}}$ |
| $f(t) = t^{a}$ a is positibe | $F(f) = \frac{\Gamma(a + 1)}{s^{a+1}}$ |
| $f(t) = e^{at}\cos \omega t$ | $F(f) = \frac{s - a}{(s - a)^{2} + \omega^{2}}$ |
| $f(t) = e^{at}\sin \omega t$ | $F(f) = \frac{\omega}{(s - a)^{2} + \omega^{2}}$ |

The last two formulae follow from the theorem given below

### First shifting theorem
\begin{align}
    L(f) &= F(s) &= \int_{t = 0}^{\infty}e^{-st}f(t)dt\newline
    \implies L(e^{at}f(t)) &= F(s - a)\newline
    \implies L^{-1}(F(s-a)) &= e^{at}f(t)
\end{align}

### Existence and Uniqueness
The Laplace transform exists if the function does not grow too fast, i.e., for all $t \geq 0$ and some $M$ and $k$
\begin{align}
    f(t) \leq Me^{kt}
\end{align}
and the transform exists for all $s > k$.

The function can be piecewise continuous, but it must demonstrate only finite jumps (at the discontinuities) for the transform to exist.

If the Laplace transform of a given function exists, it must be unique. Conversely, a given transform uniquely defines a function. If two functions have the same transform, they cannot differ on the whole interval (although they may differ at some isolated points).

Consecutively, the **inverse of the Laplace transform is also unique**.

\begin{align}
    F &= L(f)\newline
    L^{-1}(cF) &= cL^{-1}(F)\newline
\end{align}

The last equation can be verified by taking the Laplace on both the sides.

### Laplace of Derivatives
\begin{align}
    L(\diffone{f}) &= sL(f) - f(0) \; \text{if } f \leq Me^{kt} \forall t \geq 0\newline
    L(\difftwo{f}) &= s^{2}L(f) - sf(0) - \diffone{f}(0) \; \text{if } f, \diffone{f} \leq Me^{kt} \forall t \geq 0\newline
\end{align}

The first equation can be derived by considering the definition of the Laplace of derivative, and then integrating by parts to solve for the right hand side.

Generalizing to derivatives of higher order
\begin{align}
    L\roundbr{f^{(n)}} &= s^{n}L(f) - s^{n-1}f(0) - s^{n-2}f^{(1)}(0) - \cdots - f^{(n-1)}(0)
\end{align}

This can be remembered as roughly the multiplication of the Laplace of original function by correspondingn power of $s$.

### Laplace of Integrals
Since integration is the inverse transform of the derivatives, they can be remembered roughly as dividing Laplace of the original function by corresponding powers of $s$.

\begin{align}
    L\roundbr{\int_{0}^{t}f(\tau)d\tau} &= \frac{1}{s}F(s) = \frac{1}{2}L(f)\newline
    \implies \int_{0}^{t}f(\tau)d\tau &= L^{-1}\roundbr{\frac{1}{s}F(s)}
\end{align}

### Solving IVP with Laplace Transforms
Consider the following IVP
\begin{align}
    \difftwo{y} + a\diffone{y} + by &= r(t)\newline
    y(0) &= K_{0} \: \diffone{y}(0) = K_{1}
\end{align}

Taking the Laplace transform on both the sides $(L(y) = Y(s), L(r(t))) = R(s)$ and using the formulae seen above
\begin{align}
    \squarebr{s^{2}Y(s) - sy(0) - \diffone{y}(0)} + a\squarebr{sY(s) - y(0)} + bY(s) &= R(s)\newline
    \implies Y(s) &= \frac{R(s) + (s+a)K_{0} + K_{1}}{s^{2} + as + b}
\end{align}

Where,
\begin{align}
    \frac{1}{s^{2} + as + b} &= \frac{1}{\roundbr{s + \frac{a}{2}}^{2} + \roundbr{b - \frac{a}{4}}^{2}} = Q(s)
\end{align}

also called the **transfer function**. In the special case that $K_{0} = K_{1} = 0$,
\begin{align}
    Y(s) &= R(s)Q(s)\newline
    y = L^{-1}\roundbr{R(s)Q(s)}
\end{align}

Where the right hand side can be solved by the method of partial fractions.

**Shifted Data**: If the initial conditions are both at a different point $t_{0}$ than $0$, we make the substituition $t^{\*} = t - t_{0}$ so that the initial conditions now lie at $t^{\*} = 0$.

## Unit Step (Heaviside Function)
This function is defined as
\begin{align}
    u(t - 1) &= \begin{cases}0 &\mbox{if $t < a$}\newline 1 &\mbox{otherwise}\end{cases}
\end{align}

$a$ is usually positive since $t$ denotes time.
\begin{align}
    L\roundbr{u\roundbr{t - a}} = \int_{0}^{\infty} e^{-st}u(t-a)dt = \int_{a}^{\infty} e^{-st}dt = \frac{e^{-sa}}{s}
\end{align}

where $s > 0$. Note that in general, $f(t-a)$ means shifting the function $f$ right by $a$ units.

If we have a step function that is positive for a fixed interval like
\begin{align}
    f(t) &= \begin{cases}0 &\mbox{if $t < a$}\newline 1 &\mbox{if $a \leq t \leq b$}\newline 0 &\mbox{otherwise} \end{cases}\newline
    \implies f(t) &= u(t - a) - u(t - b)
\end{align}

This brings us to the second shifting theorem.

### Second Shift Theorem
\begin{align}
    L\roundbr{f(t-a)u(t-a)} &= e^{-as}F(s)\newline
    \implies f(t-a)u(t-a) &= L^{-1}\roundbr(e^{-as}F(s))
\end{align}

For instance
\begin{align}
    L\roundbr{5\sin\roundbr{t-2}u\roundbr{t-2}} &= 5e^{-2s}L\roundbr{\sin t }\newline
    &= 5e^{-2s}\frac{1}{s^{2} + 1}
\end{align}

Further, we have a similar formula
\begin{align}
    L\roundbr{f(t)u(t-a)} &= e^{-as}L\roundbr{f\roundbr{t+a}}
\end{align}

This theorem is convenient when calculating inverses too
\begin{align}
    L^{-1}\roundbr{e^{-3s}\frac{1}{\roundbr{s+2}^{2}}}
\end{align}

Two things to note here: $e^{-3s}$ appears when considering the second shift theorem. The remaining part inside the inverse can be understood as
\begin{align}
    L^{-1}\roundbr{\frac{1}{\roundbr{s+2}^{2}}} &= e^{-2t}t
\end{align}

Thus, applying the second shift theorem on this _entire function_,

\begin{align}
    L^{-1}\roundbr{e^{-3s}\frac{1}{\roundbr{s+2}^{2}}} &= e^{-2(t-3)}(t-3)u(t-3)
\end{align}

The substituition $t \to t-a$ should be made on the _entire function_.

### Dirac Delta Theorem
Given
\begin{align}
    f_{k}(t - a) = \begin{cases}\frac{1}{k} &\mbox{$a \leq t \leq a + k$}\newline
    0 &\mbox{otherwise}\end{cases}
\end{align}
where $t > 0$ since it denotes time. Impulse is defined as the integral of a force over a short period of time. Dirac Delta or unit impulse is
\begin{align}
    \delta (t - a) = \lim_{k \to 0} f_{k}(t - a)
\end{align}

This is not a function in the usual sense, but defined more for convenience in solving ODEs where impulse forces act.

**Sifting Property**
\begin{align}
    \int_{0}^{\infty} g(t)\delta (t-a) dt = g(a)
\end{align}

because the delta function _sifts_ through the function $g(t)$ and brings out its value at the given point $a$.

Laplace transform of a delta function can be derived by using unit step functions and considering the limit
\begin{align}
    f_{k}(t - a) &= \frac{1}{k}\squarebr{u(t-a) - u(t-(a+k))}\newline
    L(f_{k}(t - a)) &= \frac{e^{-as}}{ks}\roundbr{1 - e^{-as}}\newline
    \lim_{k \to 0} L \roundbr{f_{k}(t - a)} &= e^{-as} \: \text{using Lhopital rule}\newline
    \implies L\roundbr{\delta (t - a)} &= e^{-as}
\end{align}

#### Heaviside Expansions
Based on the previous sections and some of the exercises, we can see that the most common Laplace transform is of the exponential function and has the form $1/(s - a)$. Hence, we need quick methods to solve the partial fractions arising out of these.

In general, if there is a single unrepeated factor of $s - a$, we can assume the partial fraction to be of the form $\frac{A}{s-a}$ where $A$ is a constant.

If the factor occurs twice, the choice of partial fraction will be $\frac{A_{0}}{s-a} + \frac{A_{1}}{(s-a)^{2}} where $A_{0}$ and $A_{1}$ are constants. Depending on the number of repeatitions, we will keep increasing the terms that appear in the partial fractions.

In case of an unrepeated complex fraction $(s - a)(s - \bar{a})$ the partial fraction is assumed to be $\frac{As + B}{(s - \alpha)^{2} + \beta^{2}}$ where $a = \alpha + i\beta$.

### Convolution.
So far, we have not covered how convolution of multiplication of functions would look like. We will see convolution operations next.

\begin{align}
    h(t) &= (f \* g)(t) = \int_{0}^{t}f(\tau)g(t - \tau) d\tau \newline
    H(s) &= F(s)G(s)
\end{align}

where the captial letter functions denote the Laplace Transform.

Properties of convolution
* $f \* g = g \* f$
* $f \* (g_{1} + g_{2}) = f \* g_{1} + f \* g_{2}$
* $f \* (g \* v) = (f \* g) \* v$
* $f \* 0 = 0 \* f$

Note that $f \* 1 \neq f$ in general.

With this operation, we now have the solution to the Differential equation which has been converted using Laplace Transform $Y(s) = R(s)Q(s)$ as $y = \int_{0}^{t}r(\tau)q(t - \tau) d\tau$ provided we know the inverse transforms of the functions $R$ and $Q$.

#### Integral Equations
Convolutions are also useful in solving integral equations where the unknown function $y(t)$ appears both inside and outside the integral. For instance

\begin{align}
    y(t) - \int_{0}^{t}y(\tau)\sin (t - \tau) d\tau &= t\newline
    \implies y(t) - t &= \int_{0}^{t}y(\tau)\sin (t - \tau) d\tau \newline
    \implies Y(s) - \frac{1}{s^{2}} &= Y(s) \frac{1}{s^{2} + 1}\newline
    Y(s) &= \frac{s^{2} + 1}{s^{4}} = \frac{1}{s^{2}} + \frac{1}{s^{4}}\newline
    y(t) &= t + \frac{t^{3}}{6}
\end{align}

where we first used the Laplace transform of the convolution and then took the inverse transform to find out the function $y$.

### Differentiation and Integration of Transforms
\begin{align}
    F(s) &= \int_{0}^{\infty}e^{-st}f(t)dt\newline
    \implies \diffone{F}(s) &= -\int_{0}^{\infty}e^{-st}tf(t)dt = -L\roundbr{tf(t)}\newline
    \implies L^{-1}\roundbr{\diffone{F}(s)} &= -tf(t)
\end{align}

Similarly, for integrals,
\begin{align}
    L\roundbr{\frac{f(t)}{t}} &= \int_{s}^{\infty}F(\widetilde{s})d\widetilde{s}\newline\
    \implies L^{-1}\roundbr{\int_{s}^{\infty}F(\widetilde{s})d\widetilde{s}} = \frac{f(t)}{t}
\end{align}

#### Special ODEs that use this Method of Solution
##### Laguerre's ODE
\begin{align}
    t\difftwo{y} + (1-t)\diffone{y} + ny = 0
\end{align}

Taking Laplace Transform of each term,
\begin{align}
    L\roundbr{t\difftwo{y}} &= -\frac{d}{ds}L(\difftwo{y}) = -\frac{d}{ds}\roundbr{s^{2}Y - sf(0) - \diffone{f}(0)}\newline
    &= -2sY - s^{2}\frac{dY}{ds} + f(0)\newline
    L\roundbr{(1 - t)\diffone{y}} &= L\roundbr{\diffone{y}} - L\roundbr{t\diffone{y}}\newline
    &= (sY(s) - f(0)) - \roundbr{-\frac{d}{ds}\roundbr{sY - f(0)}}\newline
    &= (sY(s) - f(0)) - \roundbr{Y + s\frac{dY}{ds}}
\end{align}

Putting back in the Laplace Transform of the original equation
\begin{align}
    -2sY - s^{2}\frac{dY}{ds} + f(0) + sY - f(0) + Y + s\frac{dY}{ds} + nY &= 0\newline
    Y(1 + n - s) + s(1-s)\frac{dY}{ds} = 0\newline
    \implies \frac{dY}{Y} &= -\frac{n + 1 - s}{s(1-s)}ds\newline
    &= \roundbr{\frac{n}{s-1} - \frac{n+1}{s}}\newline
    \implies \ln Y = n\ln \roundbr{s-1} - \roundbr{n+1}\ln s\newline
    Y &= \frac{(s-1)^{n}}{s^{n+1}}
\end{align}

Now consider (from the first shift theorem)
\begin{align}
    L\roundbr{e^{-t}t^{n}} &= L\roundbr{t^{n}}(s + 1) = \frac{n!}{\roundbr{s+1}^{n+1}}\newline
    L\roundbr{\frac{d^{n}}{dt^{n}} t^{n}e^{-t}} &= s^{n}L\roundbr{t^{n}e^{-t}} - s^{n-1}f(0) - s^{n-2}\diffone{f}(0) - \cdots - f^{(n-1)}(0)\newline
    &= s^{n}\frac{n!}{\roundbr{s+1}^{n+1}}\newline
    \frac{1}{n!}L\roundbr{e^{t}\frac{d^{n}}{dt^{n}}t^{n}e^{-t}} &= \frac{1}{n!}L\roundbr{d^{n}dt^{n}t^{n}e^{-t}}(s-1)\newline
    &= \frac{1}{n!}\frac{\roundbr{s-1}^{n}n!}{s^{n+1}} = \frac{\roundbr{s-1}^{n}}{s^{n+1}}
\end{align}

Hence,
\begin{align}
    Y &= \frac{(s-1)^{n}}{s^{n+1}}\newline
    \implies y &= L^{-1}\roundbr{\frac{(s-1)^{n}}{s^{n+1}}}\newline
    &= \frac{e^{t}}{n!}\frac{d^{n}}{dt^{n}}\roundbr{t^{n}e^{-t}}
\end{align}

### Miscellaneous
#### System of ODEs
For a system of ODEs, we take the Laplace of all the equations, and then solve for the $Y$s algebraically. We leverage all the formulae for single ODE derived above.

#### Periodic Functions
Suppose $f$ is periodic with period $p$. Then,
\begin{align}
    L(f) = \frac{1}{1 - e^{-ps}}\int_{0}^{p}e^{-st}f(t)dt
\end{align}
