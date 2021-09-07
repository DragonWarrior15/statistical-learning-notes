---
title: "Series Solutions of ODEs"
---

## Series Solutions of ODEs
Here we look at some methods that are useful for solving ODEs with variable coefficients.

### Power Series Method
We assume the solution to be a polynomial (a power series) and try to determine the coefficients of the same. We try to compare this series to expansions of common functions (if possible) to determine the final solution form, or even the series form which can be used for approximate solutions, graphs etc. (Please see the section [Existence of Solution](#existence-of-solution) for the conditions when a power series solution exists)

Common series expansions
\begin{align}
    \frac{1}{1 - x} &= 1 + x + x^{2} + \cdots\newline
    e^{x} &= 1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + \cdots\newline
    \sin x &= 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!}\newline
    \cos x &= x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!}
\end{align}

We assume the solution to be a power series
\begin{align}
    y = a_{0} + a_{1}\roundbr{x - x_{0}} + a_{2}\roundbr{x - x_{0}}^{2} + a_{3}\roundbr{x - x_{0}}^{3} + \cdots
\end{align}
where $a_{i}$ are constants (**coefficients**) and $x_{0}$ is called the **center** of the series.
and substitute in the equation. Further, we will also insert the power series expansions of the coefficients. This way, the entire equation only contains different powers of $x$ (in the form of power series). Then, we equate the coefficients of $x$ (and the constant) on either side of the equation to determine the values of the series coefficients.

Every power series can be associated with an **nth partial sum** and the **remainder**
\begin{align}
    s_{n}(x) &= a_{0} + a_{1}\roundbr{x - x_{0}} + a_{2}\roundbr{x - x_{0}}^{2} + a_{3}\roundbr{x - x_{0}}^{3} + \cdots + a_{n}\roundbr{x - x_{0}}^{n}\newline
    R_{n}(x) &= a_{n + 1}\roundbr{x - x_{0}}^{n + 1} + a_{n + 2}\roundbr{x - x_{0}}^{n + 2} + \cdots
\end{align}

This sequence of partial sums $s_{1}(x), s_{2}(x), \ldots$ is said to be **convergent** if for some $x_{1}$
\begin{align}
    \lim_{n \to \infty}s_{n}(x_{1}) = s(x_{1})
\end{align}
where $s(x_{1})$ will be a number called the **value** or _sum_ of the power series. Then,
\begin{align}
    s(x_{1}) &= \sum_{m = 0}^{\infty}a_{m}\roundbr{x_{1} - x_{0}}^{m}
\end{align}
and for every $n$
\begin{align}
    s(x_{1}) &= s_{n}(x_{1}) + R_{n}(x_{1})
\end{align}

In case of convergence, for every $\epsilon$, there is a corresponding $N$ such that
\begin{align}
    \detm{R_{n}(x_{1})} = \detm{s(x_{1}) - s_{n}(x_{1})} < \epsilon \forall n > N
\end{align}

The series is always convergent at $x_{0}$ and there may be other values where the series converges. In that case, these values form an interval with $x_{0}$ as the center and the radius $R$ such that convergence happens for all $\detm{x - x_{0}} < R$. For other values, the series diverges.

The radius of convergence can be determined using each of the formulae
\begin{align}
    R &= \frac{1}{\lim_{m \to \infty} \detm{a_{m}}^{1/m}}\newline
    R &= \frac{1}{\lim_{m \to \infty\detm{\frac{a_{m+1}}{a_{m}}}}}
\end{align}

$R = \infty$ is the best possible case since convergence happens everywhere, while $R = 0$ is not really useful since it means convergence happens only at a point.

The power series assumption is valid under the condition that the assumed series is convergent. That is,
\begin{align}
    s_{n}(x_{0}) &= \sum_{i=1}^{n} a_{i}(x - x_{0})^{i}\newline
    \lim_{n \to \infty} s_{n}(x_{0}) &= s(x_{0})
\end{align}

and the series is said to be convergent at $x = x_{0}$.

### Existence of Solution
For the ODE in standard form (coefficient of $\difftwo{y}$ is unity)
\begin{align}
    \difftwo{y} + p(x)\diffone{y} + q(x)y = r(x)
\end{align}

A power series solution exists if $p(x)$, $q(x)$ and $r(x)$ have power series expansions around some point $x_{0}$ with a positive radius of convergence.

More precisely, a function $f(x)$ is called **analytic** at point $x = x_{0}$ if it can be expressed as a power series in terms of $x - x_{0}$ with radius of convergence $R > 0$.

Thus, in more technical terms, if $p(x)$, $q(x)$ and $r(x)$ are analytic at a point $x = x_{0}$, then every solution of the mentioned ODE is also analytic and can be represented as a power series in powers of $x - x_{0}$ with radius of convergence $R > 0$.

Some algebraic operations will also follow convergence if the original power series converges. That is, the series obtained by taking **derivatives** also converges in the same interval. Further, if two series are analytic, there **sum** or **product** will also be analytic in the same interval. This is important since it ensures all terms in the ODE are themselves convergent and algebraic operations remain valid.

**Vanishing Coefficients**: if a power series has a positive radius of convergence and a sum that is identically zero throughout this interval, then each coefficient of this series must be zero.
