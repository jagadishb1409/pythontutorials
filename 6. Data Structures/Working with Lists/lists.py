numbers = [1, 2, 3, 4, 5]
print(numbers)

mixed = [1, "two", 3.0, [4, 5]]
print(mixed)

numbers = list(range(10))
print(numbers)

numbers = [1, 2, 3, 4, 5]
print(numbers[0]) # 1
print(numbers[4]) # 5

numbers = [1, 2, 3, 4, 5]
print(numbers[-1]) # 5
print(numbers[-2]) # 4

numbers = [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.insert(0, 0)
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)

numbers = [1, 2, 3, 4, 5]
print(numbers.pop(2))
print(numbers)

numbers = [5, 3, 4, 1, 2]
numbers.sort()
print(numbers)

numbers = [5, 3, 4, 1, 2]
numbers.sort(reverse=True)
print(numbers)

list = [1, 2, 3, 4, 5]
print(3 in list) # True
print(6 in list) # False

list = [1, 2, 3, 4, 5]
print(3 not in list) # False
print(6 not in list) # True

string = "Hello, World!"
print("Hello" in string) # True
print("hello" in string) # False
print("hello" not in string) # True

list = [1, 2, 3, 4, 5]
list.index(3) # 2

list = [1, 2, 3, 4, 5, 3, 6]
for i, value in enumerate(list):
     if value == 3:
         print(i)
# 2
# 5

