
import re

text = "Hello, world!"
pattern = "hello"

if re.search(pattern, text, re.IGNORECASE):
    print("Match found")
else:
    print("Match not found")
    

text = "Call me at (123) 456-7890 or (987) 654-3210"
pattern = r"\(\d{3}\) \d{3}-\d{4}"

matches = re.findall(pattern, text)
print(matches)


text = "The color of the sky is blue"
pattern = "color"
replacement = "colour"

new_text = re.sub(pattern, replacement, text)
print(new_text)
