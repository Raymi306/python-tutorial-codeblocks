# How to run code
## Using the Interpreter
### On Windows:
- open up the [command line](https://github.com/Raymi306/python-tutorial/blob/miscellanea/markdown/misc.md#command-prompts-shells-terminals)
- type `python` and hit enter

### On Linux:
- open up a terminal
- type `python3` and hit enter

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
Write the python code using a [text editor](https://github.com/Raymi306/python-tutorial/blob/miscellanea/markdown/misc.md#common-text-editors) or interactive developer environment (IDE) of your choice.

When ready to run the code, make sure to save it.
From your operating system's command prompt, call the python executable and pass the [path to your file](https://github.com/Raymi306/python-tutorial/blob/miscellanea/markdown/misc.md#file-paths) as the argument.
```sh
python3 helloworld.py
```
It will run your file to completion.
