## Disaggregation
During inference, the Prefill stage is compute heavy, while the Decode stage is memory heavy. On a given GPU, then can both start to compete for resources, with larger batches and more compute intensive operations making things even worse.

The idea of disaggregation is to separate out prefill and decode onto separate GPUs or nodes and breakdown the process into three steps
- Prefill engine digests the input sequence to generate a KV cache and also generate the first token
- Prefill engine sends the KV cache to Decode engine over hardware interconnect
- Decode engine computes all successive tokens

There is also another concept called **condidtional disaggregation** where a request is first sent to the decode engine which checks if the input sequnce is already cached, or is short enough to handle locally
- If yes, the decode engine itself handles the entire sequence, skipping disaggregation
- Else, the decode engine transfers the request to prefill engine for disaggregated serving

This is better for real world traffic.

### When to use Disaggregation
Use when
- Serving large volume of traffic, say billions of tokens per day
- Serving a large model, say 100 billion+ parameters
- Traffic is prefill heavy with long input sequences

A good use case of disaggregation is a code editing agent, where there are multiple developers using the system in parallel, and also the input contains of long sequences which are the large codebase contexts.

### xPyD
The number of prefill and decode engines can vary and is represented by **xPyD**. For instance, %P3D means 5 prefill and 3 decode engines for a single model deployment.

In all of this, prefill queue holds the incoming requests for when all the prefill engines are saturated. Dynamic allocation of xPyD at runtime is needed to ensure that the queue length does not grow too large.
