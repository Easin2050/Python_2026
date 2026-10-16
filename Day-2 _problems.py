''' Declare your age as integer variable
Declare your height as a float variable
Declare a variable that store a complex number
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9.
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
There is no 'on' in both dragon and python
Find the length of the text python and convert the value to float and convert it to string
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10
Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125 '''

# x=int(input('Enter a your age: '))
# print(x)
# y=float(input('Enter your height: '))
# print(f'Your height is {y:.2}')
# complex_input=3 + 4j
# print('The complex number is: ',complex_input)
# base = float(input('Enter the base: '))
# height = float(input('Enter the height: '))
# area = 0.5 * base * height
# print(f'The area of the triangle is {area:g}')

# a=int(input("Enter a:"))
# b=int(input('Enter b:'))
# c=int(input('Enter c:'))
# print('The perameter of triangle is:',a+b+c)

# length = float(input('Enter the length: '))
# width = float(input('Enter the width: '))

# area = length * width
# perimeter = 2 * (length + width)

# print(f'The area of the rectangle is {area:g}')
# print(f'The perimeter of the rectangle is {perimeter:g}')

# import math

# r = float(input('Enter the radius: '))

# area = math.pi * r ** 2
# circumference = 2 * math.pi * r

# print(f'Area: {area:.2f}')
# print(f'Circumference: {circumference:.2f}')

import math

# x1, y1 = 2, 2
# x2, y2 = 6, 10

# slope = (y2 - y1) / (x2 - x1)
# distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# print('Slope:', slope)
# print(f'Euclidean distance: {distance:.2f}')

# for x in range(-10, 11):
#     y = x ** 2 + 6 * x + 9

#     if y == 0:
#         print('x:', x)
#         break

# if(len('dragon')!=len('python')):
#     print('True')
# else:
#     print('False')

# if 'on' in 'python' and 'on' in 'dragon':
#     print('True')
# else:
#     print('False')

# sentence='I hope this course is not full of jargon'
# if 'jargon' in sentence:
#     print('True')
# else:
#     print('False') 

# if 'on' not in 'dragon' and 'on' not in 'python':
#     print('True')
# else:
#     print('False')

# length = len('python')
# length_float = float(length)
# length_string = str(length_float)

# print(length_float)
# print(length_string)

# num=int(input("Enter the number:"))
# if num%2==0:
#     print('Even number')
# else:
#     print('Odd number')

# if(3//2)==int(2.7):
#     print('True')
# else:
#     print('False')

# if type('10')==type(10):
#     print('True')
# else:
#     print('False')

# print(int(float('9.8')) == 10)


# hours=input('Enter hours:')
# rate=input('Enter rate:')
# print(f'Your weekly earning is {int(hours)*int(rate)}')

# years=int(input('Enter number of years you have lived:'))
# print(f'You have lived for {years*365*24*60*60} seconds')

# for i in range(1, 6):
#     print(i, 1, i, i ** 2, i ** 3)