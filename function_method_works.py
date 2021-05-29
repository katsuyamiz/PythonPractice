

def vol(rad):

    return 4/3 * 3.14*rad**3


result = vol(2)
print(result)

print('-------')

def ran_check(num, low, high):
    if low < num < high:
        return f'{num} is in the range between {low} and {high}'
    else:
        return f'{num} is in not the range between {low} and {high}'

"""
num in range(low, high + 1)
"""

result = ran_check(5, 2, 7)
print(result)
result = ran_check(8, 2, 7)
print(result)


print('-------')


def up_low(s):
    u = 0
    l = 0
    for i in s:
        if i .isupper():
            u += 1
        if i .islower():
            l += 1

    return f'No. of Upper case characters : {u}\nNo. of Upper case characters : {l}'


result = up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
print(result)


"""
d = {'upper': 0, 'lower': 0}
d['upper'] += 1
d['lower'] += 1
"""

print('-------')


def unique_list(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)

    return new_lst


result = unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])
print(result)

"""
set(lst)
"""

print('-------')


def multiply(numbers):
    r = 1
    for i in numbers:
        r *= i
    return r


result = multiply([1, 2, 3, -4])
print(result)


print('-------')


def palindrome(s):
    lst = []
    n = 0
    while n <= len(s)/2:
        if s[n] == s[-(n + 1)]:
            lst.append(True)
        else:
            lst.append(False)
        n += 1
    print(lst)
    return all(lst)


result = palindrome('asddsa')
print(result)
"""
s.replace(' ', '')
remove space
"""
print('------')

import string


def is_pangram(str1, alphabet=string.ascii_lowercase):

    result1 = set(str1.lower())
    if ' ' in result1:
        result1.remove(' ')
    result2 = set(alphabet)
    if result1 == result2:
        return True
    else:
        return False


print(is_pangram("The quick brown fox jumps over the lazy dog"))


