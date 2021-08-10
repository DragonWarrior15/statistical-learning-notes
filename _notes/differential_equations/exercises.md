---
title: Exercises
---

1. Solve the following differential equation
    \begin{align}
        \diffone{y} &= \frac{1}{6e^{y} - 2x}
    \end{align}

    **Solution**
    Taking the reciprocal on both sides,
    \begin{align}
        \frac{dx}{dy} &= 6e^{y} - 2x\newline
        \implies \diffone{x} + 2x &= 6e^{y}\newline
    \end{align}
    which is a linear differential equation. Considering the integrating factor as $exp \roundbr{\int 2dy} = exp \roundbr{2y}$,
    \begin{align}
        \implies \diffone{x}e^{2y} + 2xe^{2y} &= 6e^{3y}\newline
        \frac{d}{dy} \roundbr{xe^{2y}} &= 6e^{3y}\newline
        xe^{2y} &= \int 6e^{3y}dy + c = 2e^{3y} + c
    \end{align}

    Another problem leveraging is the same transformation is
    \begin{align}
        \roundbr{y^{2} + 2x}\frac{dy}{dx} = y
    \end{align}

1. Solve
    \begin{align}
        \difftwo{y} = 1 + \roundbr{\diffone{y}}^{2}
    \end{align}

    **Solution**
    Substitute $v = \diffone{y}$. Rearranging,
    \begin{align}
        \diffone{v} &= 1 + v^{2}\newline
        \frac{\diffone{v}}{1 + v^{2}} &= 1\newline
        \implies \tan^{-1} v &= x + c\newline
        v &= tan \roundbr{x + c}\newline
        \diffone{y} &= tan \roundbr{x + c}\newline
        \implies y &= -\ln \roundbr{\cos \roundbr{x + c}}
    \end{align}

1. Solve
    \begin{align}
        \difftwo{y} + \roundbr{1 + \frac{1}{y}}\roundbr{\diffone{y}}^{2} = 0
    \end{align}

    **Solution**
    Rearranging (ignore handling/conversion of constant),
    \begin{align}
        \difftwo{y} &= -\roundbr{1 + \frac{1}{y}}\roundbr{\diffone{y}}^{2}\newline
        \implies \frac{\difftwo{y}}{\diffone{y}} &= -\diffone{y} - \frac{\diffone{y}}{y}\newline
        \ln \diffone{y} &= -y - \ln y + c_{1}\newline
        \implies \diffone{y} &= \frac{c_{1}e^{-y}}{y}\newline
        e^{y}y\diffone{y} &= c_{1}\newline
        \implies ye^{y} - e^{y} &= c_{1}x + c_{2}\newline
    \end{align}

    where the last equation is obtained after using integration by parts.

1. Solve
    \begin{align}
        x^{2}\difftwo{y} -3x\diffone{y} + 4y = 0
    \end{align}
    Using [Euler-Cauchy equation]({{ "/notes/differential_equations/order_two_linear.html/#euler-cauchy-equations" | relative_url }}), we know that $x^{m}$ is a solution. Substituiting and taking out the common factor $x^{m}$,
    \begin{align}
        m^{2} - 4m + 4 &= 0\newline
        \implies m &= 2
    \end{align}

    Since this is the case of double root, the general solution is
    \begin{align}
        y = \roundbr{c_{1} + c_{2}\ln x}x^{2}
    \end{align}

1. Solve the IVP
    \begin{align}
        \difftwo{y} + 3\diffone{y} + 2.25y = -10e^{-1.5x}
    \end{align}

    **Solution** (Refer to the [method of undetermined coefficients]({{ "/notes/differential_equations/order_two_linear.html#method-of-undetermined-coefficients" | relative_url }}))
    * We first check that the coefficient of $\difftwo{y}$ is 1.
    * We solve the homogenous ODE first.
        \begin{align}
            \difftwo{y} + 3\diffone{y} + 2.25y &= 0\newline
            \implies m^{2} + 3m + 2.25 &= 0\newline
            m &= -\frac{3}{2} = -1.5
        \end{align}
    * The solution to the homogenous equation becomes
        \begin{align}
            \roundbr{c_{1} + c_{2}x}e^{-1.5x}
        \end{align}
    * Based on $r(x) = -10e^{-1.5x}$, the solution to the homogenous equation will be of the same form. However, using the modification rule, we multiply an extra term of $x^{2}$ to it making $y_{p} = Cx^{2}e^{1.5x}$
    * Substituing this solution in the differential equation we obtain
        \begin{align}
            \roundbr{2Ce^{-1.5x} - 6Cxe^{-1.5x} + 2.25Cx^{2}e^{-1.5x}} + 3\roundbr{2Cxe^{-1.5x} - 1.5Cx^{2}e^{-1.5x}} + 2.25Cx^{2}e^{-1.5x} &= -10e^{-1.5x}
        \end{align}
        Talking out the common factor of $e^{-1.5x}$ and simplifying,
        \begin{align}
            2C = -10 \implies C = -5
        \end{align}
        It is important to determine the constants relating to $y_{p}$ first, before using the initial conditions and getting the constants related to $y_{h}$
    * Thus, the general solution is
        \begin{align}
            \roundbr{c_{1} + c_{2}x}e^{-1.5x} - 5x^{2}e^{-1.5x}
        \end{align}
    * Using the initial conditions, we obtain
        \begin{align}
            \roundbr{1 + 1.5x}e^{-1.5x} - 5x^{2}e^{-1.5x} = \roundbr{1 + 1.5x - 5x^{2}}e^{-1.5x}
        \end{align}
