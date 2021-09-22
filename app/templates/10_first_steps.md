# Humble Beginnings
Lets explore two built-in tools provided to us by Python, `print` and `input`.

## <built-in function print\>
We can use `print` to print text to the screen.
A simple syntax to use it is as follows:

```py
{{hello_world}}
```

The parentheses denote that we are calling a function, that is to say that we are invoking its action.
The quotation marks around 'Hello world' tell Python that it is a string, a data type used to hold human-readable text.
It is important to indicate that 'Hello world' is a string, otherwise, Python will view this as a syntax error; 
It would try and interpret 'Hello' and 'world' as labels with special meaning, perhaps user defined variables, and syntactically it would require a comma between these two labels. 
When you try running this code, experiment with removing the quotation marks and removing words to see how Python tries to tell us what we're doing wrong. 
'syntax error' may be a little vague to us right now, but getting comfortable with common errors will make it easier to know where to look for help and what to do next time. Overall, though, Python makes the classic 'Hello world' programming tutorial very simple indeed!

## <built-in function input\>
`input` is also a function, and it has something of the opposite intent of `print`.
When input is called, it waits for the user to hit the enter button.
When the user hits the enter button, any keys that they have pressed will be saved as a string, and 'returned' by input.

```py
{{input_noop}}
```

This is boring because it doesn't do anything.
It returns what we typed in to it, and in the interpreter, it will print that return value out for you. 
However, this doesn't let us manipulate it in any way.
What we need is a way to store that information for later, so that we can manipulate it in some other way.


```py
{{input_and_print}}
```

Here, we are assigning the result of input, the *return value*, to a variable that we decided to call 'my_variable'.
A variable is a label matched to information that it stores. 
The label can be used to retrieve the data, and can also be pointed at different types of data.
You can call your labels whatever you like, so long as it adheres to certain rules in Python regarding naming things.
You want to be sure to not reuse an important name, such as with a statement like `print = input()`. 
This would hide the built-in function `print` with whatever string input returns, and will likely lead to confusion.
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
# preview of the future
# if we begin a line with a '#', Python will ignore it
# these lines are called comments
# they can be useful for documenting important things in your code
# leaving notes for yourself and others can be very important as you write more code
# its not uncommon to return to code after just a week away and have no idea where you left off or why...

{{futures_try_int_input}}
```

### A Few Steps Back...Using help()

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

So far, we have just been passing one value into the print function, specifically, strings. The information that you pass into a function is called **arguments** or **parameters**. Print has several more useful abilities beyond printing strings; It can print useful information for any Python object, and can even accept multiple objects, separated by comments.  This ability to take multiple arguments is denoted by the '...' in the 2nd line of the help. The other arguments are keyword arguments, they can be specified by name as follows: `print('Hello world, with no line ending!', end='')` *('\n' is a way of indicating a new line)*. When using keyword arguments by name, make sure to put them after the positional arguments that do not have a name specified. If you forget, Python will remind you with an error!

Feel free to read the help for `input` as well! It is ok if you don't understand everything the documentation is referring to, perhaps with the print function you have no concept of why forcibly flushing a stream is important, or what a stream even is. However, this still gives you a great starting point, and helps you to know what question to ask next in your learning journey.

Not all of the help entries are as short as `print` and `input`. Some of them will require scrolling, and present a lot of information that you might want to search through. You can scroll using the up and down arrow keys, or `j` and `k` keys. To search for a term, press `/`, type your search query, and hit enter. To jump between matches, use `n` and `N` to go forwards and backwards respectively. When you are ready to leave, hit `q`

You can also ask for help on other things, when inside interactive help, try typing one of: `modules, keywords, symbols, topics`. Then, try entering one of the entries within into the help. Many of the topics go quite in depth, and should match the official documentation online for your version of Python. You can also get help outside of interactive help mode by using help as a function, and passing either a string with what you need help on (as listed in modules, keywords, etc), or a python object. I believe `help` to be an underutilized and underappreciated feature of Python that can help programmers of any skill level.

## Conditions and Branching
Reacting the same way to every possible input is boring. Let's take a different action, depending on what the user types

```py
{{conditions_names}}
```

Several things are going on here. 
We are using some fancy new keywords, if, elif (python for else if), and else.

after our `if` keyword, we put a conditional statement.
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

White space is important in Python! Some languages use brackets `{}` to group code together logically, Python relies on levels of indentation, using either tabs or spaces (take care not to mix them).
4 spaces are the standard level of indentation when coding in Python, however, so long as you are consistent, your code will work.

## Repetition, Looping

Generally, code executes line by line, starting at the top and continuing to the bottom. If we want to do the same thing more than once, repeating yourself is clumsy and hard to read. We program to be lazy, a good mantra is DRY: Don't Repeat Yourself! Loops provide the structure to do a task repeatedly, repeat until a condition is met, repeat until every item in a collection is examined, or repeat indefinitely.

Lets first examine the `while` loop:

```py
{{loops_scream}}
```

This highly cursed code will cause your computer to scream out in pain, forever. Feel free to run it, you can stop the code from executing by sending a 'keyboard interrupt', by pressing `Ctrl + c`.

The infinite loop can be a valuable tool for programs that you want to run until the user wishes to perform some action to close out of it. Let's combine a while loop with some earlier knowledge, and demonstrate how to exit a loop with the `break` keyword:

```py
{{loops_input_to_break}}
```

This program will continually prompt the user for input, and print it back out to them. Unless, that is, the user enters 'q'. Then, when code execution reaches the 'break' statement, code execution will exit the loop. Since that is the end of this code sample, the program ends.


```py
{{loops_2_var_counter}}
```

This program uses 2 variables, and places a condition just like the ones we use with 'if' statements after the 'while' keyword.
Can you guess what you have to do to exit this program once it begins running? No cheating by using a keyboard interrupt!

Sometimes in a loop, we want to skip to the next iteration if a condition is met. We can achieve this effect with the `continue` keyword.

```py
# TODO is this example too contrived..?
{{loops_weird_continue}} 
# Output:
# 2
# 4
# 6
# 8
# 10
```

Here, we also introduce the modulus operator '%'. This operator returns the remainder of a division.
