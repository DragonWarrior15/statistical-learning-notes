# System of ODEs

## Motivation
To understand how a system of ODEs will arise in practical applications, refer to the motivation for [eigenvalues](../linalg/linear_eq/eigen.md#motivation-from-differential-equation).

## Conversion of $n^{th}$ order ODE to a system
Given an $n^{th}$ order ODE

$$
\begin{aligned}
    y^{(n)} = F(t, y, \diffone{y}, \ldots, y^{(n-1)})
\end{aligned}
$$


we can convert it to a system of ODEs by making the substituitions

$$
\begin{aligned}
    y_{1} &= y\newline
    y_{2} &= \diffone{y}\newline
    &\vdots\newline
    y_{n} &= y_{(n-1)}
\end{aligned}
$$


This gives the following system of first order equations

$$
\begin{aligned}
    \diffone{y_{1}} &= y_{2}\newline
    \diffone{y_{2}} &= y_{3}\newline
    &\vdots\newline
    \diffone{y_{n}} &= F(t, y_{1}, y_{2}, \ldots, y_{n-1})
\end{aligned}
$$


We can test it out on a mass on a spring problem

$$
\begin{aligned}
    m\difftwo{y} + c\diffone{y} + ky &= 0\newline
    \implies \difftwo{y} &= -\frac{c}{m}\diffone{y} - \frac{k}{m}y\newline
\end{aligned}
$$

Making the substituitions

$$
\begin{aligned}
    y_{1} &= y\newline
    \diffone{y_{1}} &= y_{2}\newline
    \diffone{y_{2}} &= -\frac{c}{m}y_{2} - \frac{k}{m}y_{1}\newline
    \implies \diffone{\detm{\begin{matrix}y_{1}\newline y_{2} \end{matrix}}} &= \begin{bmatrix}0 &1\newline -\frac{k}{m}y_{1} &-\frac{c}{m}y_{2}\end{bmatrix}\begin{bmatrix}y_{1}\newline y_{2}\end{bmatrix}
\end{aligned}
$$

We can solve for this system by finding the eigenvalues of the matrix. The characteristic equation is

$$
\begin{aligned}
    (-\lambda)(-\frac{c}{m}-\lambda) + \frac{k}{m} &= 0\newline
    \implies \lambda^{2} +\frac{c}{m}\lambda + \frac{k}{m} &= 0
\end{aligned}
$$
