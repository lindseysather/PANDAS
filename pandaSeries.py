
'''
Notes:

- pandas Series: 1 dimensional array (1 column with lots of rows)
- pandas DataFrame: 2 dimensional array (columns and rows)

- can ignore missing values

- when printing panda, also shows datatype 

- DESCRIBE method prints all aggregate functions of array (mean, max, min, etc)

- Can use string indexing (grades = pd.Series)

- Can also use dictionaries
    - Keys become index values
'''

import pandas as pd
print() 
print()

grades = pd.Series([87,100,94])

'''print(grades)'''

grades2 = pd.Series(98.6, range(3))

#print(grades2)

#print first number in grades
'''print(grades[0])'''

#shows all aggregate functions of array (avg, std, etc)
'''print(grades.describe())'''

grades = pd.Series([87,100,94], index=['Wally', 'Eva', 'Sam'])
#is the same as:
grades = pd.Series({'Wally':87, 'Eva':100, 'Sam':94})

'''
print()
print(grades)

print('\nEva Grade:')
print(grades['Eva'])

print('\nWally Grade:')
print(grades.Wally)

print()
#prints datatype:
print(grades.dtype)

#prints values:
    #will return NumPy array 
print(grades.values)
'''

hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])
#hardware is a Series object - can use string method

#tells which word has an a:
print(hardware.str.contains('a'))

print(hardware.str.upper())

#if you have string values within you series, you can use string methods


print()
print()
print()