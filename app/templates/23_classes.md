[index]({{int_index}})

[TOC]

# Classes: WIP
Every data type in Python is an object.
Let's explore how to make our own.

## Simple Classes
When we want to create our own type of object, we use the `class`{: .smolcode} keyword.
Let's start with an example, and then we'll go over it line by line:

```py
class MyType:
    class_attribute = 0
    def __init__(self, arg):
        self.regular_attribute = arg
        MyType.class_attribute += 1
        self.instance = MyType.class_attribute

    def method(self):
        return self.class_attribute, self.regular_attribute
```

First off, we need to name our class.
The convention in Python is to use Pascal case, where we capitalize the beginning of each word and do not use underlines.

Next, we can optionally create class attributes. These look like variable definitions in the main class body.
Class attributes will be inherent to the data type, not to individual object instances.

After this, we typically define a magic method called `__init__`{: .smolcode}.
There are a variety of magic methods that we can define, and we will cover some of them later.
Magic methods can be identified by the double-under scores (dunder for short).
\_\_init\_\_, short for initialize or initialization, controls the creation of an instance, and always takes one argument called `self`{: .smolcode}.
Additional arguments can be defined as you would with any other function.
Note that functions defined as part of class definitions are referred to as methods.
Inside of \_\_init\_\_, you may perform any steps that you need to create an instance of your class. If you assign to 'self', you will create attributes that will be unique to that class instance.
They are unique in the sense that if you change one instance's attributes, no other instance will be affected.
If you refer to a class attribute by using the class's name in any class method, you will affect ALL instances of the class.
In our example, we increase a counter by 1, and save the result as an instance attribute.
You can also read class attributes from self, but not mutate them.

Finally, we define a regular method.
This method's first argument must be self, but it can take additional arguments.
The "self" argument is what makes a method special compared to a regular function; it can access the attributes stored on self and also make changes to them.

Let's create instances of our class and interrogate them, and hopefully things will begin to click.

```py
>>> MyType.class_attribute
0
>>> MyType.regular_attribute
AttributeError: type object 'MyType' has no attribute 'regular_attribute'
>>> instance_1 = MyType(42)
>>> instance_1.class_attribute, instance_1.instance
1, 1
>>> MyType.class_attribute
1
>>> instance_1.regular_attribute
42
>>> instance_1.regular_attribute = -700
>>> instance_1.regular_attribute
-700
>>> instance_2 = MyType(13)
>>> instance_2.class_attribute, instance_2.instance
2, 2
>>> instance_1.class_attribute, instance_1.instance
2, 1
>>> instance_2.regular_attribute
13
```

## A Selection of Magic Methods
### `__str__(self), __repr__(self)`
Implementing these magic methods on your class allows for printing both a pretty and a debug representation of your object.

"\_\_str\_\_" is called by the builtin functions "print" and "format". It is also called when attempting to convert the object into a string with "str". The return value must be a string, and the value can be some convenient or concise description of the object or however you want the object represented as a string. If \_\_str\_\_ is not implemented, \_\_repr\_\_ is used in its stead.

"\_\_repr\_\_"'s implementation's return value should contain enough information to recreate the object instance.
If this is not possible, then information in the form of `<...descriptive information goes here...>`{: .smolcode} should be returned.
The return value for \_\_repr\_\_ must be a string.
### `__eq__(self, other)`
Implementing "\_\_eq\_\_" allows for equality checks between two object instances. You may choose to compare certain attributes of the class to itself, or perhaps use the id of the class.
```py
class Foo:
    def __init__(self, value):
        self.value = value

    # def __eq__(self, other):
    # """only equal if objects have the same id,
    # that is to say that they are the same exact object instance"""
        # return self is other:

    def __eq__(self, other):
        return self.value == other.value
```
### `__call__`
Implementing "\_\_call\_\_" allows you to call an object as if it were a function, performing the action that you have defined inside of the body of "\_\_call\_\_".
### `__enter__, __exit__`
context managers are used in "with" statements.
An action is performed when you enter the context manager per the implementation of "\_\_enter\_\_".
An other action is performed when you exit the context manager, typically to perform cleanup tasks. This is defined by the implementation of "\_\_exit\_\_".


## Enumerations
If a class represents a type of an object, an enum, or enumeration, represents a collection of possibilities.
Imagine the colors of a stop light. There are 3 possibilities.
You could use strings to represent them, "green", "yellow", and "red".
However, strings are vulnerable to typos, and there is always the possibility of a different color entirely being passed in.
If you wish to codify a set of choices, create an enumeration as follows:

```py
from enum import Enum

# The below syntax represents inheritance
# This means that our class StoplightColors has all of the properties of the Enum class
class StoplightColors(Enum):
    # You must assign an integer to each enumerated value
    GREEN = 1,
    YELLOW = 2,
    RED = 3,

>>> StoplightColors.YELLOW
StoplightColors.YELLOW
>>> StoplightColors.YELLOW.value
2

# The below syntax represents multiple inheritance
# This gives the properties of both str and Enum to our class
# This may be useful if we want to retrieve a string value instead of an integer value
class StoplightColors(Enum, str):
    GREEN = 'green',
    YELLOW = 'yellow',
    RED = 'red,

>>> StoplightColors.GREEN
StoplightColors.GREEN
>>> StoplightColors.GREEN.value
'green'
```

## Dataclasses
A common pattern is to use a class as a simple container mapping named attributes to data.
We can do this manually easily enough, but there are a lot of magic methods that need to be filled in to make the resulting objects behave nicely in a wide variety of situations.
There is a function that we can import to do this for us.
```py
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```
"dataclass" is being used as a decorator here with the "@" symbol.
All a decorator does is wrap a function or class.
By way of wrapping, the decorator can perform transformations and other tasks and return a modified version of the class or function definition.
Here we also see annotations for the first time.
Annotations describe what data type we expect for the attributes on the class.
Note that these are not enforced like they are in some other languages!

TODO: Explain in a little more detail about dataclasses and what it gets you for free
[link]({{ext_stdlib_dataclasses}})

## Exploring Unfamiliar Classes and Objects
Never forget the Python interpreter's help function!
You may call "help" with the object or class as an argument and receive any documentation that the author wrote.
You may document your own creations with [docstrings]({{ext_pep_257}}).
A handy trick to see what attributes and methods are available on a given object is to use the builtin "dir" function.
Call "dir" and pass the object or class as an argument and receive a list of all the available attributes.
