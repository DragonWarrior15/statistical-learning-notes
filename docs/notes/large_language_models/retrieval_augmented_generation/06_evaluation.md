# Evaluations

- **Context Relevance**: Is the retrieved context relevant/useful.
- **Groundedness**: Did the LLM generate the answer based on retrieved context or hallucinate.
- **Answer Relevance**: Did the generated response answer the user query.

## Measures

### MRR (Mean Reciprocal Rank)

Mean reciprocal rank. This measures how high the most relevant document is ranked.

RR (Reciprocal Rank) = 1 / Rank of top relevant item.
MRR = Mean across multiple queries

This measure ranges between 0 to 1.

- 0 means the top relevant item is not in the list.
- 1 means the top relevant item has the highest score.

### DCG (Discounted Cumulative Gain)

Each item is assigned a relevance score (by some external policy). For instance, consider an ecommerce website. We want to understand how good the list of products is for a given query. If a product is added to cart, we assign relevance of 5, if product is just viewed, relevance is 2 and 0 if not interacted at all.

CG (Cumulative Gain) = Sum of relevance scores of top k items

$ DCG@k = \sum_{i=1}^{k} \frac{relevance_{i}}{log_{2}(i + 1)} $

where $i$ is the position by the retriever. So high relevance, but lower position gets penalized a lot more.

$NDCG = \frac{DCG}{IDCG}$

Where IDCG is the Ideal DCG: DCG on items retrieved by the retriever, but sorted based on the relevance scores.
