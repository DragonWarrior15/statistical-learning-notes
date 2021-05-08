---
title: "Key Considerations while Clustering"
---

## Key Considerations while Clustering

Following are a set of general rules when doing clustering

-   centering and bringing the variables to the same scale is useful when measuring Euclidean distance for the obvious reason of not letting magnitudes affect the distances.

-   Different types of clustering approaches should be explored to check which performs the best. This is important as in unsupervised learning, the structure of data is not known beforehand and it is important to explore multiple hypothesis.

-   Several choices of similarity measures and linkages can be explored for further understanding of data.

-   Clustering can be non robust and thus the results should be _validated_ by performing clustering on multiple subsets of data to assure stability.

-   In come cases, the hard cluster assignment of $K$-means and hierarchical clustering may not be useful. Probabilistic models like mixture models can be explored in this case.
