---
title: "Types of States"
---

## Recurring and Transient States
First lets define **accessible** states. A state $j$ is accessible from $i$ if $r_{ij}(n)$ is positive for sufficiently large $n$. This means even after running the chain for a long time, its possible to reach $j$ from $i$.

A state $i$ is called **recurrent** if, starting from $i$, and travelling anywhere, it is always possible to return to $i$. Using the concept of _accessibility_ defined above, let $A(j)$ denote the set of states accessible from $j$. Then, for every state $i \in A(j)$, $j \in A(i)$. Meaning that we can wander to any accessible state of $j$ and expect to return back to $j$ with finite probability.

If a state is not recurrent, it is **transient**. This means that there exists at least one $i \in A(j)$ such that $j \notin A(i)$.

All these definitions only depend on the sign of the transition probabilities (whether they are positive or not), and not on the values.

In the below figure, we see examples of different types of states.
* State 1 is recurrent since only 1 is accessible from 1.
* 2 is transient since all other states are accessible from 2, but 2 is not accessible from either of those.
* 3 and 4 are accessible only from each other and are thus recurrent.

{% include image.html url="notes/probability/images/markov_3.png" description="Sample Markov chain with transient and recurrent states" img_classes="notes-img markov_3" %}

Any set of states such that they are all accessible from each other form a _recurrent class_. In the figure above, states 3,4 from one recurrent class while state 1 is a recurrent class in itself.

### Markov Chain Decomposition
* A Markov chain can be decomposed into one or more recurrent classes, plus a few transient states.
* A recurrent state is accessible from all other recurrent states in its class, but is not accessible from states in other recurrent classes.
* A transient state is not accessible from any recurrent state.
* At least one, possibly more, recurrent states are accessible from a given transient state.

Decomposing a Markov chain and understanding the recurrent and transient components is a great way to reason out the behaviour of the chain. We note the following two observations
* If a chain enters or starts in a class of recurrent states, it stays within the class since by definition they are all accessible from each other and are visited an infinite number of times.
* If the initial state is transient, the chain first goes through a set of transient states before finally settling down in a class of recurrent states.

States in a recurrent class are **periodic** if they can be grouped into $d > 1$ groups such that all transitions from one group lead to the next group (in a fixed order). A recurrent class is **aperiodic** if it is not periodic.
