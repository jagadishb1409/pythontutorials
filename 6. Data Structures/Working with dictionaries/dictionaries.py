employee_ages = {"John": 35, "Emily": 28, "Tom": 42}

print(employee_ages["Emily"]) # Output: 28

employee_ages["Kate"] = 29

del employee_ages["Tom"]

for name in employee_ages:
    print(name, employee_ages[name])

 for name, age in employee_ages.items():
    print(name, age)
