---
title: "Answer"
---

1.
    \begin{align}
                P(A \cap B) &= P(A) P(B)\newline
                P(A) &= P((A \cap B) \cup (A \cap B^{c}))\newline
                    &= P(A \cap B) + P(A \cap B^{c}) \quad\text{since disjoint}\newline
                P(A \cap B^{c}) &= P(A) - P(A)P(B)\newline
                    &= P(A)(1 - P(B)) = P(A)P(B^{c})
            \end{align}

2.
    \begin{align}
                (A \cup B)^{c} &= A^{c} \cap B^{c}\newline
                P(A^{c} \cap B^{c}) &= 1 - P(A \cup B)\newline
                                &= 1 - P(A) - P(B) + P(A \cap B)\newline
                                &= (1 - P(A))(1 - P(B))\newline
                                &= P(A^{c})P(B^{c})
            \end{align}
