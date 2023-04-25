<<[prev]({{int_installation}}) [index]({{int_index}}) [next]({{int_programming_overview}})>>
# How to run code
## Using the Interpreter
### On Windows:
- open up the [command line]({{int_misc_shells}})
- depending on the version installed, type `python`{: .smolcode} or `py`{: .smolcode} and hit enter
- to exit, type `quit()`{: .smolcode}, and hit enter

### On Linux:
- open up a terminal
- type `python3`{: .smolcode} and hit enter
- to exit, type `quit()`{: .smolcode}, and hit enter. You can also use `Ctrl+D`{: .smolcode}

Output will likely be similar to this:

```
Python 3.9.2 (default, Feb 28 2021, 17:03:44)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

Inside the interpreter, you can type anything you like and Python will attempt to run it as code.
When you see the default prompt of '>>>' the interpreter is ready for you to type more things and hit enter.
If you see '...' the interpreter recognizes that you have begun a multiline statement and is expecting more input.
You can hit enter again to finish the multiline statement.

## Running Code from a File
Write the python code using a [text editor]({{int_misc_text_editors}}) or interactive developer environment (IDE) of your choice.

When ready to run the code, make sure to save it, remembering the name that you choose to give your file.
From your operating system's command prompt, run the code by typing in the name of the python program followed by the [path to your code file]({{int_misc_file_paths}})
```
python3 helloworld.py
```
It will interpret your file as code and run it from start to finish.
