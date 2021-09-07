---
title: Special Matrices
---

## Special Matrices

### Identity Matrix
A square matrix whose all elements are zeros except the diagonal elements which are all 1.
* $AI = IA = A$
* $I^{n} = I$
* $I^{-1} = I = I^{T}$
* $\detm{I} = 1$
* The columns or rows form the basis of $\real^{n}$
* All eigenvalues are same and equal to 1

Identity matrix of size $n \times n$ is denoted by $I_{n}$.
\begin{align}
    I_{3} = \begin{bmatrix} 1 &0 &0\newline 0 &1 &0\newline 0 &0 &1 \end{bmatrix}
\end{align}

### Null Matrix
Any matrix with all elements 0 is called a null matrix (it need not be square). A square null matrix of size $n$ is denoted by $O_{n}$
* $\detm{O_{n}} = 0$
* A + O = O + A = A

### Upper Triangular Matrix
A square matrix in which all the elements below the main diagonal are 0, i.e., $a_{ij} = 0 \: \forall i > j$.
* $\detm{A}$ = product of all the diagonal elements
* eigenvalues(A) are the diagonal elements

### Lower Triangular Matrix
A square matrix in which all the elements above the main diagonal are 0, i.e., $a_{ij} = 0 \: \forall i < j$
* $\detm{A}$ = product of all the diagonal elements
* eigenvalues(A) are the diagonal elements

### Idempotent Matrix
Any square matrix which satisfies $A^{2} = A$. Null matrix and identity matrix are examples of such matrices.

### Involuntary Matrix
A square matrix which satisfies $A^{2} = I$.

### Nilpotent Matrix
A matrix $A$ is said to be nilpotent of class $x$ if $x$ is the smallest index such that $A^{x} = O$ and $A^{x-1} \neq O$.

### Singular Matrix
A square matrix is singular if its determinant is 0. Equivalently, a square matrix is non-singular if its determinant is non-zero. A singular matrix is not invertible.

### Symmetrix MAtrix
A square matrix is symmetric if $a_{ij} = a_{ji} \: \forall i,j$. Or simply, if $A^{T} = A$.

For any matrix A
* $AA^{T}$ is always symmetric
* $(A + A^{T})/2$ is always symmetric
* If A and B are symmetric, A + B and A - B are also symmetric

### Skew Symmetric Matrix
A square matrix is skew symmetric if $a_{ij} = a_{ji} \: \forall i,j$. This is equivalent to saying $A^{T} = -A$.
* A skew symmetric matrix must have all zeros in the diagonal $(A = A^{T} = O)$
* $(A - A^{T})/2$ is always skew symmetric

Any square matrix can be expressed as a sum of a symmetric and a skew symmetric matrix
\begin{align}
    A = \frac{A + A^{T}}{2} + \frac{A - A^{T}}{2}
\end{align}

### Orthogonal Matrix
**Orthogonal** or **orthonormal** matrix is a matrix whose rows and columns are orthonormal vectors. An orthogonal matrix $Q$ will satisfy
\begin{align}
    QQ^{T} &= Q^{T}Q = I\newline
    Q^{-1} &= Q^{T}\newline
    det(Q) &= \pm 1
\end{align}

The last one follows from the fact that
\begin{align}
    1 = det(I) = det(QQ^{T}) = det(Q)^{2}
\end{align}

* Orthogonal matrices play an important role in QR decomposition and SVD.
* If A and B are orthogonal matrices, then AB and BA are also orthogonal
* If matrix A is orthogonal, then $\detm{A} = \pm 1$, but the converse is not always true
