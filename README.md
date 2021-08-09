# statistical-learning-notes
Accessible at [https://DragonWarrior15.github.io/statistical-learning-notes/](https://DragonWarrior15.github.io/statistical-learning-notes/)

## Building Locally
* Run `make jekyll_serve` to serve using jekyll

## MathJax Usage
* MathJax overview: See [1](https://memory.psych.mun.ca/tech/js/mathjax.shtml) and [2](https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm).
* To espace the curly braces inside math mode, use a double back slash like `\\{`. This is because of two levels of processing by Jekyll and MathJax ([see here](https://stackoverflow.com/questions/41312777/mathjax-curly-brackets-dont-show-up-using-jekyll)).
* Any hanging pair of square brackets `[ ]` in math mode should be escaped using `\[ \]` so that markdown does not process them as hyperlinks.
* Refer to [include_mathjax.html](/_includes/include_mathjax.html) for examples on defining new macros and including extensions. This files also defines the complete configuration to import MathJax to a jekyll project.
* Instead of `\bigg` use `\left` and `\right` for automatically sizing brackets. However, `\left` and `\right` should be present in pairs with matching pairs of brackets. Otherwise, MathJax can throw errors like `missing left or right` or `missing &`.
* The actual `$` symbol can be included as `\\$`, i.e., by double escapting `\` so that its interpreted as `\$`. Just using `\$` will make it be interpreted as `$` and begin as math mode.
* The following will work
    ```tex
    \begin{alignat}{2}
        \text{Accept} \quad &H_{0} \quad &&\text{if} \quad \chi_{1-\alpha/2, n-1}^{2} \leq TS \leq \chi_{\alpha/2, n-1}^{2}\newline
        \text{Reject} \quad &H_{0} \quad &&\text{otherwise}
    \end{alignat}
    ```
    while this will not show proper alignment
    ```tex
    \begin{alignat}{2}
        \text{Accept} \quad &H_{0} \quad &\text{if} \quad \chi_{1-\alpha/2, n-1}^{2} \leq TS \leq \chi_{\alpha/2, n-1}^{2}\newline
        \text{Reject} \quad &H_{0} \quad &\text{otherwise}
    \end{alignat}
    ```
    This is probably because of how alignment is handled for the text command in math mode.
* If only a math mode text is present in some list of items, begin it from next line as shown below for correct formating
    ```md
    1.
        \begin{align}
            E = mc^{2}
        \end{align}
    ```
* Linking to another page of the project can be done by following the template
    ```md
    {{ "/notes/full_path_to_file/file.html/#a-heading-name" | relative_url }}
    ```
    For a heading in the same file, a simple `#a-heading-name` will suffice

### Custom mathjax shorthands
* Set notations
    * `\real` to denote the set of real numbers
    * `\comp` to denote the set of complex numbers
    * `\field` to denote a field
    * `\setv` to denote the set V
    * `\setw` to denote the set W
    * `\setlm` to denote the matrix L
    * `\matm` to denote the matrix M
* Operators
    * `\minimize`, `\maximize`, `\argmin` and `\argmax` are defined to denote the minimization, maximization, minimum value index, and maximum value index positions respectively.
* Operators with arguments
    * `\KL{arg 1, arg2}` to denote the KL divergence between functions `arg1` and `arg2`
    * `\detm{arg}` to denote the determinant of the matrix `arg`
    * `\roundbr{arg}` to create round brackets around `arg` with the appropriate sizing
    * `\diffone{arg}` to denote the first derivative of `arg` using a single prime character in power
    * `\difftwo{arg}` to denote the second derivative of `arg` in the double prime notation

## Codes in markdown+jekyll
* To use double curly braces inside a code block, enclose it inside the raw tag
    ```html
    {% raw %}
    This is a code with double curly braces {{ user.name | uppercase }}
    {% endraw %}
    ```
### Common problem in WSL
**In case you are running WSL and unable to connect to the server**
* Close the ubuntu window
* Open cmd and type `wsl --shutdown`
* Restart cmd and type `wsl`
* Now try running the commands
