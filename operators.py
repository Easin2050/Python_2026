import cmath
'''
#1
age=int(input("Enter your age:"))
#2
height=float(input("Enter your height:"))
#3
complex_number=(3+4j)
#4
number=complex(input("Enter a complex number:"))
#5 Area of a triangle
base=int(input("Enter the base:"))
height=int(input("Enter the height:"))
print(f"The area of the triangle is {int(0.5*base*height)}")
#6 Perimeter of triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

perimeter = a + b + b + c  
semi_perimeter = (a + b + c) / 2

print(f"The perimeter of the triangle is {perimeter:.2f}")
print(f"The semi-perimeter of the triangle is {semi_perimeter:.2f}")

#7 Area of a triangle
lenght=int(input("Enter the length:"))
width=int(input("Enter the width:"))

print(f"The area of the triangle is {lenght*width}")
print(f"The perimeter of the triangle is {2*(lenght+width)}")

#8 Radius of the circle
r=float(input("Enter the radius of the circle:"))
print(f"The radius of the circle is {3.14*r**2}")

#9 Slope of the line
x=float(input("Enter the x coordinate of the first point:"))
y=(2*x)-2
print(f"The y coordinate of the first point is {y}")

x1=int(input("Enter x1:"))
x2=int(input("Enter x2:"))
y1=int(input("Enter y1:"))
y2=int(input("Enter y2:"))

slope=(y2-y1)/(x2-x1)
print(f"The slope of the line is {slope}")

#10 Compare of the slopes in tasks 8 and 9
if y<slope:
    print("The slope of the line in task 8 is less than the slope of the line in task 9.")
elif(slope>y):
    print("The slope of the line in task 8 is greater thn the slope of the line in task 9.")
else:
    print("The slope of the line in task 8 is equal to the slope of the line in task 9.")

#11 Find the value of x
a = 1
b = 6
c = 9

d = b*b - 4*a*c

if d == 0:
    x = -b / (2*a)
    print(f"The value of x is {x}")

#12 Find the length of strings

print(len("python")==len("dragon"))

#13 Check on in python
print('on' in 'python' and 'on' in 'dragon')

#14 Use of in

print('jargon' in 'I hope this course is not full of jargon')

#15 
print('on' not in 'python' and 'on' not in 'dragon')

#16
length_of_word=len('python')
x=float(length_of_word)
y=str(x)
print(f'x,y = {x},{y}')

#17 even or odd
number=int(input("Enter a number:"))
if(number%2==0):
    print(f"{number} is an even number.")

#18

if(7//3==int(2.7)):
    print("True")

#19
print(type('10')==type(10))

#20
print(int(9.8)==10)
#21

hours=int(input("Enter hours:"))
rate=int(input("Enter rate per hour:"))
print("Your weekly earning is",hours*rate)

#22
year=input("Enter a year:")
print(f"You have lived for {year*60*60*24*365} seconds.")'''

#23
print(f'1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125')






