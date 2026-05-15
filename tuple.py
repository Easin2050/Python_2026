'''
Exercises: Level 1
Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Exercises: Level 2
Unpack siblings and parents from family_members
Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
Slice out the first three items and the last three items from food_stuff_lt list
Delete the food_stuff_tp tuple completely
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')'''

#1 Create an empty tuple
empty_tuple=()
print(empty_tuple)
#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
tuple_sisters=('sister1','sister2','sister3')
tuple_brothers=('brother1','brother2')
#3 Join brothers and sisters tuples and assign it to siblings
siblings=tuple_sisters+tuple_brothers
print(siblings)
#4 How many siblings do you have?
print(len(siblings))
#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members=siblings+('father','mother')
print(family_members)

#Exercises: Level 2
#1 Unpack siblings and parents from family_members
len_siblings=len(siblings)
siblings=family_members[:len_siblings]
parents=family_members[len_siblings:]
print(siblings)
print(parents)
#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('Apple','Mango','Banana','Lichie','Grapes')
vegetables=('Tomato','Potato','Cabbage','Onion','Carrot')
amimal_products=('Milk','Eggs','Meat','Cheese','Yogurt')
food_stuff_tp=fruits+vegetables+amimal_products
print(food_stuff_tp)
#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)
#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index=len(food_stuff_tp)//2
if len(food_stuff_tp)%2==0:
    middle_items=food_stuff_tp[middle_index-1:middle_index+1]
else:
    middle_items=food_stuff_tp[middle_index]
print(middle_items) 
#5 Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
#6 Delete the food_stuff_tp tuple completely
del food_stuff_tp

#7 Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
#8 Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)