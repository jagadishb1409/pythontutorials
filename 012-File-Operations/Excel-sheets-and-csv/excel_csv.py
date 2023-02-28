import csv

with open('file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
 




import pandas as pd

df = pd.read_excel('file.xlsx', sheet_name='Sheet1')
print(df)



import pandas as pd

df = pd.read_csv('file.csv')
print(df)


