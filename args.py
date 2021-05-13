# def myfunc(a, b, c=0, d=0, e=0):
#     return sum((a, b, c, d, e)) * 0.05
#
#
# print(myfunc(40, 60, 100, 100))
#
#
# def fun(*args):
#     # unlimited number of args
#     return print(sum(args) * 0.5)
#
#
# fun(10, 10, 10, 10, 10)
#
#
# def func(**kwargs):
#     if 'fruit' in kwargs:
#         print('My choice is {}'.format(kwargs['fruit']))
#     else:
#         print('None chosen')
#
#
# func(fruit='apple', veggie='tomato')
#
#
# def myfunc(*args, **kwargs):
#
#     print('I would like {} {}'.format(args[0], kwargs['food']))
#
#
# myfunc(10, 20, 30, fruit='orange', food='tomato', animal='rabbit')
#
#
# def myfunc(arg):
#     i = 0
#     emp = ''
#     for a in arg:
#         if arg.index(a) % 2 == 0:
#             emp += a.lower()
#         elif arg.index(a) % 2 != 0:
#             emp += a.upper()
#
#     return emp
#
#
# print(myfunc('aaaaaaaaaa'))
#
#

def myfunc(arg):
    i = 0
    new_arg = ''
    while i < len(arg):
        if i % 2 == 0:
            new_arg += arg[i].lower()
        else:
            new_arg += arg[i].upper()
        i += 1
    return new_arg


print(myfunc('aaaaaaaaaa'))



