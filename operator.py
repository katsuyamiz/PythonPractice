from random import shuffle
from random import randint

for num in range(10):
    print(num)

for num in range(2, 5):
    print(num)

a = list(range(0, 11, 2))
print(a)

index_count = 0
for i in 'abcd':
    print('at index {} the letter is {}'.format(index_count, i))
    index_count += 1
print('-- enumerate --')
word = 'Happy'
for letter in enumerate(word):
    print(letter)
print('-- zip --')
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for item in zip(list1, list2):
    print(item)
print('-- check in --')
print('x' in [1, 2, 3])
print('x' in ['x', 'y', 'z'])

print('john' in {'john': 'doctor'})

d = {'mike': 100}
print(100 in d.values())
d = {'mike': 100}
print(100 in d.keys())
print('-- max --')
dlist = [1, 2, 1, 2, 1, 2]
print(max(dlist))
print('-- shuffle --')
shuffle(dlist)
# shuffle impoted function
print(dlist)
print('-- random int --')
random_number = randint(0, 1000)
print(random_number)

print('-- input --')

user_input = int(input('Enter number: '))
print('your input was {}'.format(user_input))













