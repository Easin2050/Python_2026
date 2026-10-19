'''Exercises - Day 4
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
8 ** 6 = 262144 '''

# a='Thirty'
# b='Days'
# c='Of'
# d='Python'
# space=" "
# print(a+space+b+space+c+space+d)

# a='Coding'
# b='For'
# c='All'
# space=" "
# print(a+space+b+space+c)
company='Coding For All'
# print(company)
# print(len(company))
# print(str.upper(company))
# print(str.lower(company))
# print(str.capitalize(company))
# print(str.title(company))
# print(str.swapcase(company))
# print(company[:6])
# sub_string='Coding'
# print(company.find(sub_string))
# print(company.index(sub_string))
# print(company.replace('Coding','Python'))
# sentence='Python For Everyone'
# print(sentence.replace('Everyone','All'))

# sentence = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# print(sentence.split(', '))

# print(company[0])
# index=len(company)
# print(company[index-1])
# print(company[-1])

# sentence = "Python For Everyone"
# sub_string = ''

# for cap in sentence:
#     if cap.isupper():
#         sub_string = sub_string + cap

# print(sub_string)

# sentence = "Coding For All"
# sub_string = ''

# for cap in sentence:
#     if cap.isupper():
#         sub_string = sub_string + cap

# print(sub_string)

# print(company.find('C'))
# print(company.find('F'))
# print(company.rfind('l'))

# sentence = 'You cannot end a sentence with because because because is a conjunction'

# start = sentence.index('because')
# end = sentence.index(' is a conjunction')

# result = sentence[start:end]

# print(result)

# print(company.startswith('Coding'))
# print(company.endswith('coding'))
# sentence='   Coding For All      '
# print(sentence.strip(''))

# s1='30DaysOfPython'
# s2='thirty_days_of_python'
# a=s1.isidentifier()
# b=s2.isidentifier()
# print(a)
# print(b)

# list=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# result='# '.join(list)
# print(result)

# print("I am enjoying this challenge.\nI just wonder what is next.")

# print('Name\tAge\tCountry\tCity')
# print("Asabeneh\t250\tFinland\tHelsinki")

# import math
# r=10
# print('Radius = {}'.format(r))
# # area = 3.14 * radius ** 2
# print('area = {} * {} ** {}'.format(3.14,r,2))
# print('The area of a circle with radius {} is {} meters square.'.format(r,3.14 * r ** 2))

# a = 8
# b = 6

# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a, b, a - b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} / {} = {:.2f}'.format(a, b, a / b)) 
# print('{} % {} = {}'.format(a, b, a % b))
# print('{} // {} = {}'.format(a, b, a // b))
# print('{} ** {} = {}'.format(a, b, a ** b))

# My word game

import random

wordlist = [
    "python", "developer", "keyboard", "Coffee", "gadget",
    "creative", "30days", "Bangladesh", "Salary",
    "programming", "software", "computer", "laptop", "mouse",
    "monitor", "internet", "technology", "artificial", "intelligence",
    "student", "teacher", "university", "scholarship", "education",
    "learning", "practice", "project", "database", "website",
    "application", "framework", "Django", "JavaScript", "HTML",
    "CSS", "algorithm", "function", "variable", "string",
    "engineer", "career", "interview", "company",
    "office", "manager", "communication", "problem", "solution"
]

random_word = random.choice(wordlist)

print("Welcome to the Word Guessing Game!")
print("You have 10 attempts to guess the secret word.")
print("You have 5 hints available from your friends.")
print("Let's start!\n")

print("Friend Name\tAge")
print("Abir\t\t25")
print("Sakib\t\t27")
print("Imran\t\t20")
print("Nokib\t\t26")
print("Fahad\t\t34")

count = 10
hint = 5
attempt = 0
won = False

while count > 0:

    picked_word = input("\nWrite your word: ").strip()
    count -= 1
    attempt += 1

    if picked_word.lower() == random_word.lower():
        print(f"Congratulations! You guessed the word in {attempt} attempts.")
        won = True
        break

    print(f"Wrong guess! Attempts left: {count}")
    want_hint = input("Do you need a hint? (yes/no): ").strip().lower()

    if want_hint == "yes":

        if hint <= 0:
            print("You do not have any hints left!")
            continue

        user_input = input("Friend name: ").strip().lower()
        user_age = input("Friend age: ").strip()

        if user_input == "abir" and user_age == "25":
            print(f"The length of the word is: {len(random_word)}")

        elif user_input == "sakib" and user_age == "27":
            vowels = 0

            for char in random_word.lower():
                if char in "aeiou":
                    vowels += 1

            print(f"The number of vowels is: {vowels}")

        elif user_input == "imran" and user_age == "20":
            middle_index = len(random_word) // 2
            print(f"The middle character is: {random_word[middle_index]}")

        elif user_input == "nokib" and user_age == "26":
            print(f"The word ends with: {random_word[-1]}")

        elif user_input == "fahad" and user_age == "34":
            print(f"The word reversed is: {random_word[::-1]}")

        else:
            print("Invalid friend name or age.")
            continue

        hint -= 1
        print(f"Hints remaining: {hint}")

    elif want_hint == "no":
        print("Okay, continue guessing!")

    else:
        print("Please enter yes or no.")

if won:
    print("\nYou won the game!")
else:
    print(f"\nGame over! The correct word was: {random_word}")
