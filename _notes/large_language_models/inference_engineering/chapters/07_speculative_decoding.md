## Speculative Decoding
The decode phase of inference is autoregressive and generates tokens one by one. This is a memory bound process during low to moderate batch sizes as the compute sits idle while waiting for the model weights to be loaded into memory.

**Speculative Decoding** takes advantage of that idle compute time to generate multiple tokens per round trip through the LLM. This positively affects the token throughput (or TPS). However TTFT is unaffected by this.

### Common Mechanism
The model that we are trying to accelerate via this approach, lets call it the **target model**.

The common mechanism has the below steps
- Speculator/Draft model generates one or more draft tokens
- Target model performs validation on these tokens to check if they match what th emodel would have generated
- Target model accepts valid draft tokens and generates an additional token itself, completing the forward pass

Generate draft tokens also needs memory and complte. However, it is usually much faster for the target model to validate a draft token, compared to generating one. This is analogous to a sudoku, where solving the sudoku (generating one token) is hard when compared to validating a given solution for correctness (validating a draft token).

### Draft Token Validation
This is an interesting process that leverages the forward pass of the sequence through the LLM prefill stage. Lets suppose, we have a sequence of $K = 5$ draft tokens, and the model has already processed and generated a few tokens, making the total sequence obtained so far of length $N$.

Now, the draft model will first generate the 5 tokens using some mechanism. It will also create a probability distribution based on which it drew the 5 tokens (one distribution for each token). Lets denote the individual probability values by by $q(x_{k})$

Next, the new sequence of $N + K$ is processed through the target model the same way we process a sequence to generate the next token. In total, we are now interested in the probability distributions of these $K$ tokens, and we have also got the probability distribution of the next token free of cost (whether it is used or not depends on if all the $K$ tokens were accepted by the model). Note that we are working with a decoder only style of model here, hence we get the probability distribution as output on each step. Lets denote the individual distributions by $p(x_{k})$. Also remember that the causal attention masks allows us to compute everything in parallel, there is no sequential step here.

Now the validation stage happens, and is essentially a rejection sampling algorithm
- If $p(x_{k}) >= q(x_{k})$, meaning, the target model agrees that the token probability is almost as likely as the draft model thought it was, the token is directly accepted
- Otherwise, $p(x_{k}) <> q(x_{k})$ and we do the below
    - Note that $\frac{p(x_{k})}{q(x_{k})} < 1$. We calculate a random variable $r$ sampled from a uniform distribution in range $[0, 1]$. If $r$ is less than the fraction, the token is accepted, else rejected
        - This is a representation of probability. We want to accept $x_{k}$ only $\frac{p(x_{k})}{q(x_{k})}$ out of $1$ as according to the target model, this is not that good of a token. But since we are dealing with uncertainties, we do want to take a chance here. If the fraction is tiny, the token is also correspondingly accepted only a small fraction of times and vice versa
    - Otherwise, we reject the token and our sequence of draft tokens is terminated here itself at $k$ out of $K$
        - However, we can leverage the full distributions at this point to sample a new token, instead of doing a full forward pass
        - We compute a new distribution, that subtracts the effects of draft model distribution, since we dont want the _bad_ token to have a similar chance of getting sampled as before
        - Compute a new distribution $p'(x) = max(0, p(x) - q(x))$ which is renormalized post calculation
        - Draw a sample from this new distribution, whatever way the model is working so far, this is our new token for the $k^{th}$ position
        - In this case, note that all the tokens after this position have already filled up the KV cache. We need to perform a cache eviction to remove the rejected tokens

If all the draft tokens are accepted, we can use the probability distribution of the next token (which was already calculated on the forward pass) and use that to sample the next token. Effectively, during this validation exercise, in the best case we are able to validate and generate the next token as well.

We can then feed this information back to the draft model and repeat the entire exercise.

### Factors affecting Performance Uplift
- Draft tokens do involve some time and cost for their generation
- Draft token sequence length, or the number of draft tokens generated per forward pass
- Token acceptance rate: the percentage of draft tokens that were accepted by the target model
    - Token acceptance rate is usually high early in the sequence and falls off deeper into the sequence, essentially denoting less reliability in longer sequences

We should aim for shorter sequences that have high percentage of acceptance, so that we are optimally using compute resources and not wasting them.

Draft token validation though cheap, still involves an overhead as seen above. Once a given draft token is rejected, all the subsequence draft tokens in that sequence are also rejected/discarded.

Temperature also affects this whole process. Higher temperature, produces token distributions that are harder to predict, reducing effectiveness of speculative decoding. Subject matter can also make a difference on acceptance rate if the draft model has slightly difference performances compared to the target model in a given domain.

Speculative decoding is most useful in lower batch sizes where spare compute cycles are available. We should dynamically disable it at larger batch sizes as compute is already too satureated. Different implementations navigate these tradeoffs differently.

### Draft Token Target Speculative Decoding
This is the original method of speculative decoding and uses two models: a **draft model** and a **target model**.

We need a good draft model that has a high token acceptance rate and uses fewer resources. Typically, a smaller model of the same family of models is used. The rule of thumb is tok have a model with parameters at least 10 times fewer than the target model. Further improvements are possible by fine tuning and distillation.

This approach is quick to setup out of the box. However, there are a lot of things to consider. Both the models compete for resources in this case, as the draft model itself needs its own prefill and caching. Both models also need to be kept coordinated, creating additional overheads.

### Medusa
In this approach, we fine tune the target model to have multiple decoder heads and we can generate multiple draft tokens (typically 2 to 4). The draft tokens get validated on the next forward pass.

This method is limited by the draft token counts and acceptance rates, and not used in production use cases. This did inspire techniques like EAGLE.

### EAGLE
Off the shelf cheap models are good to run as a cheal LLM, but do not work will on the task of generating draft tokens. EAGLE uses a model trained specifically for this purpose and generates sequences of up to 8 tokens.

The target model has hidden states populated during token generation, which carries important context and is useful for generating draft tokens. EAGLE uses these hidden states (one from early layers, one from middle, and one from later layers) as inputs to generate the draft token sequences. The model is typically kept around 1B parameters. The target model and EAGLE can share the same weights and we can generate both outputs in a single inference run.

This technique gives improved latency when batch size is reduced, which means a lower throughput and higher cost.

### N-gram Speculation and Lookahead Decoding
There is no draft model in this approach. Instead, the inference engine, in parallel to generating the KV cache, also constructs an n-gram dictionary that maps a single starting token to an observed sequence of N tokens (the n-gram).

The sequences are based on input text and constructed during prefill stage itself. During decode, the generated token is fed to the dictionary and any one of the observed sequences is picked. In the next forward pass, the target model validates the sequence and the process continues.

We can get longer draft token sequences, upto 10 tokens. But for the approach to be useful, output should closely match the input. In coding domain, where the syntax is predictable, this approach can easily outperform EAGLE.

An alternate technique, Lookahead decoding generates n-grams during inference to fill the dictionary. This is more general than n-gram speculation as it does not rely as much on highly repetitive input context, but it does require the extra compute to generate the n-grams.
