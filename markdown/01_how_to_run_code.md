# How to run code
## Using the Interpreter
### On Windows:
- open up an interpreter (cmd or powershell)
- type `python` and hit enter

### On Linux:
- open up an interpreter
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
Write the python code using a text editor or interactive developer environment (IDE) of your choice. 
Your text editor can be as simple as Notepad, or as complex as Visual Studio for Windows.
Note that smarter text editors and IDEs will have niceties such as autoindentation and the ability to run helpful tools to develop more efficiently.

When ready to run the code, make sure to save it.
From your operating system's command prompt, call the python executable and pass the path to your file as the argument.
```sh
python3 helloworld.py
```
It will run your file to completion.
