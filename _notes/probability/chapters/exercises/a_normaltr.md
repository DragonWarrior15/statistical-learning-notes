---
title: "Answer"
---

Questions of this type must only be approached through CDF. First find the CDF of Y and then it's PDF.
\begin{align}
            F_{Y}(y) &= P(Y \leq y) = P(g(X) <= y)\newline
                    &= P(X \in [-y, 0] \cup X \in [0, y^{2}])\newline
                    &= (F_{X}(0) - F_{X}(-y)) + (F_{X}(y^{2}) - F_{X}(0))\newline
                    &= F_{X}(y^{2}) - F_{X}(-y)\newline
            p_{Y}(y) &= \frac{F_{Y}(y)}{dy}\newline
                    &= \frac{dF_{X}(y^{2})}{dx} \frac{d(y^{2})}{dy} - \frac{dF_{X}(-y)}{dx} \frac{d(-y)}{dy}\newline
                    &= 2yp_{X}(y^{2}) + p_{X}(-y)\newline
                    &= 2y\frac{1}{\sqrt{2\pi}}e^{-y^{4}/2} + \frac{1}{\sqrt{2\pi}} e^{-y^{2}/2}
        \end{align}
