# Working with Dictionaries in Python

A dictionary is a collection of key-value pairs. Each key is associated with a value, much like a word in a dictionary is associated with its definition. In Python, dictionaries are a fundamental data structure and are used extensively in many programming tasks.

## Creating a Dictionary

You can create a dictionary by enclosing comma-separated key-value pairs within curly braces. For example, the following code creates a dictionary of employee names and their corresponding ages:

````python
employee_ages = {"John": 35, "Emily": 28, "Tom": 42}
````

## Accessing Values in a Dictionary

To access the value associated with a particular key in a dictionary, you can use square brackets and specify the key. For example, the following code retrieves the age of the employee named "Emily":

````python
print(employee_ages["Emily"]) # Output: 28
````

## Adding or Modifying Key-Value Pairs

You can add a new key-value pair to a dictionary by specifying the key and its value. If the key already exists, the value will be overwritten. For example, the following code adds a new employee named "Kate" to the dictionary:

````python
employee_ages["Kate"] = 29
````

## Removing Key-Value Pairs

You can remove a key-value pair from a dictionary by using the del keyword and specifying the key. For example, the following code removes the employee named "Tom" from the dictionary:

````python
del employee_ages["Tom"]
````

## Looping Through a Dictionary

You can loop through a dictionary using a for loop. By default, the loop iterates through the keys in the dictionary. For example, the following code prints the name and age of each employee:

````python
for name in employee_ages:
    print(name, employee_ages[name])
````

Alternatively, you can use the items() method to loop through both the keys and values in the dictionary. For example, the following code prints the name and age of each employee using the items() method:

````python
for name, age in employee_ages.items():
    print(name, age)
````

## Conclusion

Dictionaries are a powerful tool in Python, allowing you to store and manipulate key-value pairs. With the information provided in this readme, you should have a good understanding of how to create, access, modify, and remove key-value pairs in a dictionary, as well as how to loop through a dictionary.
