## Positional Encodings

The current transformer architecture is equivariant to permutations of the input. That is, the current network does not care about the ordering of the words. Two sentences with the same ordering but different meanings will give the same output from this architecture.

However, in practices, the order of elements in the sequence does matter, and we want the network to focus on the ordering as well.

### Desired Properties
We want the positional information to have the following characteristics
- Add position information in the input instead of the architecture so that we retain the powerful parallelization of transformers
- We should add the information in the input instead of concatenation, as the latter will simply increase the dimensionality
    - The intuition behind addition is that two randomly chosen vectors (uncorrelated) tend to be orthogonal in spaces of very high dimensions
    - Due to this orthogonal nature, network is able to isolate them into individual components wherever needed
    - This saves us a lot of compute as concatenation would drastically increase the network parameters, as seen in the compute section earlier (dependence on $D$)
- Linear processing in transformers means that additive transformation behaves very similar to concatenated representation

$$
\begin{aligned}
\tilde{X_{n}} = X_{n} + R_{n}
\end{aligned}
$$

where $R_{n}$ is the positional encoding vector.

### Ideal Position Encoding
- Provides a unique representation of each position
- Is bounded
- Should generalize to longer sequences
- Should have a good consistent way to represent the number of steps between two tokens
    - In practice, the distance between tokens is often more valuable than their absolute positions in the sequence
    - i.e, the relative positions matter more than the absolute ones

### Sinusoidal Encodings
One simple approach is to use $sin$ and $cos$ functions that depend on the sequence length and the position

$$
\begin{aligned}
r_{ni} = \begin{cases}sin\bigr(\frac{n}{L^{i/D}}\bigr)&(i \enspace \text{is even})\\cos\bigl(\frac{n}{L^{(i-1)/D}}\bigr)&(i \enspace \text{is odd})\end{cases}
\end{aligned}
$$

$r_{n}$ has elements which are $sin$ and $cos$ functions of increasing wavelengths.
