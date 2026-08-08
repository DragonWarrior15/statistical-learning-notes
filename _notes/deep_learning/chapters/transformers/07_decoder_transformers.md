## Decoder Transformers
We build upon a similar intuition from the previous section on sequence modelling, specifically the RNN case.

- Input is the $n-1$ tokens and output is the $n^{th}$ token
- Can do this recursively to keep generating the next token (by feeding the latest token back into the sequence)

### Training
This is simply next token predition problem, given the previous tokens (typically capped at some number).

We use a few techniques to improve speed
- Generate outputs for all timesteps at the same time
    - Transformers map $X$ to a different space $\tilde{X}$ of the same dimension
    - We can then apply $Y = softmax[\tilde{X}W^{p}]$ where $W^{p} \in \mathbb{R}^{D \times K}$
    - Here $K$ is the dictionary size and dimensions of $Y$ are $N \times K$, i.e., outputs of N steps/positions
    - Note this is only for training, not applicable at inference
- Shift sequences to introduce causality
    - \<start> produces $y_{1}$, \<start>, $y_{1}$ produces $y_{2}$ and so on
- Masked Attention
    - Very important to maintain causal relationship
    - Attention at any $x_{i}$ should only depend on $x_{1}$ to $x_{i-1}$
    - Rest of attention values are made 0 and renormalized so that the actual attention values from $x_{1}$ to $x_{i-1}$ sum up to 1
    - This is also called _causal attention_
- Reuse attention values as for any $x_{i}$ attention values are only dependent on $x_{1}$ to $x_{i-1}$ and this remains true for the entire lifecycle of training of current sequence, or even the inference
- During inference, we only worry about the latest output
- Can use the \<pad> token in case of variable length sequences, with attention to \<pad> always 0
    - This is useful for parallezation when we expected an entire batch to have the same sequence length
