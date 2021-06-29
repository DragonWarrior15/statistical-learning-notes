---
title: find
---

## `find`
`find` command allows a quick and easy scan through the file system and perform tasks on the returned results.

### Find for files and folders
* `find .`
    * Lists all the files and folders in the current directory, and also returns the files and folders from all subfolders too
* `find dir_name/`
    * Works similar to `find .` but only lists the files and folders from the directory named `dir_name`

### Find only files or folders
* `find . -type d`
    * Works similar to `find .` but only returns the directories and not the files (works recursively)
* `find . -type f`
    * Works similar to `find .` but only returns the files and not the directories (works recursively)

#### Find by name
* `find . -type f -name "file_name"`
    * Will search recursively in the current directory through the files and try to locate the file named `file_name`
    * if something like `file_*` is used instead of `file_name`, all files with the prefix `file_` will be returned (handy in case the exact file name is not known)
    * the `-name` option is case sensitive
    * using the file name as `*.py` will return all the files with the extension `.py`
* `find . -type f -iname "file_name"`
    * Performs the same search as the previous command but in a case insensitive fashion

#### Find by last modified, last accessed and changed time
* `find . -type f -mmin -10`
    * Finds all the files whose contents have been modified in the last 10 minutes
    * `mmin` refers to modified in minutes
    * `-10` refers to less than 10 minutes
    * `+10` refers to greater than 10 minutes
* `find . -type f -mmin +5 -min -10`
    * Demonstrates how to combine the queries
    * here we search for all the files that have been modified in the last 5-10 minutes
* `find . -type f -mtime -1`
    * Will return all the files modified in the last 1 day
    * `-mtime` refers to the units in days
    * Similar to `-mmin`, `+1` will return files modified more than a day back
* Other flags
    * `amin` and `atime` refer to the last access time in minutes and days respectively
    * `cmin` and `ctime` refer to the last changed time in minutes and days respectively; changed refers to changes in both metadata and content

### Find by file size
* `find . -size +5M`
    * Finds all the files that have file size upwards of 5 MB
    * `-size` is the flag to search by file size
    * The syntax is simlar to the find by last modified where `+` refers to more than while `-` is for less than
    * `+5M` is greater than 5 *M*egabytes
    * `k` can be used for *k*ilobytes
    * `G` can be used for *G*igabytes

### Logical Operators
* In all the earlier examples, specifying multiple flags together implicitly means using the `and` operator
* `and` and `or` operators are available as the `-a` and `-o` switch
* `()` can also be used to group certain flags, but they must be enclosed in `''` or `""` since they are special characters in linux
* `find . -type f "(" -mmin -5 -o -mtime +1 ")"`
    * finds all _files_ `and` only those that were modified `(` either less than 5 minutes ago `or` more than a day ago `)`
    * `find . -type f -a "(" -mmin -5 -o -mtime +1 ")"` is an equivalent formulation since the `-a` is redundant

### Find all empty files
* `find . -empty`
    * Will return all empty files and there is no need to apply the file flag

### Find by permission
* `find . -perm 777`
    * Finds all the files and folders with the given permissions in the `777` format

### Controlling the depth of traversal
* `-maxdepth` flag is useful when we wish to find the files till a certain level of depth
* `find . -type f -maxdepth 1`
    * Will find all the files in the current directory only
    * `find . -type f -maxdepth 2` on the other hand searches both the current directory and only the subdirectories (not the directories inside them)
    * not specifying this flag (as done in earlier examples) means searching the entire depth of the directory
* Similarly `-mindepth` will start the search at the specified minimum depth

### Executing commands
* Commands can be executed on files with the `-exec` flag
* `find . -type f -name "*.md" -exec head {} ';'`
    * Will execute the `head` command on all the files that are found
    * `{}` refer to the placeholder that will contain the entire file path on which to execute the command
    *  `';'` terminates the command; `'` are used since `;` is also a special character in linux
* In addition to ending the command with `;`, we also have the `+` option when we wish to pass in the list of files to a command
* `find . -type f -name "*.md" -exec tar -czf md_files.tar.gz {} '+'`
    * passes all the files of extension `.md` to the `tar` command
* Similar to `-exec`, there is `-execdir` to execute commands on directories with the `;` and `+` options available

### References
* [Linux/Mac Terminal Tutorial: How To Use The `find` Command](https://www.youtube.com/watch?v=KCVaNb_zOuw)
* [A Guide to the Linux `find` Command](https://www.booleanworld.com/guide-linux-find-command/#:~:text=The%20find%20command%20supports%20the,files%20or%20subdirectories%20in%20it.)
