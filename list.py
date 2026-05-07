fruits=['banana','orange','mango','lemon']
print('Fruits:', fruits)
print('Length of the list:',len(fruits))
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types
print('List:', lst)
print('First element:', lst[0])
print('Last element:', lst[-1])

lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)  
print(second_item)
print(third_item)  
print(rest)

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr) 
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

all_fruits=fruits[::2]
print(all_fruits)
