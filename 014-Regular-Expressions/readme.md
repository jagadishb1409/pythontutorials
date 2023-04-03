# Regular Expressions

Regular expressions (regex) are a powerful tool used to match patterns in text. They can be used in various programming languages, including Python. In this guide, we'll explore how to use regular expressions in Python to match and manipulate text.

## What are regular expressions?

A regular expression is a sequence of characters that define a search pattern. It's a way to match and manipulate strings based on a certain set of rules. Regular expressions are often used in text editors, command-line utilities, and programming languages to manipulate and search for text.

## Using regular expressions in Python

Python has a built-in module called re that provides support for regular expressions. The re module provides various functions to search and manipulate text using regular expressions.

## Simple matching
Let's start with a simple example. Suppose we have a string and we want to check if it contains the word "hello". We can use the search() function from the re module to do this:

````python
import re

text = "Hello, world!"
pattern = "hello"

if re.search(pattern, text, re.IGNORECASE):
    print("Match found")
else:
    print("Match not found")
````

In the code above, we first import the re module. We then define a 'text' variable that contains the string we want to search. We also define a pattern variable that contains the regular expression we want to match against the text. We use the 'search()' function to search for the pattern in the text. The IGNORECASE flag is used to make the search case-insensitive.

## Matching multiple patterns

Regular expressions can be used to match multiple patterns. For example, suppose we have a string that contains phone numbers in the format (123) 456-7890. We can use regular expressions to extract the phone numbers from the text:

````python
import re

text = "Call me at (123) 456-7890 or (987) 654-3210"
pattern = r"\(\d{3}\) \d{3}-\d{4}"

matches = re.findall(pattern, text)
print(matches)
````

In the code above, we define a regular expression pattern that matches phone numbers in the format (123) 456-7890. We use the 'findall()' function to find all occurrences of the pattern in the text. The matches variable contains a list of all the phone numbers found in the text.

## Replacing text

Regular expressions can also be used to replace text. For example, suppose we have a string that contains the word "color" and we want to replace it with "colour". We can use the sub() function from the re module to do this:

````python
import re

text = "The color of the sky is blue"
pattern = "color"
replacement = "colour"

new_text = re.sub(pattern, replacement, text)
print(new_text)
````

In the code above, we define a regular expression pattern that matches the word "color". We also define a replacement variable that contains the word "colour". We use the sub() function to replace all occurrences of the pattern with the replacement text. The 'new_text' variable contains the updated string.

## Conclusion

Regular expressions are a powerful tool for manipulating and searching text in Python. The re module provides various functions for working with regular expressions. By mastering regular expressions, you can save time and effort when working with text data.
