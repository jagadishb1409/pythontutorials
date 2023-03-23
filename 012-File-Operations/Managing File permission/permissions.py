
import os

# Get file permissions
permissions = oct(os.stat("example.txt").st_mode)[-3:]

# Print file permissions
print("File permissions:", permissions)


# Set file permissions to read-only
os.chmod("example.txt", 0o400)

