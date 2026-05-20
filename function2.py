#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
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