'''Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries
'''
#1 Create a empty dictonary called dog
dog=dict()
print(dog)
#Create a student dictionary and add first_name,last_name,gender,age,merital status,skills,country,city and address as the keys for the dictonary
student={
    'first_name': 'ABC',
    'last_name':'XYZ',
    'age':25,
    'gender':'Male',
    'merital status':False,
    'skills':['HTML','CSS','JS','Python','SQL'],
    'country':'Banland',
    'city':'Dha',
    'address':{
        'street':'123,beggers street',
        'area':'Dhankhandi'
    }
}
print(student)
#3 Get the length of the student dictionary
print(len(student))
#4 Get the value of skills and check the data type, it should be a list
print(type(student.get('skills')))
#5 Modify the skills values by adding one or two skills
student['skills'].append('CP')
student['skills'].append('DSA')
print(student['skills'])
#6 Get the dictionary keys as a list
keys=student.keys()
print(keys)
#7 Get the dictionary values as a list
values=student.values()
print(values)
#8 Change the dictionary to a list of tuples using items() method
student.items()
print(type(student))
#9 Delete one of the items in the dictionary
print(student.pop('age'))
#10 Delete one of the dictionaries
student2=student.copy()
del student2
print(student)
