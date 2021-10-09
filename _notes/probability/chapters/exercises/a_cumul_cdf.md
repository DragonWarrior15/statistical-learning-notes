---
title: "Answer"
---

We have $\mu = 1$ and $\sigma = 2$. Now,
\begin{align}
    P(1 < X^{2} < 9) &= P(-3 < X < -1) + P(1 < X < 3)\newline
    &= P\roundbr{\frac{-3 - 1}{2} < \frac{X - 1}{2} < \frac{-1 - 1}{2}} + P\roundbr{\frac{1 - 1}{2} < \frac{X - 1}{2} < \frac{3 - 1}{2}}\newline
    &= \Phi(-1) - \Phi(-2) + \Phi(1) - \Phi(0)
\end{align}
where we first converted to standard normals by subtracting the mean and dividing by the standard deviation. Then we used the cumulative distribution value for the standard normal.

Important thing to note here is that $P(-3 < X < -1) \neq P(1 < X < 3)$ because the normal distribution is symmetric about 1 and not zero.
