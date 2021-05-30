---
title: "C++ Exercises 03"
---

## Course 03 : some name

***

### Quiz 01

1. According to video lesson 1.1.1, a hash table consists of three things. Which of these was **NOT** one of those three things?
    1. An array
    1. Collision handling
    1. Encryption
    1. A hash function

2. Given a hash function h(key) that produces an index into an array of size N, and given two different key values key1 and key2, the Simple Uniform Hashing Assumption states which of the following?
    1. The probability that h(key1) == h(key2) is 1/N.
    1. If h(key1) == h(key2) then h needs a running time of O(N) to complete.
    1. If h(key1) == h(key2) then h needs a running time of O(lg N) to complete.
    1. The probability that h(key1) == h(key2) is 0.

3. According to video lesson 1.1.2, which of the following is a **good** hash function h(key) that translates any 32-bit unsigned integer key into an index into an 8 element array?
    (Note that an expression like "2 & 3" uses the bitwise-AND operator, which gives the result of comparing every bit in the two operands using the concept of "AND" from Boolean logic; for example, in Boolean logic with binary numbers, 10 AND 11 gives 10: for the first digit, 1 AND 1 yields 1, while for the second digit, 0 AND 1 yields 0. An expression like "4 % 8" uses the remainder operator that give the remainder from integer division; for example, 4 % 8 yields 4, which is the remainder of 4/8. In some cases, these two different operators give similar results. Think about why that is.)
    1. ```c++
        int h(uint key) {
            int index = 5;
            while (key--)
                index = (index + 5) % 8
            return index;
        }
        ```
    2. ```c++
        int h(uint key) { return key & 7; }
        ```
    3. ```c++
        int h(uint key) { return rand() % 8; }
        ```
    4. ```c++
        int h(uint key) { return max(key,7); }
        ```

4. Suppose you have a good hash function h(key) that returns an index into an array of size N. If you store values in a linked list in the array to manage collisions, and you have already stored n values, then what is the expected run time to store a new value into the hash table?
    1. O(N)
    1. O(1)
    1. O(n)
    1. O(n/N)

5. Suppose you have a good hash function h(key) that returns an index into an array of size N. If you store values in a linked list in the array to manage collisions, and you have already stored n values, then what is the expected run time to find the value in the hash table corresponding to a given key?
    1. O(n/N)
    1. O(N)
    1. O(n)
    1. O(1)

6. Which one of the following four hashing operations would run faster than the others?
    1. Finding a value in a hash table of 4 values stored in an array of 8 elements.
    1. Finding a value in a hash table of 100 values stored in an array of 1,000 elements.
    1. Finding a value in a hash table of 20 values stored in an array of 100 elements.
    1. Finding a value in a hash table of 2 values stored in an array of 2 elements.

7. When storing a new value in a hash table, linear probing handles collisions by finding the next unfilled array element. Which of the following is the main drawback of linear probing?
    1. If the hash function returns an index near the end of the array, there might not be an available slot before the end of the array is reached.
    1. There may not be an available slot in the array.
    1. Even using a good hash function, contiguous portions of the array will become filled, causing a lot of additional probing in search of the next available unused element in the array.
    1. The array only stores values, so when retrieving the value corresponding to a key, there is no way to know if the value at h(key) is the proper value, or if it is one of the values at a subsequent array location.

8. When using double hashing to store a value in a hash table, if the hash function returns an array location that already stores a previous value, then a new array location is found as the hash function of the current array location. Why?
    1. Only one additional hash function is called to find an available slot in the array whereas linear probing requires an unknown number of array checks to find an available slot.
    1. Double hashing reduces the chance of a hash function collision on subsequent additions to the hash table.
    1. Double hashing reduces the clumping that can occur with linear probing.
    1. Since the hash function runs in constant time, double hashing runs in O(1) time.

9. Which of the following data structures would be the better choice to implement a memory cache, where a block of global memory (indicated by higher order bits of the memory address) are mapped to the location of a block of faster local memory.
    1. A hash table implemented with linear probing.
    1. A hash table implemented with separate chaining, using an array of linked lists.
    1. A hash table implemented with double hashing.
    1. An AVL tree.

10. Which of the following data structures would be the better choice to implement  a dictionary that not only returns the definition of a word but also returns the next word following that word (in lexical order) in the dictionary.
    1.  An AVL tree.
    1.  A hash table implemented with separate chaining, using an array of linked lists.
    1.  A hash table implemented with linear probing.
    1.  A hash table implemented with double hashing.

***

#### Answers 01

| Question | Answer |
| -------- | ------ |
| 1 | iii |
| 2 | i |
| 3 | ii |
| 4 | ii |
| 5 | i |
| 6 | ii |
| 7 | iii |
| 8 | iii |
| 9 | iii |
| 10 | i |


Answer 4: insert is always O(1), find depends on load factor
Answer 6: calculate load factor

***

### Quiz 02

1. Using the convention followed by the video lessons, given three disjoint sets (1,3,5,7), (2,8) and (4,6), which one of these sets would be referenced by the value 3?
    1. (1,3,5,7)
    1. (2,8)
    1. (4,6)
    1. None of the above.

2. What is the union of the disjoint sets (1,3,5,7) and (2,8)?
    1. (1,2,3,5,7,8)
    1. ((1,2),(1,8),(3,2),(3,8),(5,2),(5,8),(7,2),(7,8))
    1. (2,6,8,10,14,16,24,40,56)
    1. (3,11)

3. What happens when you take the union of two disjoint sets that contain the same value?
    1. Two different disjoint sets by definition can never share the same value.
    1. Any element found in both disjoint sets will appear twice in the union of these two disjoint sets.
    1. The union operation must first check to see if the same element appears in both disjoint sets and then ensures the element appears only once in the resulting union set.
    1. The elements cancel and neither appears in the union of the two disjoint sets.

4. According to the distjoint set array representation in the video lessons, Which of the following arrays would **NOT** be a valid representation of the disjoint set (1,3,5,7)?
    1. ```c++
        index-> | 1 |  2 |  3 |  4 | 5 |  6 | 7 |  8 |
        value-> | 5 | -1 | -1 | -1 | 3 | -1 | 1 | -1 |
        ```
    1. ```c++
        index-> |  1 |  2 | 3 |  4 | 5 |  6 | 7 |  8 |
        value-> | -1 | -1 | 1 | -1 | 1 | -1 | 1 | -1 |
        ```
    1. ```c++
        index-> | 1 |  2 | 3 |  4 | 5 |  6 | 7 |  8 |
        value-> | 3 | -1 | 5 | -1 | 7 | -1 | 1 | -1 |
        ```
    1. ```c++
        index-> |  1 |  2 | 3 |  4 | 5 |  6 | 7 |  8 |
        value-> | -1 | -1 | 1 | -1 | 3 | -1 | 5 | -1 |
        ```

5. When encoding **height** into the root of an up-tree, what value should be placed in element 7 of the following array?

    | index | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    | ----- | - | - | - | - | - | - | - |
    | value | 3 | -1 | 7 | -1 | 7 | -1 | ? |

    1. -3
    1. -2
    1. -1
    1. -4

6. When encoding **size** into the root of an up-tree, what value should be placed in element 7 of the following array?

    | index | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    | ----- | - | - | - | - | - | - | - |
    | value | 3 | -1 | 7 | -1 | 7 | -1 | ? |

    1. -3
    1. -1
    1. -4
    1. -2

7. When computing the union of two disjoint sets represented as up-trees in an array, (using proper path compression) which of these strategies results in a better overall run time complexity than the other options?
    1. Always make the up-tree with fewer elements a subtree of the root of the up-tree with more elements.
    1. Always make the up-tree with a shorter height a subtree of the root of the up-tree with a larger height.
    1. The overall run time complexity is not affected by which up-tree is chosen to become a subtree of the other up-tree.
    1. Using either size or height strategies above results in the same overall run time complexity.

8. Recall that the iterated log function is denoted log* (n) and is defined to be
    ```c++
    log* (n) = 0                 for n <= 1, and
               1 + log* (log(n)) for n > 1
    ```
    Let lg* (n) be this iterated log function computed using base 2 logarithms.
    Blue Waters, housed at the University of Illinois, is the fastest university supercomputer in the world. It can run about 2^53 (about 13 quadrillion) instructions in a second. There are about 2^11 seconds in half an hour, so Blue Waters would run 2^64 instructions in about half an hour.
    Which one of the following is equal to lg* (2^64)?
    1. 64
    1. 5
    1. 6
    1. 65536

9. Which of these is considered the least run-time complexity?
    1. O(log log N)
    1. O(log* N)
    1. O(log N)
    1. O(1)

10. Which of the following best describes "path compression" as described in the video lessons to accelerate disjoint set operations? (Here we say "parent pointer" to mean whatever form of indirection is used to refer from a child to its parent; this could be a literal pointer or it could be an array index as in the lectures.)
    1. When the root of an element's node is found, all of the descendants of the root have their parent pointer set to the root.
    1. When traversing the up-tree from an element to its root, if any elements in the traversal (including the first element, but excluding the root itself) do not point directly to the root as their parent yet, they will have their parent pointer changed to point directly to the root.
    1. When the root of the up-tree containing an element is found, both the element and its parent will always have their parent pointers set to point to the root node.
    1. When the root of the up-tree containing an element is found, the element and all of its siblings that share the same parent have their parent pointers reset to point to the root node.

***

#### Answers 02

| Question | Answer |
| -------- | ------ |
| 1 | i |
| 2 | i |
| 3 | i |
| 4 | iii |
| 5 | i |
| 6 | iv |
| 7 | iv |
| 8 | ii |
| 9 | iv |
| 10 | ii |

5. value stores id -(height + 1)
6. count the root too !

***

### Assignment 01

Modify the implementation of `DisjointSets::find(int i)` below so that it uses path compression during queries.

The DisjointSets class here models a collection of one or more disjoint sets of items. This is very similar to the professor's description of *up trees*; imagine that each set is a tree, where the root of the tree represents the set it belongs to, while other items in the same set refer to it (directly or indirectly).

Given a DisjointSets instance `d`, the array `d.s` contains one `integer` for each item in the entire collection. Currently, this array is statically allocated with 256 integers, so the entire collection can involve at most 256 items. For any given item with index `i`, the value recorded at `d.s[i]` represents either the parent of item `i`, or a more distant ancestor of item `i`, or the root of the entire set that item `i` belongs to. If the value of `d.s[i]` is -1, then this means that item `i` is the root of its own set.

The provided code for find does this much already:
1. The find function queries for the ultimate root of a given item, with index `i`.
2. If the array entry for index `i` is less than 0, then return `i`, as it is the root of its own set. (This is the base case.)
3. Otherwise, the array entry currently records an ancestor of node `i` in the tree, but not the root. So, recurse on the ancestor index. Assume that `find()` succeeds in recursion: it returns the root of this set. (This assumption would be the inductive hypothesis if you were writing a proof of correctness by induction.)
4. Return the root that was found. (This fulfills the assumption that was made when we recursed in the previous step.)

You need to add the path compression feature to this `find` function. This means you must record the information that was found recursively as an update to the array before the function returns. This optimizes subsequent calls to the function.

In summary, after calling `find(i)` on one of the elements in the set, `i`, the find function should return the root index of the disjoint set (the index of its root element) and also update the `s` array to ensure that element `i` and every ancestor of `i` will refer directly to the root.

```c++
#include <iostream>

class DisjointSets {
public:
    int s[256];

    DisjointSets() { for (int i = 0; i < 256; i++) s[i] = -1; }

    int find(int i);
};

/* Modify the find() method below to
 * implement path compression so that
 * element i and all of its ancestors
 * in the up-tree refer directly to the
 * root after that initial call to find()
 * returns.
 */

int DisjointSets::find(int i) {
  if ( s[i] < 0 ) {
    return i;
  } else {
    return find(s[i]);
  }
}

int main() {
  DisjointSets d;

  d.s[1] = 3;
  d.s[3] = 5;
  d.s[5] = 7;
  d.s[7] = -1;

  std::cout << "d.find(3) = " << d.find(3) << std::endl;
  std::cout << "d.s(1) = " << d.s[1] << std::endl;
  std::cout << "d.s(3) = " << d.s[3] << std::endl;
  std::cout << "d.s(5) = " << d.s[5] << std::endl;
  std::cout << "d.s(7) = " << d.s[7] << std::endl;

  return 0;
}
```

***

#### Answer Assignment 01

Updated definition of `find`
```c++
int DisjointSets::find(int i) {
  if ( s[i] < 0 ) {
    return i;
  } else {
    int root = find(s[i]);
    s[i] = root;
    return root;
  }
}
```

***

### Quiz 03

1. Let G = (V,E) be a simple graph consisting of a set of vertices V and a set of (undirected) edges E where each edge is a set of two vertices. Which one of the following is **not** a simple graph?
    1. G = ( V = (a,b,c), E = ((a,b),(b,c),(a,c)) )
    1. G = ( V = (a,b,c), E = ((a,b), (a,c), (b,a), (b,c), (a,c), (b,c)) )
    1. G = ( V = (a,b,c), E = ((a,b)) )
    1. G = ( V = (a,b,c), E = () )

2. For a simple graph with n vertices, what is the worst case (largest possible) for the number of edges?
    1. O(2^n)
    1. O(n^2)
    1. O(n log n)
    1. O(n)

3. Which graph representation has a better worst-case storage complexity than the others for storing a simple graph of n vertices?
    1. Edge List
    1. Adjacency Matrix
    1. Adjacency List
    1. All three graph representations have the same worst-space storage complexity for a simple graph of n nodes.

4. Suppose you have a rapid data feed that requires you to add new data point vertices quickly to a graph representation. Which graph representation would you **NOT** want to utilize?
    1. Edge List
    1. Adjacency Matrix
    1. Adjacency List
    1. All three graph representations have the same time complexity for adding vertices to a simple graph.

5. Suppose you have a rapid data feed that requires you to remove existing data point vertices (and any of their edges to other vertices) quickly to a graph representation. Which graph representation would you WANT to utilize?
    1. Edge List
    1. Adjacency Matrix
    1. Adjacency List
    1. All three representations have the same time complexity for removing a vertex from a simple graph of n vertices.

6. Suppose you want to implement a function called neighbors(v) that returns the list of vertices that share an edge with vertex v. Which representation would be the better choice for implementing this neighbors() function?
    1. Edge List
    1. Adjacency Matrix
    1. Adjacency List
    1. All three representations result in the same time complexity for the neighbor() function.

7. Suppose you want to implement a function called neighborsQ(v1,v2) that returns true only if vertices v1 and v2 share an edge. Which representation would be the better choice for implementing this neighborsQ() function?
    1. Edge List
    1. Adjacency Matrix
    1. Adjacency List
    1. All three representations support the same time complexity for implementing the neighborQ() function.

8. Which of these edge lists has a vertex of the highest degree?
    1. (a, c), (e, g), (c, e), (g, a)
    1. (a, b), (a, c), (a, d), (b, d)
    1. (a,b), (b, c), (d, b), (g, b)
    1. (d,b), (g,a), (h,f), (c, e)

9. Which adjacency matrix corresponds to the edge list: (1,2), (2,3), (3,4), (1,4) (where the rows/columns of the adjacency matrix follow the same order as the vertex indices)?
    1.  |  | 1 | 2 | 3 | 4 |
        | - | - | - | - | - |
        | 1 | 0 | 0 | 1 | 1
        | 2 | | 0 | 1 | 1 |
        | 3 | | | 0 | 0 |
        | 4 | | | | 0 |

    1.  |  | 1 | 2 | 3 | 4 |
        | - | - | - | - | - |
        | 1 | 0 | 1 | 0 | 1
        | 2 | | 0 | 1 | 0 |
        | 3 | | | 0 | 1 |
        | 4 | | | | 0 |

    1.  |  | 1 | 2 | 3 | 4 |
        | - | - | - | - | - |
        | 1 | 1 | 0 | 0 | 1
        | 2 | | 1 | 0 | 0 |
        | 3 | | | 1 | 0 |
        | 4 | | | | 1 |

    1.  |  | 1 | 2 | 3 | 4 |
        | - | - | - | - | - |
        | 1 | 0 | 1 | 1 | 0
        | 2 | | 0 | 1 | 1 |
        | 3 | | | 0 | 1 |
        | 4 | | | | 0 |

10. Which graph representation would be the best choice for implementing a procedure that only needs to build a graph from a stream of events.
    1. Edge List
    1. Adjacency Matrix
    1. Adjacency List
    1. All three representations would share the same storage and time complexity for the procedure.

***

#### Answers 03

| Question | Answer |
| -------- | ------ |
| 1 | ii |
| 2 | ii |
| 3 | i |
| 4 | ii |
| 5 | iii |
| 6 | iii |
| 7 | ii |
| 8 | iii |
| 9 | ii |
| 10 | i |

refer to the data structures and algorithms notes as well

***

### Assignment 02

Suppose you are given a undirected graph specified as a list of edges. In this challenge problem, we'll use a simplified disjoint sets data structure to count how many _connected components_ the graph has, and whether each one contains a cycle or not.

First, some background information: In an undirected graph, two vertices have connectivity if there is any path leading from one to the other using any number of edges. So, a lone vertex by itself, with no edges, is not _connected_ to the other parts of the graph. A _connected component_ is any subset of the graph vertices where all the vertices have paths to each other, and where that set is maximal, meaning that no reachable vertices are left out of the set. A connected component contains a _cycle_ if there are two (or more) distinct paths connecting any two vertices--that means there is a closed loop somewhere.

Example: An edge label like _(0,1)_ means an edge between vertex 0 and vertex 1. Suppose we have vertices numbered 0 through 8, and we have these edges:

(0,1), (1,2), (0,2), (3,4), (5,6), (6,7), (7,8)

Try drawing it on a sheet of paper. The three connected components are these sets of vertices:

{0, 1, 2}, {3, 4}, {5, 6, 7, 8}

You'll see the connected components are like islands of vertices. Here, {0, 1, 2} contains a cycle, and the other two connected components do not contain cycles. Also, notice that for a set to be a connected component, it must be maximal, meaning no vertices can be left out--and so {0, 1} is not called a connected component, because the 2 is also reachable there. (Maximal does not mean _maximum_. A single, lone vertex is a connected component by itself, because the subset containing only that one vertex is maximal, considering what can be reached from it. So, the sizes of the other connected components elsewhere do not matter.)

In graph theory, it's common to say `n` for the number of vertices and `m` for the number of edges in some graph. For this problem, we'll say we have some undirected graph of some n vertices, which are arbitrarily labeled with indices from 0 through n-1. (This is reasonable because we could otherwise relabel the vertices using a hash table for lookups. Also, we won't assume that subsequent numbers are connected by edges, although that may happen in our unit tests.) Then, we'll initialize a collection of disjoint sets as n singletons (single element sets), one for each vertex; we have a DisjointSets class to represent this collection.

To create sets representing connected components, we can iterate over the graph edges: For each edge (A,B) connecting vertex A to vertex B, we can union the sets that A and B belong to, so the disjoint sets data structure now indicates now that A and B belong to the same set. Our member function for the union operation is called `dsunion` to avoid conflicting with the C++ keyword `union`.

At the end of the process of calling `dsunion()` on every pair of vertices in the edge list, the number of disjoint sets should correspond to the number of connected components in the graph.

The disjoint sets data structure can also detect cycles. As the edges are being processed, if the edge currently being processed connects vertex A and vertex B, and both vertex A and vertex B are already in the same disjoint set, then the edge connecting vertex A and vertex B completes a cycle.

In the source code provided below, you should modify the definition of `DisjointSets::dsunion` (under TASK 1) and the definition of `DisjointSets::count_comps` (under TASK 2) according to the hints in the code comments. We'll detect cycles during the union procedure and we can count the number of components after all union operations are completed.

The starter code `main()` also contains an example graph with expected output. When you're ready to submit, we'll run your code through some randomized unit tests for grading.

{% raw %}
```c++

#include <iostream>

// You are provided this version of a DisjointSets class.
// See below for the tasks to complete.
// (Please note: You may not edit the primary class definition here.)
class DisjointSets {
public:
  // We'll statically allocate space for at most 256 nodes.
  // (We could easily make this extensible by using STL containers
  //  instead of static arrays.)
  static constexpr int MAX_NODES = 256;

  // For a given vertex of index i, leader[i] is -1 if that vertex "leads"
  // the set, and otherwise, leader[i] is the vertex index that refers back
  // to the eventual leader, recursively. (See the function "find_leader".)
  // In this problem we'll interpret sets to represent connected components,
  // once the sets have been unioned as much as possible.
  int leader[MAX_NODES];

  // For a given vertex of index i, has_cycle[i] should be "true" if that
  // vertex is part of a connected component that has a cycle, and otherwise
  // "false". (However, this is only required to be accurate for a current
  // set leader, so that the function query_cycle can return the correct
  // value.)
  bool has_cycle[MAX_NODES];

  // The number of components found.
  int num_components;

  DisjointSets() {
    // Initialize leaders to -1
    for (int i = 0; i < MAX_NODES; i++) leader[i] = -1;
    // Initialize cycle detection to false
    for (int i = 0; i < MAX_NODES; i++) has_cycle[i] = false;
    // The components will need to be counted.
    num_components = 0;
  }

  // If the leader for vertex i is set to -1, then report vertex i as its
  // own leader. Otherwise, keep looking for the leader recursively.
  int find_leader(int i) {
    if (leader[i] < 0) return i;
    else return find_leader(leader[i]);
  }

  // query_cycle(i) returns true if vertex i is part of a connected component
  // that has a cycle. Otherwise, it returns false. This relies on the
  // has_cycle array being maintained correctly for leader vertices.
  bool query_cycle(int i) {
    int root_i = find_leader(i);
    return has_cycle[root_i];
  }

  // Please see the descriptions of the next two functions below.
  // (Do not edit these functions here; edit them below.)
  void dsunion(int i, int j);
  void count_comps(int n);
};

// TASK 1:
// dsunion performs disjoint set union. The reported leader of vertex j
// will become the leader of vertex i as well.
// Assuming it is only called once per pair of vertices i and j,
// it can detect when a set is including an edge that completes a cycle.
// This is evident when a vertex is assigned a leader that is the same
// as the one it was already assigned previously.
// Also, if you join two sets where either set already was known to
// have a cycle, then the joined set still has a cycle.
// Modify the implementation of dsunion below to properly adjust the
// has_cycle array so that query_cycle(root_j) accurately reports
// whether the connected component of root_j contains a cycle.
void DisjointSets::dsunion(int i, int j) {
  bool i_had_cycle = query_cycle(i);
  bool j_had_cycle = query_cycle(j);
  int root_i = find_leader(i);
  int root_j = find_leader(j);
  if (root_i != root_j) {
    leader[root_i] = root_j;
    root_i = root_j;
  }
  else {
    // A cycle is detected when dsunion is performed on an edge
    // where both vertices already report the same set leader.
    // TODO: Your work here! Update has_cycle accordingly.
  }

  // Also, if either one of the original sets was known to have a cycle
  // already, then the newly joined set still has a cycle.
  // TODO: Your work here!
}

// TASK 2:
// count_comps should count how many connected components there are in
// the graph, and it should set the num_components member variable
// to that value. The input n is the number of vertices in the graph.
// (Remember, the vertices are numbered with indices 0 through n-1.)
void DisjointSets::count_comps(int n) {

  // Insert code here to count the number of connected components
  // and store it in the "num_components" member variable.
  // Hint: If you've already performed set union on all the apparent edges,
  //  what information can you get from the leaders now?

  // TODO: Your work here!

}

int main() {

  constexpr int NUM_EDGES = 9;
  constexpr int NUM_VERTS = 8;

  int edges[NUM_EDGES][2] = {{0,1},{1,2},{3,4},{4,5},{5,6},{6,7},{7,3},{3,5},{4,6}};

  DisjointSets d;

  // The union operations below should also maintain information
  // about whether leaders are part of connected components that
  // contain cycles. (See TASK 1 above where dsunion is defined.)
  for (int i = 0; i < NUM_EDGES; i++)
    d.dsunion(edges[i][0],edges[i][1]);

  // The count_comps call below should count the number of components.
  // (See TASK 2 above where count_comps is defined.)
  d.count_comps(NUM_VERTS);

  std::cout << "For edge list: ";
  for (int i = 0; i < NUM_EDGES; i++) {
    std::cout << "(" << edges[i][0] << ","
         << edges[i][1] << ")"
         // This avoids displaying a comma at the end of the list.
         << ((i < NUM_EDGES-1) ? "," : "\n");
  }

  std::cout << "You counted num_components: " << d.num_components << std::endl;

  // The output for the above set of edges should be:
  // You counted num_components: 2

  std::cout << "Cycle reported for these vertices (if any):" << std::endl;
  for (int i=0; i<NUM_VERTS; i++) {
    if (d.query_cycle(i)) std::cout << i << " ";
  }
  std::cout << std::endl;

  // The cycle detection output for the above set of edges should be:
  // Cycle reported for these vertices (if any):
  // 3 4 5 6 7

  return 0;
}
```
{% endraw %}

***

#### Answer Assignment 02

```c++
void DisjointSets::dsunion(int i, int j) {
  bool i_had_cycle = query_cycle(i);
  bool j_had_cycle = query_cycle(j);
  int root_i = find_leader(i);
  int root_j = find_leader(j);
  if (root_i != root_j) {
    leader[root_i] = root_j;
    root_i = root_j;
  }
  else {
    has_cycle[root_i] = true;
    has_cycle[root_j] = true;
  }
  if(i_had_cycle | j_had_cycle){
    has_cycle[root_i] = true;
    has_cycle[root_j] = true;
  }
}

void DisjointSets::count_comps(int n) {
    int ans = 0;
    for(unsigned int i = 0; i < n; i++){
        if(leader[i] == -1){
            ans++;
        }
    }
    num_components = ans;
}
```

***

### Quiz 04

1. Which of these algorithms can be used to count the number of connected components in a graph?
    1. Count the number of times a breadth first traversal is started on every vertex of a graph that has not been visited by a previous breadth first traversal.
    1. Count the number of times a depth first traversal is started on every vertex of a graph that has not been visited by a previous depth first traversal.
    1. All of the above
    1. None of the above

2. Which elements encountered by a breadth first search can be used to detect a cycle in the graph?
    1. Unexplored edges to unexplored vertices that remain so after completion of the breadth first search.
    1. Discovered edges that were previously unexplored by the traversal have been added to the breadth-first traversal.
    1. Previously visited vertices that have been encountered again via a previously unexplored edge.
    1. Unexplored vertices that have been encountered by the traversal of a previously unexplored edge.

3. A breadth first traversal starting at vertex v1 of a graph can be used to find which ones of the following?
    1. The shortest path (in terms of # of edges) between vertex v1 and any other vertex in the graph.
    1. The shortest path (in terms of # of edges) between any two vertices in the graph.
    1. All of the above.
    1. None of the above.

4. Which traversal method has a better run time complexity to visit every vertex in a graph?
    1. Breadth First Traversal
    1. Depth First Traversal
    1. Both have the same run time complexity.
    1. Neither traversal method will necessarily visit every vertex in a graph.

5. The breadth first traversal of a connected graph returns a spanning tree for that graph that contains every vertex. If the graph has weighted edges, which of the following modifications is the simplest that produces a minimum spanning tree for the graph of weighted edges.
    1. An ordinary breadth first traversal is run from each vertex (as its start vertex) and the resulting spanning tree with the least total weight is the minimum spanning tree.
    1. The queue is replaced by a priority queue that keeps track of the least-weight edge that connects a vertex to the current breadth first traversal.
    1. The queue is replaced by a priority queue that keeps track of the total weight encountered by the current traversal plus each of the edges that connects a vertex to the current breadth first traversal.
    1. No modification is necessary because a breadth first traversal always returns a minimum spanning tree.

6. True of false: a connected directed graph with no cycles is a tree.
    1. True
    1. False

7. For which situation described here can Dijkstra's algorithm sometimes fail to produce a shortest path? You would want to avoid using Dijkstra's algorithm in this situation.
    1. A connected graph where there are multiple paths that have the same overall path cost (distance), and all of the edge weights are non-negative.
    1. A connected graph where some of the edge weights are negative and some have weight zero.
    1. A connected graph where some of the edge weights are zero and the rest are positive.
    1. A connected graph where all of the edges have the same positive weight.

8. Which of the following is a **true** statement about Dijkstra's algorithm? Assume edge weights (if any) are non-negative.
    1. Dijkstra's algorithm finds the shortest unweighted path, if it exists, between a start vertex and any other vertex, but only for an undirected graph.
    1. Dijkstra's algorithm finds the shortest weighted path, if it exists, between a start vertex and any other vertices, but only for an undirected graph.
    1. Dijkstra's algorithm finds the shortest weighted path, if it exists, between a start vertex and any other vertices in a directed graph.
    1. Dijkstra's algorithm finds the shortest weighted path, if it exists, between all pairs of vertices in a directed connected graph.

9. Which of the following is the optimal run time complexity to find the shortest path, if it exists, from a vertex to all of the other vertices in a weighted, directed graph of n vertices and m edges.
    1. O(n)
    1. O(m + n)
    1. O(m + lg n)
    1. O(m + n lg n)

10. Suppose you are given an undirected simple graph with unweighted edges, and for a particular specification of three vertices _u_, _v_, and _w_, you want to find the shortest path from _u_ to _w_ that goes through _v_ as a landmark. What is the most efficient method that can find this?
    1. A single run of Dijkstra's algorithm from _u_.
    1. Three runs of breadth-first search: once each from _u_, _v_, and _w_.
    1. A single run of breadth-first search from _v_.
    1. Two runs of Dijkstra's algorithm, first from _u_ and then from _v_.

***

#### Answers 04

| Question | Answer |
| -------- | ------ |
| 1 | iii |
| 2 | iii |
| 3 | i |
| 4 | iii |
| 5 | ii |
| 6 | ii |
| 7 | ii |
| 8 | iii |
| 9 | iv |
| 10 | iii |

refer to the data structures and algorithms notes as well

***

### Assignment 03

We can use disjoint sets to implement a breadth first traversal. The code below implements a `bfs()` method that implements a breadth first traversal that also measures the distance (in number of edges) from each vertex to the vertex serving as the source of the traversal.

This algorithm uses disjoint sets to keep track of two sets. All of the vertices are initialized to be singletons (the only element of their set). The `bfs(int i, int n, int m, int edges[][2])` method is called with the index `i` of the source vertex of the traversal. This vertex is assigned a distance of zero, and this vertex index `i` will be a member of the set of all processed vertices (vertices that the breadth first traversal has visited and measured an edge distance).

We then iterate. (We iterate no more than `m` times. If the graph was, for example, a long line of edges and the start vertex was at one end, then each iteration would process only one edge. For most graphs, we will probably need fewer iterations so we have a conditional break later in the loop.) Each of these iterations adds a layer of breadth to the traversal.

In each iteration, an inner loop cycles through all of the edges in the edge list. If any edge has one and only one vertex in the already-processed set (the same set as the start vertex `i`) then we add its other vertex to the current frontier set.

After the inner loop has iterated through all of the edges, the frontier set contains all of the vertices one edge away from all of the already-processed edges. When each of these vertices is added to the frontier set, we assign its distance to be the current loop counter of the outer loop. Since all of the vertices one edge away from the already-processed set of vertices have now been found (and their distance has been recorded), these new vertices can now be added to the already-processed set with a union operation. Then the outer loop can increment the edge distance counter and the next frontier of new vertices can be found.

In the code below, there are two conditions that need to be filled in. Each edge (say edge `j`) has two vertices: `edge[j][0]` and `edge[j][1]`. The condition needs to determine if one of these vertices is in the already processed set and the other is not, and if so, then the one that is not should be added to the frontier set. Your job is to figure out the condition using the variables defined, to determine if the appropriate vertex is a member (or not a member) of the already-processed set.

{% raw %}
```c++
#include <iostream>
#include <string>

// Note: You must not change the definition of DisjointSets here.
class DisjointSets {
public:
  int s[256];
  int distance[256];

  DisjointSets() {
    for (int i = 0; i < 256; i++) s[i] = distance[i] = -1;
  }

  int find(int i) { return s[i] < 0 ? i : find(s[i]); }

  void dsunion(int i, int j) {
    int root_i = find(i);
    int root_j = find(j);
    if (root_i != root_j) {
      s[root_i] = root_j;
    }
  }

  void bfs(int i, int n, int m, int edges[][2]);
};


/* Below are two conditions that need to be programmed
 * to allow this procedure to perform a breadth first
 * traversal and mark the edge distance of the graph's
 * vertices from vertex i.
 */

void DisjointSets::bfs(int i, int n, int m, int edges[][2]) {

  distance[i] = 0;

  // no need to iterate more than m times
  // but loop terminates when no new
  // vertices added to the frontier.

  for (int d = 1; d < m; d++) {

    // f is the index of the first
    // vertex added to the frontier
    int f = -1;

    // rooti is the name of the set
    // holding all of the vertices
    // that have already been assigned
    // distances

    int rooti = find(i);

    // loop through all of the edges
    // (this could be much more efficient
    // if an adjacency list was used
    // instead of a simple edge list)

    for (int j = 0; j < m; j++) {

      // root0 and root1 are the names of
      // the sets that the edge's two
      // vertices belong to

      int root0 = find(edges[j][0]);
      int root1 = find(edges[j][1]);

      if ( ***INSERT CONDITION HERE*** ) {

        // add the [1] vertex of the edge
        // to the frontier, either by
        // setting f to that vertex if it
        // is the first frontier vertex
        // found so far, or by unioning
        // it with the f vertex that was
        // already found.

        if (f == -1)
          f = edges[j][1];
        else
          dsunion(f,edges[j][1]);

        // set the distance of this frontier
        // vertex to d

        distance[edges[j][1]] = d;

      } else if ( ***INSERT CONDITION HERE*** ) {
        if (f == -1)
          f = edges[j][0];
        else
          dsunion(f,edges[j][0]);
        distance[edges[j][0]] = d;
      }
    }

    // if no vertices added to the frontier
    // then we have run out of vertices and
    // are done, otherwise union the frontier
    // set with the set of vertices that have
    // already been processed.

    if (f == -1)
      break;
    else
      dsunion(f,i);
  }
}

int main() {

  int edges[8][2] = {{0,1},{1,2},{2,3},{3,4},{4,5},{5,6},{6,7},{7,3}};

  DisjointSets d;

  d.bfs(3,8,8,edges);

  for (int i = 0; i < 8; i++)
    std::cout << "Distance to vertex " << i
              << " is " << d.distance[i] << std::endl;

// Should print
// Distance to vertex 0 is 3
// Distance to vertex 1 is 2
// Distance to vertex 2 is 1
// Distance to vertex 3 is 0
// Distance to vertex 4 is 1
// Distance to vertex 5 is 2
// Distance to vertex 6 is 2
// Distance to vertex 7 is 1


  return 0;
}
```
{% endraw %}

***

#### Answer Assignment 03
The condition must be such that one of the vertex of the edge is in the set of the vertex with index i, while the other is not
```c++
condition 1: rooti == root0 & rooti != root1
condition 1: rooti != root0 & rooti == root1
```

***
