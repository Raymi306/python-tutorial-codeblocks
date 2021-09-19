# Installation
Choose the latest active Python release for your operating system, and follow the instructions.

Linux distributions often come with a version of Python already installed.
It is worth checking the version on your system, this can be done with `python3 -V`; If you would like to use a newer version, package managers often have several versions available.
For some package managers, you may need to add another source to retrieve versions not normally included in your distributions package manager.
Installing from source is also always an option.

[link to download page](https://www.python.org/downloads/)

## What does it mean to add Python to the PATH?
*(Windows installer asks if you want to do this)*

Go to your command line\*, and type `ping google.com`. Then, type something nonsensical, such as `foobarbaz`. How did the command line know what to do when you ran the ping command?

When you try to run a command, such as `ping` on the command line, one of the places that will be searched for matching programs are all of the directories listed in the PATH variable.
When you install Python on linux, typically this is done for you, so you can type `python3` on the command line to drop into an interpreter. 
If Python is added to your path on Windows, then you can simply type `python` in the command line to invoke the program without having to navigate to the directory in which the program installed itself.

\**To reach a terminal to run Python on Windows, type 'cmd' or 'powershell' into the Window's search bar, and select the desired terminal. Both will work for these tutorials.*
