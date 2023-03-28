[index]({{int_index}})

[TOC]

# Miscellanea

---
## PATH Variable
---
### What does it mean to add Python to the PATH?
The short answer is, it lets your command line know where to find the Python program when you type things such as `py`{: .smolcode} or `python`{: .smolcode} or `python3`{: .smolcode}.
To demonstrate, we will open up a command line and try typing some different things.
Once you have your terminal ready to type into, type `ping google.com`{: .smolcode}. 
Then, type something nonsensical, such as `foobarbaz`{: .smolcode}. 
How did the command line know what to do when you ran the ping command? 
When you try to run a command, such as `ping`{: .smolcode} on the command line, one of the places that will be searched for matching programs are all of the directories listed in the PATH variable. 
You can examine this variable with Window's command prompt with `echo %PATH%`{: .smolcode}, and on Linux with `echo $PATH`{: .smolcode}. 
If you examine the directories listed you will see that there are a variety of executable programs there.
If you have already installed Python, you should also see a directory containing the Python executable.

---
## Files and File Paths
---
A file on a computer is analogous to a file in an office's filing cabinet.
It is a container of information.
Files have a location within the filesystem of your computer.
The file path indicates how to reach any given file.
### Windows
An example file path on Windows is `C:\Users\user\project\my_code.py`{: .smolcode}.
On Windows filepaths start with a drive name, most commonly 'C'.
### Linux
An example file path on Linux is `/home/user/project/my_code.py`{: .smolcode}.
On Linux, the root of the filesystem is represented by a `/`{: .smolcode}.
From there, an absolute path to all common file locations can be made by specifying every directory leading to the file.

---
## Command Prompts, Shells, Terminals
---
These terms are often used interchangeably
### Windows
There are two common choices: the command prompt (cmd) and powershell. Both will work. 
To easily find them, type the terminal name into the Window's Search Bar. 
Alternatively, press `<Windows + r>`{: .smolcode}, type 'cmd' or 'powershell', and hit enter. 
Your chosen command prompt, or shell, will then be ready to interpret your commands
### Linux
There are a variety of options for terminal and shell use, all should be fine for the purposes of this tutorial.
### Navigation
A common frustration with beginners is a disconnect between where a file is located and where their terminal currently is.
On Linux, some key commands for navigation include `pwd`{: .smolcode}, `ls`{: .smolcode}, and `cd`{: .smolcode}.
'pwd' is short for 'print working directory', and will tell you where you currently are.
'ls' will list directory contents, I often think of it as being short for list.
'cd' is short for 'change directory', and can be used to move throughout the filesystem.
If you are on Windows, an alternate to 'pwd' is 'cd' run by itself (On Linux it will return you to your home directory).
On Windows 'dir' is equivalent to 'ls', and 'cd' when given a directory can still be used to change directories.
#### Example
Say you have created a file on a Linux system at `/home/user/projects`{: .smolcode}, or on Windows at `C:\Users\User\Desktop`{: .smolcode} called sample.py.
You open your terminal, and you aren't sure where your working directory is.
```
$ pwd
/home/user
```
Running the pwd command, you see that you are in /home/user.
If you wish to run sample.py, you may try the following:
```text
$ python3 sample.py
python3: can't open file '/home/user/sample.py': [Errno 2] No such file or directory
```
The error output tells us what is going wrong: We are in /home/user, and the file sample.py does not exist there.
We can solve this in several ways:
We can provide an absolute path:
```
$ python3 /home/user/projects/sample.py
```
We can provide a relative path:
```
$ python3 projects/sample.py
```
Or we can move our working directory into projects:
```
$ cd projects
$ python3 sample.py
```

---
## Common Text Editors
---
Some folks haven't done text editing outside of MS Word and might not immediately be aware of their options for non-styled text editing.

Below is a non-exhaustive list of some choices:

### Text Editors
- IDLE *this is included with some Python downloads*
- Notepad++
- Sublime
- Atom
- Visual Studio Code
- PyCharm
- Visual Studio

### Linux Terminal Editors
- nano
- vi/vim/nvim
- emacs

Smarter text editors and IDEs will have niceties such as autoindentation and the ability to run helpful tools to develop more efficiently.

---
## Windows File Extension Woes
---
On Windows, sometimes you want to change a files extension, for instance from .txt to .py.
The default settings make this hard to do.
To allow for this, open the file explorer. From there, go to options -> view -> advanced -> and uncheck 'Hide extensions for known file types'.
After this is done, you can rename the file and edit the file extension.
