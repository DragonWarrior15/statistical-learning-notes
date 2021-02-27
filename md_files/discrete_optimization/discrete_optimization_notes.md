# Discrete Optimization
***

## Knapsack Problem
Knapsack problem is a classic optimization problem. We have a knapsack(bag) of a fixed size/capacity that we want to fill with multiple items. Each item has its associated size and value. The problem is to optimize the selection of items so that the capacity of our bag is utilized as much as possible, and the total value of items therein is as high as possible. There are multiple ways to approach this problem, and the same solution may not work in every scenario.

### Greedy Algorithm
The idea of a greedy algorithm is to take items in a greedy fashion, where the greed can be quantified by several metrics

*   Get as **many items** as possible
    
    As the name suggests, we fill the bag with as many items as possible, ignoring their value. We will sort the items in increasing order of size, and start adding them one by one until the capacity of the bag is exhausted. Item that does not fit the bag at any point in time is skipped.
*   Get as much **value** as possible
    
    Here we sort the items in descending order of value, and start adding them to the bag until its capacity is exhausted. If a certain item does not fit the bag, we simply skip over it and try the next item.
*   Utilize the **density = value/size**
    
    We create a metric called density to combine both value and size in order to get the maximum value in least possible size. After sorting the items in decreasing order of density, we add them one by one to the bag until its capcity is exhausted, and skipping over any item that may not fit the bag. We will utilize the size of the objects and not their density while making these capacity checks.

There can be several ways to greedily solve a given optimization problem. Whether they are optimal or not, will depend on the input and the same algorithm will not be the best on all data sets.

Greedy algorithms have two main advantages:

1. Quick to design and implement
2. Can be very fast

and carry the following problems:

1. No guarantee of quality of solution, which can be highly dependent on input
2. May not work on all problems as finding a _feasible_ solution may be challenging

To formulate the problem mathematically, consider a set of $I$ items with the $i^{th}$ item having weight $w_{i}$, value $v_{i}$ and an indicator $x_{i}$ denoting whether the $i^{th}$ item is selected. Let $K$ denote the capacity of the knapsack, then
\begin{align*}
    \text{Maximize} &\sum_{i=1}^{\lvert I \rvert} v_{i}x_{i} \\
    \text{Subject to} &\sum_{i=1}^{\lvert I \rvert} w_{i}x_{i} \le K
\end{align*}

### Dynamic Programming
This utilizes a divide and conquer strategy to find the best set of items. Assuming $I=\{1,2,\ldots,n\}$, let $O(k,j$) denote the solution to the knapsack problem with capacity $k$ and items selected from the set ${1,2,\ldots,j}$. Then the solution we are looking for is $O(K,n)$.

Assume for the moment that we already have the solution for $O(k,j-1)$ for all $k={0,\ldots,K}$ and want to solve for $O(k,j)$. The following two cases are possible

* $w_{j} \le k$
    
    1. We do not select the $j$ item: in this case, the answer is $O(k,j-1)$ itself
    2. We select the $j$ item: in this case, some capacity of the knapsack is taken up and the answer becomes $v_{j}+O(k-w_{j}, j-1)$
    3. The maximum of these is the best we can do

* Otherwise
    
    1. The only option is to not take this item and return the current solution $O(k,j-1)$

In summary, the solution is
\begin{align*}
    O(k,j) = \begin{cases} max(O(k,j-1), v_{j}+O(k-w_{j}, j-1)) &\mbox{$w_{j} \le k$}\\
                            O(k,j-1) &\mbox{Otherwise} \end{cases}
\end{align*}

and in the beginning, we already know that $O(k,0) = 0)$ for all $k=1,\ldots,K$. For efficiency, we will solving this in a bottom up manner (starting with a single item) and keep storing the intermediate solution in a matrix for quick lookups.

## Constraint Programming
The central idea of contraint programming is to utilize the constraints to reduce the search space so that it's easier to make a choice on what values a variable can take. When no further deductions are possible in a given configuration, we will make a choice (say assign value to a particular variable).

Here the focus is on feasibility, i.e., reduce the search space by eliminating values that cannot belong to any solution.
