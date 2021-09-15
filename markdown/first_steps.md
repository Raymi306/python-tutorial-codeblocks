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
