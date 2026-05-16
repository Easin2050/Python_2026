'''
Exercises: Level 1
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3
Exercises: Level 2
Write a code which gives grade to students according to theirs scores:
```sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
```
Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
The following list contains some fruits:
```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
Exercises: Level 3
Here we have a person dictionary. Feel free to modify it!
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
  Asabeneh Yetayeh lives in Finland. He is married.
  '''
#1 Exercises: Level 1
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:


'''age=int(input('Enter your age:'))
if age>=18:
    print('You are old enough to learn to drive')
else:
    print(f'You need {18-age} more years to learn to drive')

'''
'''
age=int(input("Give your age: "))
print('You are old enough to learn to drive') if age>18 else print(f'You need {18-age} more years to learn to drive')

#3 
a=int(input("Enter a: "))
b=int(input("Enter b: "))

if a>b:
    print(f'a greater than b')
elif a==b:
    print('Same')
else:
    print(f'b greater than a')

#2
my_age=int(input("Enter my age: "))
your_age=int(input("Enter your age: "))

if my_age>your_age:
    print(f'My age is {my_age-your_age} years greater than yours')
elif my_age==your_age:
    print('Your age is same as mine')
else:
    print(f'Your age is {your_age-my_age} years greater than mine')

#Exercise 2
#2 Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month=input("Enter the month: ")
if(month=='September'or month=='October'or month=='November'):
    print('Autumn')
elif(month=='December'or month=='January'or month=='February'):
    print('Winter')
elif(month=='March' or month=='April' or month=='May'):
    print('Spring')
else:
    print('Summer')

#3 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=input('Enter a fruit name:')
if fruit in fruits:
    print('The fruit is already in the list')
else:
    fruits.append(fruit)
    print(fruits)'''

#Exercise-3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python','SQL','DSA','CP'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#1
is_skill=person.get('skills')
print(bool(is_skill))
if bool(is_skill):
    n=len(person['skills'])
    if n%2==0:
        print(f'{person['skills'][int(n/2)-1]},{person['skills'][int(n/2)]}')
    else:
        print(person['skills'][int(n/2)])
else:
    print('Skills is not available')

#2
print('Python' in person['skills'])


