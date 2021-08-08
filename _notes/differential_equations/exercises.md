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
