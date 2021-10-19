<<[prev]({{int_running_code}}) [index]({{int_index}})

[TOC]

# Humble Beginnings
Lets explore two built-in tools provided to us by Python, `print` and `input`.

---
## <built-in function print\>
---
We can use `print` to print text to the screen.
It can be used in the following way:

```py
{{hello_world}}
```

Here, the spelling of print, parentheses after print, and quotation marks around 'Hello world' are all necessary for this code to work.
The content inside of the quotation marks does not matter. Python also allows you to use single or double quotes, so long as the opening and closing quotation marks match.

In Python, key words and built-in functions are case sensitive and only have one correct spelling.
`print` is an example of a built-in function, a tool provided in the language to perform a certain task; namely, printing text for the user of the program to read.
Computers are incredibly literal machines, `Print` or `prnt` are meaningless at the beginning of a python program.

The parentheses are necessary any time we want to call a function; that is to say, to invoke its action.

The quotation marks around 'Hello world' tell Python that 'Hello world' is text data, rather than a label with special meaning.
We refer to the type of data for representing text 'Strings' in programming, sometimes abbreviated as `str`.
When you try running this code, experiment with removing the quotation marks and other pieces of the code to see how Python tries to tell us what we're doing wrong. 
'syntax error' may be a little vague to us right now, but getting comfortable with common errors will make it easier to know where to look for help and what to do next time.
Overall, Python makes the classic 'Hello world' programming tutorial very simple indeed!

---
## <built-in function input\>
---
`input` is also a function, and rather than displaying text TO the user, it waits for text FROM the user, that can then be used inside of the program.
When input is called, it waits for the user to hit the enter button.
When the user hits the enter button, any keys that they have pressed will be saved as a string, and 'returned' by input.

```py
{{input_noop}}
```

By itself, input is rather boring as it doesn't appear to do much; We give the program text, and it immediately discards it.
What we need is a way to store the text for later, so that we can manipulate it in some other way.


```py
{{input_and_print}}
```

Here, we are assigning the result of input, the *return value*, to a variable that we decided to call 'my\_variable'.
A variable is a label matched to information that it stores. 
The label can be used to retrieve the data at a later point in our program.
You can call your labels whatever you like, so long as it adheres to certain rules in Python regarding naming things.
You want to be sure to not reuse an important name, such as with a statement like `print = input()`. 
This would hide the built-in function `print` with whatever string input returns, and will likely lead to confusion with anyone reading the code later.
Generally speaking, a variable's label, or name, can have any character from a-z A-Z, and the digits 0-9, so long as the digit is NOT the first character in the name.
The underscore character '\_' is commonly used in lieu of spaces, which are not allowed in variable names.
So what do we do with our newly defined variable?
We print the data that it references, the very same string that we typed into `input`, and prepend 'You typed: ' in front.
Note that python is quite clever, and understands that the plus operator, when used with 2 strings, should smoosh these strings together, or concatenate them.
Note also that we must specify that we want a space in 'You typed: '; Python won't do things like that implicitly.


input always returns what we type as a string, but sometimes we would like to interpret the value as a number so we can do fun things like maths.

```py
{{input_and_print_twice}}
```

This returns whatever you type in twice, even if you type in a number! That's not quite what we want.
What we need is a way to interpret the string data as numeric data, in our case, as an integer:

```py
{{input_and_print_double_v1}}
```

With programming, there are often multiple approaches to a problem that are effectively the same:

```py
{{input_and_print_double_v2}}
```
```py
{{input_and_print_double_v3}}
```
```py
{{input_and_print_double_v4}}
```

These snippets all properly double whatever number we type in! `int` is being used here to interpret the result of input as an integer; a whole number.
Note that it spits out an error message if you try giving it something that isn't a number!
Error messages tend to contain useful information for improving our programs when things go wrong, and sometimes we don't want them to end our program.
We will discuss error handling later, although an example is included below.

```py
{{futures_try_int_input}}
```

---
## A Few Steps Back...Using help()
---
Go ahead and drop into the python interpreter. Type `help()` and then press enter.
Now, go ahead and enter `print`, and you should see something like this:

```
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

So far, we have just been passing one value into the print function, specifically, strings.
The information that you pass into a function is referred to as **arguments** or **parameters**.
Print has several more useful abilities beyond printing strings; It can print useful information for any Python object, and can even accept multiple objects, separated by commas.
This ability to take multiple arguments is denoted by the '...' in the 2nd line of the above example.
The other arguments are keyword arguments, they can be specified by name as follows: `print('Hello world, with no line ending!', end='')` *('\n' is a way of indicating a new line)*.
When using keyword arguments by name, make sure to put them after the positional arguments that do not have a name specified.
If you forget, Python will remind you with an error!

Feel free to read the help for `input` as well!
It is ok if you don't understand everything the documentation is referring to, perhaps with the print function you have no concept of why forcibly flushing a stream is important, or what a stream even is.
However, this still gives you a great starting point, and helps you to know what question to ask next in your learning journey.

Not all of the help entries are as short as `print` and `input`.
Some of them will require scrolling, and present a lot of information that you might want to search through.
You can scroll using the up and down arrow keys, or `j` and `k` keys.
To search for a term, press `/`, type your search query, and hit enter.
To jump between matches, use `n` and `N` to go forwards and backwards respectively.
When you are ready to leave, hit `q`

You can also ask for help on other things, when inside interactive help, try typing one of: `modules, keywords, symbols, topics`.
Then, try entering one of the entries within into the help.
Many of the topics go quite in depth, and should match the official documentation online for your version of Python.
You can also get help outside of interactive help mode by using help as a function, and passing either a string with what you need help on (as listed in modules, keywords, etc), or a python object.
I believe `help` to be an underutilized and underappreciated feature of Python that can help programmers of any skill level.

# Conditions and Branching
Reacting the same way to every possible input is boring. Let's take a different action, depending on what the user types

```py
{{conditions_names}}
```

Several things are going on here. 
We are using some fancy new keywords, if, elif (pythonese for else if), and else.

After our `if` keyword, we put a conditional statement.
We're interested to know whether or not something is true. In this case, we are doing a comparison using '=='.
Note that when we want to check for equality, we use TWO equal signs. One equal sign is for assigning variables!
So, if the user puts their name as 'max', we take a special action, and print out 'weeb'. If it isn't max, we check to see if it is 'jax'.
If it is, we print 'cool name!'. Otherwise, we print out 'Hello, ' and their input.

Note that after our conditions, or after the 'else' keyword, we MUST put a colon `:`.
Furthermore, on the next line, we must indent.
If you have multiple lines indented to the same level, they will all execute if that branch is taken, ie:

```py
{{conditions_indent}}
```

Return to the original indentation level when you wish to write code that occurs AFTER your if statement.

White space is important in Python!
Some languages use brackets `{}` to group code together logically, Python relies on levels of indentation, using either tabs or spaces (take care not to mix them).
4 spaces are the standard level of indentation when coding in Python, however, so long as you are consistent, your code will work.

```py
{{conditions_boolean_logic}}
```

Conditional statements can be combined with parentheses, `and`, and `or`.
Parentheses are used to have part of a statement evaluate as a group, similar to how they are used in mathematical expressions.
Using `and` to combine two statements means that the full condition will evaluate as true if and only if both sides are true.
`or` evaluates as true if either side is true, or if both are true.
You can negate a condition with `not` to test for the inverse of a condition.
If you want to check for a condition that is False, negating the condition would give you `True` and thus would let the branch evaluate.
Finally, if you wish to check that two items are not equal, you can use `!=`.

# Repetition, Looping
Generally, code executes line by line, starting at the top and continuing to the bottom.
If we want to do the same thing more than once, repeating yourself is clumsy and hard to read.
We program to be lazy; a good mantra is DRY: Don't Repeat Yourself!
Loops provide the structure to do a task repeatedly, repeat until a condition is met, repeat until every item in a collection is examined, or repeat indefinitely.

Lets first examine the `while` loop:

```py
{{loops_scream}}
```

This code will cause your computer to print 'hello...' forever.
Feel free to run it, you can stop the code from executing by sending a 'keyboard interrupt', by pressing `Ctrl + c`.

The infinite loop can be a valuable tool for programs that you want to run until the user wishes to perform some action to close out of it.
Let's combine a while loop with some earlier knowledge, and demonstrate how to exit a loop with the `break` keyword:

```py
{{loops_input_to_break}}
```

This program will continually prompt the user for input, and print it back out to them.
Unless, that is, the user enters 'q'.
Then, when code execution reaches the 'break' statement, code execution will exit the loop.
Since that is the end of this code sample, the program ends.


```py
{{loops_2_var_counter}}
```

This program uses 2 variables, and places a condition just like the ones we use with 'if' statements after the 'while' keyword.
Can you guess what you have to do to exit this program once it begins running? No cheating by using a keyboard interrupt!

Sometimes in a loop, we want to skip to the next iteration if a condition is met. We can achieve this effect with the `continue` keyword.

```py
{{loops_simple_continue}}
```

This program prints out the number of each iteration, except for the cases where the iteration is equal to 3 or 7.

```py
{{futures_sock_continue}} 
```

This program uses several concepts we will cover in detail later; namely importing modules and context managers.
It checks to see if there is any data to consume, if there is, it will consume ALL data as quickly as possible.
However, if there is no data left, it sleeps, pausing and doing nothing.
If you are on a Linux platform and would like to play with this example, first, run `nc -l 12345`, then, run this program.
Finally, enter data into nc's stdin. When you hit enter, this program will print your input out one byte at a time.

```py
{{loops_for_in}}
```

TODO: Explain list collection and for loops vs while loops, check if item `in` collection
