# Exercises: Day 8
# Create an empty dictionary called dog
dog=dict()
print(dog)
# Add name, color, breed, legs, age to the dog dictionary
'''dog['name']='Tom'
dog['color']='Brown'
dog['breed']='Foreign'
dog['legs']=4
dog['age']=2
print(dog)'''
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={
    'first_name':'Imran',
    'last_name':'Khan',
    'gender':'male',
    'age':25,
    'marital_status':'No',
    'skills':['HTML','CSS','JS','C','C++'],
    'country':'Bangladesh',
    'city':'Dhaka',
    'address':{
        'House_no':'51/A',
        'Road':'Al-Madina len',
        'Area':'Dhanmondi'
    }
}
print(student)
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
skill=student['skills']
print(skill)
print(type(skill))
# Modify the skills values by adding one or two skills
new_skills=['CP','AI']
student['skills'].extend(new_skills)
print(student)
# Get the dictionary keys as a list
keys=student.keys()
print(keys)
# Get the dictionary values as a list
value=student.values()
print(value)
# Change the dictionary to a list of tuples using items() method
item=student.items()
item_tuple=tuple(item)
print(item_tuple)
# Delete one of the items in the dictionary
del student['last_name']
print(student)
# Delete one of the dictionaries
del dog
