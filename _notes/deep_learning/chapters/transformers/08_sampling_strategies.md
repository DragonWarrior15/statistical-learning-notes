## Sampling Strategies
There are several sampling strategies when we want to select a single token from a probability distribution, which is the output of a transformer network

### Greedy
- Simply select the token with highest probability
- This is not the same as choosing the most probably sequence, or the sequence with the highest probability, since in the joint distribution, successive probabilities are not independent
- greedy search costs $O(KN)$, since choosing the best at each step is a $O(K)$ operation, same as the dictionary size

### Beam Search
The core concept is to maintain a set of $B$ hypothesis at each stage of generation
- This is equivalent to saying, maintain a set of $B$ most probable sequences at any given stage
- For $B$ sequences, run each through the network, and choose the most probable $B$ tokens for each sequence
- Prune to $B$ most probably sequences by taking the joint probability distributions (note we must maintain this joint probability along with the sequences)
- The complexity of this approach is $O(BKN)$
    - At each stage we run over all $K$ probabilities $B$ times
    - The cost of pushing to a heap to get top $B$ tokens is $O(BlogB)$ and neglibible here ($B$ is typically 3 to 5, rarely exceeding 10)
    - We repeat the process $N$ times for a sequence of length $N$

### Top-p Sampling
- Calculates the cumulative probability till a threshold is reached
- Randomly sample from these top probabilities after renormalization (dont use greedy search or anything similar here as that will end up defeting the process of filtering top tokens since the max is same irrespective)

### Top-K Sampling
Equivalent to Top-p, but we sample from the top $K$ tokens instead of tokens with a cumulative probability threshold

### Temperature
Introduces a term $T$ in the softmax function

$$
\begin{aligned}
y_{i} = \frac{exp(a_{i}/T)}{\sum_{j=1}^{N}exp(a_{j}/T)}
\end{aligned}
$$

and it can be interpreted as below
$$
\begin{aligned}
T \to 0 &: \text{greedy search}\\
T = 1 &: \text{usual softmax}\\
T \to \infty &: \text{uniform distribution}\\
\end{aligned}
$$

Higher the $T$ (above 1), the more randomness we introduce into the system. Lower $T$ accentuates the differences between the logits.

Temperature flattens the distribution to give lower probability tokens higher chance of getting selected. Top-p acts as a physical cutoff for the tail of the distribution.

### Interaction of Temperature and Top-p
Lets look at different scenarios

| Sr No | Scenario | Interpretation | Outcome |
| --- | --- | --- | --- |
| 1 | High Temperature + Standard Top-p | High temperature forces flattening of distribution, meaning a standard top-p of say 0.9 will have to consider more tokens | Model is creative |
| 2 | High Temperature + Aggressive Top-p/Top-K | Distribution is still flattened, but the number of tokens considered is much more restricted | Model is somewhat creative, but prevented from generating gibberish |
