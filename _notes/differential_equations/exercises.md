---
title: Exercises
---

1. The following ODE is of what type ?
    \begin{align}
        \difftwo{u} - 2x^{2}u + \sin x = 0
    \end{align}

    **Solution**

    We can rewrite the equation in the usual format as
    \begin{align}
        \difftwo{u} + \roundbr{-2x^{2}}u = -\sin x
    \end{align}
    Hence, the equation is Linear, of order 2, degree 1, and nonhomogenous (because $r(x) = \sin x$).

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

1. Solve the following equation
    \begin{align}
        x^{2}\difftwo{y} - x\diffone{y} + y = \ln x
    \end{align}

    **Solution**

    * The general solution is $y_{h} + y_{p}$. Lets find $y_{h}$ first.
    * This is a Cauchy-Euler equation whose solution can be assumed $x^{m}$. Substituiting
        \begin{align}
            x^{2}\roundbr{m(m-1)x^{m-2}} - x\roundbr{mx^{m-1}} + x^{m} &= 0\newline
            x^{m}\roundbr{m^{2} - m - m + 1} &= 0\newline
            \implies m &= 1
        \end{align}
        The solution is of the form
        \begin{align}
            y_{1} &= x\newline
            y_{2} &= x\ln x\newline
            y_{h} &= c_{1}x + c_{2}x\ln x
        \end{align}
    * Let's try to find $y_{p}$ using variation of parameters. First we convert the cocefficient of $\difftwo{y}$ to 1
        \begin{align}
            \difftwo{y} - \frac{1}{x}\diffone{x} + \frac{1}{x^{2}}y &= \frac{\ln x}{x^{2}}\newline
            W &= y_{1}\diffone{y_{2}} - y_{2}\diffone{y_{1}}\newline
            &= x(\ln x + 1) - x\ln x(1) = x\newline
            y_{p} &= -y_{1}\int\frac{y_{2}r}{W}dx + y_{2}\int\frac{y_{1}r}{W}dx\newline
            &= -x\int\frac{\roundbr{\ln x}^{2}}{x^{2}}dx + x\ln x\int\frac{\ln x}{x^{2}} dx\newline
        \end{align}
        Lets solve the two integrals one by one
        \begin{align}
            \ln x &= t \implies dx = xdt = e^{t}dt\newline
            \int\frac{\ln x}{x^{2}} dx &= \int te^{-t}dt\newline
            &= -te^{-t} + \int e^{-t}dt = -te^{-t} - e^{-t}\newline
            &= -\frac{\ln x + 1}{x}
        \end{align}
        using integration by parts. Similarly,
        \begin{align}
            \int\frac{\roundbr{\ln x}^{2}}{x^{2}}dx &= \int t^{2}e^{-t}dt\newline
            &= -t^{2}e^{-t} + \int 2te^{-t}dt\newline
            &= -t^{2}e^{-t} - 2te^{-t} + \int 2e^{-t}dt\newline
            &= -t^{2}e^{-t} - 2te^{-t} - 2e^{-t}\newline
            &= -\frac{\roundbr{\ln x}^{2} + 2\ln x + 2}{x}
        \end{align}

        Hence,
        \begin{align}
            y_{p} &= -x\roundbr{-\frac{\roundbr{\ln x}^{2} + 2\ln x + 2}{x}} + x\ln x\roundbr{-\frac{\ln x + 1}{x}}\newline
            &= \roundbr{\ln x}^{2} + 2\ln x + 2 - \roundbr{\ln x}^{2} - \ln x\newline
            &= \ln x + 2
        \end{align}

        The general solution becomes
        \begin{align}
            y = \roundbr{c_{1}x + c_{2}x}\ln x + \ln x + 2
        \end{align}

1. Solve the differential equation
    \begin{align}
        \roundbr{1 + y^{2}}dx = \roundbr{\tan^{-1} y - x}dy
    \end{align}

    **Solution**

    Rearranging the equation, we have
    \begin{align}
        \frac{dy}{dx} &= \frac{1 + y^{2}}{\tan^{-1} y - x}
    \end{align}

    This equation is not readily solvable. However, we can instead try to get $x$ a function of $y$ by inverting the above equation
    \begin{align}
        \frac{dx}{dy} &= \frac{\tan^{-1} y - x}{1 + y^{2}}\newline
        &= \frac{\tan^{-1} y}{1 + y^{2}} - \frac{1}{1 + y^{2}}x\newline
        \implies \frac{dx}{dy} + \frac{1}{1 + y^{2}}x &= \frac{\tan^{-1} y}{1 + y^{2}}
    \end{align}

    Which is a linear equation. The integrating factor is
    \begin{align}
        IF &= e^{\int \frac{1}{1 + y^{2}}dy} = e^{\tan^{-1} y}\newline
        \implies e^{\tan^{-1} y}\frac{dx}{dy} + \frac{e^{\tan^{-1} y}}{1 + y^{2}}x &= \frac{e^{\tan^{-1} y}\tan^{-1} y}{1 + y^{2}}\newline
        xe^{\tan^{-1} y} &= \int \frac{e^{\tan^{-1} y}\tan^{-1} y}{1 + y^{2}} dy\newline
    \end{align}

    Substituiting $\tan^{-1} y = v$
    \begin{align}
        \frac{1}{1 + y^{2}}dy &= dv\newline
        \implies \int \frac{e^{\tan^{-1} y}\tan^{-1} y}{1 + y^{2}} &= \int te^{t}dt\newline
        &= te^{t} - e^{t} + c\newline
        &= e^{\tan^{-1} y}\tan^{-1} y - e^{\tan^{-1} y} + c
    \end{align}

    Thus,
    \begin{align}
        xe^{\tan^{-1} y} &= e^{\tan^{-1} y}\tan^{-1} y - e^{\tan^{-1} y} + c\newline
        \implies x &= \tan^{-1} y - 1 + ce^{-\tan^{-1} y}
    \end{align}

1. Solve the equation
    \begin{align}
        x^{3}\diffthree{y} - 3x^{2}\difftwo{y} + 6x\diffone{y} - 6y = x^{4}\ln x
    \end{align}

    **Solution**

    We first solve the homogenous equation by substituiting $x^{m}$ as the solution (this is an Euler-Cauchy equation)
    \begin{align}
        x^{3}\diffthree{y} - 3x^{2}\difftwo{y} + 6x\diffone{y} - 6y &= 0\newline
        x^{3}m(m-1)(m-2)x^{m-3} - 3x^{2}m(m-1)x^{m-2} + 6xmx^{m-1} - 6x^{m} &= 0\newline
        \implies m(m-1)(m-2) -3m(m-1) + 6m - 6 &= 0\newline
        m^{3} - 6m^{2} + 11m - 6 &= 0\newline
        m &= 1, 2, 3
    \end{align}
    Root 1 is easily identifiable by inspection. Remaining roots can be obtained by factorization. Hence, $y_{h}$ is
    \begin{align}
        y_{h} &= c_{1}x + c_{2}x^{2} + c_{3}x^{3}
    \end{align}
    with $x$, $x^{2}$ and $x^{3}$ as the bases. Since $r(x)$ is not a standard function (for method of undetermined coefficients), we will try to use variation of parameters to solve for $y_{p}$
    \begin{align}
        W &= \detm{\begin{matrix}
            x &x^{2} &x^{3}\newline
            1 &2x &3x^{2}\newline
            0 &2 &6x
        \end{matrix}} = 2x^{3}
    \end{align}
    Hence, all $W_{i}$ are
    \begin{align}
        W_{1} &= \detm{\begin{matrix}
            0 &x^{2} &x^{3}\newline
            0 &2x &3x^{2}\newline
            1 &2 &6x
        \end{matrix}} = x^{4}\newline
        W_{2} &= \detm{\begin{matrix}
            x &0 &x^{3}\newline
            1 &0 &3x^{2}\newline
            0 &1 &6x
        \end{matrix}} = -2x^{3}\newline
        W_{3} &= \detm{\begin{matrix}
            x &x^{2} &0\newline
            1 &2x &0\newline
            0 &2 &1
        \end{matrix}} = x^{2}
    \end{align}
    Now, to apply the method of undetermined, we also convert our equation to the standard form
    \begin{align}
        \diffthree{y} - \frac{3}{x}\difftwo{y} + \frac{6}{x^{2}}\diffone{y} - \frac{6}{x^{3}}y = x\ln x
    \end{align}
    \begin{align}
        y_{p}(x) &= \sum_{k=1}^{n}y_{k}(x)\int \frac{W_{k}(x)}{W(x)}r(x)dx\newline
        &= x\int\frac{x^{4}}{2x^{3}}x\ln x dx + x^{2}\int\frac{-2x^{3}}{2x^{3}}x\ln x dx + x^{3}\int\frac{x^{2}}{2x^{3}}x\ln x dx\newline
        &= \frac{x}{2}\roundbr{\frac{x^{3}}{3}\ln x - \frac{x^{3}}{9}} - x^{2}\roundbr{\frac{x^{2}}{2}\ln x - \frac{x^{2}}{4}} + \frac{x^{3}}{2}\roundbr{x\ln x - x}\newline
        &= \frac{x^{4}}{6}\ln x - \frac{11}{36}x^{4}
    \end{align}
    Thus, the general solution is
    \begin{align}
        y = c_{1}x + c_{2}x^{2} + c_{3}x^{3} + \frac{x^{4}}{6}\roundbr{\ln x - \frac{11}{6}}
    \end{align}

1. Find the radius of convergence
    \begin{align}
        \sum_{m=0}^{\inf} \frac{x^{2m + 1}}{(2m + 1)!}
    \end{align}

    **Solution**
    \begin{align}
        R &= \frac{1}{\lim_{m \to \inf} \detm{\frac{1/(2(m+1)+1)!}{1/(2m+1)!}}}\newline
        &= \frac{1}{\lim_{m \to \inf}\detm{\frac{1}{(2m+3)(2m+2)}}} = \inf
    \end{align}
    i.e., convergence happens always.
