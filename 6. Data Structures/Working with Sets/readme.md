# Working with set in python
Sets are a powerful and useful data type in Python, used to store collections of unique elements. They are an unordered collection of objects that can be iterated over. In this blog, we'll discuss the basics of working with sets in Python, including creating sets, modifying sets, and performing operations on sets.

## Creating Sets

To create a set in Python, you can use the set() function or use curly braces ({}) to define a set literal. Here's an example of creating a set using the set() function:

````python
my_set = set([1, 2, 3, 4, 5])
````

Here's an example of creating a set using a set literal:

````python
my_set = {1, 2, 3, 4, 5}
````

## Modifying Sets

Once you've created a set, you can add or remove elements from it. To add an element to a set, you can use the add() method:

````python
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}
````

To remove an element from a set, you can use the remove() method:

````python
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)  # {1, 2, 4, 5}
````

## Performing Operations on Sets

Sets support a variety of useful operations, such as union, intersection, difference, and symmetric difference.

Union: To combine two sets and remove any duplicates, you can use the union() method or the | operator:

````python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5}
````

````python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  # {1, 2, 3, 4, 5}
````

## Intersection 

To find the elements that are common to two sets, you can use the intersection() method or the & operator:

````python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)  # {3}
````

````python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(intersection_set)  # {3}
````

## Difference

To find the elements that are in one set but not the other, you can use the difference() method or the - operator:

````python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)  # {1, 2}
````

````python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2
print(difference_set)  # {1, 2}
````

## Conclusion

Sets are a powerful tool in Python for working with collections of unique elements. They can be created using the set() function or set literals, and can be modified using the add() and remove() methods. Sets support a variety of useful operations, such as union, intersection, difference, and symmetric difference, which can be performed using methods or operators. Knowing how to work with sets can greatly enhance your ability to work with collections of data in Python.
