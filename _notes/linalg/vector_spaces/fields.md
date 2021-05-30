---
title: "Fields"
---

### Fields
A field $\field$ can either be $\comp$ or $\real$. A field is a set of atleast two distinct elements $\{0, 1\}$ satisfying all the properties laid out [here]({{ site.url }}) along with addition and multiplication defined.

To define higher dimensional fields, we take the help of lists. For a positive integer $n$
\begin{align}
    \field^{n} = \{(x_{1}, x_{2}, \ldots, x_{n}) : x_{j} \in \field \; \forall j = 1, 2, \ldots, n\}
\end{align}

which is a set of all lists satisfying the above condition. Also, if $x \in \field^{n}$, then $x_{j}$ is called the $j^{th}$ coordinate of $x$.

Similar to complex fields, addition is defined as summing up the coordinates individually
\begin{align}
    (x_{1}, x_{2}, \ldots, x_{n}) + (y_{1}, y_{2}, \ldots, y_{n}) &= (x_{1} + y_{1}, x_{2} + y_{2}, \ldots, x_{n} + y_{n})
\end{align}

When dealing with $\field^{n}$, we will often just refer to an element in it with a letter $x$ rather than a list to make things more manageable.

$\field^{n}$ satisfies the following properties
* **Commutativity**

    $x + y = y + x \quad \forall \; x, y \in \field^{n}$
    \item \emph{Additive Identity Element}\newline
    There exists element $0$ such that\newline
    $x + 0 = x \quad \forall \; x \in \field^{n}$ and $0 = (0, 0, \ldots 0) \quad n $ times
* **Additive inverse**
    \begin{gather}
        \forall \quad x \in \field^{n}, \exists \; -x = (-x_{1}, -x_{2}, \ldots, -x_{n}) \; \text{such that}\newline
        x + (-x) = 0
    \end{gather}
* **Scalar Multiplication**
    \begin{align}
        \lambda \times (x_{1}, x_{2}, \ldots, x_{n}) &= (\lambda x_{1}, \lambda x_{2}, \ldots, \lambda x_{n})\newline
        \text{where} \; (x_{1}, x_{2}, \ldots, x_{n}) &\in \field^{n}, \lambda \in \field
    \end{align}
