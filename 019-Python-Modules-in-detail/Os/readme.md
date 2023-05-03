# Introduction

The os module is a built-in module in Python that provides a way of interacting with the operating system. It provides a wide range of functions that allow you to work with the file system, environment variables, processes, and more.

In this document, we will explore the os module in detail, including its main features and functions, and how to use them with practical examples.

## Getting Started

To use the os module, you first need to import it into your Python script:

````python
import os
````

After importing the module, you can use its functions and attributes by calling them on the os object.

## 1. Working with the File System

One of the main features of the os module is its ability to work with the file system. This includes functions for creating, deleting, and manipulating files and directories.

### i. Creating Directories

To create a new directory, you can use the os.mkdir() function. This function takes a single argument, which is the name of the directory to create.

````python
import os

os.mkdir("new_dir")
````

This will create a new directory named new_dir in the current working directory.

### ii. Changing Directories

To change the current working directory, you can use the os.chdir() function. This function takes a single argument, which is the path of the directory to change to.

````python
import os

os.chdir("/path/to/new/dir")
````

This will change the current working directory to the directory at /path/to/new/dir.

### iii. Listing Directory Contents

To list the contents of a directory, you can use the os.listdir() function. This function takes a single argument, which is the path of the directory to list.

````python
import os

files = os.listdir("/path/to/dir")

for file in files:
    print(file)
````

This will list all the files and directories in the directory at /path/to/dir.

### iv. Removing Files and Directories

To remove a file, you can use the os.remove() function. This function takes a single argument, which is the name of the file to remove.

````python
import os

os.remove("file.txt")
````

This will remove the file named file.txt from the current working directory.

To remove a directory and its contents, you can use the os.rmdir() function. This function takes a single argument, which is the name of the directory to remove.

````python
import os

os.rmdir("dir_to_remove")
````

This will remove the directory named dir_to_remove from the current working directory.

## 2. Working with Processes

The os module also provides functions for working with processes. This includes functions for launching new processes and retrieving information about running processes.

### i. Launching Processes

To launch a new process, you can use the os.system() function. This function takes a single argument, which is the command to run.

````python
import os

os.system("ls -l")
````

This will run the ls -l command and print the output to the console.

### ii. Retrieving Process Information

To retrieve information about running processes, you can use the os.getpid() function, which returns the current process ID.

````python
import os

pid = os.getpid()

print(pid)
````

This will print the process ID of the current Python process.

## Conclusion
The os module provides a powerful set of functions for interacting with the operating system. This includes working with the file system, processes, environment variables, and more.

By understanding how to use these functions, you can write Python scripts that are capable of performing a wide range of system-level tasks.
