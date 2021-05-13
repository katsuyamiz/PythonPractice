my_dict = {'apple': '$3', 'orange': '$5', 'watermelon': '$7'}
print(my_dict['watermelon'])

d = {'k1': 123, 'k2': [1, 2, 3], 'k3': {'inside': 100}}
print(d['k1'])
print(d['k2'])
print(d['k3'])
print(d['k3']['inside'])

myd = {'key1': ['a', 'b', 'c']}
my_lst = myd['key1']
print(my_lst)
letter = my_lst[1]
print(letter.upper())

# in a line
letter_0 = myd['key1'][1].upper()
print(letter_0)

dict1 = {'k1': 100, 'k2': 200, 'k3': 300}
dict1['k1'] = 'new value'
print(dict1)
print(dict1.keys())
print(dict1.values())









