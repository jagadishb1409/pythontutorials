my_set = set([1, 2, 3, 4, 5])

my_set = {1, 2, 3, 4, 5}

my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}


my_set.remove(3)
print(my_set)  # {1, 2, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5}


set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  # {1, 2, 3, 4, 5}


set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)  # {3}


set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(intersection_set)  # {3}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)  # {1, 2}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2
print(difference_set)  # {1, 2}

