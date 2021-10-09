# Notes
Accessible at [https://DragonWarrior15.github.io/statistical-learning-notes/](https://DragonWarrior15.github.io/statistical-learning-notes/)

## Building Locally
* Run `make jekyll_serve` to serve using jekyll

## Common Pitfalls/Suggestions
* MathJax overview: See [1](https://memory.psych.mun.ca/tech/js/mathjax.shtml) and [2](https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm).
* To escape the curly braces inside math mode, use a double back slash like `\\{`. This is because of two levels of processing by Jekyll and MathJax ([see here](https://stackoverflow.com/questions/41312777/mathjax-curly-brackets-dont-show-up-using-jekyll)).
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
    {{ "/notes/full_path_to_file/file.html#a-heading-name" | relative_url }}
    ```
    For a heading in the same file, a simple `#a-heading-name` will suffice
* Before starting any table, there should be a blank line before it, otherwise it is not parsed correctly. It is a good practice to keep a blank line after the table as well, but that may not work when table is inside lists.
* Use `\quad` in math mode for spacing between text and mathematical expression.

### Custom MathJax shorthands
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
    * `\detm{arg}` to denote the determinant of the matrix `arg`, can also be used to generate left and right vertical bars the height of the expression
    * `\roundbr{arg}` to create round brackets around `arg` with the appropriate sizing
    * `\squarebr{arg}` to create sqyare brackets around `arg` with the appropriate sizing
    * `\diffone{arg}` to denote the first derivative of `arg` using a single prime character in power
    * `\difftwo{arg}` to denote the second derivative of `arg` in the double prime notation

### Codes in markdown+jekyll
* To use double curly braces inside a code block, enclose it inside the raw tag
    ```html
    {% raw %}
    This is a code with double curly braces {{ user.name | uppercase }}
    {% endraw %}
    ```

### Defining Navigation
* Refer to [navigation.yml](_data/navigation.yml) to see how the navigation is defined currently. It follows the below format
    ```yaml
    topic:
      - name: Section/Chapter 1 Name
        link: complete_path_to_the_file.html
        subnav:
          - name: Subsection 1.1
            link: complete_path_to_the_file.html
          - name: Subsection 1.2
            link: complete_path_to_the_file.html
      - name: Section/Chapter 2 Name
        link: complete_path_to_the_file.html
        subnav:
          - name: Subsection 2.1
            link: complete_path_to_the_file.html
    ```

### Using `find` and `grep`
Suppose we rearrange the directory structure. Since the URLs are hardcoded when referring to a section somewhere else, we need to go through and replace all such links to point to the new path.

Assuming we changed `/notes/differential_equations/laplace_transforms.md` to `/notes/differential_equations/laplace_transforms/intro.md`. The command to search through all the places where the change needs to be made

```shell
find . -type f -name "*.md" -or -name "*.yml" -exec grep "/notes/differential_equations/laplace_transforms.html" {} ';'
```

And to replace with the new path
```shell
find . -type f -name "*.md" -or -name "*.yml" -exec sed -s "|/notes/differential_equations/laplace_transforms.html|/notes/differential_equations/laplace_transforms/intro.md|" {} ';'
```

### Common problem in WSL
**In case you are running WSL and unable to connect to the server**
* Close the ubuntu window
* Open cmd and type `wsl --shutdown`
* Restart cmd and type `wsl`
* Now try running the commands

