---
title: "C++ Exercises 02"
---

## Course 02: some name

***

### Quiz 01

1. ```c++
    int tri(int n) {
        int i,j;
        int count = 0;
        for (j=0; j < n; j++){
            for (i=0; i < j; i++){
                count++;
            }
        }
        return count;
    }
    ```
    Perform a run-time analysis of the code above. Express the number of times the variable count is incremented in terms of "Big Oh" notation.
    Recall that "Big Oh" notation is denoted as O() where the parameter of O() is a simple function of n that indicates how the run-time increases as n increases. For example, if the run-time grows as a polynomial of n, such as `5n^3 + 3n^2` then the "Big-Oh" notation would ignore constants and lower growing terms and simply state O(n^3) growth.
    1. O(n^2 + n)
    1. O(1)
    1. O((1/2) n^2)
    1. O(n^2)

2. You have an array that is currently length one and already contains one item. You need to implement a function Append(i) that adds the item i to the position after the current last item of the array. If the array is full, then your Append() function will need to expand the size of the array so that it can store the additional item i. Recall that expanding the size of an array requires allocating new memory for the expanded size and copying all of the current array items to the new (expanded) array before de-allocating the previous (full) array.
    (It is okay to assume there is always enough memory to allocate for an array.)
    Your Append() function will be called an unknown number of times. Which method for resizing the array would result in the fastest total run-time for calling Append() n times to add n items to the array?
    1. Doubling the length of the array every time an item is added when the array is already full.
    1. Increasing the length of the array by one every time an item is added.
    1. Increasing the length of the array by one billion every time an item is added and the array is already full.
    1. Expanding the array to length n + 1 the first time Append() is called.

3. Which one statement below is **FALSE**? Assume we are using the most efficient algorithms discussed in lecture.
    1. Adding n items, one at a time, to the end of an array takes O(n) time overall.
    1. Finding an item in a sorted array of n items cannot be done in better than O(n) time.
    1. Adding n items, one at a time, to the front of a linked list takes O(n) time overall.
    1. Finding an item in a sorted linked list of n items takes O(n) time.

4. You have a list of 100 items that are not sorted by the item value. Which one task below would run much faster on a list implemented as an array rather than implemented as a linked list?
    1. Inserting a new item between the 24th item and the 25th item.
    1. Searching the list for all items that match a given item.
    1. Finding the first item.
    1. Replacing the 25th item in the list with a different item.

5. You have a list of 100 items that are not sorted by the item value. Which one task below would run much faster on a list implemented as linked list rather than implemented as an array?
    1. Inserting a new item between the 24th item and the 25th item.
    1. Replacing the 25th item in the list with a different item.
    1. Finding the first item
    1. Searching the list for all items that match a given item.

6. Suppose you want to implement a queue ADT using a linked list. Your queue needs to be able to "push" (or "enqueue") a single item in constant time, as well as "pop" (or "dequeue") a single item in constant time. The operations need to happen at opposite ends of the queue, as would be expected of the queue ADT. However, the people who use your queue implementation don't need to know about how exactly it is implemented, so you can be somewhat creative in how you implement it, as long as the "push" and "pop" operations behave as expected. Which of the following implementations can accomplish this? Select all that apply. (For the sake of this question, let's not consider any design strategies that would close the linked list into a circle.)
    1. You can do it with a modified singly-linked list where the list has both a "head" pointer and a "tail" pointer, but each node has only a "next" pointer.
    1. You can't implement a queue as a linked list. You need a more advanced data structure.
    1. You can do it with a doubly-linked list where the list has a "head" pointer and a "tail" pointer and each node has a "next" pointer and a "previous" pointer.
    1. You can do it with a singly-linked list where the list has only a "head" pointer and each node has only a "next" pointer.

7. When implementing a queue which will need to support a large number of calls to its push() and pop() methods, which choice of data structure results in a faster run time according to "Big Oh" O() analysis?
    1. The linked list implementation of a queue has a better run time complexity than does the array implementation.
    1. A linked list because an array cannot be used to implement a queue that supports both push() and pop() methods.
    1. The array implementation of a queue has a better run time complexity than does the linked list implementation.
    1. Both array and linked list implementations of a queue have the same run time complexity.

8. When implementing a stack which will need to support a large number of calls to its push() and pop() methods, which choice of data structure results in a faster run time according to "Big Oh" O() analysis?
    1. The linked list implementation of a stack has a better run time complexity than does the array implementation.
    1. The array implementation of a stack has a better run time complexity than does the linked list implementation.
    1. Both array and linked list implementations of a stack have the same run time complexity.
    1. An array implementation because a linked list cannot be used to implement a stack that supports both push() and pop() methods.

9. Suppose this stack is implemented as a linked list.
    ```c++
    std::stack<int> s;
    s.push(1);
    s.push(2);
    s.push(3);
    ```
    What is the value at the head of the linked list used to implement the stack s?
    1. 1
    1. 3
    1. 2
    1. A stack cannot be implemented using a linked list.

10. Suppose we had the following interface for a stack and queue, along with a correct implementation.
    (Note that in this simple version, the "pop" and "dequeue" methods will remove an item and also return a copy of that same item by value. This is a little different from how the C++ Standard Template Library implementations of a stack and queue work. In STL, you have separate functions for peeking at the next value that would be removed, and for actually removing the item.)
    ```c++
    class Stack{
        public:
            Stack();
            bool push(int x);
            int pop();
            bool isEmpty();
        // other lines omitted
    };
    class Queue{
        public:
            Queue();
            bool enqueue(int x);
            int dequeue();
            bool isEmpty();
        // other lines omitted
    };
    ```
    What output does the following code produce?
    1. 4 3 2 1 0
    1. 0 1 2 3 4 4 3 2 1 0
    1. 4 3 2 1 0 0 1 2 3 4
    1. 0 1 2 3 4

***

#### Answers 01

| Question | Answer |
| -------- | ------ |
| 1 | iv |
| 2 | i |
| 3 | ii |
| 4 | iv |
| 5 | i |
| 6 | ii, iii |
| 7 | iv |
| 8 | iii |
| 9 | ii |
| 10 | iv |

***

### Quiz 02

1. For a linked structure of edges and nodes to be a tree, which of the following is **not** required to be true?
    1. Every node is connected to every other node by some path of edges.
    1. Every node has zero, one or two children.
    1. If any two nodes are connected, they are connected by only one path of unique nodes and edges.
    1. Every node has a parent except for one single root node.

2. Which data structure below supports the fastest run time for finding an item in a sorted list of items?
    1. Array
    1. Linked List
    1. Binary Search Tree
    1. All of these data structures have the same run time complexity for finding an item in a sorted list of items.

3. What is the height of the binary search tree created by inserting the following values one at a time in the following order of insertion: 1 2 3 4 5 6 7 ?
    1. 2
    1. 3
    1. 6
    1. 7

4. Which of the following is **NOT** true of a perfect binary search tree of a list of  n ordered items?
    1. All of the leaf nodes are at the same level.
    1. The worst-case run time to find an item is O(n).
    1. If the height of the tree is h, then n =  2^(h+1) - 1.
    1. Every non-leaf node has two children.

5. Which of the following is **NOT** a full binary tree?
    1. A perfect binary tree.
    1. A single node.
    1. The binary tree consisting of the subtree of ancestors of any node in any perfect binary tree.
    1. The binary search tree created by inserting the following values one at a time: 4 2 3 5 1.

6. Which of the following is **not** a true statement about a complete binary tree?
    1. Any tree that contains a node with a single child is not a complete binary tree.
    1. The worst-case run time for finding an object in a complete binary search tree of an ordered list of n items is O(lg n).
    1. No node in a complete binary tree has only a right child.
    1. The height of a complete binary tree of n nodes is floor(lg n).

7. Which one of the following functions outputs the keys of a binary search tree in item order when the root node is passed to it as its parameter.
    1. ```c++
        void print(TreeNode *node){
            if (!node) return;
            std::cout << node->key << " ";
            print(node->left);
            print(node->right);
        }
        ```
    1. ```c++
        void print(TreeNode *node){
            if (!node) return;
            print(node->left);
            std::cout << node->key << " ";
            print(node->right);
        }
        ```
    1. ```c++
        void print(TreeNode *node){
            if (!node) return;
            print(node->left);
            print(node->right);
            std::cout << node->key << " ";
        }
        ```
    1. None of these outputs all of the keys of the binary search tree in item order.

8. Consider the binary search tree built by inserting the following sequence of integers, one at a time: 5, 4, 7, 9, 8, 6, 2, 3, 1
    Which method below will properly remove node 4 from the binary search tree?
    1. Set the left pointer of node 5 to point to the node pointed to by the left pointer of node 4, and then delete node 4.
    1. Find the in order predecessor (IOP) of node 4, which is node 3. Remove node 3 from the tree by setting the right pointer of its parent (node 2) to nullptr. Then copy the key and any data from node 3 to node 4, turning node 4 into a new node 3, and delete the old node 3.
    1. Find the in order predecessor (IOP) of node 4, which is node 3. Remove node 3 from the tree by setting the right pointer of its parent (node 2) to point to the node pointed to by the left pointer of node 3. Then copy the key and any data from node 3 to node 4, turning node 4 into a new node 3, and delete the old node 3.
    1. Set the left pointer of node 5 to nullptr, and then delete node 4.

9. Suppose that we have numbers between 1 and 1000 in a binary search tree and we want to search for the number 363.  Which of the following sequences can **not** be the sequence of nodes visited in the search?
    1. 925, 202, 911, 240, 912, 245, 363
    1. 2, 399, 387, 219, 266, 382, 381, 278, 363
    1. 2, 252, 401, 398, 330, 344, 397, 363
    1. 924, 220, 911, 244, 898, 258, 362, 363

10. Given any binary tree with 128 nodes where each node has a left pointer and a right pointer, how many of these pointers are set to nullptr?

***

#### Answers 02

| Question | Answer |
| -------- | ------ |
| 1 | ii |
| 2 | i |
| 3 | iii |
| 4 | ii |
| 5 | iii |
| 6 | i |
| 7 | ii |
| 8 | i |
| 9 | i |
| 10 | 129 |

***

### Quiz 03

**Assume that balance factor is height of right subtree - height of left subtree**

1. Create a binary search tree by inserting the following five values one at a time:
    4 6 5 7 8
    What is the height of this tree?
    (Recall how we calculate the height of a tree or subtree: The height of a leaf node by itself is 0. The height of a non-existent tree is -1. Otherwise, the height of a tree is the longest path length from the root of that tree to any one of its leaves.)

2. Create a binary search tree by inserting the following eight values one at a time:
    3 1 2 4 6 5 7 8
    What is the balance factor of the root node of this tree? (For this question, do not perform any rotations on this tree as you insert the items. It's just a binary search tree, not necessarily a balanced BST such as an AVL tree.)

3. For the binary search tree created by inserting these items in this order: 4 3 5 1 2, which node among 1 through 5 is the deepest node with a balance factor of magnitude two or greater? (For this question, do not perform any balancing rotations as you insert these items.)

4. Consider the binary search tree that you constructed in the previous question. If we interpret it now as an AVL tree, it has an imbalance that can be fixed with a rotation. (Remember that we focus on the deepest point of imbalance, where the magnitude of the balance factor is 2 or greater, to perform the rotation.)
    After performing the correct balancing rotation about the node that we identified in the previous question, the resulting tree is identical to which one of the following binary search trees? (We'll describe these other trees by listing the order in which you would insert items to create the trees directly.)
    1. Inserting `2 1 4 3 5` one node at a time.
    1. Inserting `3 2 4 1 5` one node at a time.
    1. Inserting `4 2 5 1 3` one node at a time.
    1. Inserting `3 5 2 4 1` one node at a time.

5. The code that ensures the balance of an AVL tree after node insertion or removal only checks if the height balance factor is +2 or -2. What happens if the height balance factor of a node in an AVL tree after node insertion or removal is greater that +2 or less than -2?
    1. When insertion and removal create a node whose height balance factor is greater than +2 or less than -2, that node always has a descendant with a height balance factor equal to +2 or -2 and when all of its descendant nodes are resolved, then its height balance factor will be no greater than +2 or no less than -2.
    1. There is additional code not shown that handles the cases when the height balance factor is greater than +2 or less than -2.
    1. An AVL tree never has a node with a height balance factor greater than +2 or less than -2, even after a node insertion or removal.
    1. We ignore nodes in an AVL tree with height balance factor greater than +2 or less than -2 because they are statistically rare and are unstable, such that they are removed as soon as any tree balancing rotation occurs.

6. If, after inserting a new node into an AVL tree, you now have a node with a height balance factor of -2 with a child with a height balance factor of -1, which of the following operations should be performed?
    1. Left Rotation
    1. Right-Left Rotation
    1. Right Rotation
    1. Left-Right Rotation

7. If, after inserting a new node into an AVL tree, you now have a node with a height balance factor of -2 with a child with a height balance factor of +1, which of the following operations should be performed?
    1. Right-Left Rotation
    1. Right Rotation
    1. Left Rotation
    1. Left-Right Rotation

8. Which one of the following is **NOT** a valid reason to choose the B-Tree representation over a standard AVL binary search tree?
    1. B-Trees require fewer block read accesses for tree operations.
    1. B-Trees have better algorithmic "Big-O" run-time complexity for the find operation.
    1. B-Trees run faster on large data sets than do AVL trees.
    1. B-Trees work faster in networked cloud environments than do AVL trees.

9. Which of the following statements is **NOT** true for a B-Tree of order m?
    1. All leaf nodes are at the same level of the B-Tree.
    1. Each node can have at most one more child than key.
    1. Each node can hold an ordered list of as many as m keys.
    1. Any node that is not the root or a leaf holds at least half of the total number of keys allowed in a node.

10. If a B-Tree is completely filled, meaning every node holds its maximum number of keys and all non-leaf nodes has the maximum number of children, then what happens when an additional key is inserted into the B-Tree?
    1. A new node containing the new key is added above the previous root and becomes the new root. The new root will have one pointer leading to the old root node.
    1. Every leaf node in the entire B-Tree becomes parent to a new leaf node, but all but one of these leaf nodes are "blank" placeholder nodes that contain zero key values.
    1. A new leaf node is simply added to the B-Tree.
    1. After searching for the leaf node where the new key should go, the leaf is split in half as two separate leaf nodes, and then the middle value is thrown up to the layer above as an inserted key, and this insertion and rebalancing repeats until a new root key rises to the top, which adds a layer to the tree.

***

#### Answers 03

| Question | Answer |
| -------- | ------ |
| 1 | 3 |
| 2 | 2 |
| 3 | 3 |
| 4 | iii |
| 5 | iii |
| 6 | iii |
| 7 | iv |
| 8 | ii |
| 9 | iii |
| 10 | iv |

***

### Quiz 04

1. Assume you are storing a complete binary tree as a contiguous list of keys in an array such that the root's key is stored at location 1 of the array, the keys from all of the nodes at the next level of the tree are stored  in left-to-right order in subsequent locations in the array, then similarly for all of the nodes of each subsequent level.
    At what array location would the key stored in the node that is the left child of the right child of the root?

2. When using an array to store a complete tree, why is the root node stored at index 1 instead of at the front of the array at index 0?
    1. We use index zero as a guard to prevent overstepping the root when propagating up the tree from its leaf nodes, which would cause a memory access fault.
    1. We avoid using index 0 to avoid confusion with the value of 0 (nullptr) that we normally store in the child pointer of a node to indicate that child does not exist.
    1. This makes the math for finding children and parents simpler to compute and to explain.
    1. Array index 0 is used to store the number of nodes in the complete tree stored in the array.

3. When is a binary tree a min-heap?
    1. When the leaf nodes represent the smallest values in the tree, and every leaf node is smaller than the root.
    1. When every node's value is less than its parent's value.
    1. When every node's value is greater than its parent's value.
    1. When every node's value lies between the maximum value of its left child's subtree and the minimum value of its right child's subtree.

4. How should one insert a new value into a heap to most efficiently maintain a balanced tree?
    1. Maintain the heap as a complete tree and insert a new value at the one new node position that keeps the tree as a complete tree. Then continually exchange the new value with the value of its parent until the new value is in node where it is greater than the value of its parent.
    1 .Maintain the heap as a balanced binary search tree. Walk down the tree from the root exploring the left children first, then the right children, until a node is found that is greater than the new value. Insert a new node with the new value at that position and make the previous node the left child of that new node. Rebalance the tree if the height balance factor magnitude of the new node or its parent exceeds one.
    1. Maintain the heap as an array. Walk down the tree from the root at position 1 in the array, exploring the left children first, then the right children, until a node position is found whose value is greater than the new value. Copy the value at that position and all subsequent positions in the array to one greater position in the array, and store the new value at that position.
    1. Maintain the heap as an AVL tree. Walk down the tree from the root exploring the left children first, then the right children, until a node is found that is greater than the new value. Insert a new node with the new value at that position and make the previous node the left child of that new node. Then call the appropriate rotation routine to rebalance the tree if the height balance factor magnitude of the new node or its parent reaches two.

5. The removeMin operation removes the root of a min-heap tree. Which of the following implements removeMin efficiently while maintaining a balanced min-heap tree.
    1. Replace the root value with the value of the last leaf (rightmost node at the bottom level) of a complete binary tree, and delete the last leaf. Then repeatedly exchange this last-leaf value with the smaller of the values of its node's children until this last-leaf value is smaller than the values of its node's children, if any.
    1. Delete the root and if the root has two children, then merge its left subtree with its right subtree by inserting each right subtree node value into the left subtree. Then delete the right subtree.
    1. Set the root value to +infinity. If the left child is smaller than the right child, perform a Right-Rotation, otherwise perform a Left-Rotation. Repeat this process at the new infinity-node location until the infinity node is a leaf, then remove and delete it.
    1. Increment the address used to indicate the base location of the array storing the complete binary tree.

6. How many nodes of a complete binary tree are leaf nodes?
    1. About a fourth.
    1. About the square root.
    1. Unknown. Could be one. Could be all.
    1. About half.

7. Recall that the heapifyDown procedure takes a node index whose children (if any) are heaps, but the value of the node might not satisfy the heap property compared to its children's values. This procedure then swaps the node's value with the smallest child value larger than it (if any), and then calls itself on that smallest child node it just swapped values with to further propagate that value down the heap until it finds a valid location for it.
    ```c++
    template <class T>
    void Heap<T>::_heapifyDown(int index) {
        if (!_isLeaf(index)) {
            T minChildIndex = _minChild(index);
            if (item_[index] > item_[minChildIndex] ) {
                std::swap( imem_[index], item_[minChildI]);
                _heapifyDown(minChildIndex);
            }
        }
    }
    ```
    When you call heapifyDown on a given node, what is the maximum number of times heapifyDown is called (including that first call) to find a valid location for the initial value of that node?
    1. The maximum number of times heapifyDown is called is the number of non-leaf nodes in its subtree.
    1. heapifyDown is only called once since its children are already heaps.
    1. The maximum number of times heapifyDown is called is one plus the height of the node.
    1. The maximum number of times heapifyDown is called is the number of nodes in its subtree.

8. What is the run-time algorithmic complexity of calling heapifyDown on every non-leaf node in a complete tree of n nodes?
    1. O(n lg n)
    1. O(1)
    1. O(n^2)
    1. O(n)

9. Which of the following is the fastest way to build a heap of n items?
    1. Create a complete tree of the items in any order, then call heapifyUp on every node in the tree from the root down to the leaf nodes.
    1. Create a complete tree of the items in any order. If this is not a heap, then swap the items between two randomly chosen nodes and check again. Repeat the random swapping until you get a heap.
    1. Create a complete tree of the items in any order, then call heapifyDown on every non-leaf node from the bottom of the tree up to the root.
    1. Create a heap with a single node holding the first item. Then insert the remaining n-1 items into the heap.

10. Which of the following is NOT a step of the heap sort algorithm?
    1. Load the data in any order into a complete tree.
    1. Run heapifyDown on every non-leaf node.
    1. Remove the root node.
    1. Insert the next item into the current heap.

***

#### Answers 04

| Question | Answer |
| -------- | ------ |
| 1 | 6 |
| 2 | iii |
| 3 | iii |
| 4 | i |
| 5 | i |
| 6 | i |
| 7 | iii |
| 8 | iii |
| 9 | iii |
| 10 | iv |

***

### Assignment 1

Implement downHeap(Node \*n) for a min heap data structure, that is here implemented as a node-based binary tree with an integer member variable "value" and left and right child pointers. (Unlike the video lesson which implemented downHeap on an array implementation of a complete binary tree, the binary tree in this challenge problem is not stored as an array and is not necessarily complete; any node might have only a left child, only a right child, both, or neither.)

The starter code below defines a class called "Node" that has two child pointers ("left" , "right") and an integer "value" member variable. There is also a constructor Node(int val) that initializes the children to nullptr and the node's value to val.

Your job is to implement the procedure "downHeap(Node \*n)" . The procedure should assume that n->left is the root of a min heap subtree (or nullptr) and the same for n->right.  The value at Node \*n (specifically n->value) might not be less than the values in its left subtree and in its right subtree, and so the tree with Node \*n as its root might not be a min heap (even though its left subtree and right subtree are both min heaps). Your code should modify the tree rooted at Node \*n so it is a min heap. You do not need to balance the tree or turn it into a complete tree. You only need to ensure that the tree satisfies the min heap property:

For a min heap, it is okay for a node's value to be equal to one or both of its children, but the node's value must not be greater than either of its children. You should not perform swaps with nodes of equal value, as this does needless work.

Again, as is implied by the above description, for this exercise you may assume that only the root node violates the min heap property at the beginning, if any node does (as the left and right subtrees are already valid heaps). This means it's possible to implement the downHeap function as O(log n). If your algorithm has a running time worse than O(logn), it is probably incorrect. The significance of this O(log n) algorithm is that it can be used as an efficient tool in the O(n)-time algorithm that corrects a new heap in multiple steps from the bottom up, as described in lecture.

```c++
/*

Below, please implement the downHeap procedure for
a min heap data structure, which we will represent
as node-based tree for this exercise (not an array).

Suppose you are given a tree where the left and right
subtrees are min heaps, but the root node in particular
might not maintain the min heap property. Your code
should modify the tree rooted at Node* n so it is a
min heap. This means you need to satisfy the min heap
property: it is okay for a node's value to be equal to
one or both of its children, but the node's value must
not be greater than either of its children.

Tips:
Unlike the video lessons which demonstrated downHeap
implemented with an array implementation, this assignment
uses an ordinary binary tree with left and right child
pointers. This ordinary binary tree might not be complete
or balanced: any node might have only one child or the
other, or both, or neither. (You do not have to try to
balance the tree or turn it into a complete tree.)

If the root node exists, and if it has a left or right
child, and if one of the children has a smaller value
than the root node, then you should swap the root node
with the smaller child to move the large value down
into the tree. (This may need to be done recursively.)
Be careful to check whether pointers are null before
dereferencing them, as always; that includes using "->"
to access a class member through a pointer. In addition,
you must be careful not to accidentally compare "left"
and "right" pointers directly if you really intend to
compare the stored values "left->value" and "right->value".

Assume that these headers have already been included
for you:

#include <iostream>
#include <string>

You have the following class Node already defined.
You cannot change this class definition, so it is
shown here in a comment for your reference only:

class Node {
public:
  int value;
  Node *left, *right;
  Node(int val = 0) { value = val; left = right = nullptr; }
  ~Node() {
    delete left;
    left = nullptr;
    delete right;
    right = nullptr;
  }
};

This function has also previously been defined for you:

void printTreeVertical(const Node* n);

You can use it to print a verbose, vertical diagram of
a tree rooted at n. In this vertical format, a left child
is shown above a right child in the same column. If no
child exists, [null] is displayed.

*/


void downHeap(Node *n) {
  Node * swap_with = nullptr;
  // Implement downHeap() here.
}

// You can also use this compact printing function for debugging.
void printTree(Node *n) {
  if (!n) return;
  std::cout << n->value << "(";
  printTree(n->left);
  std::cout << ")(";
  printTree(n->right);
  std::cout << ")";
}

int main() {
  Node *n = new Node(100);
  n->left = new Node(1);
  n->right = new Node(2);
  n->right->left = new Node(3);
  n->right->right = new Node(4);
  n->right->right->right = new Node(5);

  downHeap(n);

  std::cout << "Compact printout:" << std::endl;
  printTree(n);
  std::cout << std::endl << "Vertical printout:" << std::endl;
  printTreeVertical(n);

  delete n;
  n = nullptr;

  return 0;
}

```

#### Answer Assignment 01
```c++
void downHeap(Node *n) {
  Node * swap_with = nullptr;
  // Implement downHeap() here.
  // if no child, do nothing
  if(!n->left && !n->right){}
  else if(!n->left && n->right){
    // check if value is greater than the right child
    if(n->value > n->right->value){
      swap_with = n->right;
    }
  }else if(n->left && !n->right){
    // check if value is greater than the left child
    if(n->value > n->left->value){
      swap_with = n->left;
    }

  }else{
    // both children exist
    if(n->value <= n->left->value && n->value <= n->right->value){}
    else{
      if(n->left->value < n->right->value){
        swap_with = n->left;
      }else{
        swap_with = n->right;
      }
    }
  }

  if(swap_with){
    int temp = n->value;
    n->value = swap_with->value;
    swap_with->value = temp;
    downHeap(swap_with);
  }
}
```

***
