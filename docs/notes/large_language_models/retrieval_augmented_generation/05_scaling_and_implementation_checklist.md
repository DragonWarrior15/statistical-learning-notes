# Scaling and Implementation Checklist
## Scaling
For highly scalable embedding search, use HNSW, but it requires careful tuning of the relevant algorithm parameters.
* <1M vectors: Chroma or pgvector
* 1M-100M vectors: pgvector + pgvectorscale
* >100M vectors: Milvus or elastisearch (for distributed/sharded architecture)

### HNSW
Most modern vector databases rely on HNSW (Hierarchical Navigable Small Worlds). The parameters are
* `M` (connectivity): A higher M means higher recall, but memory usage explodes and index builds can begin to slow down.
* `ef_construction`: Controls the index quality during the build phase.
* `ef_search`: A higher value means higher recall but also more latency.

**Ceiling Warning**: Chunking strategy + embedding quality caps the retrieval quality. A perfect index tuned on bad data just retrieves bad answers faster.

## 7-step implementation checklist
* **Stabilize basic retrieval**: Metadata based rules along with sensible chunking strategies.
* **Add hybrid search**: Combine dense vectors with sparse ones for search.
* **Query understanding**: Use expansions like HyDE to bridge phrasing gaps.
* **Optimize context supply**: Parent document logic + Contextual compression retriever.
* **Structure data relationally**: Load normalized entities and relations into a TAG based knowledge graph.
* **Enable agent Q&A**: Plan-route-verify for multi-hop search.
* **Harden grounding and security**: CRAG style checks and RBAC on labels and properties.
