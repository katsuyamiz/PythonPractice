#
# def name_of_function(name):
#     print('hello, ' + name)
#
#
# def add_func(num1, num2):
#     return num1 + num2
#
#
# result = add_func(1, 3)
# print(result)
#
#
# def say_hello():
#     print('hello')
#     print('are')
#     print('you')
#
#
# say_hello()
#
#
# def say_hello(name='Default'):
#     print(f'hello, {name}')
#
#
# say_hello()

# difference between return and print is that, return allows to save


# def even_odd():
#     a = input('enter numb')
#     if int(a) % 2 == 0:
#         print('even')
#     else:
#         print('odd')
#
#
# even_odd()


# def check_even(number):
#     result = number % 2 == 0
#     return result
#
#
# print(check_even(20))


# def check_even_list(num_list):
#     # placeholder variables
#     even_numbers = []
#
#     for number in num_list:
#         if number % 2 == 0:
#             even_numbers.append(number)
#
#         else:
#             pass
#
#     return even_numbers
#
#
# print(check_even_list([1, 2, 3, 4, 5, 6, 7, 8]))


stock_price = [('April', 200), ('good', 300)]

for item in stock_price:
    print(item)

for ticker, price in stock_price:
    print(price+(0.1*price))

work_hours = [('Abby', 20000), ('Billy', 4000), ('Casie', 8000)]

def employee_check(work_hours):
    c_max = 0
    top_month = ''

    for emp, hours in work_hours:
        if hours > c_max:
            c_max = hours
            top_month = emp
        else:
            pass


    return(top_month, c_max)


result = employee_check(work_hours)
print(result)

name, hour = employee_check(work_hours)

print(name)
print(hour)
# print(location) error

