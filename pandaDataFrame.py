'''
Notes:

Indexing: colons (:) are for consecutive 
          commas (,) are for separate, but you must use brackets [',']

'''

import pandas as pd

grades_dict = {'Wally':[87,96,70], 
                'Eva':[100,87,90], 
                'Sam':[94,77,90], 
                'Katie':[100,81,82], 
                'Bob':[83,65,85]}
                #5 columns, 3 rows 
                #KEYS ARE COLUMNS HEADERS, VALUES ARE ROWS 

grades = pd.DataFrame(grades_dict)

#adds row headers: 
grades.index = ['Test1', 'Test2', 'Test3']
'''
print(grades, '\n')

print("Eva's Grades:")
print(grades['Eva'], '\n')

print("Sam's Grades:")
print(grades.Sam, '\n')
'''


#USING LOC AND ILOC METHODS
    #loc uses custome indexes (strings you made in your dictionary)
    #iloc is for integers

'''
print()
print(grades.loc['Test2'])
#same as:
print()
print(grades.iloc[1])
'''

#For consecutive rows:
print(grades.loc['Test 1':'Test3'])
#same as
print(grades.iloc[0:3])


#for non-consecutive rows:
print(grades.loc[['Test1', 'Test3']])
print(grades.iloc[[0,2]])

#first give rows you want, then columns:
print(grades.loc['Test1':'Test2',['Eva','Katie']])

print(grades.loc[['Test1','Test3'], 'Sam':'Bob'])

#DON'T NEED BRACKETS FOR CONSECUTIVE   


grades_A = grades[grades>=90]

#will print grades over 90 and replaces less than values with NaN (not a number)
print(grades_A)


grades_B = [(grades>=80) & (grades<90)]
print(grades_B)

# | is or
grades_A_or_B = [(grades>=90) | (grades>=80)]
print(grades_A_or_B)


pd.set_option('precision',2)
#describes by column (by each student)
print(grades.describe())

#describes by row (by each test) because you Transpose it
print(grades.T.describe())


#sorts in descending order
print(grades.sort_index(ascending=False))

#sorts column indexes in alphabetical order
print(grades.sort_index(axis=1))
print(grades.sort_index(axis=1, ascending=False))

#sorts by highest grades in Test1, sorted in columns though 
print(grades.sort_values(by='Test1', axis=1, ascending=False))

#just switches rows and columns; make sure to take out axis 
print(grades.T.sort_values(by='Test1', ascending=False))

print()
#just shows column 1
print(grades.loc['Test1'].sort_values(ascending=False))