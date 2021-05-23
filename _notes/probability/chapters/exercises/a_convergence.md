---
title: "Answer"
---

1.  No, since $X_{i}$ is also uniform in $[-1,1]$

2.  Yes, $E[Y_{i}] = 0$ by symmetry. For $\epsilon > 0$,
    \begin{align}
                    \lim_{i \to \infty}(P\vert Y_{i} - \mu_{i} \vert > \epsilon) &= \lim_{i \to \infty} P(\vert \frac{X_{i}}{i} - 0 \vert > \epsilon)\newline
                    &= \lim_{i \to \infty} P(\frac{X_{i}}{i} > \epsilon \text{ and } \frac{X_{i}}{i} < -\epsilon)\newline
                    &= \lim_{i \to \infty} [P(X_{i} > i\epsilon) + P(X_{i} < -i\epsilon)] = 0
                \end{align}

3.  Yes, $E[Y_{i}] = 0$ by symmetry. For $\epsilon > 0$,
    \begin{align}
                    \lim_{i \to \infty}P(\vert Z_{i} - 0 \vert > \epsilon) &= \lim_{i \to \infty}P((X_{i})^{i} > \epsilon \text{ or } (X_{i})^{i} < -\epsilon)\newline
                    &= \lim_{i \to \infty} [\frac{1}{2}(1 - \epsilon^{1/i}) + \frac{1}{2}(1 - \epsilon^{1/i})]\newline
                    &= \lim_{i \to \infty}(1 - \epsilon^{1/i}) = 0
                \end{align}
