---
title: "Answer"
---

The following is the joint probability distribution of $X$ and $Y$
\begin{align}
            f_{XY}(x, y) = f_{X}(x) f_{Y|X}(y|x) = \frac{1}{l} \frac{1}{x} = \frac{1}{xl} \quad \forall \quad 0 \leq y \leq x \leq 1
        \end{align}

Using marginal probabilities, we can calculate $f_{Y}(y)$ and $E[Y]$ as
\begin{align}
            f_{Y}(y) = \int f_{XY}(x,y) dx = \int_{y}^{l} \frac{1}{xl} dx = \frac{1}{l} \log \frac{l}{y} \quad\text{Note that for any $y$, $y \leq x \leq l$}\newline
            E[Y] = \int y f_{Y}(y) = \int_{0}{l} y \frac{1}{l} \log\frac{l}{y} = \frac{l}{4}
        \end{align}

This problem can also be approched using iterated expectation
\begin{align}
            E[Y] &= E[E[Y|X]] = E[\text{uniform random variable between $0$ and $x$}]\newline
                &= E[\frac{X}{2}] =\frac{1}{2}E[X]\newline
                &= \frac{l}{4}
        \end{align}
