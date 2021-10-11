---
title: "Answer"
---

We first calculate $X_{i}$ in terms of $Y_{i}$ and find the joint distribution of $Y_{i}$s.

\begin{align}
    Y_{1} &= \lambda_{1}X_{1} + \lambda_{2}X_{2}\newline
    Y_{2} &= \frac{\lambda_{1}X_{1}}{\lambda_{1}X_{1} + \lambda_{2}X_{2}}\newline
    \implies X_{1} &= \frac{1}{\lambda_{1}}Y_{1}Y_{2}\newline
    \implies X_{2} &= \frac{1}{\lambda_{2}}Y_{1}\roundbr{1 - Y_{2}}\newline
\end{align}

The Jacobian
\begin{align}
    J &= \begin{vmatrix}
        \frac{\partial x_{1}}{\partial y_{1}} &\frac{\partial x_{1}}{\partial y_{2}}\newline
        \frac{\partial x_{2}}{\partial y_{1}} &\frac{\partial x_{2}}{\partial y_{1}}
    \end{vmatrix} = \begin{vmatrix}
        \frac{1}{\lambda_{1}}y_{2} &\frac{1}{\lambda_{1}}y_{1}\newline
        \frac{1}{\lambda_{2}}\roundbr{1 - y_{2}} &-\frac{1}{\lambda_{2}}y_{1}
    \end{vmatrix} = \detm{-\frac{y_{1}}{\lambda_{1}\lambda_{2}}}\newline
    &= \frac{y_{1}}{\lambda_{1}\lambda_{2}}
\end{align}

Now the joint distribution
\begin{align}
    f_{X_{1}X_{2}}(x_{1}, x_{2}) &= \frac{\lambda e^{-\lambda x} (\lambda x)^{\alpha - 1}}{\Gamma(\alpha)} \frac{\lambda e^{-\lambda x} (\lambda x)^{\alpha - 1}}{\Gamma(\alpha)}\newline
    &= \frac{\lambda_{1}^{\alpha_{1}}\lambda_{2}^{\alpha_{2}}}{\Gamma(\alpha_{1}\Gamma(\alpha_{2}))}e^{-\roundbr{\lambda_{1}x_{1} + \lambda_{2}x_{2}}}x_{1}^{\alpha_{1} - 1}x_{2}^{\alpha_{2} - 1}\newline
    \implies f_{Y_{1}Y_{2}}(y_{1}, y_{2}) &= \frac{\lambda_{1}^{\alpha_{1}}\lambda_{2}^{\alpha_{2}}}{\Gamma(\alpha_{1}\Gamma(\alpha_{2}))}e^{-y_{1}}\roundbr{\frac{y_{1}y_{2}}{\lambda_{1}}}^{\alpha_{1} - 1}\roundbr{\frac{y_{1}(1-y_{2})}{\lambda_{2}}}^{\alpha_{2} - 1}\newline
    &= \frac{1}{\Gamma(\alpha_{1})\Gamma(\alpha_{2})}e^{-y_{1}}y_{1}^{\alpha_{1} + \alpha_{2} - 1}y_{2}^{\alpha_{1} - 1}\roundbr{1 - y_{2}}^{\alpha_{2} - 1}\newline
    B(\alpha_{1}, \alpha_{2}) &= \frac{\Gamma(\alpha_{1}\Gamma(\alpha_{2}))}{\Gamma(\alpha_{1} + \alpha_{2})}\newline
    \implies f_{Y_{1}Y_{2}}(y_{1}, y_{2}) &= \frac{e^{-y_{1}}y_{1}^{\alpha_{1} + \alpha_{2} - 1}}{\Gamma(\alpha_{1} + \alpha_{2}, 1)} \frac{y_{2}^{\alpha_{1} - 1}\roundbr{1 - y_{2}}^{\alpha_{2} - 1}}{B(\alpha_{1}, \alpha_{2})}\newline
    &= Gamma(\alpha_{1} + \alpha_{2}, 1) B(\alpha_{1}, \alpha_{2})
\end{align}

Since the joint distribution can be factorised into two independent distributions of $Y_{1}$ and $Y_{2}$, the two variables are independent. Further, $Y_{2}$ is a $Beta$ distribution.
