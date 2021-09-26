---
title: "Generating Continuous Random Variables"
---

## Generating Continuous Random Variables

To generate a random variable $X$, We utilise it's cumulative distribution function $F$. Note that $F$ is strictly increasing from $0$ to $1$ and the probability density $f$ and $F$ have a one to one mapping, i.e., $F$ has an inverse $F^{-1}$. So, to get $X$, we first generate $U \in (0, 1)$ and then $X = F^{-1}(U)$.


### Exponential Random Variable

The distribution function $F = 1 - exp(-\lambda x)$. Then, the inverse is
\begin{align}
        x &= -\frac{1}{\lambda}log(1 - F)\newline
        \text{or, }\quad X &= \frac{1}{\lambda}log(1 - U)
    \end{align}
and $X$ will follow the exponential distribution. Further, replacing $U$ with $1-U$ will still remain a uniform distribution, meaning $X$ will still be exponential.

### Normal Random Variable

Consider $X, Y \sim \mathcal{N}(0, 1)$. Then,
\begin{align}
        f_{XY}(x,y) = \frac{1}{2\pi}exp(-\frac{x^{2}+y^{2}}{2})
    \end{align}
is the joint distribution. $(X, Y)$ is a point on the cartesian plane and thus, will have an equivalent polar coordinate $(R, \Theta)$ implying $R^{2} = X^{2} + Y^{2}$ which is a $\chi_{2}^{2}$ variable. From relation between gamma and $\chi_{2}^{2}$ variable,
\begin{align}
       f_{R^{2}}(r) &= \frac{1}{2}exp(-\frac{r}{2})\newline
       \text{and} \quad f_{XY}(x,y) &= \frac{1}{2\pi} exp(-\frac{r}{2}) \quad \text{when} \quad x^{2} + y^{2} = r
    \end{align}

Now, $R$ and $\Theta$ are independent variables and can be used to generate $X$ and $Y$. $\Theta$ is uniformly distributed in $[0, 2\pi]$. Taking the inverse of cumulative distribution of $R^{2}$ (Note that $f_{R^{2}}(r)$ is a distribution on $R^{2}$ and not $R$),
\begin{align}
        R^{2} &= -2log(1 - U_{1})\newline
        \Theta &= 2\pi U_{2}
    \end{align}
where $U_{1}$ and $U_{2}$ are uniform random variables. Using the transformation back to cartesian coordinates from polar ones,
\begin{align}
        X &= \sqrt{-2log(1 - U_{1})}cos(2\pi U_{2})\newline
        Y &= \sqrt{-2log(1 - U_{1})}sin(2\pi U_{2})
    \end{align}
This approach is called *Box-Muller method*. To generate standard normals with mean $\mu$ and variance $\sigma^{2}$, we simply return $\mu + \sigma X, \mu+\sigma Y$.

### Normal Random Variable from Uniform Distribution

Using the central limit theorem, we can add up multiple uniform distributions to get a normal random variable.
\begin{align}
        Y = \bigg(\sum_{i=1}^{12}X_{i} \bigg) - 6 \sim \mathcal{N}(0,1)
    \end{align}
because the mean of 12 uniform random variables is $12 * 0.5 = 6$ and the variance of sum of 12 independent random variables is $12 \times (1-0)^{2}/12 = 1$. The same equation with 30 uniform distributions will become
\begin{align}
        Y = \sqrt{\frac{2}{5}}\bigg[\bigg(\sum_{i=1}^{30}X_{i} \bigg) - 15\bigg] \sim \mathcal{N}(0,1)
    \end{align}
and combining more variables will increase the accuracy of the approximation, but also increase computational time.
