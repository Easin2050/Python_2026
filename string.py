'''
Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
Declare a variable named company and assign it to an initial value "Coding For All".
Print the variable company using print().
Print the length of the company string using len() method and print().
Change all the characters to uppercase letters using upper() method.
Change all the characters to lowercase letters using lower() method.
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
Cut(slice) out the first word of Coding For All string.
Check if Coding For All string contains a word Coding using the method index, find or other methods.
Replace the word coding in the string 'Coding For All' to Python.
Change "Python for Everyone" to "Python for All" using the replace method or other methods.
Split the string 'Coding For All' using space as the separator (split()) .
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
What is the character at index 0 in the string Coding For All.
What is the last index of the string Coding For All.
What character is at index 10 in "Coding For All" string.
Create an acronym or an abbreviation for the name 'Python For Everyone'.
Create an acronym or an abbreviation for the name 'Coding For All'.
Use index to determine the position of the first occurrence of C in Coding For All.
Use index to determine the position of the first occurrence of F in Coding For All.
Use rfind to determine the position of the last occurrence of l in Coding For All People.
Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Does 'Coding For All' start with a substring Coding?
Does 'Coding For All' end with a substring coding?
'   Coding For All      '  , remove the left and right trailing spaces in the given string.
Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144

#1 Concate of string
s1='Thirty'
s2='Days'
s3='of'
s4='Python'
sentence=s1+' '+s2+' '+s3+' '+s4
print(sentence)

#2 Concate of string
s1='Coding'
s2='For'
s3='All'
sentence=s1+' '+s2+' '+s3
print(sentence)'''

#3 Declare a variable named company and assign it to an initial value "Coding For All".
company='Coding For All'
#4 Print the variable company using print().
print(company)

#5 Print the length of the company string using len() method and print().
print(len(company))

#6 Change all the characters to uppercase letters using upper() method.
print(company.upper())
#7 Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9 Cut(slice) out the first word of Coding For All string.
print(company[6:])

#10 Check coding is there or not
print(company.find('Coding'))

sub_string='Coding'
print(company.index(sub_string))

#11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))

#12 Change "Python for Everyone" to "Python for All" using the replace method or other methods.
sentence='Python for Everyone'
print(sentence.replace('Everyone','All'))

#13 Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' '))

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

string2='Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon'
string_split=string2.split(',')
print(string_split)

#15 What is the character at index 0 in the string Coding For All.
print(company[0])

#16 What is the last index of the string Coding For All.
print(len(company)-1)

#17 What character is at index 10 in "Coding For All" string.
print(company[10])

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.

string3='Python For Everyone'
acronym=''
for word in string3.split(' '):
    acronym+=word[0]
print(acronym)

#19 Create an acronym or an abbreviation for the name 'Coding For All'.

short=''
for word in company.split(' '):
    short+=word[0]
print(short)

#20 Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

#21 Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence2='You cannot end a sentence with because because because is a conjunction'
print(sentence2.find('because'))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence2.rindex('because'))

 