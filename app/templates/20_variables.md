<<[prev]({{int_programming_overview}}) [index]({{int_index}}) [next]({{int_first_projects}})>>

[TOC]

# Variables
## Basics

Variables consist of a label and data to be stored for later.
You can give this label a descriptive name, so long as it meets certain rules [a-zA-Z], [0-9] but NOT as the first character, '_', and many UTF-8 characters, and is NOT a keyword.
The stored data may be any Python object. It could be a number value that you wish to reuse or want to accumulate results in, a list, a string, and more.
To assign a variable, use the single equals sign '=' assignment operator.
Variable assignments are statements. If you need a variable assignment as an expression, use ':='.
This can make for more concise code in some cases.

```py
# assignment as statement
my_var = foo()
if my_var:
    do_something(my_var)
# assignment as expression, using 'walrus' operator
if my_var := foo():
    do_something(my_var)

# a more complicated example
if (var_1 := foo()) and (var_2 := bar()):
    do_something(var_1, var_2)
```

## Scope
Scope is the concept of where in code a variable is accessible from.
A variable is 'in-scope' on succeeding lines, with the exception of inside of class definitions.
Class definitions create a new scope.
Functions have their own unique scope.

```py
var_1 = 2
def func_1():
    var_2 = 3

print(var_1)  # 2
print(var_2)  # NameError: name 'var2' is not defined
```

[Variable resolution occurs at runtime](https://docs.python.org/3/reference/executionmodel.html?highlight=variable%20scope#interaction-with-dynamic-features)
The below example shows one possibly unexpected ramification of this.
```py
i = 15
def foo():
    print(i)
i = 3
foo()  # prints 3
```

## Mutating Outer Scope Variables

Two keywords exist to allow you to assign to variables in a higher scope, 'nonlocal' and 'global'
Below are some examples of variable assignment with and without using the keywords.

```py
var_1 = 9.3

def func_1():
    # accessing variables from an outer scope works fine
    print(var_1)  # 9.3
    # trying to change them will not work as expected
    var_1 = 0.0
    print(var_1)  # 0.0
func_1()
print(var_1)  # 9.3

def func_2():
    # the global keyword here grants the ability to modify var_1
    global var_1
    var_1 = 'foo'

func_2()
print(var_1)  # 'foo'
```

```py
def outer_func():
    var_1 = 42
    def inner_func():
        nonlocal var_1
        var_1 = 13
    inner_func()
    print(var_1)  # 42
```

Mutating global variables can lead to unexpected behavior in different parts of your program far removed from where you made the change.
It is often considered bad practice.
If you find yourself relying heavily on the 'global' keyword, restructuring your code may be of great help.

## Mutable vs Immutable Objects
Some objects such as numbers, booleans, tuples, and strings are immutable in Python.
This means that if you want to perform an operation on them, a new object is created for the result as the original cannot be changed.
If you try and assign two variables to the same immutable object, and then make a change to one of the variables, a new object is created.
However, user-defined objects and many collections besides tuples are mutable objects.
If you point two variables at the same mutable object, changes to one will affect the other.
The best way to illustrate the consequences of this is an example:
```py
list_1 = [1, 2, 3]
list_2 = list_1  # this does not copy the list, both variables will reference the same list
list_1.append(4)
print(list_2)  # [1, 2, 3, 4]
```
We may use the copy module to achieve the desired behavior
```py
import copy
list_1 = [1, 2, 3]
list_2 = copy.copy(list_1)
list_1.append(4)
print(list_2)  # [1, 2, 3]

# alternatively, you may copy a list with the following syntax:
list_3 = list_1[:]

# dictionaries have a copy method, saving you an import
dict_1 = {1: 2}
dict_2 = dict_1.copy()
```

## Naming Conventions
**Note: Maybe move or duplicate me in a page about style**
Just because you can give a variable any name doesn't necessarily mean that you should.
In Python, convention is to use "snake case" for variable and function names.
Snake case is all lower case with words separated by underscores.
Constants, or variables that are not intended to change, should be screaming snake case, or all upper case with words separated by underscores.
Classes should use Pascal case. Each word should start with an upper case letter, and the rest are lower case.
In addition to cases, be kind to yourself, your future self, and others when naming variables.
Unnecessarily short variables are hard to understand, as are unnecessarily long ones.
Be as descriptive as you need to be with the variable.
If there are important assumptions about the data that are not immediately obvious, such as a time being in seconds rather than minutes, consider adding that info to the variable name.
