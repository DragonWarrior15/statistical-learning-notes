---
title: "Order Statistics"
---

## Order Statistics
Let $X_{1}, \ldots, X_{n}$ denote a random sample from a random variable $X$ having a continuous distribution and a finite support $(a, b)$ where neither is infinite. Now, let $Y_{1}, \ldots Y_{n}$ denote the arrangement of $X_{i}$s so that they are in ascending order, i.e., $Y_{1} < \ldots < Y_{n}$. In this case, $Y_{i}$ will denote the **ith order statistic** of $X_{i}$.

The joint distribution of $Y_{i}$s is given by
\begin{align}
    g(y_{1}, \ldots, y_{n}) = \begin{cases}
        n! f(y_{1})\cdots f(y_{n}) &\mbox{$a < y_{1} < \cdots < y_{n} < b$}\newline
        0 &\mbox{otherwise}
    \end{cases}
\end{align}

To derive the above, consider that $X_{i}$ take up the values $y_{1}, \ldots, y_{n}$. This is so that the inequality order between the $y_{i}$s is always maintained. There are $n!$ ways to assign an arrangement of $y_{i}$s to $X_{i}$s. Any such assignment will be of the form $y_{i}$ = $x_{j}$ such that there is a one to one mapping. This assignment/change of variables has a Jacobian of 1 (since the matrix contains only 1s and 0s, and we can rearrange the rows to get an identity matrix in the end).

So we simply sum up the pdfs of all such combinations in $X_{i}$ to get the final pdf for $Y_{i}$s.

### PDF of Any Order Statistic
We know that
\begin{align}
    F_{X}(x) = \int_{a}^{x}f_{X}(x)dx
\end{align}

is the cumulative function in the support $(a, b)$. $F_{X}(x) = 0$ if $x \leq a$ and $F_{X}(x) = 1$ if $b \geq x$. Also, we have
\begin{align}
    \int_{a}^{x}F_{X}(w)^{\alpha - 1}f_{X}(x)dw &= \frac{F_{X}(x)^{\alpha}}{\alpha} \quad \alpha > 0\newline
    \int_{y}^{b}(1-F_{X}(w))^{\beta - 1}f_{X}(x)dw &= \frac{(1-F_{X}(y))^{\beta}}{\beta} \quad \beta > 0\newline
\end{align}

Now the marginal pdf of any $Y_{k}$ is
\begin{align}
    g_{Y_{k}}(y_{k}) &= \int_{a}^{y_{k}}\cdots\int_{a}^{y_{2}}\int_{y_{k-1}}^{b}\cdots\int_{y_{n-1}}^{b} g(y_{1}, \ldots, y_{n}) dy_{n}\cdots dy_{k+1} dy_{1}\cdots dy_{k-1}\newline
    &= n!f_{X}(y_{k})\int_{a}^{y_{k}}\cdots\int_{a}^{y_{2}}\int_{y_{k-1}}^{b}\cdots\int_{y_{n-1}}^{b} f_{X}(y_{1})\cdots f_{X}(y_{n}) dy_{n}\cdots dy_{k+1} dy_{1}\cdots dy_{k-1}
\end{align}

we took out $f_{X}(y_{k})$ since $y_{k}$ only appears in the last integral. Also, carefully notice the order of the integral. We first integrate $y_{n}, \ldots, y_{k+1}$ and then from $y_{1}, \ldots y_{k-1}$. This ordering is important to simplify the integral. This further helps choose the right limits that respect the inequalities between the variables. For instance, the first integral $y_{n}$ will go from $y_{n-1}$ to $b$ since $Y_{n-1} < Y_{n}$ by definition. The next will be from $y_{n-2}$ to $b$ since $Y_{n-2} < Y_{n-1}$ by definition, and we have already integrated $y_{n}$ out so that the upper limit of the integral is $b$.

Solution to the first few integrals
\begin{align}
    \int_{y_{n-1}}^{b}f_{X}(y_{n})dy_{n} &= 1 - F_{X}(y_{n-1})\newline
    \int_{y_{n-2}}^{b}(1 - F_{X}(y_{n-1}))f_{X}(y_{n-1})dy_{n-1} &= \frac{1 - F_{X}(y_{n-2})}{2}\newline
\end{align}

Solving all the integrals, we will get the formula
\begin{align}
    g_{Y_{k}}(y_{k}) = \frac{n!}{(k-1)!(n-k)!}F_{X}(y_{k})^{k-1}\roundbr{1 - F_{X}(y_{k})}^{n - k}f(y_{k})
\end{align}
for $a < y_{k} < b$ and zero otherwise.
