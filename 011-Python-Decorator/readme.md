# Python Decorators

Python decorators are a powerful feature that allows you to modify the behavior of functions or classes without modifying their source code. 
Decorators are higher-order functions, which means they take another function as an argument and return a new function as a result.

## Example 1: Adding Logging to a Function
In this example, we'll create a decorator that logs information about a function call. Here's what the code looks like:

````python
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function
def my_function(x, y):
    return x + y

result = my_function(3, 4)
print(result)
````

In this example, we define a decorator called 'log_function' that takes a function 'func' as an argument. The decorator defines a new function 'wrapper' that prints out information about the function call and then calls the original function 'func'. The 'wrapper' function is returned by the decorator.

We then apply the 'log_function' decorator to the 'my_function' function using the '@' symbol. When we call my_function with arguments '(3, 4)', the decorator prints out information about the function call and returns the result '7'.

This can be a useful way to debug your code or understand what is happening inside a function.

## Example 2: Input Validation for a Function
In this example, we'll create a decorator that ensures that the inputs to a function are integers. Here's what the code looks like:

````python
def validate_inputs(func):
    def wrapper(x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Inputs must be integers")
        return func(x, y)
    return wrapper

@validate_inputs
def sum_integers(x, y):
    return x + y

@validate_inputs
def multiply_integers(x, y):
    return x * y

result1 = sum_integers(2, 3)
result2 = multiply_integers(4, 5)

print(result1)  # Output: 5
print(result2)  # Output: 20

sum_integers(2.5, 3)  # Raises a ValueError
````

In this example, we define a decorator called 'validate_inputs' that takes a function 'func' as an argument. The decorator defines a new function 'wrapper' that checks if the inputs to the function are integers. If the inputs are not integers, the decorator raises a 'ValueError'. The 'wrapper' function then calls the original function func. The wrapper function is returned by the decorator.

We then apply the 'validate_inputs' decorator to the 'sum_integers' and 'multiply_integers' functions using the '@' symbol. When we call these functions with integer inputs, the decorator ensures that the inputs are valid and returns the expected results. But when we try to call 'sum_integers' with non-integer inputs, such as '(2.5, 3)', the decorator raises a 'ValueError'.

This can be a useful way to ensure that your functions are receiving the correct inputs, which can prevent bugs and improve code quality.

## Conclusion

Python decorators are a powerful feature that can save time and improve the quality of your code. In this post, we demonstrated two examples of how decorators can be used to add functionality to functions. Decorators can be used for a wide range of purposes, such as caching results, measuring function execution time, or adding security checks. By using decorators, you can keep your code modular and maintainable by separating the concerns of your code into smaller, more focused functions.

When creating your own decorators, remember that they should be as general as possible, so they can be used with different functions. Also, make sure that the decorator returns a function with the same signature as the original function. This is important for maintaining compatibility with other parts of your code.

Finally, keep in mind that decorators can be nested, meaning that you can apply multiple decorators to a single function. This can be useful for applying different kinds of functionality to a function in a modular way.

Overall, decorators are a powerful and flexible feature of Python that can help you write better, more modular code. Whether you're adding logging, input validation, or some other kind of functionality, decorators can save you time and improve the quality of your code.
