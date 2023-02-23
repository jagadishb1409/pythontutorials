
s1 = "hello"
s2 = "world"
s3 = s1 + " " + s2
print(s3) # Output: "hello world"


name = "Alice"
age = 25
print("My name is %s and I am %d years old." % (name, age)) # Output: "My name is Alice and I am 25 years old."

name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age)) # Output: "My name is Alice and I am 25 years old."

s = "apple,banana,orange"
fruits = s.split(",")
print(fruits) # Output: ["apple", "banana", "orange"]

fruits = ["apple", "banana", "orange"]
s = ",".join(fruits)
print(s) # Output: "apple,banana,orange"

s = "  hello world  "
s = s.strip()
print(s) # Output: "hello world"

s = "hello world"
s = s.replace("world", "Python")
print(s) # Output: "hello Python"

s = "hello world"
index = s.find("world")
print(index) # Output: 6

s = "hello world"
print(s.startswith("hello")) # Output: True
print(s.endswith("world")) # Output: True
