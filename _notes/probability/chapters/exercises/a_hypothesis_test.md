---
title: "Answer"
---

We will solve the problem using $p-value$ as well as critical regions. Let $\bar{X}$ denote the mean of the samples. First, lets find the critical region to reject $H_{0}$.
\begin{align}
        P(\lvert \bar{X} \rvert > c \lvert H_{0} \quad\text{is true}) &= \alpha = 0.05\newline
        P \bigg(\bigg\lvert \frac{\bar{X} - 30}{20/\sqrt{10}} \bigg\rvert > c \bigg) &= 0.05
    \end{align}
Since this is a double sided test, $c = z_{0.05/2} = z_{0.025} = 1.96$. We reject the hypothesis if either the test statistic $> 1.96$ or $< -1.96$. The test statistic in this case is $(27-30) \sqrt{10} / 20 = -2.12$ rejecting $H_{0}$.


For solution using *p-value*, we calculate the following
\begin{align}
        P \bigg(Z > \bigg\lvert \frac{\bar{X} - 30}{20/\sqrt{10}} \bigg\rvert \bigg) &= P(Z > 2.12 \cup Z < -2.12)\newline
        &= 2P(Z > 2.12) = 2(1-\Phi(2.12)) = 2(1-0.98300)\newline
        &= 0.034 < 0.05
    \end{align}
Since the *p-value* is smaller than the significance level, we accept $H_{a}$ which states that the mean is different than $30$.
