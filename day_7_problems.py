it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Exercises: Level 1
# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# Insert multiple IT companies at once to the set it_companies
new_it_companies=['Tesla','Oracole']
it_companies.update(new_it_companies)
print(it_companies)
# Remove one of the companies from the set it_companies
# it_companies.remove('Facebook')
it_companies.pop()
print(it_companies)
# What is the difference between remove and discard
it_companies.remove('Apple')
it_companies.discard('Google')
print(it_companies)
# Exercises: Level 2
# Join A and B
C=A.union(B)
print(C)
'''C=A.update(B)
print(C)'''
# Find A intersection B
print(A.intersection(B))
# Is A subset of B
print(A.issubset(B))
# Are A and B disjoint sets
print(A.isdisjoint(B))
# Join A with B and B with A
C=A.union(B)
D=B.union(A)
print(C)
print(D)
# What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# Delete the sets completely
del(A)
del(B)
# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
l=len(age)
age=set(age)
set_l=(len(age))
if l>set_l:
    print('List length greater than set list')
else:
    print('Set length greater than list length')
l = len(age)
age_set = set(age)
set_l = len(age_set)

if l > set_l:
    print('List length is greater than set length')
elif l < set_l:
    print('Set length is greater than list length')
else:
    print('Both lengths are equal')

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split()
unique_words = set(words)

print(unique_words)
print(len(unique_words))