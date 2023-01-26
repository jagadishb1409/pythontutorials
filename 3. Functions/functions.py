def say_hello():
    print("Hello, World!")

say_hello()  # Output: Hello, World!

def say_hello(name):
    print(f"Hello, {name}!")

say_hello("John")  # Output: Hello, John!

def add(x, y):
    return x + y

result = add(5, 3)
print(result)  # Output: 8

def say_hello(name="John", age=25):
    print(f"Hello, {name}! You are {age} years old.")

say_hello()  # Output: Hello, John! You are 25 years old.


def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)
# Output:
# 1
# 2
# 3

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_kwargs(name="John", age=25)
# Output:
# name = John
# age = 25


add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output

