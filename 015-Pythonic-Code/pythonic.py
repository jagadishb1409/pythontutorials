
# Non-Pythonic
squares = []
for i in range(10):
    squares.append(i**2)

# Pythonic
squares = [i**2 for i in range(10)]


# Non-Pythonic
s = 'Hello, World!'
result = ''
for i in range(len(s)):
    if i % 2 == 0:
        result += s[i]

# Pythonic
s = 'Hello, World!'
result = s[::2]


# Non-Pythonic
f = open('file.txt', 'r')
try:
    data = f.read()
finally:
    f.close()

# Pythonic
with open('file.txt', 'r') as f:
    data = f.read()
    
    
# Non-Pythonic
names = ['Alice', 'Bob', 'Charlie']
for i in range(len(names)):
    print(i, names[i])

# Pythonic
names = ['Alice', 'Bob', 'Charlie']
for i, name in enumerate(names):
    print(i, name)
    
# Non-Pythonic
def add(a, b):
    if b is None:
        b = 0
    return a + b

# Pythonic
def add(a, b=0):
    return a + b
