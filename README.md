# Learning Notes

Personal notes on probability, statistics, mathematics, programming, machine
learning, deep learning, time series, Linux, and large language models.

The published site is available at
[DragonWarrior15.github.io/statistical-learning-notes](https://DragonWarrior15.github.io/statistical-learning-notes/).

## MkDocs development

The content under `docs/` is the authoritative source. Edit those files
directly.

Migrated collections live under `docs/notes/` to preserve their existing
published URLs, such as `/statistical-learning-notes/notes/probability/...`.

Install the locked Python dependencies:

```shell
uv sync
```

Start the local MkDocs development server:

```shell
make mkdocs_serve
```

Build the site with warnings treated as errors:

```shell
make mkdocs_build
```

## Common Pitfalls/Suggestions
* MathJax overview: See [1](https://memory.psych.mun.ca/tech/js/mathjax.shtml) and [2](https://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm).
* MathJax configuration and custom macros live in [`docs/javascripts/mathjax.js`](docs/javascripts/mathjax.js).
* Use `\{` and `\}` for literal curly braces in math mode.
* Instead of `\bigg` use `\left` and `\right` for automatically sizing brackets. However, `\left` and `\right` should be present in pairs with matching pairs of brackets. Otherwise, MathJax can throw errors like `missing left or right` or `missing &`.
* The actual `$` symbol can be included as `\$`.
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
* In MkDocs content, link to another page using a relative Markdown source path,
  for example `[label](../distributions/normal_distribution.md#a-heading-name)`.
  For a heading in the same file, `[label](#a-heading-name)` is sufficient.
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

### Defining Navigation
Navigation is defined in [`mkdocs.yml`](mkdocs.yml). Each subject has an
`index.md` overview and a subject-scoped hierarchy in the left sidebar.

### Using `find` and `grep`
Suppose we rearrange the directory structure. Since the URLs are hardcoded when referring to a section somewhere else, we need to go through and replace all such links to point to the new path.

Assuming we changed `docs/notes/differential_equations/laplace_transforms.md`
to `docs/notes/differential_equations/laplace_transforms/intro.md`, search for
references to the old path before moving it:

```shell
rg 'laplace_transforms\.md' docs mkdocs.yml
```

## `uv` Setup
- Visit the official [astral site](https://docs.astral.sh/uv/) for the latest download instructions
- Run `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Run `uv sync` to setup the environment
