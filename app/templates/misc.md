[index]({{int_index}})

[TOC]

# Miscellanea
---
## PATH variable
---
### What does it mean to add Python to the PATH?
The short answer is, it lets your command line know where to find the Python program when you type things such as `py` or `python` or `python3`.
To demonstrate, we will open up a command line and try typing some different things.
Once you have your terminal ready to type into, type `ping google.com`. 
Then, type something nonsensical, such as `foobarbaz`. 
How did the command line know what to do when you ran the ping command? 
When you try to run a command, such as `ping` on the command line, one of the places that will be searched for matching programs are all of the directories listed in the PATH variable. 
You can examine this variable with Window's command prompt with `echo %PATH%`, and on Linux with `echo $PATH`. 
If you examine the directories listed you will note that there are a variety of executable programs there.
If you have already installed Python, you should also see a directory containing the Python executable.
---
## File paths
---
Files have a location within the filesystem of your computer.
The file path indicates how to reach any given file.
### Windows
An example file path on Windows is `C:\Users\user\project\my_code.py`.
A historical artifact of Windows is that filepaths start with a drive name, most commonly 'C'.
### Linux
An example file path on Linux is `/home/user/project/my_code.py`.
On Linux, the root of the filesystem is represented by a `/`.
From there, an absolute path to all common file locations can be made by specifiying every directory leading to the file.
### File paths in Python
STUB

---
## Command Prompts, Shells, Terminals
---
These terms are often used interchangeably
### Windows
There are two common choices; The command prompt and powershell. Both will work. 
To easily find them, type the terminal name into the Window's Search Bar. 
Alternatively, press <Windows + r> and type 'cmd' or 'powershell' and hit enter. 
Your chosen command prompt, or shell, will then be ready to interpret your commands
### Linux
there are a variety of options for terminal and shell use, all should be fine for the purposes of this tutorial.

---
## Common Text Editors
---
Some folks haven't done text editing outside of MS Word and might not immediately be aware of their options for non-styled text editing.
Below is a non-exhaustive list of some choices
- IDLE *this is included with some Python downloads, making it a solid beginning choice*
- Notepad++
- Sublime
- Atom
- Visual Studio Code
- PyCharm
- Visual Studio
- Notepad
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
To change this, you need to have the file explorer open. From there, go to options -> view -> advanced -> and uncheck 'Hide extensions for known file types'.
