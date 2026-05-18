'''language='Python'
for p in language:
    if p=='y':
        continue
    print(p)'''

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
print(st)