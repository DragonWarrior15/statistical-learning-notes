---
title: "Algebraic Properties of Matrices"
---

### Trace
For any square matrix, the **trace** is defined as the sum of all the diagonal elements. Specifically, for a matrix $A$ of size $n$, $trace(A) = \sum_{i=1}^{n} a_{ii}$. Trace is also denoted by $Tr()$.
* Tr($\lambda$A) = $\lambda$Tr(A)
* Tr(A + B) = Tr(A) + Tr(B)
* Tr(AB) = Tr(BA)

The last statement can be proved by writing out the product.

### Transpose
Let A be a $m \times n$ matrix. Then the $n \times m$ matrix obtained by switching the rows and columns is called the transpose and is denoted by $A^{T}$.
\begin{align}
A &= \begin{bmatrix} 1 &2\newline 3 &4\newline 5 &6\newline \end{bmatrix}\newline
A^{T} &= \begin{bmatrix} 1 &3 &5\newline 2 &4 &6 \end{bmatrix}
\end{align}

* $(A^{T})^{T}$ = A
* $(A + B)^{T}$ = $A^{T} + B^{T}$
* $(AB)^{T}$ = $B^{T}A^{T}$
* $(ABC)^{T}$ = $C^{T}B^{T}A^{T}$
* $(kA)^{T}$ = $kA^{T}$ (k being any complex number)

### Conjugate Matrix
The matrix obtained by taking complex conjugate of all the elements of the given matrix A is called its conjugate matrix and is denoted by $\bar{A}$.

The real numbers remain unchanged, but for the complex numbers, the sign of the imaginary part is reversed ($2 + 3i$ becomes $2 - 3i$).

* $\bar{(\bar{A})} = A$
* $\detm{\bar{A}} = \bar{\detm{A}}$
* $\bar{(A + B)} = \bar{A} + \bar{B}$
* $\bar{(kA)} = \bar{k}\bar{A}$
* $\bar{(AB)} = \bar{A}\bar{B}$
* $\bar{A} = A$ if A is real

Transposed conjugate of a matrix is defined as $(\bar{A})^{T}$ and is denoted by $A^{\theta}$ or $A^{\*}$.

* $(A^{\theta})^{\theta} = A$
* $\detm{A^{\theta}} = \detm{A}$
* $(A + B)^{\theta} = A^{\theta} + B^{\theta}$
* $(kA)^{\theta} = \bar{k}A^{\theta}$
* $(AB)^{\theta} = B^{\theta}A^{\theta}$ (order is reversed because of the transpose)

### Complex Matrices
* **Hermitian Matrix**: $A^{\theta} = A$
* **Skew-Hermitian Matrix**: $A^{\theta} = -A$
* **Unitary Matrix**: $A^{\theta} = A^{-1}$ or $AA^{\theta} = I$

Properties
* $(A + B)^{\theta} = A^{\theta} + B^{\theta}$
* $(AB)^{\theta} = B^{\theta}A^{\theta}$
* The diagonal elements of a Hermitian matrix are necessarily real (otherwise the conjugate will change the values)
* Every square matrix A can be written a sum of Hermitian and Skew-Hermitian matrix
    \begin{align}
        A = \frac{A + A^{\theta}}{2} + \frac{A - A^{\theta}}{2}
    \end{align}
* Absolute value of the determinant of a unitary matrix is 1
    \begin{align}
        AA^{\theta} &= I\newline
        \detm{AA^{\theta}} &= \detm{A} \detm{A^{\theta}} = \detm{A}^{2} = 1
    \end{align}
