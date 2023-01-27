# Control Flow in Python

Control flow refers to the order in which the instructions in a program are executed. 
In Python, we use control flow statements to determine the flow of execution of our program. These statements include:

- If-Else: The 'if-else' statement is used to make a decision based on a certain condition. 
  If the condition is true, the code in the 'if' block will be executed, otherwise, the code in the 'else' block will be executed.

````python
if condition:
    # code to be executed if condition is true
else:
    # code to be executed if condition is false
````

- For Loops: The 'for' loop is used to iterate over a sequence, such as a list, tuple or string.

````python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
````

- While Loops: The 'while' loop is used to repeat a block of code as long as the given condition is true.

````python
i = 1
while i < 6:
    print(i)
    i += 1
````

- Break and Continue: The 'break' and 'continue' statements are used to control the flow of execution within loops. 
The 'break' statement is used to exit the loop when a certain condition is met, 
while the 'continue' statement is used to skip the current iteration of the loop and move on to the next one.


````python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
````

It's important to note that control flow statements are used to control the flow of execution in a program and it's very important 
to use them properly and not to overuse them as they can make the code more complex.
