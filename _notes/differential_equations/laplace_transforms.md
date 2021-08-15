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
