<<[prev]({{int_linter}}) [index]({{int_index}})

[TOC]

*work in progress*

# Exception Handling

Sometimes, things go wrong.
If your code attempts an unsupported operation, such as dividing by zero or accessing a key in a dictionary that doesn't exist, an exception is thrown.
An unhandled exception causes the program to halt, but sometimes, we want to recover from or handle these errors.
Let's explore how to handle exceptions!

## Illustrating the Problem

Consider the following function:
```py
def delta(x):
    return abs(1 / x)
```
For what values will x work?
You can try calling the function with a few:
```
>>> delta(1)
1
>>> delta(2)
0.5
>>> delta(-2)
0.5
>>> delta(3.14)
0.3184713375796178
```
These all seem to work OK.

What happens though, if the number is 0?
```
>>> delta(0)
ZeroDivisionError: division by zero
```

What happens if x is not a number?

```
>>> delta('foo')
TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

We can solve this problem in a few ways.
We could have a guard statement before the dangerous division operation to protect against divide by zero:

```py
def delta(x):
    if x == 0:
        return None
    return abs(1 / x)
```

To protect against the passing of a non-number, we could use the Python builtin `isinstance` to check if x is an int or float:

```py
def delta(x):
    if x == 0 or not (isinstance(x, float) or isinstance(x, int)):
        return None
    return abs(1 / x)
```

We have introduced a new problem.
We are returning two different types, None or a number, and leaving it to the user of our function to handle the possible None values.
This may be OK.
Additionally, the user may wish to pass something that is divisible by 1 that we haven't thought of yet:  Perhaps a custom number type.
Let's look at how duck typing and exceptions can allow us to handle this.

## Duck Typing

There are a variety of common ways to express duck typing.
"If it looks like a duck and quacks like a duck, then it's a duck"

The gist of duck typing boils down to worrying about what an object can do rather than what an object inherently is.

Let's return to the original simple version of the function:
```py
def delta(x):
    return abs(1 / x)
```

Instead of trying to prevent the error, let's embrace it!
We can try an operation, see if it raises an exception, and then choose how to continue.
To do this, we will use the try...except key words.

```py
try:
    result = delta(0)
except:
    print("That didn't work, lets carry on and try something else")
```

Above we have a bare except:  This will catch ANY error, and is awfully broad.
Being indiscriminate with error catching can lead confusion or a different, harder to diagnose error later.
As a general rule of thumb, we WANT to know what goes wrong in our code rather than hide it.
We can narrow down the exceptions we want by specifying one or more errors:

```py
try:
    result = delta(0)
except ZeroDivisionError:
    print("You tried to divide by zero!")
except TypeError:
    print("You tried dividing something that is not divisible!")

# OR

try:
    result = delta(0)
except (ZeroDivisionError, TypeError):
    print("Whoops!")
```

You may be curious as to what errors are possible.
Hopefully, whatever function you are using has a good documentation string laying out the possibilities.
Otherwise, it may come down to trial and error.
Test your code thoroughly, and hopefully the exceptions will make themselves evident.

## Controlling the Flow

### else...

You can specify code that you wish to run after the try block ONLY if it succeeeds with the "else" keyword.

```py
try:
    foo = func()
except:
    print("Oh no!")
else:
    process_foo(foo)
```

### finally...

A common pattern is to need to clean things up regardless of if something fails or succeeds.
You can accomplish this with the "finally" keyword.

```py
import random

def fail_maybe():
    num = random.randint(0, 1)
    if num == 1:
        raise RuntimeError()

try:
    fail_maybe()
except RuntimeError:
    print("I only print when an error occurs")
else:
    print("I only print when no error occurs")
finally:
    print("I will print every time")
```

## Being Overly Broad is Bad, Part 2
You may be tempted to write code like this:

```py
try:
    task_1()
    task_2()
    task_3()
    print("About to do task 4")
    task_4()
    foo = 2 / 3 + task_5()
    return foo, task_6()
    cleanup()
except:
    print("Something went wrong!")
```

If "Something went wrong" gets printed...WHAT went wrong?
Which of the lines were you actually worried about causing an error?
You can gather error information in the except block to try and allieviate this, but that does not help the coder at read-time.
In the above example, if the only task that you are concerned of raising an error is task 3, consider:

```py
task_1()
task_2()

try:
    task_3()
except TaskError as e:
    print("Task 3 failed! {e}")
else:
    print("About to do task 4")
    task_4()
    foo = 2 / 3 + task_5()
    return foo, task_6()
finally:
    cleanup()
```

This isn't a hard and fast rule, sometimes, it ends up being cleaner to have many statements in the try block and to sort it out with one or more except blocks.

## Raise Your Own Exceptions

You can raise exceptions in your own code as well!
You may wish to do this if someone attempts to use a function you wrote in an unintended or unsupported way.
You may also wish to catch several disparate errors and raise just one for the end user to worry about.

Use the "raise" keyword:

```py
def func():
    raise RuntimeError("Optional information goes here")
```

If you are raising an error because of another error, it is best practice to use the "from" keyword.
This provides additional context to the error that shows up in the new error's stack trace.

```py
def func(num):
    try:
        return num / 2 
    except DivideByZeroError as e:
        raise RuntimeError from e
```

## Create Your Own Exception

While Python provides [a large list of built-in Exceptions](https://docs.python.org/3/library/exceptions.html#concrete-exceptions), it can be useful to create your own.
This allows one to narrow down to just your specific exception in exception handling code.
If your exception is related to an existing one, you may inherit from it.  Otherwise, inheriting from "Exception" is usually a good choice.
You can create your own hierarchy of errors by creating one that inherits from "Exception", and then inheriting from that in turn.
If you try to catch an exception higher up the chain, it will in turn catch its children.
Remember that if you specify "Exception", you catch ALL exceptions as it is the most basic exception that all others derive from.

```py
class MyException(Exception):
    """Raised when the bad thing happens"""

class MyExceptionChild(MyException):
    pass
```
