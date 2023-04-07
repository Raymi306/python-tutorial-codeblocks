<<[prev]({{int_first_steps}}) [index]({{int_index}}) [next]({{int_variables}})>>

[TOC]

# Bringing it all together

## The Standard Library

Python includes extra functionality that can be accessed with the 'import' keyword.
This functionality includes solutions to common problems and access to operating system functionality.
For documentation on the many modules in the standard library, look [here]({{ext_python3_stdlib}}).
Below I will show how to import and use standard library modules, as well as modules downloaded from other sources such as the Python Package Index (PyPI).

## Randomness

Randomness is great for adding some variety and spice to a program.
Pseudorandom functionality is provided by the [random]({{ext_stdlib_random}}) module in the standard library.
Make sure to read the documentation for a full overview of the capabilities of the module.

```py
{{random_numbers}}
```

## Making a game

You should have the tools to make yourself a guessing game now. You may want to give it a go yourself, and then compare it to the sample below:

```py
{{guessing_game}}
```

## Command Line Arguments

You can use command line arguments to pass values into a program when it starts.

This is similar to passing an argument into a function.

Assuming your program is called hello.py,

```
python3 hello.py foobarbaz
```

Your program will receive the string foobarbaz as an argument which it can then use.

Python too is a program, and it is being given the argument "hello.py".
In this case Python uses the argument to know which file to run.

The below sample illustrates basic usage of arguments, using functionality from the [sys]({{ext_stdlib_sys}}) module:

```py
{{argv}}
```

## File I/O

Reading and writing files will let us expand beyond user input.
It will allow us to read information from and write information to files.
Now we have a way to make our data persist even after our program ends!

```py
{{file_io}}
```

The 'with' clause is introduced here.
It provides a guarantee that at the end of the with block, all cleanup will be taken care of for you.
With statements use [context managers]({{ext_python3_context_managers}}) behind the scenes.
Later, you'll be able to create your own context managers, but for a beginner, with statements offer a convenient and powerful way to safely handle working with files.
Context managers and with statements allow you to conveniently reuse chunks of code that require setup and teardown with error handling.

By default, files get opened in text mode.
You can add a 'b' to the end of the mode to open them in binary mode.
You might open a file in binary mode if it is an image file or other special format to gain more direct access to the underlying bits and bytes without the assumptions that text mode makes.
To learn more about reading and writing files, check out the [official documentation]({{ext_python3_file_io}}).
## More about imports; Working with dependencies; Exploring the web

Every file is its own module as well!
If you have two python files, named 'example\_a.py' and 'example\_b.py' that are in the same directory, example\_a.py can use code written in the other file:
```
{{imports_1}}
```

### Downloading packages from the Python Package Index (PyPI)
pip is the tool used to install packages from online.
It should have come with your Python installation.
It's a good idea to keep pip up to date, you can use the below command for this.

```sh
pip install --upgrade pip
```

On Linux, if you find that you do not have pip, you can use your system's package manager to install it.
For instance, on a Debianlike operating system with the Aptitude package manager, you could run:
```sh
sudo apt install python3-pip
```

### Managing dependencies and versions
If you install a package with pip, that version is likely to end up available for ALL of your python projects on your computer.
This can cause conflicts and confusion, particularly if you ever need to have projects using different versions of things.
For this reason, we create a virtual environment for each python project.
A virtual environment stores our downloaded packages and keeps them isolated.

When we want to run our project, we must make sure the virtual environment is activated.
Below are Linux commands to create a virtual environment called 'venv', to activate the environment, and to download packages listed in a file.

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

See [this link]({{ext_python3_venv_activate_commands}}) for all the ways to activate a venv on different platforms.

If you are on Linux and find that you do not have access to the venv module, you can install it with your system's package manager.
An example using Aptitude is below:
```sh
sudo apt install python3-venv
```

### Browsing the web with the requests package
Let's use a package from PyPI! 
Our first step is optional, but strongly recommended.
First, create a virtual environment and enable it.
```sh
python3 -m venv venv
source venv/bin/activate
```
Then run:
```sh
pip install requests
```
Now, when your Python programs run inside of the virtual environment they can `import requests`{: .smolcode} and make use of the tools in this library.
[Check out the documentation]({{ext_requests_docs}}) for the library to get a feel for all of the things you can do with it!
Let's look at the contents of a website:
```py
{{requests_demo}}
```
The body of the response for this webpage is in HTML.
This website is fairly simple, with only a few elements in its body.
Getting the raw HTML of a page isn't immediately useful to us; how do we make sense of it?
Let's pull in [another library]({{ext_beautifulsoup4_docs}})!
```sh
pip install beautifulsoup4
```
```py
{{soup_demo}}
```
On HTML pages, important information is often stored in header elements.
Header elements are numbered and their tag is "hn", with n being a number. Lower numbers are more important, with 1 being most imporant.
With a little bit of study into how HTML is structured, you can use different HTML tags and information inside the tags such as classes and ids to extract any information you want out of a website!
Using your browser's developer tools can be helpful here.
On most desktop browsers, you can open the developer tools by hitting F12.
Not only can you inspect the HTML content, but you can also inspect the network requests that a website makes in order to work.
Be aware that some websites generate content with a combination of scripts and web requests.
If this is the case, you can often mimic the web requests that the site is making and get the information directly.

<<[prev]({{int_first_steps}}) [index]({{int_index}}) [next]({{int_variables}})>>
