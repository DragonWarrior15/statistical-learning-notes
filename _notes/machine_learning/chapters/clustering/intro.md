---
title: "Clustering"
---

# Clustering

Clustering is an unsupervised learning techniques that aims to finds clusters or groups in the data such that observations in the same group are similar to each other while observations in different groups are different from each other.


Clustering is useful for an exploratory analysis of the data and also useful in problems like customer segmentation. It comes in three flavours

-   **Combinatorial Algorithms** : such algorithms work using the provided data, without assuming any underlying probability distribution.

-   **Mixture Modelling** : such algorithms assume the data to be independently and identically distributed from a probability distribution whose parameters are unknown. The same distribution with different parameters is assumed for each of the clusters, and the intent is to find the parameters through the data, usually using Maximum Likelihood.

-   **Mode Seeking Algorithms** : these algorithms aim to find modal points in the data where the density of the points is highest. Observations close to the mode define the cluster. PRIM is a fine example of such bump hunting algorithm.
