## Caching
During prefill phase, LLM builds the KV cache (the store for keys and values for each token, across different transformer layers) and updates the cache for every token during decode.

KV Caching is used by default in inferencing (which is very slow otherwise). Caching gives a higher benefit when used across different requests, in addition to use within the same request.

Suppose we run inference for a given sequence. Now, another request comes where there is a match with some initial part of the sequence. We can use KV cache for that partial part and only perform newer calls for the remaining part. This improves TTFT. Cost for cache hit is also usually lower compared to cache miss.

Caching is most beneficial in shared context. Examples include agent runs (where same set of prior messages get processed on every LLM call), common system instructions (used as a prefix) on every request.

To take advantage of prefix caching, it is important to ensure that the novel tokens occur later in the sequence.

### Storing KV Cache
There are multiple options. One of them is to store the cache inside the free memory of a GPU, after accounting for some part of the memory that gets filled up because of model weights. As the cache builds up and uses more and more memory, we also need to consider evicting the cache to make more memory space.

Level | Memory Type | Approximate Bandwidth | Approximate Size |
| --- | --- | --- | --- |
| 1 | Device Memory (GPU VRAM) | Terabytes per second | 10s to 100s of GBs |
| 2 | Host Memory (CPU RAM) | 10s to 100s GB per second | 100s of GBs to TBs |
| 3 | SSD (Local) | 5 to 10 GBs per second | In Terabytes |
| 4 | SSD (Networked) | GBs per second | 10s of TBs |

The above list is in descending order of memory bandwidth.

NVIDIA Dynamo provides support for KV cache offloading via KVBM (KV Block Manager) via APIs to move cache blocks among different levels of memory, with most frequently used blocks inside the higher bandwidth memory and vice versa.

### Cache Aware Routing
For KV Cache use to be effective, requests with the same prefixes should be routed to the same replica. For instance, requests of a multi turn conversation from the same user should go to the same replica for good cache hit.

There is an alternate too, where we build a global KV cache that is shared across the replicas. This way, we can build much bigger cache stores, that can be independently accessed across multiple replicas. However, due to latency advantages, it is often more practical to use GPU based cache and cache aware routing makes more sense.

### Long Sequence Handling
A long sequence can start to cause problems if the sequence length is long enough to cause problems during inference. At common cutoffs like 32K, 64K, 128K etc., the cache can start to take a lot of space in the VRAM, which is also an important resource, especially for the decode phase (which is memory bound phase).
 