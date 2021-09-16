# Humble Beginnings
Lets explore two built in tools provided to us by Python, `print` and `input`.

## \<built-in function print\>
`print` is something called a function, when called, it prints a statement to the screen. 
A simple syntax to use it is as follows:

```py
print('Hello world')
```

The parentheses denote that we are calling this function, that we are invoking its action.
The quotation marks around 'Hello world' tell Python that this is a string, a data type that holds text content.
It is important to indicate that 'Hello world' is a string, otherwise, Python will view this as a syntax error; It would try and interpret 'Hello' and 'world' as labels with special meaning, perhaps user defined variables, and syntactically it would require a comma between these two labels.

Try running this code, and try to put different things inside of the quotation marks and see what effect it has. Python makes the classic 'Hello world' programming tutorial very simple indeed!

## \<built-in function input\>
`input` is also a function, and it has something of the opposite effect.
When input is called, it waits for the user to hit the enter button.
When the user hits the enter button, any keys that they have pressed will be saved as a string, and 'returned' by input.

```py
input()
```

This is boring because it doesn't do anything.
It returns what we typed in to it, but nothing happens!
What we need is a way to store that information for later, so that we can manipulate it in some other way.


```py
my_variable = input()
print('You typed: ' + my_variable)
```

Here, we are assigning the result of input, the *return value*, to a variable that we decided to call 'my_variable'.
Then, we print what we typed right back at us, prepending 'You typed: ' in front.
Note that python is quite clever, and understands that the plus operator, when used with 2 strings, should smoosh these strings together, or concatenate them.
Note also that we must specify that we want a space in 'You typed: '; Python won't do things like that implicitly.


input always returns what we type as a string, but sometimes we would like to interpret the value as a number so we can do fun things like maths.

```py
my_number = input()
print(my_number * 2)
```

This returns whatever you type in twice, even if you type in a number! That's not quite what we want.

```py
my_number = int(input())
print(my_number * 2)
```

This properly doubles whatever number we type in! `int` is being used here to interpret the result of input as an integer; a whole number.
Note that it spits out an error message if you try giving it something that isn't a number!
Error messages tend to contain useful information for improving our programs when things go wrong, and sometimes we don't want them to end our program.
We will discuss error handling at a later date

```py
# preview of the future
my_number_as_string = input()
try:
    my_number = int(my_number_as_string)
except ValueError:
    print('That\'s not a number!')
else:
    print(my_number * 2)
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

So far, we have just been passing one value into the function, specifically, strings. The things that you can pass into a function are called **arguments**. Print has several more useful abilities beyond printing strings; It can print useful information for any Python object, and can even accept multiple objects, separated by comments.  This ability to take multiple arguments is denoted by the '...' in the 2nd line of the help. The other arguments are keyword arguments, they can be specified by name as follows: `print('Hello world, with no line ending!', end='')` *('\n' is a way of indicating a new line)*. When using keyword arguments by name, make sure to put them after the positional arguments that do not have a name specified. If you forget, Python will remind you with an error!

Feel free to read the help for `input` as well! It is ok if you don't understand everything the documentation is referring to, perhaps with the print function you have no concept of why forcibly flushing a stream is important, or what a stream even is. However, this still gives you a great starting point, and helps you to know what question to ask next in your learning journey.

Not all of the help entries are as short as `print` and `input`. Some of them will require scrolling, and present a lot of information that you might want to search through. You can scroll using the up and down arrow keys, or `j` and `k` keys. To search for a term, press `/`, type your search query, and hit enter. To jump between matches, use `n` and `N` to go forwards and backwards respectively. When you are ready to leave, hit `q`

You can also ask for help on other things, when inside interactive help, try typing one of: `modules, keywords, symbols, topics`. Then, try entering one of the entries within into the help. Many of the topics go quite in depth, and should match the official documentation online for your version of Python. You can also get help outside of interactive help mode by using help as a function, and passing either a string with what you need help on (as listed in modules, keywords, etc), or a python object. I believe `help` to be an underutilized and underappreciated feature of Python that can help programmers of any skill level.

## Conditions and Branching
Reacting the same way to every possible input is boring. Let's take a different action, depending on what the user types

```py
user_input = input('What\'s your name?')
if user_input == 'max':
    print('weeb')
elif user_input == 'jax':
    print('cool name!')
else:
    print('Hello, ' + user_input)
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
if True:
    print('True is true...')
    print('You\'ll see this get printed too!')
```

Return to the original indentation level when you wish to write code that occurs AFTER your if statement.

White space is important in Python! Some languages use brackets `{}` to group code together logically, Python relies on levels of indentation, using either tabs or spaces (take care not to mix them).
4 spaces are the standard level of indentation when coding in Python, however, so long as you are consistent, your code will work.

## Repetition, Looping

Generally, code executes line by line, starting at the top and continuing to the bottom. If we want to do the same thing more than once, repeating yourself is clumsy and hard to read. We program to be lazy, a good mantra is DRY: Don't Repeat Yourself! Loops provide the structure to do a task repeatedly, repeat until a condition is met, repeat until every item in a collection is examined, or repeat indefinitely.

Lets first examine the `while` loop:

```py
while True:
    print('hewwo???')
```

This highly cursed code will cause your computer to scream out in pain, forever. Feel free to run it, you can stop the code from executing by sending a 'keyboard interrupt', by pressing `Ctrl + c`.

The infinite loop can be a valuable tool for programs that you want to run until the user wishes to perform some action to close out of it. Let's combine a while loop with some earlier knowledge, and demonstrate how to exit a loop with the `break` keyword:

```py
while True:
    user_input = input('Type \'q\' to exit')
    if user_input == 'q':
        break
    # An alternate way to format strings, note the f before the lead quote, and the braces around the variable name
    print(f'You said, {user_input}')
```

This program will continually prompt the user for input, and print it back out to them. Unless, that is, the user enters 'q'. Then, when code execution reaches the 'break' statement, code execution will exit the loop. Since that is the end of this code sample, the program ends.
