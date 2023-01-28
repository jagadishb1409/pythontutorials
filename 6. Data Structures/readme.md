# Data structures in Python

Data Structures in Python are used to store and organize data in an efficient manner. They are a way to organize and structure data in a logical and meaningful way. 
In intermediate level of python, you will learn about various data structures such as Lists, Tuples, Sets, and Dictionaries.

## Lists

Lists are ordered collections of items. They are defined by placing items inside square brackets [] separated by commas. 
Lists are mutable, meaning that items can be added, removed, or modified. 
They are also indexed, which means you can access items by their position in the list. For example:

````python
fruits = ["apple", "banana", "orange"]
print(fruits[0]) # Output: "apple"
````

## Tuples
Tuples are similar to lists, but they are immutable, meaning that once they are created, their items cannot be modified. 
They are defined by placing items inside parentheses () separated by commas. 
They are also indexed and you can access items by their position in the tuple. For example:

````python
fruits = ("apple", "banana", "orange")
print(fruits[0]) # Output: "apple"
````

## Sets
Sets are unordered collections of unique items. They are defined by placing items inside curly braces {}. 
Sets automatically remove any duplicates and are commonly used for membership testing and set operations. For example:

````python
fruits = {"apple", "banana", "orange"}
print("banana" in fruits) # Output: True
````

## Dictionaries
Dictionaries are unordered collections of key-value pairs. They are defined by placing items inside curly braces {} separated by colons :. 
The keys must be unique and are used to access the values. Dictionaries are also mutable. For example:

````python
fruits = {"apple": 1, "banana": 2, "orange": 3}
print(fruits["banana"]) # Output: 2
````

In addition to these data structures, Python also has advanced data structures such as Queues, Stacks, and Linked Lists. 
Understanding these data structures and how to use them efficiently is crucial for writing efficient and effective Python code in the intermediate level.

