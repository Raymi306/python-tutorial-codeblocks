<<[prev]({{int_classes}}) [index]({{int_index}})

[TOC]

# Style and Early Error Detection
Coding style governs things such as how to name variables, how many new lines to put between blocks, how your imports are organized, and more.
There is one definitive source of guidelines that you should be aware of: [PEP 8]({{ext_pep_8}}).

PEP 8 outlines the coding convention that the Python project follows for code in the standard library.
PEP 8 can be followed manually, but tools exist to check for style violations.
Linters check for issues of style, and can also check for possible errors such as using a module that you forgot to import.
The sooner in your project that you start using a linter, the easier it is to keep your code compliant.

## [Pylint]({{ext_pylint}})
Quoting from Pylint's PyPi page,
> Pylint is a static code analyser for Python 2 or 3. The latest version supports Python 3.7.2 and above. Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored.

Pylint is simple to install and use.
```
pip install pylint
pylint --help
pylint app
```
Replace app with the name of your Python package.
Pylint is thorough, but slow.

## [Ruff]({{ext_ruff}})
On the opposite end of the speed spectrum is Ruff.
A newer linter than Pylint, Ruff is blazingly fast and has many plugins.
It may be harder to collect the plugins to check for the issues that you want, but the speed cannot be beat.
To install ruff and to check files in the current directory:
```
pip install ruff
ruff check .
```
