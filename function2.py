'''#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def sum_all_nums(a,b):
    return a+b

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
print(sum_all_nums(num1,num2))

#2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

import math

pie=math.pi
def area(r):
    return pie*r**2
print(f'Area of the circle:{area(5):.2f}')

#3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# Temperature in °C can be converted to °F using this formula: 

def add_all_numbers(*args):
    total=0
    for i in args:
        if type(i)!=int and type(i)!=float:
            return 'Not all elements are numbers'        
        total+=i
    return total

print(add_all_numbers(1,3,5,7,2.35,10))

#4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def celcius_to_fahrenheit(c):
    f=(c*9/5)+32
    return f

print(f'C to F:{celcius_to_fahrenheit(6):.2f}')'''

#5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

'''def check_season(month):
    if(month=='September'or month=='October'or month=='November'):
        return ('Autumn')
    elif(month=='December'or month=='January'or month=='February'):
        return ('Winter')
    elif(month=='March' or month=='April' or month=='May'):
        return ('Spring')
    else:
        return ('Summer')

month=input("Enter the month:")
print(check_season(month))'''

# Write a function called calculate_slope which return the slope of a linear equation

'''def calculate_slope(x1,x2,y1,y2):
    slope=(y2-y1)/(x2-x1)
    return f'{slope:.2f}'

a,b,c,d=input("Enter the four values: ").split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
print(calculate_slope(a,b,c,d))'''

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

'''import math

def quadratic_equation(a,b,c):
    d=(b**2)-4*a*c

    sol1=-b+math.sqrt(d)
    sol2=-b-math.sqrt(d)

    return sol1,sol2

a,b,c=input("Enter the values: ").split(',')
a=int(a)
b=int(b)
c=int(c)
roots=quadratic_equation(a,b,c)
print('The roots are {roots[0]} and {roots[1]}')'''

#8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

'''def list_print(list_values):
    for items in list_values:
        print(items,end=',')

list_values=('Enter the values using comma: ').split(',')
list_print(list_values)'''

#9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

'''def list_print(list_values):
    new_list = []
    n = len(list_values)

    for i in range(n - 1, -1, -1):
        new_list.append(list_values[i])

    return new_list


list_values = input("Enter the values using comma: ").split(',')
print(list_print(list_values))'''

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

'''def capitalize_list_items(user_list):
    cap_list=[]
    for items in user_list:
        after_cap=items.capitalize()
        cap_list.append(after_cap)
    return(cap_list)

user_list = input("Enter items separated by spaces: ").split(',')
print(capitalize_list_items(user_list))'''

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

'''def add_items(user_list,element):
    list=[]
    for items in user_list:
        list.append(items)
    list.insert(len(user_list),element)

    return list
user_list = input("Enter items separated by spaces: ").split(',')
element=input('Enter the element to add: ')
print(add_items(user_list,element))'''

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

'''def remove_item(user_list,element):
    user_list.remove(element)
    return user_list


user_list = input("Enter items separated by spaces: ").split(',')
element=input('Enter the perameter to remove: ')

if element not in user_list:
    print('The element not in the list.')
else:
    print(remove_item(user_list,element))'''

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

'''def sum_of_numbers(number):
    sum=0
    for i in range(number):
        sum=sum+i
    return sum

print(sum_of_numbers(5))'''

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

'''def sum_of_odds(r):
    sum=0
    for i in range(r):
        if i%2!=0:
            sum=sum+i

    return sum

num=input('Enter the number perameter: ')
print(sum_of_odds(int(num)))'''

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(r):
    sum=0
    for i in range(r):
        if i%2==0:
            sum=sum+i

    return sum

num=input('Enter the number perameter: ')
print(sum_of_even(int(num)))