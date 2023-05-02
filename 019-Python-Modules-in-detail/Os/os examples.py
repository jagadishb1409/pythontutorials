# Creating Directories

import os

os.mkdir("new_dir")

# Changing Directories

os.chdir("/path/to/new/dir")

# Listing Directory Contents

files = os.listdir("/path/to/dir")

for file in files:
    print(file)


# Removing Files and Directories

os.remove("file.txt")

# Removing a directory and its content.

os.rmdir("dir_to_remove")

# Working with Processes
# Launching Processes

os.system("ls -l")

# Retrieving Process Information

pid = os.getpid()
print(pid)
