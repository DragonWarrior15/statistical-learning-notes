---
title: "Answer"
---

We first calculate the inverse transforms
\begin{align}
    X_{1} &= Y_{1}X_{2} = Y_{1}Y_{2}\newline
    X_{2} &= Y_{2}\newline
    \implies J &= \begin{vmatrix}
        \frac{\partial x_{1}}{y_{1}} &\frac{\partial x_{1}}{y_{2}}\newline
        \frac{\partial x_{2}}{y_{1}} &\frac{\partial x_{2}}{y_{2}}
    \end{vmatrix} = \begin{vmatrix}
        y_{2} &y_{1}\newline
        0 &1
    \end{vmatrix} = \detm{y_{2}} = y_{2}\newline
    f_{Y}(y) &= f_{X}(y_{1}y_{2}, y_{2}) \detm{J}\newline
    &= 10(y_{1}y_{2})(y_{2}^{2})y_{2} = 10y_{1}y_{2}^{4}
\end{align}

since $y_{2} = x_{2}$, it is always positive.

We can also find the support by considering the inequalities
\begin{align}
    0 < x_{1} < x_{2} < 1\newline
    \implies 0 < y_{1}y_{2} < y_{2} < 1\implies
    0 < y_{1}, y_{2} < 1
\end{align}

Marginal distributions can be easily found out from the joint distribution
\begin{align}
    f_{Y_{1}}(y_{1}) &= \int_{0}^{1} 10y_{1}y_{2}^{4} dy_{2} = 2y_{1}\newline
    f_{Y_{2}}(y_{2}) &= \int_{0}^{1} 10y_{1}y_{2}^{4} dy_{1} = 5y_{2}^{4}\newline
\end{align}

Clearly, $f(y_{1}, y_{2}) = f(y_{1}) f(y_{2})$ implying that the two are independent.
