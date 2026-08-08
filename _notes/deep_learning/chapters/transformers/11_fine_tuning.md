## Fine Tuning LLMs
This section is more relevant for fine tuning in the context of Large Language Models (LLM) but the general principles apply to any transformer architecture.

### LoRA (Low Rank Adaptation)
- Intuition is derived from research stating that a trained over-parametrized model has low intrinsic dimensionality wrt fine tuning
    - This means that model changes during fine tuning lie on a manifold with dimensionality much lower than total learnable parameters in the model
- Typically only the attention weights are modified

#### Approach
- Consider any matrix $W_{o}$ with dimensions $D \times D$ which might represent any of the $K$, $Q$ or $V$ matrices in an attention head
- We now add to more matrices $A$ and $B$ of dimensions $D \times R$ and $R \times D$ in the mix

$$
\begin{aligned}
\text{Original} &\quad XW_{o} &&\to \tilde{X}\\
\text{Modified} &\quad XW_{o} + XAB &&\to \tilde{X}
\end{aligned}
$$

The total new learnt parameters are $2RD$. If $R << D$, this is a very small set of new parameters.

Once fine tuned, we update the model by substituiting $\tilde{W} = W_{o} + AB$. This way the number of operations remain same as original model.

Note: Typically the MLP params are finetuned in other places. Here, they are kept fixed since they can be huge in number and difficult to fine tune at a large scale.
