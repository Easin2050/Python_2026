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

import math

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
print('The roots are {roots[0]} and {roots[1]}')