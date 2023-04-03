# Working with Stacks

A stack is a data structure that follows the Last-In-First-Out (LIFO) principle. It is a collection of elements, where the addition of new elements and the removal of existing elements always happens at the same end. In a stack, we can only add or remove elements from the top of the stack. Stacks can be implemented using arrays or linked lists.

## Stack Operations

A stack supports two main operations:

### Push Operation

The push operation adds an element to the top of the stack.

### Pop Operation

The pop operation removes the element from the top of the stack.

## Other Operations

In addition to push and pop, there are other operations that we can perform on a stack, such as:

- Peek: returns the top element without removing it from the stack.
- isEmpty: returns true if the stack is empty, false otherwise.

## Example

Let's take an example of a stack of plates. Imagine that you are stacking plates on top of each other. The last plate you put on the stack is the first one you will remove when you want to use them. This is similar to a stack data structure where the last element added to the stack is the first one to be removed.

Suppose we want to implement a stack using an array. Here is how we can do it:

````python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0
````
In the above code, we have defined a Stack class that has four methods: push, pop, peek, and isEmpty. We have implemented the push operation using the append method of the list, which adds the element to the end of the list. The pop operation is implemented using the pop method of the list, which removes and returns the last element of the list. The peek operation returns the last element of the list without removing it. The isEmpty operation returns True if the list is empty, False otherwise.

We can now use this Stack class to create a stack and perform stack operations:

````python
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())  # Output: 3
s.pop()
print(s.peek())  # Output: 2
print(s.isEmpty())  # Output: False
s.pop()
s.pop()
print(s.isEmpty())  # Output: True
````

In the above code, we have created a stack s and added three elements to it using the push method. We have then used the peek method to get the top element of the stack without removing it. We have then removed two elements from the stack using the pop method. Finally, we have used the isEmpty method to check if the stack is empty or not.

## Conclusion

In conclusion, stacks are a simple yet powerful data structure that follows the LIFO principle. They are used in various applications, such as backtracking, expression evaluation, and function calls. Stacks can be implemented using arrays or linked lists, and support operations such as push, pop, peek, and isEmpty.
