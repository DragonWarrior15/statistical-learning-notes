---
title: "Determinant"
---

Determinant is defined for square matrices and represents a transformation from $\real^{n \times n} \to \real$. Its defined as follows for $2 \times 2$ and $3 \times 3$ matrices
\begin{align}
    A &= [a]\newline
    \detm{A} &= a\newline
    A &= \begin{bmatrix}
        a &b\newline c &d
    \end{bmatrix}\newline
    \detm{A} &= ac - bd\newline
    A &= \begin{bmatrix}
        a &b &c\newline d &e &f\newline g &h &i
    \end{bmatrix}\newline
    \detm{A} &= a(ei-hf) - b(di - gf) + c(dh - ge)
\end{align}

More precisely, read below on how the formula is derived

### Minors
For any element $a_{ij}$ of the matrix $A$, the minor $M_{ij}$ is the determinant of the matrix obtained after removing the $i$ row and $j$ column.

Since the determinant of a single element is the element itself, the minor of any element of a $2 \times 2$ matrix is the diagonally opposite element.

### Cofactors
The minor $M_{ij}$ multiplied by $(-1)^{i+j}$ is called the cofactor $C_{ij}$.
\begin{align}
    C_{ij} = (-1)^{i+j}M_{ij}
\end{align}

### Adjoint
The transpose of the matrix obtained after replacing all the elements of the matrix with their cofactors is called adjoint, Adj(A). The adjoint is thus another matrix.
\begin{align}
    Adj(A)\_{ij} = [C_{ij}]^{T}
\end{align}

* A $\times$ Adj(A) = $\detm{A} \times$ I
* $A^{-1} = \frac{1}{\detm{A}} Adj(A)$

### Calculating the Determinant
Let $A$ be a $n \times n$ matrix. Consider any row (or column) $i$ of the matrix.
\begin{align}
    \detm{A} = \sum_{j=1}^{n} a_{ij} C_{ij}
\end{align}

Thus, the determinant can be obtained by expansion along any row or column. In calculation of the cofactors, the $\pm$ sign will keep alternating as is evident from the above formula. We can verify that the definition for determinants of $2 \times 2$ and $3 \times 3$ can be derived from this formula.

### Properties of Determinant
* Changing rows and columns does not change the value of the determinant $\detm{A^{T}} = \detm{A}$
* If any row or column of the matrix is zero, then $\detm{A} = 0$
* If any two rows or columns of the matrix are interchanged, the determinant is multiplied by -1
* If any two rows or columns of the matrix are identical, then $\detm{A} = 0$ as well
    * follows from the last point
* If all the elements of one row (or column) are multiplied by the same number k, the determinant is also multiplied by k
* If $A$ is $n \times n$, then $\detm_{kA} = k^{n}\detm_{A}$
* The sum of the products of the elements of any row (or column) with the cofactors of some other row (or column) is 0
    * sum of products with cofactors of the same elements is the determinant
* The value of determinant is unchanged by addition of a scalar multiple of a row (or column) to another row (or column)
* $\detm{AB} = \detm{A} \detm{B}$
    * It follows that $\detm{A^{n}} = \detm{A}^{n}$
    * $\det{A} \det{A^{-1}} = 1$
* Determinant of an upper triangular or lower triangular or diagonal matrix is the multiplication of all the diagonal elements
* Determinant of a skew-symmetric matrix of odd order is 0
* $\detm{Adj(A)} = \detm{A}^{n-1}$
* If the determinant of a matrix is non zero, then the matrix has full rank, or all its rows and columns are linearly independent, and the matrix is invertible.
