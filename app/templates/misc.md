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
Non-exhaustive
### Windows
- Notepad
- IDLE
- Notepad++
- Sublime
- Atom
- Visual Studio Code
- PyCharm
- Visual Studio
- VIM
### Linux Terminal Editors
- nano
- vi/vim/nvim
- emacs

Note that smarter text editors and IDEs will have niceties such as autoindentation and the ability to run helpful tools to develop more efficiently. They will likely even have the option to run terminal commands without leaving the editor
