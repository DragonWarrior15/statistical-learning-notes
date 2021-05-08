---
title: "Classfication Metrics"
---

## Classfication Metrics

Several classification metrics are available for binary classifiers which are used based on the problem setting.

### Confusion Matrix

This matrix tabulates the number of cases we are classifying and misclassifying.

| **Confusion Matrix** | **Actual Positive** | **Actual Negative** |
| ================ | =================== | =================== |
| **Predicted Positive** | True Positive | False Positive |
| **Predicted Negative** | False Negative | True Negative |

Based on the above table, we define the following terms

-   Accuracy $= \frac{TP + TN}{P+N}$

-   Sensitivity or True Positive Rate (TPR) or Recall $= \frac{TP}{P} = \frac{TP}{TP+FN}$

-   Specificity or True Negative Rate (TNR) $= \frac{TN}{N} = \frac{TN}{FP+TN}$

-   Precision or Positive Predicted Value (PPV) $= \frac{TP}{FP+TP}$

-   False Positive Rate $= \frac{FP}{N} = \frac{FP}{FP+TN}$

-   $F_{1}$ Score $= \frac{2 * precision * recall}{precision + recall}$

### Receiver Operating Characteristics (ROC Curve)

ROC curve is plot between **True Positive Rate** and **False Positive Rate**, or equivalently, between **sensitivity/recall** and **$1 -$ specificity**. The area under the plotted curve is know as AUC score.

The curve is plot by repeatedly constructing the confusion matrix at different probability thresholds (i.e. changing the decision boundary to see how the confusion matrix changes).

ROC Curve is agnostic of the class balancing in the data set, and is thus used frequently in case of class imbalance to judge a classifier. A random classifier will have AUC of $0.5$ as at any threshold, the number of correctly and incorrectly classified points will roughly be the same. A perfect classifier will be able to segregate the population perfectly and will have the value of AUC as $1.0$.
