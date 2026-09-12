# Retrieval Augmented Generation (RAG)
It is a baseline system that is desinged to ground LLM outputs to external authoratative data, rather than relying on model weights. The system has four stages:
1. **Ingestion**: Split the document into chunks and enrich the chunks with metadata and generate embeddings of those chunks.
2. **Indexing**: Store the embeddings in a searchable index, typically a vector store augmented with keyword based searching.
3. **Retrieval**: At runtime, uuser input is converted to an embedding and top-k chunks are retrieved based on semantic similarity (say cosine similarity)
4. **Generation**: LLM is prompted with user query along with the retrieved context to generate the answer.

## Production Failure Modes
1. **Near duplicate top-k results**: Among several documents, diversity in retrieved documents will often be lower which wastes precious token space.
2. **Missing exact tokens**: Semantic similarity makes sense at an overall level, but will often miss identifiers, proper nouns, acronyms etc.
3. **Structural context loss**: Inadequate splitting strategies might drop headers, footnotes or break tabular alignment.
4. **Thin retrieval sets**: With a weak retrieval, LLM will often hallucinate to fill in the most plausible information, which may often be incorrect.
5. **Lost in the middle dilemma**: LLMs struggle to extract context from long windows when relevant facts are buried in the middle of the context.

## Failures of basic RAG architecture
* **Vector only retrieval**: Misses the exact keyword matches (like SKU numbers).
* **Chunking boundaries**: LLM may receive fragmented or out of context information.
* **No re-ranking**: Similarity does not mean utility; k=10 position document might be most relevant.
* **Missing global information**: Retrieval focuses often on local rather than global context and may not be able to answer questions like "overall sentiment of the report".
* **Stale indices**: As data evolves over time, using the same indices leads to outdated information; example is current events data.
