def square(num):
    return num**2


nums = [1, 2, 3, 4, 5]

for item in map(square, nums):
    print(item)


a_list = list(map(square, nums))
print(a_list)


def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'EVEN'
    else:
        return my_string[0]


names = ['Alex', 'Ben', 'Chris']

print(list(map(splicer, names)))


def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]
print(list(map(check_even, my_nums)))
print(list(filter(check_even, my_nums)))


def check_odd(number):
    return number % 2 != 0


numbers = [2, 3, 4, 5, 6, 7]

result = list(filter(check_odd, numbers))
print(result)


for i in filter(check_odd, numbers):
    print(i)

print('---')


def square(number): return number ** 2


print(square(4))

print('--lamdba--')
square2 = lambda num: num ** 2

print(square2(5))


the_nums = [1, 2, 3, 4, 5, 6]
result = list(map(lambda num: num**2, the_nums))
print(result)

result = list(filter(lambda num: num % 2 == 0, the_nums))
print(result)

result = list(map(lambda name: name[::-1], names))
print(result)
