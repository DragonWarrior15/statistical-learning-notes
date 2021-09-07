---
title: "Higher Order Linear ODEs"
---

## Higher Order Linear ODEs
Much of the concepts from 2nd order linear ODEs will be applicable here in a more general and extended form. We consider all ODEs of the form
\begin{align}
    y^{(n)} + p_{n-1}(x)y^{(n-1)} + p_{n-2}(x)y^{(n-2)} + \cdots + p_{1}(x)y^{(1)} + p_{0}y = r(x)
\end{align}

With the coefficient of $y^{(n)}$, this is called the standard form. The term on the right contains only functions of $x$ (and/or constants).

An $n^{th}$ order ODE that cannot be expressed in the above form will be called _non-linear_. If $r(x) = 0$ throughout, the equation is called homogenous, and nonhomogenous otherwise.

Similar to second order case, for the _homogenous_ equation, any linear combination of $n$ independent solutions $y_{1}, \ldots, y_{n}$ is also a solution (general solution), with the $n$ solutions being linearly independent and forming a basis.

The Wronskian holds the same properties as the second order case, for the homogenous equations. However, its now defined as
\begin{align}
    W = \detm{\begin{matrix}
        y_{1} &y_{2} &\cdots &y_{n}\newline
        y_{1}^{(1)} &y_{2}^{(1)} &\cdots &y_{n}^{(1)}\newline
        \vdots &\vdots &\cdots &\vdots\newline
        y_{1}^{(n-1)} &y_{2}^{(n-1)} &\cdots &y_{n}^{(n-1)}\newline
    \end{matrix}}
\end{align}

$n^{th}$ order _linear homogenous ODE_ has **no singular** solutions.

### Homogenous Linear ODE with constant coefficients
We consider the ODE
\begin{align}
    y^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_{1}y^{(1)} + a_{0}y = 0
\end{align}

Assuming the solution as $e^{\lambda x}$, we get the below characteristic equation after taking out the common term $e^{lambda x}$
\begin{align}
    \lambda^{n} + a_{n-1}\lambda^{n-1} + \cdots + a_{1}\lambda + a_{0} = 0
\end{align}
The roots can be all real, real and repeated, some complex and some real, etc.

* **Real and distinct roots**

    Similar to the second order case, the general solution is a linear combination of $n$ exponents
    \begin{align}
        y = c_{1}e^{\lambda_{1}x} + \cdots c_{n}e^{\lambda_{n}x}
    \end{align}

* **All complex roots**

    Complex roots must occur in pairs. Suppose one of such pairs is $\lambda \pm i\omega$, then the part of general solution for just this pair will be
    \begin{align}
        y = c_{1}e^{\lambda x}\sin \omega x + c_{2}e^{\lambda x}\cos \omega x
    \end{align}
    and similar terms will be added for all other pairs of complex roots.

* **Some distinct real and complex roots**

    This case is a combination of the above two cases. Hence the general solution will be a linear combination of few purely exponential terms, and few exponent and sinusoidal terms
    \begin{align}
        y = c_{1}e^{\lambda_{1}x} + \cdots + c_{k}e^{\lambda_{k}x}\sin \omega x + c_{k+1}e^{\lambda_{k}x}\cos \omega x
    \end{align}
* **Repeating real roots**

    Analogous to the second order case, we start multiplying all repeating roots by $x$, $x^{2}$ and so on
    \begin{align}
        y = c_{1}e^{\lambda_{1}x} + c_{2}xe^{\lambda_{1}x} + c_{3}x^{2}e^{\lambda_{1}x} + c_{4}e^{\lambda_{2}x} + c_{5}xe^{\lambda_{2}x} +\cdots
    \end{align}
    In the above example, root $\lambda_{1}$ occurs thrice and we go upto $x^{2}$. Thus, if a root repeats $k$ times, we will have $k$ occurrences with the final occurrence containing $x^{k-1}$.
* **Repeating complex roots**

    Like repeating real roots, we start multiplying the terms by $x$, $x^{2}$ and so on
    \begin{align}
        y = c_{1}e^{\lambda_{1}x}\sin \omega_{1}x + c_{2}e^{\lambda_{1}x}\cos \omega_{1}x + c_{3}xe^{\lambda_{1}x}\sin \omega_{1}x + c_{4}xe^{\lambda_{1}x}\cos \omega_{1}x + \cdots
    \end{align}
    In the above case, the complex root $\lambda_{1} \pm i\omega_{1}$ occurs twice.

Thus, depending on what the roots are, we can define the basis based on the above discussed rules.

### Nonhomogenous Linear ODEs
All the methods discussed for solutions of second order nonhomogenous linear ODEs are applicable for higher orders as well. We will consider a linear ODE in its standard form
\begin{align}
    y^{(n)} + p_{n-1}(x)y^{(n-1)} + p_{n-2}(x)y^{(n-2)} + \cdots + p_{1}(x)y^{(1)} + p_{0}y = r(x)
\end{align}
Note that the coefficient of $y^{(n)}$ is unity.

The general solution $y = y_{h} + y_{p}$ where $y_{h}$ is the solution to the corresponding homogenous equation, and $y_{p}$ is a solution that satisfies the original nonhomogenous equation.

#### Method of Undetermined Coefficients
All rules followed are similar to those discussed in [second order case]({{ "/notes/differential_equations/order_two_linear.html" | relative_url }}). If the coefficients are constants, and $r(x)$ is a continuous non zero function, the ODE is
\begin{align}
    y^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_{1}y^{(1)} + a_{0}y = r(x)
\end{align}

We follow the same three rules
* **Basic rule** is same
* **Modification rule** is slightly different. If a term of choice in $y_{p}$ is already a solution of $y_{h}$ (the corresponding homogenous equation solution), we multiply this term by $x_{k}$ where $k$ is the smalles positive integer such that this term times $x^{k}$ is not a solution of the corresponding homogenous equation.
* **Sum Rule** is same

#### Method of Variation of Parameters
We extend the formula discussed in the second order case
\begin{align}
    y_{p}(x) = \sum_{k=1}^{n}y_{k}(x)\int \frac{W_{k}(x)}{W(x)}r(x)dx
\end{align}
where $W_{k}$ is obtained by replacing the $k^{th}$ column of $W$ with $(0, 0, \ldots, 0, 1)^{T}$ (i.e., the last row contains the entry 1).

The same formula can be verified for the second order case (where $W_{1}$ and $W_{2}$ simplified to a single term).
