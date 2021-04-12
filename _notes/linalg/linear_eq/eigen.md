---
title: "Eigenvectors and Eigenvalues"
---

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
## Eigenvectors and Eigenvalues
For a matrix $A \in \field^{n, n}$, eigenvalues $\lambda$ and eigenvectors $x$ are the solutions to the equation $Ax = \lambda x$. Eigenvalues are only applicable to square matrices, similar to how determinants are defined for only them. The motivation for solving this type of equations can be seen in coupled differential equations.

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
### Motivation from Differential equation
For a single equation, the solution is an exponential
\begin{align}
    \frac{du}{dt} &= au\newline
    u(t) &= ce^{at}
\end{align}
where $a$ and $c$ (obtained from initial conditions) are scalars. Consider a coupled system
\begin{align}
    \frac{dv}{dt} &= 4v - 5w\newline
    \frac{dw}{dt} &= 2v - 3w
\end{align}
Representing $v$ and $w$ by a vector $u$, we can write the above system in a matrix form
\begin{align}
    \frac{du}{dt} &= \begin{bmatrix}
        4 &-5\newline
        2 &-3
    \end{bmatrix}u
\end{align}
Assuming that we are looking for purely exponential solutions $v = e^{\lambda t}y$ and $w = e^{\lambda t}z$ (similar to the one variable case), define $x = (v, w)^{T}$
\begin{align}
    u(t) &= e^{\lambda t}x\newline
    \implies \frac{du}{dt} &= \lambda u\newline
    \implies \begin{bmatrix}
        4 &-5\newline
        2 &-3
    \end{bmatrix}u &= \lambda u
\end{align}

the solutions of which are the eigenvalues and eigenvectors of the transformation matrix. Thus, the differential equation problem is now converted to one from linear algebra.

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
### Back to the Equation
Coming back to the core equation of this part, $Ax = \lambda x$. We can rewrite this $(A - \lambda I)x = 0$. $x = \mathbf{0}$ will always be a solution to this. However, we are looking for non-zero solutions to the equation. They will exist only if $x$ lies in the null space of $A - \lambda I$; which exists only if this matrix is singular. That is,
\begin{align}
    det(A - \lambda I) = 0
\end{align}

This can be solved by writing out the determinant of $A - \lambda I$ in terms of $\lambda$ and solving the roots of the obtained polynomial, also called the characteristic polynomial of $A$. The $n$ roots are the $n$ eigenvalues of the matrix $A$.

Once the eigenvalues are known, they can be substituited back into the equation $A - \lambda I)x = 0$ to solve for $x$ (nonzero solution will exist since $A - \lambda I$ is singular). It is important to note that if $x_{1}$ is an eigenvector of $A$, then so is any scalar multiple of it.

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
### Algebraic and Geometric Multiplicity
* **Algebraic Multiplicity**: The count of repetitions of a particular eigenvalue.

    Since the characteristic polynomial can be written as the product of all the roots, the number of terms should equal $n$. The powers of each of the factor denotes how many times the root is repeated and is called the algebraic multiplicity of that root (eigenvalue).
    \begin{align}
        det(A - \lambda I) &= 0 = (\lambda - \lambda_{1})^{\mu_{1}} \cdots (\lambda - \lambda_{k})^{\mu_{k}}\newline
        n &= \mu_{1} + \cdots + \mu_{k}
    \end{align}
* **Geometric Multiplicity**: Represents the dimension of the eigenspace associated with the eigenvectors corresponding to the eigenvalue.

    the eigenspace of an eigenvalue $\lambda$ is the dimension of the null space of $A - \lambda I$ and equals the number of linearly independent eigenvectors corresponding to $\lambda$.
    \begin{align}
        \gamma_{i} = n - rank(A - \lambda_{i}I)
    \end{align}
    using the rank-nullity theorem on $A - \lambda_{i}I$.

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
### Properties of Eigenvalues and Eigenvectors
Eigenvalues have special properties listed below
* The sum of eigenvalues is the trace of the matrix (sum of elements along the diagonal).

    This can be verified by considering the polynomial expansion of det$(A - \lambda I) = 0$. The sum of roots of this polynomial (which is the sum of eigenvalues) is the coefficient of $(-\lambda)^{n-1}$ (from Vieta's formulas) which comes out to be the sum of diagonal elements.
* The product of eigenvalus is the determinant of the matrix.
* If any eigenvalue is $0$, the matrix is singular (not invertible). This follows from above.
* If all eigenvalues are non-zero, the dimension of the null space is $0$ (because the only solution to $Ax = 0 = 0x$ is the trivial solution, all zeros). By the [rank nullity theorem]({{ site.baseurl }}/notes/linalg/linear_maps/matrix.html#rank-nullity-theorem), rank$(A) = n$.
* Eigenvalues of the $A^{-1}$ are the reciprocals of the eigenvalues of $A$ for the corresponding eigenvector. Consider an eigenvalue $\lambda$ and the corresponding eigenvector $x$
    \begin{align}
         Ax &= \lambda x \implies A^{-1}Ax = \lambda A^{-1}x\newline
         \text{or,} \quad A^{-1}x &= \frac{1}{\lambda}x
    \end{align}
    The eigenvectors remain the same.
* Powers of matrix. For a natural number n, eigenvalues of $A^{n}$ are the eigenvalues of $A$ raised to the $n^{th}$ power for the corresponding eigenvectors $x$\begin{align}
        Ax = \lambda x \implies A^{2}x = \lambda Ax = \lambda^{2}x
    \end{align}
    The same logic extends to the higher powers recursively.
* Eigenvalues of $A + \alpha I$ are simply $\lambda + \alpha$, where $\alpha$ is a scalar. Consiering a pairing $\lambda$ and $x$,
    \begin{align}
        Ax &= \lambda x \implies Ax + \alpha Ix = \lambda Ix + \alpha Ix = (\lambda + \alpha)Ix = (\lambda + \alpha)x\newline
        \implies (A + \alpha I)x &= (\lambda + \alpha)x
    \end{align}
    with the eigenvalues remaining the same.
* Eigenvalues of $A$ and $A^{T}$ are same
    \begin{align}
        det(A - \lambda I) = det((A - \lambda I)^{T}) = det(A^{T} - \lambda I)
    \end{align}
    since the two polynomials are same, their roots will also be the same and so will the eigenvalues. Further, we define the left and right eigenvalues/eigenvectors of $A$. Left eigenvalues satisfy $Ax = \lambda x$ while the right eigenvalues satisfy $yA = \nu y$. Taking transpose of this equation, $A^{T}y^{T} = \nu y^{T}$. Since $A$ and $A^{T}$ share the same eigenvalues, the left eigenvector of $A$ is same as the transpose of the right eigenvector of $A$.
* If $A$ has $n$ distinct eigenvalues, it automatically has $n$ independent eigenvectors as well.
* If $A$ has $n$ independent eigenvectors, then they form a basis of $\field^{n}$.

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
### Diagonalization of a Matrix
Let $A$ have $n$ independent eigenvectors, and let $S$ denote the matrix whose columns are the $n$ independent eigenvectors. Also, let $\Lambda$ denote the matrix with all entries zeros, except the diagonal whose $n$ values are the corresponding $n$ eigenvalues of $A$. Then,
\begin{align}
    AS &= S\Lambda \implies S^{-1}AS = S^{-1}S\Lambda = \Lambda\newline
    \text{or,} \: A &= S \Lambda S^{-1}
\end{align}

Not all matrices are diagonalizble this way. An important requirement is the presence of $n$ independent eigenvectors. A matrix with shortage of eigenvectors (for instance, one with repeated eigenvalues) may not be diagonalizable (may not be since identity matrix has a single eigenvalue, but is diagonalizable).

The matrix of eigenvectors $S$ need not be unique. Any scalar multiple of an eigenvector is also an eigenvector. Only the matrix containing the eigenvectors can produce the diagonal matrix $\Lambda$.

\textbf{Eigenvectors from distinct eigenvalues are automatically independent}. Consider any two distinct eigenvalues $\lambda_{1}$, $\lambda_{2}$ and the corresponding eigenvectors $x_{1}$, $x_{2}$. To show independence, consider the solution to
\begin{align}
    c_{1}x_{1} + c_{2}x_{2} &= 0\newline
    \implies Ac_{1}x_{1} + Ac_{2}x_{2} &= 0\newline
    \implies c_{1}\lambda_{1}x_{1} + c_{2}\lambda_{2}x_{2} &= 0\newline
    \implies c_{1}\lambda_{1}x_{1} + c_{2}\lambda_{2}x_{2} - \lambda_{1}(c_{1}x_{1} + c_{2}x_{2}) &= 0\newline
    \implies c_{2}(\lambda_{2} - \lambda_{1})x_{2} &= 0
\end{align}

Since $\lambda_{1} \neq \lambda_{2}$ and $x_{2} \neq \mathbf{0}$, we must have $c_{2} = 0$ and consequently $c_{1} = 0$. This means that $x_{1} \perp x_{2}$. The idea can be extended to a combination of $k$ eigenvectors and eigenvalues as well using the same logic. Hence, it follows that distinct eigenvalues automatically imply independent eigenvectors corresponding to them.

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
#### Powers of a Matrix
Computation of the natural powers of a matrix that is diagonalizable is straightforward using eigenvalues and eigenvectors. Recall, that the natural power of a matrix $A$ has the same eigenvectors as $A$ and the eigenvalues are raise to the same power.
\begin{align}
    A^{2} &= (S \Lambda S^{-1})(S \Lambda S^{-1}) = S \Lambda^{2} S^{-1}\newline
    A^{n} &= S \Lambda^{n} S^{-1}
\end{align}

The entries of $\Lambda^{n}$ are same as the entries of $\Lambda$ raised to the $n^{th}$ power. Thus, once the matrix $S$ and $\Lambda$ are known, calculation of higher powers is quick.

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
#### Cayley-Hamilton Theorem
Cayley-Hamilton theorem states that the charecteristic equation of a given matrix is satisfied by the matrix itself. Using this equation, it is easy to calculate certain powers of the matrix and its inverse. Consider the following matrix
\begin{align}
    A = \begin{bmatrix}
        1 &2\newline 3 & 4
    \end{bmatrix}
\end{align}

The characteristic equation is
\begin{align}
    det(A - \lambda I) &= 0\newline
    (1-\lambda)(4-\lambda) - 2 \times 3 &= 0\newline
    \lambda^{2} - 5\lambda - 2 &= 0
\end{align}

Then, the matrix itself will satisfy this equation, i.e.,
\begin{align}
    A^{2} - 5A - 2I_{2} = 0_{2}
\end{align}

where the right hand side is the $2 \times 2$ matrix with all zeros. One can verify that the equation indeed holds true by substituiting the values of $A$ and $A^{2}$.

With this equation, we can calculate the different powers as follows
\begin{align}
    A^{2} &= 5A + 2I_{2}\newline
    A^{3} &= A^{2}A = 5A^{2} + 2A = 5(5A + 2I_{2}) + 2A = 27A + 10I_{2}\newline
    A^{4} &= A^{3}A = 27A^{2} + 10A = 145A + 54I_{2}\newline
\end{align}

Inverse can also be expressed in terms of $A$

\begin{align}
    A^{2} - 5A - 2I_{2} &= 0\_{2}\newline
    A^{-1}A^{2} - 5A^{-1}A - 2A^{-1}I_{2} &= A^{-1}0\_{2}\newline
    A - 5I_{2} - 2A^{-1} &= 0\_{2}\newline
    A^{-1} &= \frac{1}{2} \bigg( A - 5I_{2} \bigg)
\end{align}
