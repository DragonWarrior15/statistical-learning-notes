# Answer

Based on the definitions in [section](../life_testing/intro.md), death rate is simply the hazard function, i.e., $\lambda_{s} = 2 \lambda_{n}$ or death rate in smokers is twice that in non smokers. Now,

$$
\begin{aligned}
        P(t > B \vert t > A) &= \frac{P(t>B, t>A)}{P(t>A)} = \frac{P(t>B)}{P(t>A)}\newline
        &= \frac{1 - F(B)}{1 - F(A)} = \frac{exp(-\int_{0}^{B} \lambda(t) dt)}{exp(-\int_{0}^{A} \lambda(t) dt)}\newline
        &= exp(-\int_{A}^{B} \lambda(t) dt)\newline
        P_{s}(t > B \vert t > A) &= exp(-\int_{A}^{B} \lambda_{s}(t) dt) = exp(-\int_{A}^{B} 2\lambda_{n}(t) dt)\newline
        &= exp(-\int_{A}^{B} \lambda_{n}(t) dt)^{2} = P_{n}(t > B \vert t > A)^{2}
    \end{aligned}
$$

or, the conditional probability of survival till an age for a smoker is sqaure that of a non smoker (note that probability $< 1$).
