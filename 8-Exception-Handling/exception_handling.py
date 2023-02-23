try:
    # Some code that might raise an exception
    number = int("abc")
except ValueError as e:
    # This block will be executed if the code in the try block raises a ValueError
    print("Caught an exception:", e)

try:
    # Some code that might raise an exception
    number = int("abc")
except ValueError as e:
    # This block will be executed if the code in the try block raises a ValueError
    print("Caught a ValueError:", e)
except Exception as e:
    # This block will be executed if the code in the try block raises any other type of exception
    print("Caught an exception:", e)

try:
    # Some code that might raise an exception
    number = int("abc")
except ValueError as e:
    # This block will be executed if the code in the try block raises a ValueError
    print("Caught a ValueError:", e)
finally:
    # This block will be executed regardless of whether an exception was raised or not
    print("Finally block executed")
