---
title: RegEx
---

## `Reg`ular `Ex`pressions
Regular expresseions are useful tools in a programmers arsenal for text and string matching. In the following sections, token will refer to a character or a group of characters inside `()` that need to be matched

* Matching a single type of specific character
    * `\d` will match a single digit
    * `\D` will match a non-digit (this is similar to `[^0-9]` explained below)
    * `\w` matches a word character (`a-z`, `A-Z`, `0-9` and `_`)
    * `\W` matches any non word character (equivalent to `[^a-zA-Z0-9_]`)
    * `\s` is for any space character (`tab \t`, `space`, `newline \n`, `carriage return \r`, `form-feed \f` or `vertical tab \v`)
    * `\S` matches any character that is not in the `\s` group of characters (can also be said as non space characters)
* `[]` allow matching of any character that is placed in between the square brackets
    * `[a-z]` matches a single character, that can be any of the lower case english alphabets
    * `[a-z0-9]` matches a single character, that can either be a lowe case english alphabet, or a digit
    * `[a-zA-Z0-9_` is same as `\w` described earlier
    * with a `^` character at the start, we can create a negative character class; `[^a-z]` will match anything except the lowercase english alphabets
* `+`, `*`, `?`
    * `+` allow matching of at least `1` instance of the previous token, upto as many as it can match greedily
    * `*` on the other hand matchs `0` or more instances
    * `?` matches `0` or `1` instance of the previous token
* For matching an exact number of characters, `{}` can be used
    * `{num}` will match the previous token exactly `num` number of times
    * `{num1,num2}` matches the token between `num1` and `num2` times, as many times as needed greedily
    * `{num,}` matches the token between `num` and `unlimited` giving back greedily
    * `{,num}` will match between `0` and `num` times
* `.` is a special wildcard character that matches anything except a line terminator (characters like `\n`, `\r` and others)
* `^` and `$` can be used to match the start and end of line respectively
* To match and return groups of specific characters, `()` are used to enclose the desired set of characters
    * In case we wish to literally match the round brackets, the need to be escaped with `\` as `\(` or `\)`
    * The matched groups can be reffered back using `\1`, `\2` and so on
* To search from a set of options of character groups, `|` can be used to separate such groups
    * For instance, to match either `batman` or `superman`, we use `batman|superman`
* To literally match any of the special regex characters `.+?*|[](){}^$\`, we need to escape them/add a `\` before the character

### Python regex library
* Import the library as `import re`
* First, we need to compile the regular expression that we want to search
    * `r` prefix is used before the expression string in most cases to save time writing `\d` instead of `\\d`
    * `regex_obj = re.compile(r'\d{3}-\d{4}-\d{3}')` matches phone numbers of the form `123-4567-890`
* Following arguments can be passed to `re.compile` for specifying search settings
    * `re.IGNORECASE` for case insensitive searching
    * `re.DOTALL` to enable searching line terminators when `.` is used
    * `re.VERBOSE` ignores whitespaces in the regex
    * Multiple options can be used together by combining them with a `|`, `re.compile(r'expression', re.IGNORECASE | re.DOTALL)`
* To match on a given string/text, we can use the object returned from `re.compile` using the following functions
    * `match()` matches the expression at only the beginning of the string (returns `None` if no matches, otherwise a matched object is returned containing information about the match)
    * `search()` is similar to `match()` but searches the entire string
    * `findall()` tries to find all the matches through the entire string, returing them as a list
    * `finditer()` is similar to `findall()`, but returns an iterator instead
* The `match object`, returned by the above functions in case of a match has the following available functions
    * `group()` returns the string matched by the expression
        * An integer argument denoting the group number can be passed to `group`
        * Default argument is `0`, and `0` denotes the entire expression that was matched
        * Group matches can be accessed with the argument starting from `1`, `2`, and so on
        * In case `group(i)` does not exist, an `IndexError` is raised
    * `start()` is the starting position of the matched string
    * `end()` is the ending position of the matched string
    * `span()` is the tuple containing the start and end positions of the match
* On the compiled expression object (returned by `re.compile`), following functions allow executing specific tasks on the matched string
    * `split(string)` splits the string at the matched expression and returns the list
    * `sub(replacement, string)` substitutes all the matched expression with the argument of the `sub`
    * `subn(replacement, string)` does the same job as `sub`, but returns a tuple containing the new string and the count of replacements
    * All three functions are also present in `re` module directly, but will take an additional first argument `pattern` which is the pattern to search

#### Python regex examples
Matching a phone number
```python
>>> import re
>>> p = re.compile(r'\d{3}-\d{3}-\d{4}')
>>> p
re.compile('\\d{3}-\\d{3}-\\d{4}')
>>> p.search('My number is 415-555-4242.')
<re.Match object; span=(13, 25), match='415-555-4242'>
>>> p.search('My number is 415-555-4242.').group()
'415-555-4242'
>>> p.search('My number is 415-555-4242.').end()
25
```

Matching using groups
```python
>>> p = re.compile(r'\d+')
>>> p.search('My number is 415-555-4242.')
<re.Match object; span=(13, 16), match='415'>
>>>
>>> p = re.compile(r'(\d+)')
>>> p.findall('My number is 415-555-4242.')
['415', '555', '4242']
>>> type(p.findall('My number is 415-555-4242.')[0])
<class 'str'>
```

Matching multiple groups
```python
>>> p = re.compile(r'(\d+)-(\d+)-(\d+)')
>>> p.search('My number is 415-555-4242.')
<re.Match object; span=(13, 25), match='415-555-4242'>
>>> p.search('My number is 415-555-4242.').group(0)
'415-555-4242'
>>> p.search('My number is 415-555-4242.').group(2)
'555'
>>> p.search('My number is 415-555-4242.').group(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: no such group
>>>
```

Matching all mentions of batman and vehicles
```python
>>> p = re.compile(r'Bat(man|mobile|copter)')
>>> p.search('Batmobile, the vehicle of choice for Batman, has lost an engine.')
print('batRegex : ' + mo.group())
<re.Match object; span=(0, 9), match='Batmobile'>
>>> p.findall('Batmobile, the vehicle of choice for Batman, has lost an engine.')
['mobile', 'man']
>>> # to get the entire matched groups in findall
>>> p = re.compile(r'(Bat(man|mobile|copter))')
>>> p.findall('Batmobile, the vehicle of choice for Batman, has lost an engine.')
[('Batmobile', 'mobile'), ('Batman', 'man')]
```

#### References
* [regular expressions 101](https://regex101.com/)
* [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
