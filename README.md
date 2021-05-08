# statistical-learning-notes
Accessible at [https://DragonWarrior15.github.io/statistical-learning-notes/](https://DragonWarrior15.github.io/statistical-learning-notes/)

## MathJax Usage
* MathJax overview: See [1](https://memory.psych.mun.ca/tech/js/mathjax.shtml) and [2](https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm).
* To espace the curly braces inside math mode, use a double back slash like ```\\{```. This is because of two levels of processing by Jekyll and MathJax ([see here](https://stackoverflow.com/questions/41312777/mathjax-curly-brackets-dont-show-up-using-jekyll)).
* Any hanging pair of square brackets `[ ]` in math mode should be escaped using `\[ \]` so that markdown does not process them as hyperlinks.
* Refer to [include_mathjax.html](/_includes/include_mathjax.html) for examples on defining new macros and including extensions. This files also defines the complete configuration to import MathJax to a jekyll project.
* Instead of `\bigg` use `\left` and `\right` for automatically sizing brackets.
