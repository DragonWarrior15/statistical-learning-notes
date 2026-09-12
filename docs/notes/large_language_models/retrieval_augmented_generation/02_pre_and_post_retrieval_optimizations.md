## Pre retrieval
Here, we can enhance our understanding of the query
* Use synonyms or similar variants to ensure high recall among different variants.
* Hypothetical questions (HyDE): generate representative questions or hypothetical answers to better align user query with latent space of document chunks.

## In-flight retrieval
Solves the problem of missing tokens (exact match) by combining sparse (keyword based) and dense (embedding based) representations. For sparse representations, we use approaches like BM25 and SPLADE (this captures keyword information more correctly). Once the top documents from both sparse and dense embeddings are available, we can combine them using Reciprocal Rank Fusion (RRF) into a single optimized context set, without building additional models on top.

### Parent Retrieval Logic
After relevant chunks are identified, retrieve parent chunks/documents so that the surrounding context is better retained. This helps mitigate the fragmented context problem. As en example, our chunks could be 256 tokens long, but when retrieving the corresponding parent document, we retrieve 1k tokens to get additional context from around the main retrieved chunk.

## Post retrieval
* Reranking using a cross encoder so that useful signals sit at the top of the context.
* Distillation to summarize and compress the hits so that they better fit into the LLM context window.
    * Can use models like LLMLingua or RECOMP to compress prompt lengths. This removes redundant tokens, preserving essential context for the LLM.
    * Embedding model optimization to apply percentile or threshold based cutoffs and enhance signal to noise ratio.

## Reranking Architectures
* **Cross Encoders**: Process both the query and retrieved chunk simultaneously. Computationally expensive, but provides the highest accuracy.
* **ColBERT**: Captures interactions at token level. Has significantly more precision than cosine similarity, but lower latency than cross encoders.

Primary ranking KPIs are
* Recall@k
* MRR (Mean Reciprocal Rank)
