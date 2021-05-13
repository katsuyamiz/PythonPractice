my_list = ['apple', 'grape', 'banana']
print(my_list)
print(len(my_list))
print(my_list[0])
# list is mutable
my_list[0] = 'green apple'
print(my_list)
my_list.append('orange')
print(my_list)
my_list.pop()
print(my_list)
my_list.pop(0)
print(my_list)

my_list_2 = ['e', 'a', 'c', 'b', 'd']
my_list_2.sort()
print(my_list_2)
my_list_2.reverse()

print('-- efficient  way --')

dalist = []
my_strig = 'hello'
for i in my_strig:
    dalist.append(i)
print(dalist)
print('-- this --')
my_list = [letter for letter in my_strig]
print(my_list)

number_list = [n for n in range(1, 11)]
print(number_list)
number_list = [n**2 for n in range(1, 11) if n % 2 == 0]
print(number_list)

celcius = [10, 20, 30]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

result = [x if x % 2 == 0 else 'odd' for x in range(0, 11)]
print(result)


nested_loop = []
for i in [2, 4, 6]:
    for j in [1, 10, 1000]:
        nested_loop.append(i*j)
print(nested_loop)

poped =[]
the_list = [5, 6, 7, 8]
poped.append(the_list.pop())
print(poped)




