---
title: "sed"
---

## `S`tream `Ed`itor
`sed` is a utility that allows us to edit a stream of data by replacing some existing text with the desired one.

### Version
* `sed -V` prints the `sed` version
* `sed -h` prints a summary of the `sed` command

### Basic command
* Basic sed command to substitute characters is `sed 's|pattern to match|pattern to replace the matched pattern|'`
* a more common form is to use `/` instead of `|`: `sed 's/pattern to match/pattern to replace the matched pattern/'`
* there are always three `/` or `|`, or any other delimiter like `:`; but there should always be three otherwise an error is raised
* it is common to use a delimiter that is not a character in the input string being processed
* for instance, `echo day | sed 's|day|night|'` produces `night`
* `sed` works on every line, one by one and acts on the first match (greedy)

### Regular Expressions
* regular expressions work perfectly fine for the pattern to match (however, `\d` does not work, use `[0-9]` instead)
    * `echo "abc 123 abc 456" | sed 's/[0-9][0-9]*/& &/'` outputs `abc 123 123 abc 456`
    * `echo "abc 123 abc 456" | sed 's/[0-9]*/& &/'` outputs `abc 123 abc 456` because `[0-9]*` matches 0 or more characters and the start of line is a match; `[0-9][0-9]*` matches a string only made up of digits
* to use `+` character in the regular expression search, use `-r` flag to signify extended regular expressions
    * `echo "abc 123 abc 456" | sed -r 's:[0-9]+:& &:'` outputs `abc 123 123 abc 456`
    * in the extended regex setup, we dont need to escape capturing brackets with a `\`
* For single matches, `&` can be used to refer to the matched pattern
    * `echo "123 abc" | sed 's/[0-9]*/& &/'` gives `123 123 abc`
* Like regular expressions, we can `\1` upto `\9` (9 captured groups) to refer back to any matched group
    * `echo ab1e | sed -r 's/([a-z]+)/\1\1/'` outputs `abab1e`
* the captured group can be referred to in the search expression as well, say to check duplicated words
    * `echo ab abe | sed -r 's/([a-z]+) \1/dup/'` outputs `dupe`
    * `echo ab ae | sed -r 's/([a-z]+) \1/dup/'` outputs `ab ae`

### Flags and Options
* `-r`
    * extended regular expressions; described in the previous section
* `g`
    * to change all the occurrences of a word on the line, use the `g` flag `sed s/pattern/replacement/g`
    * `echo ab1e | sed -r 's/([a-z]+)/9/g'` outputs `919`
* `I`
    * performs case insensitive matching
    * `echo abcABCaBc | sed 's/abc/1/gI'` outputs `111`
* `-n`
    * is no printing, with just `-n` nothing will be printed
* `p`
    * specifically asks `sed` to print the modified lines
    * if no match is found, the lines are printed as is
    * for any line, if a match is found, the line is printed twice
    * `-n` together with `p` will print only the lines where a match is found
    * `printf "abc\nABC" | sed -n 's/abc/1/p'` outputs `1`
    * `printf "abc\nABC" | sed 's/abc/1/p'` outputs `1\n1`
* `-e`
    * allows executing multiple `sed` commands sequentially
    * `printf "Ah! How do you do good sir this fine evening?" | sed -e 's/e/E/g' -e 's/o/O/g' -e 's/E/e/'` outputs `Ah! HOw dO yOu dO gOOd sir this fine EvEning?`
    * note how the last executed command changes the first `E` back to `e`
    * one can also put different commands on separate lines using `\` like in a shell script

### Ranges and Specifying Lines
* Restrict to a line number
    * Add the line number before the command to act only on that line
    * `sed 'num s/pattern/replace/`
    * `printf "abc\nABC\naBc" | sed '2 s/abc/replace/I'`
        ```shell
        abc
        replace
        aBc
        ```
* Ranges by line number
    * Use two comma separated numbers instead of a single number like above to define a range for making substituitions
    * only substitute in first 10 lines, `sed '1,10 s/pat/rep/'`
    * only substitute in lines 10 to 20, `sed '10,20 s/pat/rep/'`
    * only substitute in lines 20 to end, `sed '10,$ s/pat/rep/'`
    * `$` denotes the end, similar to other utilities in shell
    * in case multiple files are being processed, the line numbers are assumed to be cumulative

### Addresses
`sed` has the ability to only apply the commands to lines that match a specific pattern using the `sed /pattern/ command` syntax.
* `sed -n '/abc/ p` mimics [`grep`]({{ "/notes/linux/grep.html" | relative_url }}); the command we are asking `sed` to execute is `p`
* there should always be a command to execute, otherwise an error is raised

### Specific Use Cases
* a use case of `sed` is to print the columns header of a file on different lines
    * `echo 'colA|colB|colC|colD' | sed -e 's/|/\n/g' | cat -n` where `|` was the column delimiter
    ```shell
    1  colA
    2  colB
    3  colC
    4  colD
    ```
    * `cat -n` prints the contents and the line numbers as well

#### Reference
* [Sed - An Introduction and Tutorial by Bruce Barnett](https://www.grymoire.com/Unix/Sed.html#uh-0)
