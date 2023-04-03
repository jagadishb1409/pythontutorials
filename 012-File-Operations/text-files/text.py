# Open a file for reading
file = open('example.txt', 'r')

# Open a file for writing
file = open('example.txt', 'w')

# Open a file for appending
file = open('example.txt', 'a')

# Close the file
file.close()

# Open a file for reading
file = open('example.txt', 'r')

# Read the contents of the file
contents = file.read()

# Close the file
file.close()

# Print the contents of the file
print(contents)


# Open a file for reading
file = open('example.txt', 'r')

# Read the first line of the file
line = file.readline()

# Close the file
file.close()

# Print the first line of the file
print(line)

# Open a file for writing
file = open('example.txt', 'w')

# Write to the file
file.write('Hello, World!')

# Close the file
file.close()

# Open a file for writing
file = open('example.txt', 'w')

# Write to the file
file.writelines(['Hello,', ' World!'])

# Close the file
file.close()


# Open a file for appending
file = open('example.txt', 'a')

# Append to the file
file.append('Hello, World!')

# Close the file
file.close()


