---
title: "K-Mediods Clustering"
---

## K-Mediods Clustering

This method is very similar to K-Means with the difference that the cluster centres are restricted to be one of the data points in the training set. Thus, the algorithm becomes

1.  Randomly select $K$ points as the cluster centres, and assign every observation in the training set to the cluster with the closest centre.

2.  For each cluster, find the point in that cluster that has the minimum total cluster distance to all the other points in the cluster.

3.  Repeat steps 1 and 2 till convergence.

The restriction of cluster centre being an oberved data point increases the computational cost because now we do not have a direct solution of the next cluster centre, but must rather iterate through all the points in the cluster.


This restriction gives rise to the property that while working with this algorithm, if we have the matrix corresponding to the dissimilarity measures, we do not need to know the individual attributes since we are not using those in the computations anymore. All the steps of the algorithm only require us to keep track of the indices that are cluster centres and the cluster assigned to each index. The dissimilarity measure can be directly used to compute the next cluster centre/cluster assignment.
