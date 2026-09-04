# Answer

Recall for a $Gamma(n, \lambda)$

$$
\begin{aligned}
        f_{X}(x) = \frac{\lambda e^{-\lambda x} (\lambda x)^{\alpha - 1}}{\Gamma(\alpha)}
    \end{aligned}
$$

We can rearrange the terms of the given expression to get a $Gamma(n/2, 1/2)$ inside the integral

$$
\begin{aligned}
        &= \lim_{n \to \infty} \bigg[ \frac{1}{2}\frac{1}{2^{n/2 - 1}\Gamma(n/2)} \int_{n + \sqrt{2n}}^{\infty} \exp \bigg( -\frac{1}{2}t \bigg) t^{n/2 - 1} dt \bigg]\newline
        &= \lim_{n \to \infty} \bigg[ \int_{n + \sqrt{2n}}^{\infty} \frac{\frac{1}{2}e^{-\frac{1}{2}t} \big(\frac{1}{2}t \big)^{\frac{n}{2} - 1}}{\Gamma(n/2)} \bigg]\newline
        &= \lim_{n \to \infty} \bigg[ P \bigg(Gamma \bigg(\frac{n}{2}, \frac{1}{2} \bigg) \geq n + \sqrt{2n}\bigg) \bigg]
    \end{aligned}
$$

But, it is known that a $\chi^{2}\_{n}$ has the same distribution as a $Gamma(\frac{n}{2}, \frac{1}{2})$ (see [section](../distributions/chi_square.md#relation-between-chi-square-and-gamma-distribution))

$$
\begin{aligned}
        &= \lim_{n \to \infty} \bigg[ P(\chi^{2}\_{n} \geq n + \sqrt{2n}) \bigg]
    \end{aligned}
$$

and, the mean and variance of a $X^{2}\_{n}$ are $n$ and $2n$ respectively

$$
\begin{aligned}
        &= \lim_{n \to \infty} \bigg[ P \bigg(\frac{\chi^{2}\_{n} - n}{\sqrt{2n}} \geq 1 \bigg) \bigg]\newline
    \end{aligned}
$$

Since $n \to \infty$, we can use central limit theorem for a standard normal variable $Z$

$$
\begin{aligned}
        &= P(Z \geq 1) = 1 - P(Z < 1) = 1 - \Phi(1) = 1 - 0.84134 = 0.15866
    \end{aligned}
$$

