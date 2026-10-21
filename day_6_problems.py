# Exercises: Level 1
# Create an empty tuple
'''t=()
print(t)'''
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers=('Fahad','Faisal','Rasel')
sisters=('No Sisters','Had one')
print(brothers)
print(sisters)
# Join brothers and sisters tuples and assign it to siblings
siblings=brothers+sisters
print(siblings)
# How many siblings do you have?
l=len(siblings)
print(l)
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents=('X','Y')
family_members=parents+siblings
print(family_members)
# Exercises: Level 2
# Unpack siblings and parents from family_members
father_family_members,mother_family_members,*sibs=family_members
print(father_family_members)
print(mother_family_members)
print(sibs)
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('Mango','Orange','Apple')
vegetables=('Potato','Cucumbers')
animal=('Cow','Goat','Sheep')
food_stuff_tp=fruits+vegetables+animal
print(food_stuff_tp)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
l=len(food_stuff_tp)
print(l)
if l%2==0:
    middle_word = food_stuff_tp[l//2 - 1:l//2 + 1]
    print('{}'.format(middle_word))
else:
    middle_word=food_stuff_tp[l//2]
    print('{}'.format(middle_word))
# Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])
# Delete the food_stuff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
# print('cow' in food_stuff_tp)
# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print('Yes it is a nordic country')
else:
    print('No It is not a nordic country')
# Check if 'Iceland' is a nordic country
if 'Iceland' in nordic_countries:
    print('Yes it is a nordic country')
else:
    print('No It is not a nordic country')
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')