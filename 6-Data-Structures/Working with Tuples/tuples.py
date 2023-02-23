my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# output: (1, 2, 3, 4, 5)

my_tuple = (1, 2, 3, 4, 5)
print("The first element of the tuple:", my_tuple[0])

Copy code
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
  print(item)
# output
# 1
# 2
# 3
# 4
# 5

my_tuple = (1, 2, 3, 4, 5)
if 3 in my_tuple:
  print("The value 3 exists in the tuple.")

my_tuple = (1, 2, 3, 4, 5, 3)
print("The number of occurrences of the value 3 in the tuple:", my_tuple.count(3))

my_tuple = (1, 2, 3, 4, 5)
print("The index of the value 3 in the tuple:", my_tuple.index(3))

my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple + (6, 7, 8)
print("The concatenated tuple:", new_tuple)
