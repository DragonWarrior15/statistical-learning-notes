---
title: grep
---

## `grep`
`grep` stands for *g*lobal *r*gular *e*xpression and *p*rint and allows us to search for text within files.

`grep` does not work with directories. If something like `grep "search" ./` is tried, an error is returned.

* `grep "text to search" file_name`
    * text to search goes inside the double quotes
    * nothing is printed in case of no results
    * each line containing the searched text is printed
* `grep -w "text" file`
    * `-w` will search for whole words
    * for instance, if two lines contain the text _you_ and _yours_, and we use `grep -w "you" file`, only the line containing _you_ will be returned
    * `grep "you" file` returns both the lines
    * `printf "you\nyours\n" | grep "you"`
        ```shell
        you
        yours
        ```
    * `printf "you\nyours\n" | grep -w "you"`
        ```shell
        you
        ```
* `grep -i`
    * will do a case insensitive search
* `grep -n`
    * will add a line number as well to the output
    * `printf "you are happy\nhow do you do\nyours truly\n" | grep -n -w "you"`
        ```shell
        1:you are happy
        2:how do you do
        ```
* Multiple flags can be combined together as `-win`
    * `grep -win` will match the full word in a case insensitive fashion and print the line numbers int eh result
* `grep -B num`
    * prints _num_ lines before the match as well so that we can get an idea of the context of the searched word
    * `printf "1\n2\n3\n4\n5\n6\n7\n8\n" | grep -wn -B 2 "5"`
        ```shell
        3-3
        4-4
        5:5
        ```
* `grep -A num`
    * will return _num_ lines after the matches
    * both the flags can be used in the same query
    * `printf "1\n2\n3\n4\n5\n6\n7\n8\n" | grep -wn -B 2 -A 3 "5"`
        ```shell
        3-3
        4-4
        5:5
        6-6
        7-7
        8-8
        ```
* `grep -C num`
    * will return _num_ lines before and after the matches
    * `-C num` is equivalent to `-A num -B num`

### Searching multiple files
* `grep "search" ./*`
    * will serch in every file in the current directory
    * an error will be returned
    * can combine with [`find`]({{ "/notes/linux/find.html" | relative_url}}) using the `-exec` flag
* `grep -r "search" ./*`
    * performs a recursive search within all the directories as well
    * in case of many subdirectories/files, recursive search might get too slow
* `grep -l "search" ./`
    * only returns the list of files where at least one match was found
    * a file will appear only once irrespective of the number of matches
* `grep -c "search" ./`
    * similar to the `-l` flag, but will also return the number of matches against each file

### Piping outputs to `grep`
* `some command | grep "keyword"`
    * will search the keyword in the output of some command
    * multiple `grep` commands can be chained together to form something similar to `and` filters

### Regular Expressions
* By default, grep uses posix compatible regular expressions, while programs like python use perl compatible regular expressions
* `-P` flag will force grep to use perl compatible regular expressions on linux systems
* Mac uses BSD version of grep and does not support the `-P` flag. GNU version of grep, which is used in linux, needs to be installed on Mac to use this flag

#### References
* [Linux/Mac Terminal Tutorial: The Grep Command - Search Files and Directories for Patterns of Text](https://www.youtube.com/watch?v=VGgTmxXp7xQ)
