---
title: "Answer"
---

Always solve such questions using the cumulative distribution approach.
\begin{alignat}{2}
            P(X \leq x) &= \begin{cases} 0 &\mbox{$x < 0$}\newline
                                        \frac{1}{2} x &\mbox{$0 \leq x \leq 2$}\newline
                                        1 &\mbox{$2 < x$} \end{cases}\newline
            P(Y \leq y) &= P(X^{3} \leq y) = P(X \leq y^{\frac{1}{3}})\newline
                        &= \begin{cases}  0 &\mbox{$y < 0$}\newline
                                            \frac{1}{2} y^{\frac{1}{3}} &\mbox{$0 \leq y^{\frac{1}{3}} \leq 2$}\newline
                                            1 &\mbox{$2 < y^{\frac{1}{3}}$} \end{cases}\newline
            f_{Y}(y) &= \frac{dP(Y <= y)}{dy}(y)\newline
                     &= \begin{cases}  0 &\mbox{$y < 0$}\newline
                                            \frac{1}{6} y^{\frac{-2}{3}} &\mbox{$0 \leq y \leq 8$}\newline
                                            0 &\mbox{$8 < y$} \end{cases}
        \end{alignat}
