---
title: Perpendicular distance in Maximum Margin Classifier
---

## Perpendicular distance in Maximum Margin Classifier

The equation of the plane is given by $\beta_{0} + \beta_{1}x_{1} + \cdots + \beta_{p}x_{p} = 0$. Let $x$ be the point whose perpendicular distance from the plane we want to calculate and let $x_{a}$ a point on the plane. The distance between $x$ and $x_{a}$ is
\begin{align}
    d^{2} = \sum_{i=1}^{p} (x_{i} - x_{ai})^{2}\end{align}
and the minimum of this distance is the required perpendicular distance. Since $x_{a}$ lies on the plane, we have a constrained optimization
\begin{align}
    \minimize_{x_{a1}, \ldots, x_{ap}} \sum_{i=1}^{p} (x_{i} - x_{ai})^{2} + \lambda (\beta_{0} + \beta_{1}x_{a1} + \cdots + \beta_{p}x_{ap})\end{align}

Taking the partial derivatives with respect to all components of $x_{a}$ and $\lambda$,
\begin{align}
    -2(x_{i} - x_{ai}) + \lambda \beta_{i} &= 0 \quad \forall \quad i = 1, \ldots, p\newline
    \beta_{0} + \beta_{1}x_{a1} + \cdots + \beta_{p}x_{ap} &= 0\newline
    \implies \beta_{0} + \sum_{i=1} \beta_{i}(x_{i} - \frac{\lambda \beta_{i}}{2}) &= 0\newline
    \implies 2\frac{\beta_{0} + \sum_{i=1}^{p} \beta_{i}x_{i}}{\sum_{i=1}^{p}\beta_{i}^{2}} &= \lambda\newline
    \implies x_{i} - x_{ai} &= \beta_{i} \frac{\beta_{0} + \sum_{i=1}^{p} \beta_{i}x_{i}}{\sum_{i=1}^{p}\beta_{i}^{2}} \quad \forall \quad i = 1, \ldots, p\newline
    \text{giving} \quad \sum_{i=1}^{p} \beta_{i}^{2} \frac{(\beta_{0} + \sum_{i=1}^{p} \beta_{i}x_{i})^{2}}{(\sum_{i=1}^{p}\beta_{i}^{2})^{2}} &= d^{2}\newline
    \text{or} \quad \frac{(\beta_{0} + \sum_{i=1}^{p} \beta_{i}x_{i})^{2}}{\sum_{i=1}^{p}\beta_{i}^{2}} &= d^{2}\end{align}

Hence, the perpendicular distance is same as putting the point in the equation of the hyperplane and dividing by the norm of the coefficients. In the special case where the norm equals 1, the distance becomes $\lvert \beta_{0} + \sum_{i=1}^{p} \beta_{i}x_{i} \rvert$.
