# Installation

## Windows | [link to download page](https://www.python.org/downloads/windows/)

Find the download link for the latest stable version of Python, and download it. Once the download is complete, make sure to run the file. For Windows, you are presented with a simple installer that guides you through the setup process. However, there are some options that it presents whose meaning might not be initially obvious. Of the options presented, **Ensure that you select the checkmark to add Python to the path**

### What does it mean to add Python to the PATH?
For this demonstration, we will need a terminal to type commands onto. On Windows, there are two common choices; The command prompt and powershell. Both will work. To easily find them, type the terminal name into the Window's Search Bar. Alternatively, press <Windows + r> and type 'cmd' and hit enter. This shortcut will run the 'cmd' command, giving you a command prompt.

Once you have your terminal ready to type into, type `ping google.com`. Then, type something nonsensical, such as `foobarbaz`. How did the command line know what to do when you ran the ping command?

When you try to run a command, such as `ping` on the command line, one of the places that will be searched for matching programs are all of the directories listed in the PATH variable.
If Python is added to your path on Windows, then you can simply type `python` or `py` in the command line to invoke the program without having to navigate to the directory in which the program installed itself and running the program from there. The installer should let you know whether it prefers the name `python` or `py` when you install it, but you can also fall back on the process of elimination and see what feedback it gives you as to whether or not you've typed the right name.

## Linux
Linux distributions often come with a version of Python already installed.
It is worth checking the version on your system, this can be done with `python3 -V`; If you would like to use a newer version, package managers often have several versions available.
For some package managers, you may need to add another source to retrieve versions not normally included in your distributions package manager.
Installing from source is also always an option.
Note that in this tutorial, you will need to mentally translate references to the `python` command `python3`; If you type just `python` there is a chance that you will be running the older Python 2 version.
