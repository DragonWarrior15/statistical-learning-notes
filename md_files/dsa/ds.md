## Binary Search Trees
### Traversals
There are three ways to traverse a binary tree
* **Inorder Traversal**: Here, we first traverse the left subtree, the print out the current node, and then traverse the right subtree.
* **Pre Order Traversal**: Here, we first print out the current node, and then traverse the left subtree and then the right subtree.
* **Post Order Traversal**: As the name suggests, we first traverse the left and right subtree in that order, and in the end print out the current node.

### Specific types of BST
* **Full Binary Tree**: Every node other than the leaf nodes has two children. Alternately, one can say that every node has exactly 0 or 2 children.
* **Complete Binary Tree**: Every level except possibly the last is completely filled and all children are as far left as possible.
* **Perfect Binary Tree**: All internal nodes have two children and all leaf nodes are at the same level.
* **Balanced Binary Tree**: If the number of nodes in such a tree are n, then the height of the tree is O(log(n)). Efficient binary trees will try to maintain this height after every update.

#### Balance Factor
To numerically ascertain whether a binary tree is balanced or not, we define **balance factor** for every node in the tree as the difference between the heigts of the right and left subtree. In a balanced binary tree, the absolute value of this difference would be atmost one at any node in the tree.

### Balanced Binary Tree
To balance an unbalanced binary tree, we need to look at the following two structres
```c++
        N           N
       / \           \
      /   \           C1
     C1   C2           \
                        C2
     Mountain      Stick
```
We know the stick is not balanced since the balance factor of `N` is 2. On the other hand, the mountain has a balance factor of 0 throughout and is balanced.

Balancing a binary tree in the smallest case is turning the stick to a mountain. In the stick, `N` < `C1` < `C2`. Hence, converting this to a mountain is simply reordering to have `C1` as the root with N as the left child and `C2` as the right child.

Another case is *unbending the elbow* where we convert an elbow to a stick and then follow the procedure above to convert the stick to a mountain. The following set of tree sturctures show the transformation left to right.
```c++
     N       N           N      
      \       \         / \      
       C2      C1      /   \     
      /         \     C1   C2     
     C1          C2              
    Elbow   Stick     Mountain   
```
In the elbow, `N` has a balance factor of 2 and at this point we must balance the tree.

Suppose an already balanced tree becomes unbalanced due to addition of one node. To balance such a tree, we have the following *rotations* that can be used

#### Generic Left Rotation
Suppose we had an addition to `t3` or `t4` in the left tree that causes `b` to have a balance factor of 2.
```c++
       \                            \
        b                            c
       / \                          / \
      t1  c        ------>         /   \
         / \       ------>        b     d
        t2  d                    / \   / \
           / \                  t1 t2 t3 t4
          t3 t4
```
Notice the following
* `b` is the deepest node (measuring depth from the root node) that is unbalanced
* `b` has a balance factor of 2
* `c` has a balance factor of 1
* an insert in `t3` or `t4` caused the imbalance
* The tree has a right slant if we observe `b-c-d`

To perform the rotation
* we notice the stick `b-c-d` and use the same method used earlier to convert this to a mountain
* We push `c` to be the root of this entire subtree under consideration 
* and retain the right subtree of `c` as is
* We push `b` as the left node of `c` and keep the left subtree `t1` of `b` as is
* Finally, we make `t2` as the right subtree of `b` to complete the rotation and achieve balance.  

#### Right-Left Rotation
```c++
       \                            \                             \        
        b                            b                             d       
       / \                          / \                           / \      
     t1   c        ------>        t1   d         ------>         /   \     
         / \       ------>            / \        ------>        b     c
        d   t4                      t2   c                     / \   / \   
       / \                              / \                  t1  t2 t3  t4  
     t2   t3                          t3   t4              
```
Notice the following
* `b` is the deepest node with the imbalance
* `b` has a balance factor of 2
* `c`, immediately below `b` has a balance factor of -1
* An insert to `t2` or `t3` caused the imbalance

If we look at linkage `b-c-d`, its an unbalanced elbow discussed above which can be converted to a balanced mountain with two rotation steps- first convert to a stick (right rotation) and then apply left rotation. the same is depicted in the set of diagrams above.

#### Balancing rotation summary
| Balance factor of the lowest point of imbalance | Balance factor of the next node in the direction of imbalance | Type of Rotation |
| ----------------------------------------------- | ------------------------------------------------------------- | ---------------- |
| 2 | 1 | Left Rotation |
| -2 | -1 | Right Rotation |
| 2 | -1 | Right-Left Rotation |
| -2 | 1 | Left-Right Rotation |

The final rotation (which is the only rotation in the first two cases) is determined by the sign of the first column. If the sign of rotation of both the columns are same, a single rotation is performed. The cases of differing sign are of an elbow.

All these rotation change the local tree structure and are just rearrangement of couple of pointers. These run in O(1) time.

### AVL Tree
An AVL tree is an extension of a balanced binary search tree. All the operations related to find, insertion and removal remain the same. The following are the additional properties of an AVL tree
* Extra work when inserting or removing element via rotations (for balancing)
* Storing the height of a node as a part of the node structure to quickly compute balance factor

To do insert in an AVL tree, we follow the following steps
1. Find the location of insert
    * This can be found out by simply traversing the binary tree similar to finding an element in the tree
    * We also note down the path we took to find the correct position to insert
1. We start updating the height of the nodes in this path in the reverse order of traversal
    If any imbalance occurs in the tree, it is bound to happen on this path itself
1. If we find an imbalance (balance factor is 2 or -2), we apply the correct set of rotations to balance the tree then and there itself
    Also update the height of nodes during this operation
1. We continue traversing the path to update heights of the remaining nodes

Removal operation is slightly more involved and proceeds as follows
1. Find the location of deletion
    * We traverse the tree until we can find the required element to delete
    * We also note the path which was followed to reach here
1. Find the inorder predecesor of this node
    * Expanding the definition, this is the last node that will be called/printed before calling/printing the current node in an inorder traversal
    * Since the right node is processed in the end in an inorder traversal, we know that the inorder predecessor is the rightmost element of the left subtree
1. Swap the current node with this inorder predecessor and delete the node
    * We may not need to physically swap the nodes, but rather overwrite the data of the current node with the inorder predecessor
    * and then delete the node corresponding to the inorder predecessor
1. Update the heights along the path, and perform balancing via rotations if the tree has become unbalanced anywhere
1. The only updates occur along the path taken to remove the element

### B-Tree
A B-Tree of *order* m means that
* All keys within a node are in sorted order
* Each node contains no more than m-1 keys
* Each internal node can have at most m children
    * A root node can be a leaf or have at most m children
    * Each non root, internal node has [ceil(m/2), m] children
        This happens because when inserting elements, we split a node into two parts as soon as the array storing keys in that node has become full and cannot accomodate any new key
        This ensures that each internal node will be at least half full (other node can be a leaf) 
* All leaves are on the same level
    * This happens due to the way the tree is created

Visually, a tree of order 3 could look like
```c++
      [65, 89]
     /   |    \
    /    |     \
 [23]   [72]   [99]
```

To do a search, at any node we will first do a linear search to find the key and if we don't locate it in the array, we need to locate the appropriate child node to search next and repeat this function recursively. The **runtime** will be **O(log m (n))**

## Heap
### Priority Queue
A Priority Queue is an abstract data type that is optimized to insert and perform find min (or max) operations. The min (or max) are often referred to as priorities and are numerically comparable. A priority queue can be implemented in several (but not limited to) ways

| Data Structure | Insert | Get Min |
| -------------- | ------ | ------- |
| Unsorted Array | O(1) (Amortized) | O(n) |
| Unsorted Linked List | O(1) | O(n) |
| Sorted Array | O(n) | O(1) |
| Sorted Linked List | O(n) | O(1) |

### (min) Heap
A balanced binary tree is a min heap if the following properties hold
* The tree is empty
* Or, for any node, the children are more than the node and both the left and right subtree are min heap as well

When considering the above checks for any subtree, we will not worry about the remaining part of the tree. Every subtree will satisfy the above properties for it to be a min heap. 

An example of such a complete binary tree is
```c++
                4
               / \
              /   \
             5     6
            / \   /
           9  15 18
```

When thinking about the tree in an abstract fashion, the above structure seems intuitive. When actually working with the same as an implementation, we consider an array with the following structure
> The array is filled starting at index 1
> The left child of a node at index i is at the index i * 2
> The right child of a node at index i is at the index i * 2 + 1

The above tree implemented as an array will look like
```c++
Index    --> | 0 | 1 | 2 | 3 | 4 | 5  | 6  |
Elements --> |   | 4 | 5 | 6 | 9 | 15 | 18 |
```

Thus, to traverse the tree, we can simply jumpy the indices using the above formula.

#### Inserting into (min) Heap
Inserting efficiently into a min heap is an intuitive algorithm that can be described as follows
* insert into the next available position into the array
    * if the array is at capacity, expand by allocating twice the memory
    * this is same as allocating memory for all the children of the last level of the tree
* if this value is greater than its parent
    * min heap propery is satisfied and the element can be kept here
* else, this value is less than its parent
    * min heap property is violated and the element must be swapped with the parent
    * min heap property is checked recursively for the element and its new parent
    * this process can be repeated till the min heap property is not satisfied (max runtime O(log(n)))

As a working example, consider the above described tree and the following operations to insert 3
```c++
Index    --> | 0 | 1 | 2 | 3 | 4 | 5  | 6  | 7 |
Elements --> |   | 4 | 5 | 6 | 9 | 15 | 18 |
Add 3
Elements --> |   | 4 | 5 | 6 | 9 | 15 | 18 | 3 |
heap property violated between 3 and its parent at index 7/2 = 3, swap
Elements --> |   | 4 | 5 | 3 | 9 | 15 | 18 | 6 |
heap property violated between 3 and its new parent at index 3/2 = 1, swap
Elements --> |   | 3 | 5 | 4 | 9 | 15 | 18 | 6 |
```

Note that any swap will satisfy the heap property for subtree below it and we only need to worry about the remaining upper part of the tree. We can refer to this function has **heapify up**.

#### Removing from (min) Heap
Removal of element from heap will always return the minimum element in the min heap. Hence, we can simply return the element of the array at index 1. But, after removing this element, we need to restructure the tree to satisfy the min heap property.

To do this,
* swap the root node (minimum element) with the last element of the array
* reduce the size of the array by one (size variable, not physically shrink the memory)
* if the new root is larger than any of the two children of the root, swap the root with the **smaller** of the two children
* while the min heap property is violated at the new position of the above element, perform the above **heapify down** operation till that element is smaller than both the children

As an example, consider remove min operation on the above tree
```c++
Index    --> | 0 | 1 | 2 | 3 | 4 | 5  | 6  | 7 |
Elements --> |   | 3 | 5 | 4 | 9 | 15 | 18 | 6 |
Swap root with the last element and reduce the size of array
Elements --> |   | 6 | 5 | 4 | 9 | 15 | 18 |
heap property violated between 6 and its children, pick the minimum
of the two children and swap with that, (children at indices 1 * 2, 1 * 2 + 1)
Elements --> |   | 4 | 5 | 6 | 9 | 15 | 18 |
heap property satisfied for element at index 3, its satisfied throughout the tree
```

#### Building a Heap
Given any data that is stored in an array like structure, we can perform a build heap operation in O(n) time by recursively using heapify down from bottom to up.

## Hashing
Hashing is the process of mapping any input, integer, string etc., to a fixed integer in a given range. Suppose we have several key-value pairs available with us. Using hashing, we can map every key to some integer/index, and store the value for this key-value pair in that index of an array. Now, when we want to search for that key, we first run hashing through the key to find the index where to look in the array and the retrieve the value stored at the location in O(1).

This fixed integer in a given range determines the index of the array (or the key in dictionary terms) where we put the new element. The function that enables such a mapping is called a hash function. It is possible that multiple inputs are mapped to the same integer and this can cause collision. Any implementaition of a hashmap will have built in logic to handle these for us.

### Hash Function
A simple case of hash function can be taking the first character of the name of a string if the input to the hashing function are all strings. In that case, assuming sanitized strings, we can map each string to one of 26 possibilities. As is clear, this is not a great hash function since many different strings will be mapped to the same integers causing a lot of collisions.

### Collision Handling
Consider a hash function for integer inputs that determines the position to place an input by taking the modulo of the input with 7. Our key array is of fixed size 7. Multile collisions will happen since there are several inputs that can leave the same remainder with 7.

To handle the collisions, we simple make the index of the key array to point to a linked list. As we encounter collisions, we keep adding elements to the beginning of the linked list. This gives an O(1) insertion time. In worst case, the find/remove operation is O(n). Let's denote the load factor of the hashing function by load factor alpha = n/N where n is the number of elements in the hash table and N is distinct number of keys possible in the array.

A load factor < 1 is ideal since that would mean there are at most one element per index on average. This ensure remove and find operations on the linked list to be almost O(1).

#### Linear probing
Linear probing is a special method to handle collisions where if we find a collision, we check for the next available position in the array to put the element. Clearly, in worse case this can require looping over the entire array before we find the suitable position to find an available slot.

#### Double Hashing
This is an add on to the linear probing method, where we utilize a second hash function to find the index to store the element. Since this method jumps around to find an available slot, we have a less chance of creating local clusters. The runtime of this approach will depend on the load factor and not the size of the data itself.

The formula is h(k, i) = (h1(x) + i * h2(x))%N, where h1 and h2 are two indices. We start with i = 0 and keep incrementing it if we encounter collisions. Thus, in the first try h1 is only used to determine the index. h2 begins to come into play after the first try has produced a collision.

#### Rehashing
As seen above, maintaining the load factor is critical to have an efficiently working hash function. Rehashing resizes the array whenever it encounters a full array. Rehashing will reassign new keys for already existing data and create space to add new entries. Usually, the array size will be doubled.


## Disjoint-Sets
A disjoint-set data structure keeps tracks of elements that have been partitioned into disjoint subsets. It supports two main operations:
* __find__: find the subset to which a particular element belongs to; this is useful to check if two elements are present in the same subset
* __union__: combine two subsets or partitions into a single subset

*Disjoint-Sets* data structures are also sometimes called *Union-Find* data structures due to the primary operations associated with these, *union* and *find*.

However, note that *union* is a reserved keyword in C and C++, and thus the actual function name could be something like *set_union*.

#### Naive implementation
A naive implementation of this data structure is using an array. We simply have the indices as the elements/keys in the disjoint subsets, and the stored array value as the representative element of the disjoint subset. This can simply be the first element of the subset.

Thus, if we have three subsets with elements (0,4), (1,3,5), (2,6,7), the corresponding representation as an array will be
```c++
Index    --> | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
Elements --> | 0 | 1 | 2 | 1 | 0 | 1 | 2 | 2 |
```

Clearly, _find_ will work in O(1) since we can directly fetch the value at the index. However, _union_ will be O(n), since we will need to traverse the entire array to check if the element belongs to the particular subset which we need to merge.

#### UpTrees
In this implementation, we still continue using the array indices as the keys, but now the value of the array is
* -1 if we have found the representative element
* index of parent if we haven't found the representative element

Suppose we have 4 elements, all in different subsets initially,
```c++
Index    --> |  0 |  1 |  2 |  3 |
Elements --> | -1 | -1 | -2 | -1 |
```

Now if we want to merge 0 and 3, we simply make 0 as the parent of 3
```c++
Index    --> |  0 |  1 |  2 | 3 |
Elements --> | -1 | -1 | -1 | 0 |
```
Thus, _find(3)_ is 0, which is not -1 and we recurse. _find(0)_ is -1 which means that the representative element of the subset in which 3 resides is 0. We can also refer to this element as the root of the corresponding UpTree.

Extending this idea, merging any two elements is same as making the root node of one subset point to the root node of the other subset. This way, the update operation boils down to finding the root nodes of the two elements on which union operation is called.

For instance, if we want to merge 3 and 1, we make the representative element/root of the subset where 3 resides to point to 1. The first part of the algorithm is to traverse the tree and get the root of the tree. _find(3)_ gives 0, and _find(0)_ gives -1, indicating that 0 is the root element. We update the array as array[0] = 1
```c++
Index    --> | 0 |  1 |  2 | 3 |
Elements --> | 1 | -1 | -1 | 0 |
```

The run time of this _find_ algorithm is O(height) where the height will be n in the worst case, and the run time will be same as the naive implementation.

With this worst case complexity, an **ideal UpTree** is the one that has flat trees, i.e., every element of a subset points to the root. The complexity of _find_ in such a case will be O(1).

#### Smart _union_
* union by height
  Instead of storing -1 in the array at the root element, we will store negative of height - 1. Since the runtime of union is proportional to the height of the tree, while doing union it makes sense to add the shoter tree to the taller tree so that the height of the tallest tree in the entire array is still unchanged.
  However, the height of many nodes could increase by 1, resulting in larger cost of run for those elements now.
  **idea: keep the height of the tree as small as possible**
* union by size
  As the name suggests, we utilize the information regarding the size of the tree before deciding the order of union. Smartly doing this will ensure that the height of minimum number of elements is unchanged after this operation.
  We will store the negative of the size of the tree in the root element now. When doing the union, the smaller sized tree is made to union with the larger sized tree.
  **idea: minimize the number of nodes whose height changes**

Both the approaches ensure that the height of trees are bounded by O(log n).

#### Path Compression
When we called _find_ on an element, we need to traverse the entire path to reach the root from that element. Since we are traversing the entire path, we can ensure that the subsequent _find_ calls are efficient by path compression. For every node on this path, we will update its value in the array so that it points directly to the root element.

Any node pointing to one of the nodes along the path, has their height reduced. This helps bring the data structure closer to the ideal UpTree where the trees are as flat as possible.

#### Runtime
The iterative log is defined as
```c++
log * (n) = 0                  if n <= 1
            1 + log * (log(n)) otherwise
log * (2 ^ 65536) = 5
```

For disjoint-sets implemented with smart union and path compression, the runtime for m queries (combination of union and find operations) is O(m * log * (n)) where n is the size of disjoint-set. Since iterative log is a very small value for even very large values of n, the amortized time can be said to be same as O(m)* , making one operation on the disjoint set constant time (amortized).

## Graphs

Graphs are a collection of vertices (nodes) and edges denoted by G = (V, E). The number of vertices is denoted by n and the number of edges by m.

Key terms
| Term | Definition |
| ---- | ---------- |
| Incident Edges (v) | For a vertex, it is the collection of all edges directly connected to it {(x,v) in E} |
| Degree (v) | The number of incident edges |
| Adjacent Vertices (v) | Collections of all vertices that are connected to v by an edge, {x : (x,v) in E} |
| Path | Sequence of vertices connected by edges |
| Cycle | Path with a common begin and end vertex |
| Simple Graph | A graph with no cycles or multiple-edges |
| Subgraph | A graph whose vertices and edges are a subset of another (parent) graph |

### Graph Implementations
#### Edge List
In an edgelist implementation, we store a list of vertices (as a vector), and a list of edges (as a vector). Every element in the list of edges contains information about the two vertices connected by the edge, and any other information, like the edge weight, stored as well.

Different operations on this implementation
| Operation | Description |
| --------- | ----------- |
| InsertVertex(v) | simply expand the vertex list to add the new node, O(1) amortized |
| RemoveVertex(v) | O(m) since we will also remove all edges which have vertex v; this requires traversal through the entire list of edges |
| areAdjacent(vertex v1, vertex v2) | O(m) since we need to traverse the entire edge list and check if the two vertices are part of the same edge anywhere in the list |
| IncedentEdges(v) | O(m) since we will traverse the entire list to check all edges and count the ones which have the vertex v present in them |

#### Adjacency Matrix
In the implementation, we still store a list of vertices, along with a matrix whose rows and columns are all the vertices. The value at any location indicates whether an edge is present between the two vertices. Usually, 0 will denote the absence of any edge.

For a more exhaustive implementation, we could store edges and related information in a separate list of edges (as above), and store pointers to this edge list in the adjacency matrix. With this extra storage, we have the flexibility to traverse the list of edges for certain operations, while still retaining the ability to find edges corresponding to any vertex via the matrix.

Different operations and their runtimes
| Operation | Description |
| --------- | ----------- |
| InsertVertex(v) | this now becomes O(n) since a new row and column must be added to the adjaceny matrix |
| RemoveVertex(v) | O(m) + O(n) since we remove one row and column from the adjacency matrix |
| areAdjacent(vertex v1, vertex v2) | O(1) because its a simple lookup in the matrix |
| IncedentEdges(v) | O(n) as we lookup in the corresponding row and column of the matrix to check for existence of edges |

#### Adjacency List
This implementation extends the idea of an edge list. In addition to the vertex list and the edge list, each element of the vertex list points to a linked list which is the list of all edges adjacent to that vertex in the graph. Each element of this list points to the corresponding edge in the list of edges.

Different operations and their runtimes
| Operation | Description |
| --------- | ----------- |
| InsertVertex(v) | Still O(1)* since we will be adding an element to the array |
| RemoveVertex(v) | O(deg(v)) where deg denotes degree, since we need to traverse through all the edges having v as one of the vertices |
| areAdjacent(vertex v1, vertex v2) | min(O(deg(v1), deg(v2))) as we will traverse the smaller list of one of the two nodes and check all the edges |
| IncedentEdges(v) | O(deg(v)) since the entire linked list of the node needs to be traversed |

