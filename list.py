
"""
Declare an empty list

Declare a list with more than 5 items

Find the length of your list

Get the first item, the middle item and the last item of the list

Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

Print the list using print()

Print the number of companies in the list

Print the first, middle and last company

Print the list after modifying one of the companies

Add an IT company to it_companies

Insert an IT company in the middle of the companies list

Change one of the it_companies names to uppercase (IBM excluded!)

Join the it_companies with a string '#;  '

Check if a certain company exists in the it_companies list.

Sort the list using sort() method

Reverse the list in descending order using reverse() method

Slice out the first 3 companies from the list

Slice out the last 3 companies from the list

Slice out the middle IT company or companies from the list

Remove the first IT company from the list

Remove the middle IT company or companies from the list

Remove the last IT company from the list

Remove all IT companies from the list

Destroy the IT companies list

Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

Exercises: Level 2
The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Sort the list and find the min and max age
Add the min age and the max age again to the list
Find the median age (one middle item or two middle items divided by two)
Find the average age (sum of all items divided by their number )
Find the range of the ages (max minus min)
Compare the value of (min - average) and (max - average), use abs() method
Find the middle country(ies) in the countries list
Divide the countries list into two equal lists if it is even if not one more country for the first half.
['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic coutries"""

# Declare an empty list
empty_list=[]

#2 Declare a list with more than 5 items
empty_list=[1,2,3,4,5,6]
#3 Find the length of your list
print(len(empty_list))
#4 Get the first item, the middle item and the last item of the list
print(empty_list[0])
print(empty_list[len(empty_list)//2])
print(empty_list[-1])

#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
user_info=['John',30,5.6,'single','abc street,Dhaka']
print(user_info)
#6 Declare a list variable named it_companies and assign inital values Facebook,Google,Microsoft,Apple,IBM,Oracle and Amazon
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#7 Print the list using print()
print(it_companies)
#8 Print the number of companies in the list
print(len(it_companies))
#9 Print the first, middle and last company

print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

#10 Print the list after modifying one of the companies
it_companies[0]='Meta'
print(it_companies)
#11 Add an IT company to it_companies
it_companies.append('Tesla')
print(it_companies)

#12 Insert an IT company in the middle of the companies list
middle_index=len(it_companies)//2
it_companies.insert(middle_index,'Samsung')
print(it_companies)
#13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[4]=it_companies[4].upper()
print(it_companies)

#14 Join the it_companies with a string '#;  '
for company in it_companies:
    print(company,end='#;  ')
print()

#15 Check a certain company is there in the it_companies list
print('Meta' in it_companies)
#16 Sort the list using sort() method
print(sorted(it_companies))
#17 Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)
#18 Slice out the first 3 companies from the list
print(it_companies[:3])
#19 Slice out the last 3 companies from the list
print(it_companies[-3:])
#20 Slice out the middle IT company or companies from the list
middle_index=len(it_companies)//2
print(it_companies[middle_index])
#21 Remove the first IT company from the list
del it_companies[0]
print(it_companies)
#22 Remove the middle IT company or companies from the list
del it_companies[middle_index]
print(it_companies)
#23 Remove the last IT company from the list
del it_companies[-1]
print(it_companies)
#24 Remove all IT companies from the list
it_companies.clear()
print(it_companies)
#25 Destroy the IT companies list
it_companies=[]
print(it_companies)
#26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack=front_end+back_end
print(full_stack)
#27 After joining the lists in question 26. Copy the joined list and assign it to
# a variable full_stack, then insert Python and SQL after Redux.
full_stack=front_end+back_end
index_of_redux=full_stack.index('Redux')
full_stack.insert(index_of_redux+1,'Python')
full_stack.insert(index_of_redux+2,'SQL')
print(full_stack)

#Practice Day-2
#1 The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#2 Sort the list and find the min and max age
ages_sorted=sorted(ages)
print(ages_sorted[0])
print(ages_sorted[-1])
#3 Add the min age and the max age again to the list
ages.append(ages_sorted[0])
ages.append(ages_sorted[-1])
print(ages)
#4 Find the median age (one middle item or two middle items divided by two)
ages_sorted=sorted(ages)
n=len(ages_sorted)
if n%2==0:
    median=(ages_sorted[n//2-1]+ages_sorted[n//2])/2
else:    median=ages_sorted[n//2]
print(median)
#5 Find the average age (sum of all items divided by their number )
average=sum(ages)/len(ages)
print(average)
#6 Find the range of the ages (max minus min)
age_range=ages_sorted[-1]-ages_sorted[0]    
print(age_range)
#7 Compare the value of (min - average) and (max - average), use abs() method
min_average_diff=abs(ages_sorted[0]-average)
max_average_diff=abs(ages_sorted[-1]-average)
print(min_average_diff)
print(max_average_diff)
#8 Find the middle country(ies) in the countries list
countries=['China','Pakistan','Bangladesh','Russia','Japan','Finland','USA']
n=len(countries)
if n%2==0:
    middle_countries=countries[n//2-1:n//2+1]
else:
    middle_countries=[countries[n//2]]
print(middle_countries)

#9 Divide the countries list into two equal lists if it is even if not one more country for the first half.
n=len(countries)
if n%2==0:
    first_half=countries[0:n//2]
    second_half=countries[n//2:]
else:
    first_half=countries[0:(n//2)+1]
    second_half=countries[(n//2)+1:]
print(first_half)
print(second_half)
#10 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic coutries
countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
a,b,c,*scandic=countries
print(f'{a},{b},{c}')
print(scandic)


