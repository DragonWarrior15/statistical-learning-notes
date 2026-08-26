---
title: "Gaussian Mixture Models (GMM)"
---

## Gaussian Mixture Models (GMM)

GMM is a soft assignment method where we don't assign a cluster to each data point, rather we know the relative probabilities of the point belonging to individual clusters. Suppose there are $K$ clusters and $\theta$ denote the common set of parameters for $K$ independent gaussian distributions, then,

$$
\begin{aligned}
    p(x_{i}|\theta) = \sum_{j=1}^{K} \pi_{j} \big( \mathcal{N}(\mu_{j}, \sigma_{j}^{2}) \; at \; x_{i} \big)\newline
    \text{with,} \quad \sum_{j=1}^{K} \pi_{j} = 1, \quad \pi_{j} \geq 0, \quad \Sigma_{j} > 0\newline
    \theta = \{ \pi_{1}, \ldots, \pi_{K}, \mu_{1}, \ldots, \mu_{K}, \Sigma_{1}, \ldots, \Sigma_{K} \}
\end{aligned}
$$

where $\pi$ are probabilities of a point belonging to a particular cluster, and is constant for the whole data set. This implies that to calculate the likelihood of each data point, we are using a weighted sum of all the gaussians.

The additional constraint on covariance matrices simply means that they are positive semi definite, which is a necessary condition for invertability, and we know that the inverse is used in the probability distribution of a mutivariate normal.


The parameters can be found by maximizing the log likelihood of the data

$$
\begin{aligned}
    \max_{\theta} \prod_{i=1}^{N}\sum_{j=1}^{K} P(x_{i}|\text{cluster} = j)P(\text{cluster} = j)\newline
    \text{subject to} \quad \sum_{j=1}^{K} \pi_{j} = 1, \quad \pi_{j} \geq 0, \quad \Sigma_{j} > 0
\end{aligned}
$$

which is often difficult to perform due to the complexity of the distribution. When we take log on both sides, we will still have a summation inside the log term making optimization difficult.


### The Algorithm

To solve the problem of GMMs in a tractable way, we formulate a latent variable $t_{i}$ for each data point that indicates which cluster the point came from. This will be the same as $\pi_{j}$ defined earlier

$$
\begin{aligned}
    p(t = j|\theta) = \pi_{j}, \quad \sum_{j=1}^{K} p(t = j|\theta) = 1\newline
    p(x_{i} | \theta) = \sum_{j=1}^{K} p(x_{i} | t = j, \theta) p(t = j|\theta)
\end{aligned}
$$

The last equation formulates the original equations in a conditional probability format.


#### Calculating parameters when cluster assignments are known

Suppose we already knew the cluster assignments of each of the points, then we could simply calculate the mean of the gaussians as

$$
\begin{aligned}
    \mu_{j} = \frac{\sum_{i=1}^{N} I(t_{i} = j) x_{i}}{\sum_{i=1}^{N} I(t_{i} = j)}
\end{aligned}
$$

which is nothing but the MLE estimate of a gaussian distribution (assuming we know the points which fall in this particular gaussian). Here, $I(t_{i} = j)$ denotes the indicator variable for whether the $i^{th}$ point belongs to cluster $j$. Summing up such indicator variables helps us total up the count of points inside that cluster, which is represented in the denominator. On similar lines, the numerator of the above expression follows.

In our case, we do not know the hard assignments, but rather the soft assignments. Define responsibility as below

$$
\begin{aligned}
\gamma_{ij} = p(t_{i}=j|x_{i},\theta)
\end{aligned}
$$

Now, we modify the above formula to include all points, but weighted by the cluster assignment probabilities (responsibilities)

$$
\begin{aligned}
    \mu_{j} = \frac{\sum_{i=1}^{N} \gamma_{ij} x_{i}}{\sum_{i=1}^{N} \gamma_{ij}}
\end{aligned}
$$

which is very similar to the earlier hard cluster assignment expression, but we are using probabilities instead of binary assignments. The transition is simply $I(t_{i}=j) \to \gamma_{ij}$.


#### Calculating cluster assignment when parameters are known

If we know the parameters of the gaussian already, we can derive the cluster assignments as

$$
\begin{aligned}
    p(t_{i} = j|x_{i}, \theta) \propto \pi_{j} \mathcal{N}(\mu_{j}, \Sigma_{j}) \; at \; x_{i}\newline
    \sum_{j=1}^{K} p(t_{i} = j|x_{i}, \theta) = 1
\end{aligned}
$$

where the last equation helps in normalization to get valid probability distributions. The first expression can be derived by considering $p(x_{i}|\theta)$, $p(x_{i}|t_{i}=j, \theta)$ and Bayes rule.

We can notice that we have landed in a cyclic problem. Given the cluster assignments, we can always calculate the gaussian parameters, and given the gaussian parameters, cluster assignments can be calculated.

Hence, to solve the problem of estimating the GMM parameters, we break it in two steps, similar to Expectation Maximization (EM) Algorithm (In EM, we generally initialize $\theta$ first)

1.  Assume a random value for the parameters of the gaussians (with all $\Sigma_{j} > 0$)
2.  Repeat until convergence of likelihood
    1.  Calculate soft cluster assignments for all points using (we are inferring the distribution over $t$ here)

        $$
        \begin{aligned}
            \gamma_{ij} \propto \pi_{j} \mathcal{N}(\mu_{j}, \Sigma_{j}) \; at \; x_{i}, \quad \sum_{j=1}^{K} \gamma_{ij} = 1
        \end{aligned}
        $$

    2.  Calculate gaussian parameters using the above cluster assignments
        
        $$
        \begin{aligned}
            \mu_{j} = \frac{\sum_{i=1}^{N} \gamma_{ij} x_{i}}{\sum_{i=1}^{N} \gamma_{ij}}
        \end{aligned}
        $$


This is a simplified version of EM algorithm. EM is known to give local optima (global optima is NP hard) and hence the results will vary with different initializations. Advisable to try and check different initializations.

The E step calculates the expected likelihood, while the M step gathers the updated $\theta$ to maximize that log likelihood.
