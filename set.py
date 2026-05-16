'''
Exercises: Level 1
Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard
Exercises: Level 2
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely
Exercises: Level 3
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.'''

#Exercises: Level 1
#Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Netflix', 'Airbnb'])
print(it_companies)
#Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies)
#Exercises: Level 2
#1Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))
#Find A intersection B
print(A.intersection(B))
#Is A subset of B
print(A.issubset(B))
#Are A and B disjoint sets
print(A.isdisjoint(B))
#Join A with B and B with A
A=A.union(B)
B=B.union(A)
print(A)
print(B)
#What is the symmetric difference between A and B
print(A.symmetric_difference(B))
#Delete the sets completely
del A
#Exercises: Level 3
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set=set(ages)
print(len(ages))
print(len(ages_set))
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.'''
sentence='I am a techer and I love to inspire and teach people'
unique_word=set(sentence.split(' '))
print(unique_word)

