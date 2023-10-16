# Python Style Guide

A lot of this guide is inspired by
https://google.github.io/styleguide/pyguide.html

## Docstrings

Each file, function, and class should have a docstring. This should be of the
format specified in
https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings,
surrounded by three quotes and occurring inside the file/function/class but
before any corresponding code.

The docstring should contain a one-line summary of the code chunk it's
documenting. If necessary, it can also contain a more detailed description in a
paragraph below the summary.

For a function, the docstring should contain:

- Argument names, types, and descriptions. If there are no arguments, this can
  be omitted
- Return type and description. If there is no return value, this can be omitted

For a class, the docstring should contain:

- Class attribute names, types, and descriptions. If there are no attributes,
  this can be omitted

For a file, the docstring should contain:

- Global constants defined in the file

Example of a function docstring:

```
def my_function(arg_1, arg_2, arg_3):
  """
  One-line summary of function.

  More detailed description of function.

  Args:
    arg_1: A bool indicating whether to do something.
    arg_2: A string representing the user's name.
    arg_3: An int representing the user's age.

  Returns:
    A string containing the user's name and age.
  """
```

Example of a function docstring with no arguments or return value:

```
def my_function():
  """
  One-line summary of function.

  More detailed description of function.
  """
```

## Linting:

The linting can be handled with two VSCode extensions:
[Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
and [Pylint](https://pypi.org/project/pylint/).

Some key points:

- Indentations should be 4 spaces
- All functions and files should be documented with a docstring
- All lines should be 80 characters or less

## Naming Conventions

Use MACRO_CASE for global constants, snake_case for everything else (variables,
functions, etc)

Names can only be a single character in the following cases:

- i, j, k, etc. for counters/iterators
- e for exception identifiers in try/except statements
- f as a file handle in `with` statements

Private/protected variables/functions should be prefixed with an underscore:

```
def _my_private_function():
  pass
```

Files should be named with characters and underscores (no dashes)

Test files should be named with the convention: `test_<name>.py`
