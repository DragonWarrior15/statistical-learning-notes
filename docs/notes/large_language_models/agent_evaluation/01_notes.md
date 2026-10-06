# Agent Evaluation

Ordinary Software has unit tests where for a given single input, we have a single output. LLMs break this concept in four ways

- **Non determinism**: Same prompt can produce different outputs at times. We need many runs and statistics to be confident about the response.
- **No single right answer**: _summarize_ can have multiple acceptable answers, equality checks can fail. We need rubrics and judges.

Agent evaluations measure whether an agent achieves the outcome the user wanted through an acceptable trajectory, at an acceptable cost, reliably across repeated runs and verified inputs.
