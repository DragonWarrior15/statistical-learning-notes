---
title: "Exercises"
---

# Exercises

1.  **Blocks and Diagonalization**

    Suppose $A$ is diagonalizable as $S \Lambda S^{-1}$. Diagonalize the block matrix
    \begin{align}
            B = \begin{bmatrix}
                A &0\newline 0 &2A
            \end{bmatrix}
        \end{align}
    and find its eigenvalues and eigenvectors.

    **Solution**

    We break $B$ into three component block matrices made up of $S$, $\Lambda$, and $S^{-1}$.
    \begin{align}
            B = \begin{bmatrix}
                A &0\newline 0 &2A
            \end{bmatrix} =
            \begin{bmatrix}
                S\Lambda S^{-1} &0\newline 0 &2S\Lambda S^{-1}
            \end{bmatrix} =
            \begin{bmatrix}
                S &0\newline 0 &S
            \end{bmatrix}
            \begin{bmatrix}
                \Lambda &0\newline 0 &2\Lambda
            \end{bmatrix}
            \begin{bmatrix}
                S^{-1} &0\newline 0 &S^{-1}
            \end{bmatrix}
        \end{align}
    We can verify that the above multiplications give back the original block matrix $B$. Further,
    \begin{align}
            \begin{bmatrix}
                S &0\newline 0 &S
            \end{bmatrix}
            \begin{bmatrix}
                S^{-1} &0\newline 0 &S^{-1}
            \end{bmatrix} =
            \begin{bmatrix}
                I &0\newline 0 &I
            \end{bmatrix} = I_{2n}
        \end{align}

    Hence, the above form is the correct diagonalized form of $B$ with the eigenvectors
    \begin{align}
            \begin{bmatrix}
                S &0\newline 0 &S
            \end{bmatrix}
        \end{align}
    and eigenvalues $(\lambda, 2\lambda)$ where $\lambda$ are all the diagonal entries of $\Lambda$ (eigenvalues of $A$).
