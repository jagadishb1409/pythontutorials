employee_ages = {"John": 35, "Emily": 28, "Tom": 42}

print(employee_ages["Emily"]) # Output: 28

employee_ages["Kate"] = 29

del employee_ages["Tom"]

for name in employee_ages:
    print(name, employee_ages[name])

 for name, age in employee_ages.items():
    print(name, age)

    
my_dict = {
    'fruits': {
        'apples': {
            'red': 3,
            'green': 5,
            'yellow': 1
        },
        'bananas': {
            'green': 2,
            'yellow': 7
        },
        'oranges': {
            'navel': 4,
            'valencia': 6
        }
    },
    'vegetables': {
        'carrots': {
            'orange': 8
        },
        'spinach': {
            'green': 9
        }
    }
}

print(my_dict)

print(my_dict.get('fruits').get('apples').get('green'))

print(my_dict.get('fruits').keys())

print(my_dict.get('fruits').values())

print(my_dict.get('fruits').get('apples').values())

# print spinach green value
print(my_dict.get('vegetables').get('spinach').get('green')) # 9
