---
title: "sed"
---

## `S`tream `Ed`itor
`sed` is a utility that allows us to edit a stream of data by replacing some existing text with the desired one.

* basic sed command to substitute characters is `sed 's|pattern to match|pattern to replace the matched pattern|'`
    * a more common form is to use `/` instead of `|`: `sed 's/pattern to match/pattern to replace the matched pattern/'`
    * there are always three `/` or `|`, or any other delimiter like `:`; but there should always be three otherwise an error is raised
    * it is common to use a delimiter that is not a character in the input string being processed
    * for instance, `echo day | sed 's|day|night|'` produces `night`
    * regular expressions work perfectly fine for the pattern to match (however, `\d` does not work, use [0-9] instead)
    * `sed` works on every line, one by one and acts on the first match (greedy)
        * `echo "abc 123 abc 456" | sed 's/[0-9][0-9]*/& &/'` outputs `abc 123 123 abc 456`
        * `echo "abc 123 abc 456" | sed 's/[0-9]*/& &/'` outputs ` abc 123 abc 456` because `[0-9]*` matches 0 or more characters and the start of line is a match; `[0-9][0-9]*` matches a string only made up of digits
    * to use `+` character in the regular expression search, use `-r` flag to signify extended regular expressions
        * `echo "abc 123 abc 456" | sed -r 's:[0-9]+:& &:'` outputs `abc 123 123 abc 456`
* for single matches, `&` can be used to refer to the matched pattern
    * `echo "123 abc" | sed 's/[0-9]*/& &/'` gives `123 123 abc`
* a use case of `sed` is to print the columns header of a file on different lines
    * `echo 'colA|colB|colC|colD' | sed -e 's/|/\n/g' | cat -n` where `|` was the column delimiter
    ```shell
    colA
    colB
    colC
    colD
    ```

#### Reference
* [Sed - An Introduction and Tutorial by Bruce Barnett](https://www.grymoire.com/Unix/Sed.html#uh-0)
