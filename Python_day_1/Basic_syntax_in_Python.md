# Basic Syntax in Python:
Contains all of the note and basic syntax used in Python practice at day 1

## Print

**Print** will print the result out

Examples:

When typing _print "Hello World"_

```Python
print "Hello"

s = "Printing using variables"

print s
```

## Rule for Identifiers:

- Class names start with an uppercase letter. All other identifiers start with a lowercase letter.

- Starting an identifier with a single leading underscore indicates that the identifier is private.

- Starting an identifier with 2 leading underscores indicates a strongly private identifier.

- If the identifier also ends with 2 trailing underscores, the identifier is a language-defined special name.

## Lines and Identation:

Blocks of code are denoted by line indentation, which is rigidly enforced.

Example:

```Python
if True:
    print "answer"
    print "True"
else:
    print "Answer"
    print "False"
```
Thus, in Python all the continuous lines indented with same number of spaces would form a block.

## Multi-Line Statements:

Statements in Python typically end with a new line. However, Python allow the use of the line continuation character  **\** to denote that the line should continue.

Example:

```Python
total = item_one + \
        item_two + \
        item_three
```

Statements containded in the [], {}, or () brackets do not need to use the **\**

## Quotation in Python

Python accepts single ('), double " and the tripe quotes to denote string literals, as long as the same type of quote starts and ends the string.

## Comments in Python

A hash sign # that is not inside a string literal begins a comment. All characters after the # and up to the end of the physical line are part of the comment and the Python interpreter ignores them.

```Python
# First comment       
print "Hello World!" # Second comment.
```

## Using Blank Lines

Python ignores the blank lines.

## Waiting for the user

"\n\n" is used to create two new lines before displaying the actual line.

```Python
raw_input("\n\nPress the enter key to exit")
```

## Multiple Statements on a Single Line

The semicolon allows multiple statements on the single line given that neither statement starts a new code block.

## Multiple Statement Groups as Suites

A group of individual statements, such as if, while, der, and class require a header line and a suite.

Header lines begin the statement and terminate with a colon and are followed by one or more lines which make up the suite. For example:

```Python
If expression :
  Suite
elif expression :
  suite
else :
  Suite
```
