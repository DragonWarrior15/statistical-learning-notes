## Query Decomposition
A pattern where the system uses query decomposition to break a complex question into sub sentences, retrieving pertinent triplets for each part before synthesizing the final answer.

## Graph RAG
Formalizes the use of Text Attributed Graphs (TAGs), a universal format where nodes and edges possess textual attributes as the foundation for retrieval. It consists ofo 3-steps
1. **G-Indexing**: Construct a graph database that maps the context of the data.
2. **G-Retrieval**: Extract relational knowledge (SPO or Subject-Predicate-Object tuples) rather than just flat text.
3. **G-Generation**: Converting retrieved graph patterns into natural language or code-like forms for the LLM. Some examples of this are paths, syntax trees and graph embeddings in some cases.

### Retrieval Granularity
1. **Nodes (Entities)**: Specific attributes for targeted look-ups.
2. **Triplets (SPO tuples)**: Subject Predicate Object sets (eg: Monet-Influenced-Modern Art).
3. **Paths**: Sequences of relationships capturing multi-hop dependencies.
4. **Subgraphs**: Comprehensive relational communities that provide global context for broad queries.

## Corrective RAG (CRAG)
A feedback loop that verifies context quality of the retrieved chunks. If the quality is weak, an external search is triggered for additional context or a new retrieval pass is triggered to ensure LLM is never forced to guess the answer.

## Agentic RAG
Its a dynamic orchestration loop where the agent identifies sub-goals and routes them to specific tools. It consists of
* **Plan**: Break the query into different tasks.
* **Route**: Direct the tasks to the built graph for relationships and do a hybrid retrieval for facts/lookups.
* **Verify**: Check fo conflicts or weak evidence before concluding.

It also has memory and search modules which augment previous turn memory using relevant historic information to prevent context bloat.

We can also use Chain of Thought (CoT) which acts as a private scratchpad for the agent. It allows the agent to outline reasoning hops and track intermediate findings and provides a traceable chain of logic for enhanced explainability.

## Comparative Analysis and Tradeoffs

| Feature | Naive RAG | Hybrid RAG | Graph RAG |
| --- | --- | --- | --- |
| **Relevance** | Semantic | Hybrid | Relational |
| **Explainability** | Low | Moderate | Highest |
| **Relational Depth** | Poor | Moderate | Excellent (multi-hop) |
| **Best use case** | Demos | Enterprise | Complex reasoning/compliance |
