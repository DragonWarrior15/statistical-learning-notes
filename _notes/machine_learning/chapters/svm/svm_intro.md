---
title: "Support Vector Machines"
---

# Support Vector Machines

Maximal margin classifier is the first idea for the development towards SVMs. Maximal margin classifier utilizes hyperplanes and requires that the data is linearly separable. The extension of this is Support Vector Classifier that can be applied to an even broader class of problems where classes may not be perfectly separable. SVMs are a further extension of SVCs to account for non linear separation boundaries.

##### Hyperplane

in a $p$-dimensional space is a surface that is an affine subspace (means it need not pass through origin) in the $p-1$ dimensional space. For a 2D space it will be a 1D line, for a 3D space it will be a 2D plane, and so on. The equation is of the form
\begin{align}
        \beta_{0} + \beta_{1}X_{1} + \beta_{2}X_{2} + \cdots + \beta_{p}X_{p} = 0
    \end{align}
Any point in the vector space can fall into one of the three regions
\begin{align}
        \beta_{0} + \beta_{1}X_{1} + \beta_{2}X_{2} + \cdots + \beta_{p}X_{p} \begin{cases}
            > 0\newline
            = 0\newline
            > 0
        \end{cases}
    \end{align}
and thus a hyperplane can be a useful demarcation between two regions or classes.


From now on, let $\beta^{T} = (\beta_{1}, \ldots, \beta_{p})$, $x^{T} = (x_{1}, \ldots, x_{p})$, $\beta_{0}$ be a scalar, and $N$ denote the total number of training data points. Although not represented by a bold font, $\beta$ and $x$ are both vectors. Since $\beta^{T}x$ is a scalar, $\beta^{T}x = x^{T}\beta$.
