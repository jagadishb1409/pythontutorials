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
