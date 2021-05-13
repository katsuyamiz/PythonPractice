#
# st = 'Print only the words that start with s in this sentence'
# word_list = st.split(' ')
# print(word_list)
# for word in word_list:
#     if word[0] == 's':
#         print(word)
#
#
# for x in range(0, 11):
#     if x % 2 == 0:
#         print(x)
#
#
# result = [x for x in range(1, 51) if x % 3 == 0]
# print(result)
#
#
# st = 'Print every word in this sentence that has an even number of letters'
# result = st.split(' ')
# for i in result:
#     if i.count('') & 2 == 0:
#         print(i)
#
#
# for i in range(1, 101):
#     if i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 15 == 0:
#         print('FizzBuzz')
#     else:
#         print(i)
#
#
# st = 'Create a list of the first letters of every word in this string'
# c_list = [i[0] for i in st.split(' ')]
# print(c_list)


# def lesser_of_two_evens(a, b):
#
#     if a % 2 == 0 and b % 2 == 0:
#         if a > b:
#             return b
#         if b > a:
#             return a
#     else:
#         if a > b:
#             return a
#         if a < b:
#             return b
#
#
# print(lesser_of_two_evens(19, 23))


# def animal_crackers(arg):
#     split = arg.split()
#     return split[0][0].lower() == split[1][0].lower()
#
#
# print(animal_crackers('Base lall'))


# def other_side_of_seven(arg):
#     number = 0
#     if arg < 7:
#         number = 7 + (7 - arg)*2
#     if arg > 7:
#         number = 7 - (arg - 7)*2
#
#     return number
#
#
# print(other_side_of_seven(12))


# def old_macdonald(arg):
# #     i = 0
# #     new_arg = ''
# #     while i < len(arg):
# #         if i == 0:
# #             new_arg += arg[i].upper()
# #         elif i == 3:
# #             new_arg += arg[i].upper()
# #         else:
# #             new_arg += arg[i]
# #         i += 1
# #     return new_arg
# #
# #
# # print(old_macdonald('abcdef'))


# def reverse(arg):
#     new_arg = ''
#     new_list = arg.split()
#     new_list.reverse()
#     for i in new_list:
#         new_arg += i + ' '
#     return new_arg
#
#
# print(reverse('we are ready'))


# def don_go_far(num):
#     n10 = num - 10
#     p10 = num + 10
#     if 90 <= n10 <= 100 or 100 <= n10 <= 110 or 190 <= n10 <= 200 or 200 <= n10 <= 210:
#         return True
#     elif 90 <= p10 <= 100 or 100 <= p10 <= 110 or 190 <= p10 <= 200 or 200 <= p10 <= 210:
#         return True
#     else:
#         return False
#
#
# print(don_go_far(210))

# def laughter(sub, string):
#     count = 0
#     for x in range(len(string) - len(sub) + 1):
#         if string[x:x + len(sub)] == sub:
#             count += 1
#     return count
#
#
# print(laughter('hah', 'hahahah'))


# def has_33(nums):
#     for i in range(len(nums) - 1):
#         if nums[i] == 3 and nums[i + 1] == 3:
#             return True
#
#     return False
#
#
# print(has_33([1, 3, 2, 3, 1, 3]))


# def paper_doll(string):
#     new_str = ''
#     for i in string:
#         new_str += i*3
#     return new_str
#
#
# print(paper_doll('Hello'))


# def blackjack(a, b, c):
#
#     a_list = [a, b, c]
#     num_sum = sum(a_list)
#     if num_sum <= 21:
#         return num_sum
#     if num_sum > 21 and 11 in a_list:
#         return num_sum - 10
#     if num_sum > 21 and 11 not in a_list:
#         return 'BUST'
#
#
# print(blackjack(5, 6, 7))
# print(blackjack(9, 9, 9))
# print(blackjack(9, 9, 11))

# flag
# def rock(nums):
#     smr = 0
#     flag = True
#     for i in nums:
#         if i == 6:
#             flag = False
#         if flag:
#             smr += i
#         if i == 9:
#             flag = True
#     return smr
#
#
# print(rock([4, 5, 6, 7, 8, 9]))
# print(rock([2, 1, 6, 9, 11]))


# def james(nums):
#     num_list = []
#     for i in nums:
#         if i == 0 or i == 7:
#             num_list.append(i)
#     if num_list[0] == 0 and num_list[1] == 0 and num_list[2] == 7:
#         return True
#     else:
#         return False
#
#
# print(james([1, 2, 4, 0, 0, 7, 5]))
# print(james([1, 0, 2, 4, 0, 5, 7]))
# print(james([1, 7, 2, 0, 4, 5, 0]))


# def primes(num):
#     a_list = []
#     for i in range(3, num):
#         for y in range(2, i):
#             if i % y == 0:
#                 break
#             if i % y != 0:
#                 a_list.append(i)
#     return a_list
#
#
# print(primes(100))

# answer
# def count_primes(num):
#
#     primes = [2]
#     x = 3
#     if num < 2:
#         return 0
#     while x <= num:
#         for y in primes:  # use the primes list!
#             if x % y == 0:
#                 x += 2
#                 break
#         else:
#             primes.append(x)
#             x += 2
#     print(primes)
#     return len(primes)
#
#
# print(count_primes(100))


# def print_big(letter):
#     patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
#     alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
#     for pattern in alphabet[letter.upper()]:
#         print(patterns[pattern])
#     print(alphabet['A'])
#
# print(print_big('a'))

# def g():
#     alphabet = {'A': [1, 2, 3, 4], 'B': [4, 3, 2, 1]}
#     for i in alphabet['B']:
#         print(i)
#
#
# g()




















