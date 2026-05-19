'''language='Python'
for p in language:
    if p=='y':
        continue
    print(p)

language='Python'
for i in range(len(language)):
    print(language[i])

numbers=(1,2,3,4,5,6)
for number in numbers:
    print(number,end=' ')

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)

for key,value in person.items():
    print(key,value)

it_companies={'Facebook','Google','Microsoft','IBM','Apple'}
for company in it_companies:
    print(company)

numbers=(1,2,3,4,5,6)
for number in numbers:
    print(number)
    if number==3:
        break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')


lst=list(range(11))
print(lst)

st=set(range(1,11))
print(st)'''

'''
Exercises: Level 1
Iterate 0 to 10 using for loop, do the same using while loop.

Iterate 10 to 0 using for loop, do the same using while loop.

Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

Use for loop to iterate from 0 to 100 and print only even numbers

Use for loop to iterate from 0 to 100 and print only odd numbers

Exercises: Level 2
Use for loop to iterate from 0 to 100 and print the sum of all numbers.
The sum of all numbers is 5050.
Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

The sum of all evens is 2550. And the sum of all odds is 2500.
Exercises: Level 3
Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
Go to the data folder and use the countries_data.py file.
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world
'''

#1 
for i in range(0,11,1):
    print(i,end=',')

print()

#2
i=10
while(i>=0):
    print(i,end=',')
    i=i-1
print()
#4
rows=int(input('Enter the raw:'))
cols=int(input('Enter the col:'))
for i in range(rows):
    for j in range(cols):
        print('#',end='')
    print()

#3 
row=int(input('Enter the raws:'))
col=int(input('Enter the cols:'))
for i in range(row+1):
    for j in range(i):
        print('#',end='')
    print()

#5
for i in range(11):
    print(f'{i}x{i}={i*i}')
print()