from random import shuffle


def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


def guessing():
    guess_ = ''
    while guess_ not in ['0', '1', '2']:
        guess_ = input('Pick a number from 0 - 2: ')

    return int(guess_)


def check_guess(my_list, guess_):
    if my_list[guess_] == 'O':
        print('correct')
        print(my_list)
    else:
        print('Wrong')
        print(my_list)


# INITIAL LIST
my_list = ['', 'O', '']
# SHUFFLE LIST
mixed_list = shuffle_list(my_list)
# USER GUESS
guess = guessing()
# CHECK GUESS
check_guess(mixed_list, guess)


# def fun():
#
#     a = input('enter a number: ')
#     return int(a)
#
#
# def add(b):
#     return print(b + 1)
#
#
# c = fun()
# add(c)






