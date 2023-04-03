## Managing file permissions

Managing file permissions is an important aspect of working with files in any operating system. In this article, we will explore how to manage file permissions using Python.

File permissions control access to files and directories by users and groups. There are three basic permissions for files and directories: read, write, and execute. Read permission allows a user to view the contents of a file, write permission allows a user to modify a file, and execute permission allows a user to run a file as a program.

Python provides an easy-to-use module called os that allows us to manage file permissions. The os module provides several functions that allow us to set, get, and modify file permissions. Let's take a look at some of the most commonly used functions.

## Checking File Permissions
Before we can manage file permissions, we need to know what permissions are currently set on the file. We can use the os.stat() function to get information about a file, including its permissions. Here's an example:

````python
import os

# Get file permissions
permissions = oct(os.stat("example.txt").st_mode)[-3:]

# Print file permissions
print("File permissions:", permissions)
````

In this example, we use the os.stat() function to get information about the "example.txt" file, and then we use the oct() function to convert the file permissions to octal notation. The result is a string containing the three digits representing the file permissions (in octal notation).

Changing File Permissions
Once we know what permissions are currently set on a file, we can use the os.chmod() function to change them. Here's an example:

```python
import os

# Set file permissions to read-only
os.chmod("example.txt", 0o400)
````

In this example, we use the os.chmod() function to set the file permissions of "example.txt" to read-only (400 in octal notation). This means that only the owner of the file will be able to read the contents of the file.

## Conclusion
Managing file permissions is an important part of working with files in any operating system. Python's os module provides a simple and easy-to-use interface for managing file permissions. In this article, we've looked at how to check and change file permissions using Python. With this knowledge, you'll be able to better manage your files and keep them secure.
