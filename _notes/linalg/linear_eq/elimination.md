---
title: "Linear Equations"
---

<!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
# Linear Equations
## Gauss Jordan Elimination
This method of solving linear equations uses three elementary matrix operations
* Shuffle rows of the matrix
* Multiply a row with a non zero scalar
* Add or subtract scalar multiple of a row from another row

The purpose of elimination is to convert the matrix to a reduced row echelon form (RREF) which has the following characteristics
* All rows with only zero entries are at the bottom of the matrix
* The first non zero entry in a row called the leading entry or the pivot of each non zero row is to the right of the leading entry of the row above it
* The leading entry in any non zero row is 1 (not required in row echelon form)
* All other entries in a column containing a leading 1 are zeros (not requried in row echelon form)

The following are the steps to perform the elimination algorithm
* Swap the rows so that all rows with 0 entries are at the bottom of the matrix
* Swap the rows so that the row with the largest leftmost non zero entry is at the top
* Multiply the top row by a scalar so that the leftmost entry becomes 1
* Add or subtract multiples of the top row from all the other rows so that all the entries in the column containing the topmost row's leading entry apart from the topmost row become 0
* Ignoring the first column, repeat steps 2-4 for the next leftmost entry until all the leading entries are 1
* Swap the rows so that the leading entry of each nonzero row is to the right of the leading entry of the row above it
* Any column with all zero entries denotes an undeterminate variable

As an example, consider solving the following system of equations
\begin{align}
    x + 2y + z &= 2\newline
    3x + 8y + z &= 12\newline
    4y + z &= 2\newline
    \text{or, } \begin{bmatrix}
    1 &2 &1\newline
    3 &8 &1\newline
    0 &4 &1\newline
    \end{bmatrix}
    \begin{bmatrix}
        x\newline y\newline z
    \end{bmatrix} &= \begin{bmatrix}
        2\newline 12\newline 2
    \end{bmatrix}
\end{align}
The matrix we will work with during the algorithm is a composite matrix $A \vert b$, also called the augmented matrix
\begin{gather}
    \begin{bmatrix}
    1 &2 &1 &\vert &2\newline
    3 &8 &1 &\vert &12\newline
    0 &4 &1 &\vert &2\newline
    \end{bmatrix} \overset{R_{1} \leftrightarrow R_{2}}\rightarrow
    \begin{bmatrix}
    3 &8 &1 &\vert &12\newline
    1 &2 &1 &\vert &2\newline
    0 &4 &1 &\vert &2\newline
    \end{bmatrix} \overset{R_{1}/3}\rightarrow
    \begin{bmatrix}
    1 &8/3 &1/3 &\vert &4\newline
    1 &2 &1 &\vert &2\newline
    0 &4 &1 &\vert &2\newline
    \end{bmatrix} \overset{R_{2} - R_{1}}\rightarrow
    \begin{bmatrix}
    1 &8/3 &1/3 &\vert &4\newline
    0 &-2/3 &2/3 &\vert &-2\newline
    0 &4 &1 &\vert &2\newline
    \end{bmatrix}\newline
    \overset{R_{2} / (-2/3)}\rightarrow
    \begin{bmatrix}
    1 &8/3 &1/3 &\vert &4\newline
    0 &1 &-1 &\vert &3\newline
    0 &4 &1 &\vert &2\newline
    \end{bmatrix} \overset{R_{1} - (8/3) R_{2}}\rightarrow
    \begin{bmatrix}
    1 &0 &3 &\vert &-4\newline
    0 &1 &-1 &\vert &3\newline
    0 &4 &1 &\vert &2\newline
    \end{bmatrix} \overset{R_{3} - 4 R_{2}}\rightarrow
    \begin{bmatrix}
    1 &0 &3 &\vert &-4\newline
    0 &1 &-1 &\vert &3\newline
    0 &0 &5 &\vert &-10\newline
    \end{bmatrix}\newline
    \overset{R_{3}/5}\rightarrow
    \begin{bmatrix}
    1 &0 &3 &\vert &-4\newline
    0 &1 &-1 &\vert &3\newline
    0 &0 &1 &\vert &-2\newline
    \end{bmatrix} \overset{R_{1} - 3R_{3}}\rightarrow
    \begin{bmatrix}
    1 &0 &0 &\vert &2\newline
    0 &1 &-1 &\vert &3\newline
    0 &0 &1 &\vert &-2\newline
    \end{bmatrix} \overset{R_{2} + R_{3}}\rightarrow
    \begin{bmatrix}
    1 &0 &0 &\vert &2\newline
    0 &1 &0 &\vert &1\newline
    0 &0 &1 &\vert &-2\newline
    \end{bmatrix}
\end{gather}
which is the RREF of the matrix. We can directly read the solutions as
\begin{align}
    x = 2, y = 1, z = -2
\end{align}

The RREF of a matrix is unique. A column in this augmented matrix which contains a leading $1$ is called a pivot column, and the variables corresponding to these columns are called the pivot variables. All the other variables in the matrix are called free variables. In the RREF, we can check the types of solutions as
* **No solution**: If one of the rows in the augmented matrix contains all zeros except the rightmost entry, no solution is possible since the equation is of the form $0 = 1$.
* **Infinitely many solutions**: If there is a free variable in the matrix, we can set it to any value and still obtain a solution.
* **Unique solution**: If none of the above two cases happen, the augmented matrix only contains pivot variables, and thus has a single unique solution.

We can also calculate the rank of the matrix from the RREF. The number of non-zero rows in the RREF is the rank of the matrix. By getting the RREF of the augmented matrix, we can get the ranks of both $A$ and $A\vert b$.

### Rank of Augmented Matrix and Existence of Solutions
To determine the number of solutions to the equation $Ax = b$ with $n$ unknowns, we can compare the ranks of $A$ and the augmented matrix $A \vert b$
* No solution: if and only if $rank(A) < rank(A\lvert b)$
* Unique solution: if and only if $rank(A) = rank(A\vert b) = n$
* Infinitely many solutions: if and only if $rank(A) = rank(A\vert b) < n$

In the previous example where we demonstrated Gauss-Jordan elimination, the RREF of the augmented matrix was
\begin{align}
    \begin{bmatrix}
    1 &0 &0 &\vert &2\newline
    0 &1 &0 &\vert &1\newline
    0 &0 &1 &\vert &-2\newline
    \end{bmatrix}
\end{align}

Clearly, the number of pivot columns in the above is $3$, $\implies$ rank$(A \vert b)$ = $3$. From the above, we can also read off that the rank$(A) = 3$. Hence, rank$(A) =$ rank$(A \vert b) = 3$ (number of unknowns). Hence, there is a unique solution.
