# 💻 Exercises: Day 5
# Exercises: Level 1

# Declare an empty list
input_list = list()
print(input_list)

# Declare a list with more than 5 items
my_list = ['CSS', 'Python', 'HTML', 'AI', 'Tech']

# Find the length of your list
print(len(my_list))
print(my_list)

# Get the first item, the middle item and the last item
print(my_list[0])
middle = len(my_list) // 2

if len(my_list) % 2 != 0:
    print(my_list[middle])
else:
    print(my_list[middle - 1], my_list[middle])

print(my_list[-1])

# Declare mixed_data_types
mixed_data_types = ['A', 25, 5.8, 'single', '24, abc street, USA']
print(mixed_data_types)
print(type(mixed_data_types[2]))

# Declare it_companies
it_companies = [
    'Facebook', 'Google', 'Microsoft', 'Apple',
    'IBM', 'Oracle', 'Amazon'
]

# Print the list
print(it_companies)

# Print the number of companies
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
middle = len(it_companies) // 2

if len(it_companies) % 2 != 0:
    print(it_companies[middle])
else:
    print(it_companies[middle - 1], it_companies[middle])

print(it_companies[-1])

# Modify one of the companies
target = 'Facebook'
change_company = 'Meta Facebook'

if target in it_companies:
    pos = it_companies.index(target)
    it_companies[pos] = change_company
    print(it_companies)

# Add an IT company
it_companies.append('Tesla')
print(it_companies)

# Insert an IT company in the middle
new_company = 'Tesla'

if len(it_companies) % 2 != 0:
    middle = len(it_companies) // 2
    it_companies.insert(middle, new_company)
else:
    middle = len(it_companies) // 2
    it_companies.insert(middle, new_company)

print(it_companies)

# Change one company name to uppercase (IBM excluded)
index = int(input('Enter the word index you want to capitalize: '))

if it_companies[index] != 'IBM':
    it_companies[index] = it_companies[index].upper()
    print(it_companies)
else:
    print('IBM is already capitalized')

# Join the companies with '#;  '
print('#;  '.join(it_companies))

# Check if a company exists
s = input('Give the company name you want to check: ')

if s in it_companies:
    print(s)
else:
    print('The company name is not there')

# Sort the list
it_companies.sort()
print(it_companies)

# Reverse the list in descending order
it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies
print(it_companies[0:3])

# Slice out the last 3 companies
print(it_companies[-3:])

# Slice out the middle IT company or companies
middle = len(it_companies) // 2

if len(it_companies) % 2 != 0:
    print(it_companies[middle:middle + 1])
else:
    print(it_companies[middle - 1:middle + 1])

# Remove the first IT company
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies
middle = len(it_companies) // 2

if len(it_companies) % 2 != 0:
    it_companies.pop(middle)
else:
    del it_companies[middle - 1:middle + 1]

print(it_companies)

# Remove the last IT company
it_companies.pop()
print(it_companies)

# Remove all IT companies
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Copy the joined list and insert Python and SQL after Redux
joined_list = front_end + back_end
print(joined_list)

full_stack = joined_list.copy()
pos = full_stack.index('Redux')
full_stack[pos + 1:pos + 1] = ['Python', 'SQL']

print(full_stack)


# 💻 Exercises: Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the minimum and maximum age
ages.sort()
min_age = ages[0]
max_age = ages[-1]

print('Minimum age: {}, Maximum age: {}'.format(min_age, max_age))

# Add the minimum and maximum age again to the list
ages.extend([min_age, max_age])
print(ages)

# Find the median age
ages.sort()
middle = len(ages) // 2

if len(ages) % 2 != 0:
    median = ages[middle]
else:
    median = (ages[middle - 1] + ages[middle]) / 2

print('Median age: {}'.format(median))

# Find the average age
average = sum(ages) / len(ages)
print('Average: {:.2f}'.format(average))

# Find the range of the ages
age_range = max(ages) - min(ages)
print('Age range:', age_range)

# Compare the values of (min - average) and (max - average)
value1 = abs(min_age - average)
value2 = abs(max_age - average)

if value1 < value2:
    print('max-average is greater than min-average')
elif value1 > value2:
    print('min-average is greater than max-average')
else:
    print('Both values are equal')

# Find the middle country or countries
countries = [
    'China', 'Russia', 'USA', 'Finland',
    'Sweden', 'Norway', 'Denmark'
]

middle = len(countries) // 2

if len(countries) % 2 != 0:
    print(countries[middle])
else:
    print(countries[middle - 1:middle + 1])

# Divide countries into two halves
# If odd, the first half gets one extra country
middle = (len(countries) + 1) // 2

list_1 = countries[:middle]
list_2 = countries[middle:]

print(list_1)
print(list_2)

# Unpack the first three countries and the rest as Nordic countries
a_countries, b_countries, c_countries, *nordic_countries = countries

print(
    '{}, {}, {}, Nordic countries: {}'.format(
        a_countries,
        b_countries,
        c_countries,
        nordic_countries
    )
)