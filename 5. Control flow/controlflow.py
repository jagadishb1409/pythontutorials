if condition:
    # code to be executed if condition is true
else:
    # code to be executed if condition is false

# for loop example

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

i = 1
while i < 6:
    print(i)
    i += 1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
