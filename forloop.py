my_items = [1, 2, 3, 4, 5]
for item in my_items:
    print(item)
print('-- my_list --')
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in my_list:
    print(i)
print('-- hello --')
hello = [1, 2, 3]
for h in hello:
    print('hello')
print('-- even numbers--')
for even_num in my_list:
    if even_num % 2 == 0:
        print(even_num)
print('-- sum --')
result = 0
for i in my_list:
    result += i
print(result)
print('-- letter --')
my_string = 'Hello'
for letter in my_string:
    print(letter)
print('-- cool --')
for _ in 'cool':
    print(_)
# tuple
print('-- tuple list --')
a_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(len(a_list))
for i in a_list:
    print(i)
# tuple unpacking
print('-- tuple unpacking --')
for (a, b) in a_list:
    print(b)
# for dictionary
print('-- dictionary --')
d = {'k1': 1, 'k2': 2, 'k3': 3}
# only returns keys
for i in d:
    print(i)
for j in d.items():
    print(j)

for value in d.values():
    print(value)








