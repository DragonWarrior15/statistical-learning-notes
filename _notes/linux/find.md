---
title: find
---

## `find`
`find` command allows a quick and easy scan through the file system and perform tasks on the returned results.

* `find .`

    Lists all the files and folders in the current directory, and also returns the files and folders from all subfolders too
* `find dir_name/`

    Works similar to `find .` but only lists the files and folders from the directory named `dir_name`
* `find . -type d`

    Works similar to `find .` but only returns the directories and not the files (works recursively)
* `find . -type f`

    Works similar to `find .` but only returns the files and not the directories (works recursively)
* `find . -type f -name "file_name"`
    * Will search recursively in the current directory through the files and try to locate the file named `file_name`
    * if something like `file_*` is used instead of `file_name`, all files with the prefix `file_` will be returned (handy in case the exact file name is not known)
    * the `-name` option is case sensitive
    * using the file name as `*.py` will return all the files with the extension `.py`
* `find . -type f -iname "file_name"`

    Performs the same search as the previous command but in a case insensitive fashion

