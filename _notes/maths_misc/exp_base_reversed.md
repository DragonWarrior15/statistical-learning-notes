---
title: Exponent and Base Reversed
---

### Question: Which of the two is larger, $12^{11}$ or $11^{12}$

### Solution
To solve any such questions, suppose we have two real numbers $a$ and $b$ that satisfy the inequality $e \leq a \lt b$ where $e$ is the natural exponent. Then, $a^{b} > b^{a}$.

To prove this, consider changing the inequality slightly
\begin{align}
    a^{b} &> b^{a}\newline
    \implies \left( a^{b} \right)^{1/ab} &> \left( b^{a} \right)^{1/ab}\newline
    \implies a^{1/a} &> b^{1/b}
\end{align}

To show that the last equation is indeed true, consider the function $x^{1/x}$ and its derivative
\begin{align}
    y &= x^{1/x}\newline
    \ln y &= \frac{1}{x} \ln x\newline
    \frac{1}{y} \frac{dy}{dx} &= \frac{-1}{x^{2}} \ln x + \frac{1}{x} \frac{1}{x}\newline
    \implies \frac{dy}{dx} &= y \left( \frac{1}{x^{2}} (1 - \ln x) \right)\newline
    &= \frac{x^{1/x}}{x^{2}} \left( 1 - \ln x \right)
\end{align}

The first term of the derivative is always positive for positive values of $x$ (note: the function is only defined for positive values of $x$). As for the second term, its positive for $x < e$ and vice versa. This means that $x = e$ is the global maxima of the function as the derivative changes sign from positive to negative. Further, this is the only maxima for this function. Hence, for any two real numbers $a$ and $b$ satisfying $e \leq a \lt b$, $a^{1/a} > b^{1/b}$; which is what we set out to prove.

If both the numbers lie on the left side of $e$, then the function is increasing and we reverse the inequality. For two numbers on the opposite sides of $e$, directly making a claim is difficult and will require some algebra to derive the relation.
