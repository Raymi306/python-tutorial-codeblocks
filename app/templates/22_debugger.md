<<[prev]({{int_operators}}) [index]({{int_index}})

[TOC]

# Debugging
Unfortunately, things don't always go to plan when you're coding.
When things break or behave unexpectedly, having visibility into what exactly the code is doing is important.
One simple way to debug problems is to fill your code with print statements that log important variables and confirm that code is being reached.
However, a better tool exists, and it comes with Python.

## Python Debugger: pdb
On a new line in your code, write `breakpoint()`{: .smolcode} and run your code.
When execution hits a line with a breakpoint, the code will pause and drop you into pdb.
From here, you can explore the state of the program, set new breakpoints, jump forwards or backwards in code, step through the program, and more.
If you ever forget what commands are available to you, type `help`{: .smolcode}. For a detailed help explaining all available commands at once and a summary of how to use pdb, type `help pdb`{: .smolcode}.

## Where am I?
There are several commands that can help orient you.
"l" run by itself will list 11 lines of the source code around the current line.
If you run "l" again, it will continue to print subsequent lines until the end of the file.
You can also pass arguments to this command to print a certain range of lines (`l lineno1 lineno2`{: .smolcode}) or to always print around the current line (`l .`{: .smolcode}).
Remember that you can type "help" and a command to get detailed information about how to use it!

Sometimes, you want more context than just the surrounding 11 lines.
"ll" will list the whole source code of the current function or frame.

Sometimes, you aren't even sure what module you're in!
In this case, the "where" command comes in handy.
It prints a stack trace, with the most recent frame at bottom and an arrow indicating the current frame.
When a frame is printed it includes the path to the module, the line number of the code if applicable, and the name of the function being run if applicable.
Frames are a container of local and global state at a given point in time of the program.
Often times, functions are a common source of frames.
When you call a new function, you enter a new frame.
The frame that you are in determines the context of the commands that you run, and is similar to a scope in this sense.

Many commands can be abbreviated.
In the help, if a command is listed with parentheses such as "w(here)", you may either type the full command or the abbreviation to the left of the parentheses.
"help" also lists all valid abbreviations.

## What's going on?
Inside the debugger, you can type any python expression and it will attempt to evalulate it in the same way the interpreter might.
If you type "p" followed by a variable name and hit enter, you can see the current value.
You may omit the "p" if the variable name does not collide with a pdb command.
"pp" will pretty print the value, which sometimes makes reading collections and nested data structures easier on the eyes.
If you wish to run a function or inspect a variable with a name collision, you can start your command with an exclamation point "!".
This allows us to access the Python interpreter's help, rather than pdb's help, by typing `!help()`{: .smolcode}.

We also might want to monitor the state of a variable over time.
Use the "display" command followed by an expression or the variable name, and it will print out the result of the expression with each step through the code.

## Where to next?
To execute the current line and step into the next function or line, run the "step" command or "s" for short.

To continue execution until the next line, run "n(ext)". This will NOT go in to a function.

To continue up until a specified line "n", run "unt(il) n".
If not given a line number n, it will continue execution until a line with a number greater or equal to the current is reached.

To continue until the return of a frame, run "r(eturn)".

To continue until the next breakpoint, run "cont(inue)".

To quit out of the debugger, run "quit".

<<[prev]({{int_operators}}) [index]({{int_index}})
