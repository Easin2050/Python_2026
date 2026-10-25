# Exercises: Day 9
# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
'''age=int(input('Enter your age:'))
print('You are old enough to learn to drive') if age>=18 else print(f'You need {18-age} to learn to drive')'''
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
'''a=int(input('Enter your age of a:'))
b=int(input('Enter your age of b:'))
if a==b:
    print ('{} is equal {}'.format(a,b))
elif a>b:
    print('{} is greater than {}'.format(a,b))
else:
    print('{} is greater than {}'.format(b,a))'''
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ``` As i am learning fast i won't do it because i have done it once and it is easy.
# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
'''month=input('Enter the month:')
month=month.capitalize()
list=['September','October','November']
list2=['December', 'January', 'February']
list3=['March','April','May']
# list4=['June','July','August']

if month in list:
    print('Autumn')
elif month in list2:
    print('Winter')
elif month in list3:
    print('Spring')
else:
    print('Summer')'''

# The following list contains some fruits:
# ```sh
# fruits = ['banana', 'orange', 'mango', 'lemon']
# ```
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
'''fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=input('Enter the fruit name:')
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
print(fruits)'''
# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
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
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skill = person['skills']
    middle = len(skill) // 2
    if len(skill) % 2 != 0:
        print(skill[middle])
    else:
        print(skill[middle - 1], skill[middle])
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'Python' in skill:
    print('Yes')
else:
    print('No')
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'React' in skill and 'Node' in skill and 'MongoDB' in skill:
    print('He is a fullstack developer')

elif 'JavaScript' in skill and 'React' in skill:
    print('He is a frontend developer')

elif 'Node' in skill and 'Python' in skill and 'MongoDB' in skill:
    print('He is a backend developer')

else:
    print('Unknown')
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
if person['country']=='Finland' and person['is_married']==True:
    print('{} {} lives in Finland and He is married'.format(person['first_name'],person['last_name']))
else:
    print('Unknown')
