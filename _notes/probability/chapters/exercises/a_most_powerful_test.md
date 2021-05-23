---
title: "Answer"
---

The most powerful test will follow the [Neyman-Pearson Lemma]({{ "/notes/probability/chapters/hypothesis_testing/mean_normal.html#neyman-pearson-lemma" | relative_url }}). To apply that, we need to first calculate the likelihood ratio of the five observed values under the two hypothesis.
\begin{align}
        L &= \frac{f(X_{1}, \ldots, X_{5} \lvert H_{1})}{f(X_{1}, \ldots, X_{5} \lvert H_{0})} =\frac{\bigg( \frac{1}{\sqrt{2 \pi }} \bigg)^{5} \exp \bigg(-\frac{1}{2} \sum_{i=1}^{5} (X_{i} - 2)^{2} \bigg)}{\bigg( \frac{1}{\sqrt{8 \pi}} \bigg)^{5} \exp \bigg( -\frac{1}{8} \sum_{i=1}^{5} (X_{i} - 2)^{2}\bigg)}\newline
        &= 32 \exp \bigg(-\frac{3}{8} \sum_{i=1}^{5} (X_{i} - 2)^{2} \bigg) > \eta\newline
        \implies \sum_{i=1}^{5} (X_{i} - 2)^{2} &< -\frac{8}{3} \ln \big( \frac{\eta}{32} \big) = c
    \end{align}
Hence, the critical region (rejecting $H_{0}$) for the test is defined as
\begin{align}
         \sum_{i=1}^{5} (X_{i} - 2)^{2} < c
     \end{align}

Note that the above sum is a scaled version of the $\chi_{5}^{2}$ variable. Using the size of test, $\alpha = 0.05$,
\begin{align}
         P(\text{Reject}\quad H_{0} \lvert H_{0} \quad \text{is true}) &= P \bigg(\sum_{i=1}^{5} (X_{i} - 2)^{2} < c \lvert \sigma^{2} = 4 \bigg)\newline
         \implies P \bigg(\sum_{i=1}^{5} \bigg(\frac{X_{i} - 2}{2} \bigg)^{2} < \frac{c}{4} \bigg) &= 0.05\newline
         P \bigg(\chi_{5}^{2} \geq \frac{c}{4} \bigg) &= 1 - 0.05 = 0.95\newline
         \implies \frac{c}{4} &= \chi_{5, 0.95}^{2} = 1.15\newline
         c &= 4.6
     \end{align}

Hence, the critical region is given by
\begin{align}
         C = \left\\{ (X_{1}, \ldots, X_{5}) : \sum_{i=1}^{5} (X_{i} - 2)^{2} < 4.6 \right\\}
     \end{align}
