<<[prev]({{int_first_steps}}) [index]({{int_index}})

[TOC]

W.I.P.
# Bringing it all together

## Randomness

Randomness is great for adding some variety and spice to a program

```py
{{random_numbers}}
```

## Making a game

You should have the tools now to make yourself a guessing game now. You may want to give it a go yourself, and then compare it to the sample below:

```py
{{guessing_game}}
```

## System Arguments

You can use system arguments to pass values into a program when it starts.

This is similar to passing an argument into a function.

Assuming your program is called hello.py,

```
python3 hello.py foobarbaz
```

Your program will receive the string foobarbaz as an argument which it can then make use of.

Python too is a program, and it is being given the argument "hello.py", which in this case Python uses to know what file to run.

The below sample illustrates basic usage of arguments:

```py
{{argv}}
```

## File I/O

Reading and writing files will let us expand beyond user input, and read information from and write information to files.
Now, we have a way to make our data persist even after our program ends!

```py
{{file_io}}
```

By default, files get opened in text mode.
You can add a 'b' to the end of the mode to open them in binary mode.
You might open a file in binary mode if it is an image file or other special format, to gain more direct access to the underlying bits and bytes without the assumptions that text mode makes.

## Working with file systems

Learn how to look around and interact with files located anywhere on your computer.

```py
{{filesystem}}
```

## More about imports; Working with dependencies; Exploring the web

```py
{{imports}}
```

### Downloading packages from the Python Package Index (PyPI)
```sh
pip install --upgrade pip
```

### Managing dependencies and versions
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Browsing the web with the requests package
```py
{{requests}}
```
