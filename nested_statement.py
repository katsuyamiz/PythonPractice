# name = 'global'
# # global
#
#
# def greet():
#     name = 'enclosing'
#     # enclosing
#
#     def hello():
#         # local
#         name = 'local'
#         print('Hi,' + name)
#
#     hello()
#
#
# print(greet())

x = 50


def func(x):

    print(f'X is {x}')

#local
    x = 'new value'
    print(f'X changed to local x: {x}')
    return x


x = func(x)
func(x)
print(x)



