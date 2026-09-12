# Chunking Strategies
Choose a strategy that represents the documents inherent structure.

| Strategy Type | Definition | Use case |
| --- | --- | --- |
| **Fixed size/Sentence aware** | Standard splits based on character count and sentence boundaries | General use cases like blogs, memos |
| **Semantic Chunking** | Identify boundaries based on embedding variance | Messy text, where logical shifts dont align with paragraph markers |
| **Document aware/adaptive** | Segmenting based on DOM structure, headings, tables, code blocks etc. | Technical manuals, financial reports, source code |
| **Parent/child retriever** | Decoupling retrieval units from the generation unit | Balancing precision (small child chunks) with context (large parent blocks) |
