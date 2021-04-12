---
title: "Matrix"
---

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
## Matrix
The matrix of a linear map $\matm(T)$ is defined with respect to a set of basis for $\setv$ and $\setw$. The entries of $\matm(T)$ are defined as
\begin{align}
    Tv_{k} = A_{1,k}w_{1} + A_{2,k}w_{2} + \cdots + A_{m,k}w_{m} \; k=1,\ldots, n
\end{align}
where $v_{1}, \ldots, v_{n}$ and $w_{1}, \ldots, w_{m}$ are the basis vectors of $\setv$ and $\setw$ respectively. $\matm(T)$ is a $m$-by-$n$ matrix and each element $\in \field$. Unless stated otherwise, we will use the standard basis.
It is important to note that the matrix of a linear map is always defined with respect to a set of basis vectors.


<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
### Addition and Multiplication
Addition of matrices of the same size is defined as matrix whose each element is the sum of the corresponding elements of the two matrices.
\begin{align}
    (A+B)\_{i,j} = A_{i,j} + B_{i,j}
\end{align}

Thus, the matrix of sum of linear maps is the sum of matrices of those linear maps
\begin{align}
    \matm(S + T) = \matm(S) + \matm(T) \quad S, T \in \setlm(\setv, \setw)
\end{align}

The scalar multiplication with $\lambda \in \field$ is same as multiplying each element of the original matrix with $\lambda$
\begin{align}
    (\lambda A)\_{i,j} = \lambda (A_{i,j})
\end{align}

Thus, the matrix of a scalar times a linear map is same as the scalar times the matrix of the linear map
\begin{align}
    \matm(\lambda T) = \lambda \matm(T) \quad T \in \setlm(\setv, \setw)
\end{align}

We will denote the set of all $m-$by$-n$ matrices with elements in $\field$ by $\field^{m,n}$. This set of all matrices is also a vector space on the addition and scalar multiplication rules for matrices defined above. The basis for such space is the collection of all matrices with all but one element zeros, and one element 1. There are $mn$ such matrices meaning dim $\field^{m,n} = mn$.


<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
### Matrix Multiplication
Matrix multiplication is important to define in order to work with product of linear maps. We wish to have the following hold
\begin{align}
    \matm(ST) = \matm(S) \matm(T) \quad T \in \setlm(U, \setv), S \in \setlm(\setv, \setw)
\end{align}
For two matrices $A$ and $B$ of sizes $m$-by-$n$ and $n$-by-$p$ respectively, their matrix multiplication is defined as
\begin{align}
    (AB)\_{i,j} = \sum_{k=1}^{p} A_{i,k}B_{k,j}
\end{align}
Which is the sum product of the $i^{th}$ row of $A$ and $j^{th}$ column of $B$. Notice that the matrices have one dimension same. It is a necessary condition for the multiplication to be valid and also implies that the range of $T$ is same as domain of $S$. Furthermore, $AB$ is of size $m$-by-$p$.

Matrix multiplication is not commutative (since the multiplication may not be defined or the products may not be the same otherwise), but is distributive and associative.


<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
### Inverse Linear Map
A linear map $T \in \setlm(\setv, \setw)$ is invertible if there exists $T \in \setlm(\setw, \setv)$ such that $ST$ is the identity map on $\setv$ and $TS$ is the identity map on $\setw$. $S$ is said to be the inverse of $T$ with $ST = I$ and $TS = I$, and there exists a unique inverse for a linear map (can be proven by contradiction).

We denote the unique inverse of a linear map $T \in \setlm(\setv, \setw)$ with $T^{-1} \in \setlm(\setw, \setv)$ and they satisfy $TT^{-1} = I$ and $T^{-1}T = I$.

A linear map is invertible if and only if it is both injective and surjective. To prove this, we first assume the linear map to be invertible and show that the latter part of statement is true and vice versa.

Two vector spaces are isomorphic if there is an isomorphism (an invertible linear map) from one vector space onto the other.


<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
### Operator
A linear map from a vector space onto itself is called an operator. $\setlm(\setv)$ denotes the set of all operators from $\setv$ onto itself. It is the same notation as $\setlm(\setv) = \setlm(\setv, \setv)$.

On a finite dimensional vector space $\setv$, any linear map $T \in \setlm(\setv)$ is \textbf{invertible}, \textbf{injective} and \textbf{surjective}.

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
### Rank of a Matrix
Suppose $A \in \field^{m, n}$. Row and column ranks are two non negative integers defined as
* Row Rank: Dimension of the span of the rows of $A$ in $\field^{1, n}$
* Column Rank: Dimension of the spaan of the columns of $A$ in $\field^{m, 1}$

But for any $A \in \field^{m, n}$, row rank $=$ column rank (can be proved using duality). Hence, we simply use the word rank to denote the column rank of a matrix.

Rank is defined for a matrix, whereas dimension is defined for a vector space. This is the important distinction between the two. The rank can be found by counting the number of non-zero rows in the row echelon form of a matrix ([see here]({% link _notes/linalg/linear_eq/elimination.md %})).

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
#### Rank-Nullity Theorem
We restate the theorem from [fundamental theorem of linear maps]({% link _notes/linalg/linear_maps/linear_maps.md %}) using the concepts of dimension and ranks. For any vector spaces $V$ and $W$, and linear map $T \in \setlm(\setv, \setw)$
\begin{align}
    \text{rank}(T) + \text{Nullity}(T) = \text{dim}(V)
\end{align}
where dim$(V)$ is the number of basis vectors of the vector space $V$. Usually, the dim$(V)$ is the number of columns in the matrix $T$. For a matrix, the dimension of the null space will be determined by the number of basis vectors of the solution set to $Ax=0$.

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
### Block Matrix
Sometimes, block matrices can help simplify cumbersome operations. For the purpose of demonstration, consider a matrix $A$ of dimensions $n \times n$, which we break into four blocks: $B$ of size $m \times m$, $C$ of size $m \times n-m$, $D$ of size $n-m \times m$, and $E$ of size $n-m \times n-m$. Then,
\begin{align}
    A = \begin{bmatrix}
        B &C\newline D &E
    \end{bmatrix}
\end{align}
Then, the calculation of $A^{2}$ is
\begin{align}
    A^{2} &= \begin{bmatrix}
        B &C\newline D &E
    \end{bmatrix}
    \begin{bmatrix}
        B &C\newline D &E
    \end{bmatrix} =
    \begin{bmatrix}
        B^{2} + CD &BC + CE\newline DB + ED &DC + E^{2}
    \end{bmatrix}
\end{align}

We obtained $B^{2}$ using $2 \times 2$ multiplication on the four elements of the block matrix. All the multiplications agree in terms of the dimensions. This technique is especially useful when the matrix can be broken in such a way that individual matrix are identity matrix, diagonal matrix etc.

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
### Orthogonal Matrix
Orthogonal or \textbf{orthonormal} matrix is a matrix whose rows and columns are orthonormal vectors. An orthogonal matrix $Q$ will satisfy
\begin{align}
    QQ^{T} &= Q^{T}Q = I\newline
    Q^{-1} &= Q^{T}\newline
    det(Q) &= \pm 1
\end{align}

The last one follows from the fact that
\begin{align}
    1 = det(I) = det(QQ^{T}) = det(Q)^{2}
\end{align}

Orthogonal matrix play an important role in QR decomposition and SVD.

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
### Determinant
Determinant is defined for square matrices and represents a transformation from $\real^{n \times n} \to \real$. Its defined as follows for $2 \times 2$ and $3 \times 3$ matrices
\begin{align}
    A &= \begin{bmatrix}
        a &b\newline c &d
    \end{bmatrix}\newline
    det(A) &= ac - bd\newline
    A &= \begin{bmatrix}
        a &b &c\newline d &e &f\newline g &h &i
    \end{bmatrix}\newline
    det(A) &= a(ei-hf) - b(di - gf) + c(dh - ge)
\end{align}

The term outside the bracket is the entry from the first row, and the entry inside the brackets is the determinant of the $n-1 \times n-1$ matrix formed by not considering the first row and the column corresponding to the entry outside the bracket. We put alternating $+$ and $-$ signs before each term. This way the definition extends to any $n \times n$ matrix.

If the determinant of a matrix is non zero, then the matrix has full rank, or all its rows and columns are linearly independent, and the matrix is invertible.
