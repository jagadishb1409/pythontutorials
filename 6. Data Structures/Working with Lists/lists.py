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
