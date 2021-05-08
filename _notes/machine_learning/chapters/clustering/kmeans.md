---
title: "K-Means Clustering"
---

## K-Means Clustering

A very powerful technique that organizes the data into $K$ distinct groups such that each observation will fall into exactly one group and when all the groups are combined, they cover the entire data set. $K$ is determined beforehand and is the number of clusters we are going to make.


The fundamental idea of clustering is to reduce the within cluster variation. Let $C_{k}$ denote the set containing the indices of the points falling in the cluster $k$ and $W(C_{k})$ be the within cluster variation for cluster $k$. Then,
\begin{align}
        \minimize_{C_{1},\ldots,C_{K}} \sum_{k=1}^{K} W(C_{k})
    \end{align}

Using Euclidean distance as a measure of the intercluster distance between two points, we can redefine the optimization summing across all the dimensions of the data as
\begin{align}
        \minimize_{C_{1},\ldots,C_{K}} \sum_{k=1}^{K} \frac{1}{\vert C_{k} \vert} \left\\{\sum_{i_{1}, i_{2} \in C_{k}} \sum_{j=1}^{p} (x_{i_{1}j} - x_{i_{2}j})^{2} \right \\}
    \end{align}
where $\vert C_{k} \vert$ is the number of observations in the cluster $C_{k}$. Considering all possible partitions is impossible for large $n$ and we use the following algorithm to obtain the local optimum.

### Algorithm

We repeat the following until some predefined convergence criteria

1.  Randomly assign a cluster in $1, \ldots, K$ to each observation in the data.

2.  Repeat the following till convergence

    1.  Calculate the centroid for each cluster where centroid is a $p$ dimensional vector whose each component is the average of the components of all the points that fall in the considered cluster.

    2.  Assign each observation the cluster index of the centroid that is closest to the given observation (using Euclidean distance).

**It is usually a good idea to center and standardize the variables first** so that the individual magnitudes and variances don't affect the Euclidean distances drastically.

To see why using distance from centroid is a good replacement for the pairwise distance, consider the following equation
\begin{align}
        \sum_{i_{1}, i_{2} \in C_{k}} (x_{i_{1}} - x_{i_{2}})^{T} (x_{i_{1}} - x_{i_{2}}) = \frac{1}{2} \sum_{i \in C_{k}} \sum_{j \in C_{k}} (x_{i} - x_{j})^{T}(x_{i} - x_{j})
    \end{align}
where the right side allows for all possible pairs including the ones where the indices might repeat. Continuing to expand the right hand side,
\begin{align}
        \sum_{i \in C_{k}} \sum_{j \in C_{k}} (x_{i} - x_{j})^{T}(x_{i} - x_{j}) &= \sum_{i \in C_{k}} \left(\vert C_{k} \vert (x_{i}^{T} x_{i}) - 2x_{i}^{T} \sum_{j \in C_{k}} x_{j} + \sum_{j \in C_{k}} x_{j}^{T} x_{j} \right)\newline
        &= \sum_{i \in C_{k}} \left( \vert C_{k} \vert (x_{i}^{T} x_{i}) - 2\vert C_{k} \vert x_{i}^{T} \bar{x} + \sum_{j \in C_{k}} x_{j}^{T} x_{j} \right)\newline
        &= \sum_{i \in C_{k}} \left( \vert C_{k} \vert (x_{i}^{T} x_{i}) - 2\vert C_{k} \vert x_{i}^{T} \bar{x} \right) + \sum_{i \in C_{k}} \vert C_{k} \vert x_{i}^{T} x_{i}\newline
        &= \sum_{i \in C_{k}} \left( 2\vert C_{k} \vert (x_{i}^{T} x_{i}) - 2\vert C_{k} \vert x_{i}^{T} \bar{x} \right)\newline
        &= 2 \vert C_{k} \vert \left\\{ \left( \sum_{i \in C_{k}}  (x_{i}^{T} x_{i}) \right) - \vert C_{k} \vert \bar{x}^{T} \bar{x} \right\\}\newline
        &= 2 \vert C_{k} \vert \left\\{ \left( \sum_{i \in C_{k}}  (x_{i}^{T} x_{i}) \right) - 2\vert C_{k} \vert \bar{x}^{T} \bar{x} + \vert C_{k} \vert \bar{x}^{T} \bar{x} \right\\}\newline
        &= 2 \vert C_{k} \vert \left\\{ \left( \sum_{i \in C_{k}}  (x_{i}^{T} x_{i}) \right) - 2 (\sum_{i \in C_{k}} x_{i}^{T} \bar{x}) + \vert C_{k} \vert \bar{x}^{T} \bar{x} \right\\}\newline
        &= 2 \vert C_{k} \vert \left\\{ \sum_{i \in C_{k}}  x_{i}^{T} x_{i} - 2 x_{i}^{T} \bar{x} + \bar{x}^{T} \bar{x} \right\\}\newline
        &= 2 \vert C_{k} \vert \left\\{ \sum_{i \in C_{k}}  (x_{i} - \bar{x})^{T} (x_{i} - \bar{x}) \right\\}\newline
        \text{Thus, } \frac{1}{\vert C_{k} \vert} \left\\{\sum_{i_{1}, i_{2} \in C_{k}} \sum_{j=1}^{p} (x_{i_{1}j} - x_{i_{2}j})^{2} \right\\} &= \left\\{ \sum_{i \in C_{k}}  (x_{i} - \bar{x})^{T} (x_{i} - \bar{x}) \right\\}
    \end{align}

Thus, the quantity we set out to minimize for each cluster is indeed the sum of distance of each point from the centroid of the cluster, which means the cluster is to be chosen based on the closest centroid to minimize the overall intra cluster distance.


**The optimum found by K-means clustering is local which makes it important to run the algorithm with different random initializations to get the minima**.


**Elbow Curve** is a plot between the total intra cluster distance vs the number of cluster $K$ and is a visual method to obtain the optimum number of clusters to use. The elbow shape refers to the fact that if there is indeed clusters present in the data, the plot will see a sharp decline in the intra cluster distance for some $k$.

Note that the curve is going to always keep decreasing as in the limiting case when we have $n$ points and $n$ clusters, the total distance will be zero. Hence, the number of clusters must be carefully chosen.


K-Means has a few problems when working with a dataset. Firstly, it requires all data to be numeric, and the distance metric used is the squared distance. Hence, the algorithm lacks robustness and is sensitive to outliers. Hence, it is worthwhile to explore other clustering strategies and dissimilarity measures that better suit the data
