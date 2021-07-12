

try:
    result = 10 + 20
except:
    print("error")
else:
    print(result)
    print("no error")
print("-----")

try:
    f = open('tesfile', 'w')
    f.write("Wirte something")
except TypeError:
    print("Type error")
except OSError:
    print("OS error")
except:
    print("any error")
finally:
    print("finally")


# def get_int():
#     while True:
#         try:
#             result = int(input("enter number"))
#         except:
#             print("not number")
#             continue
#         else:
#             print("its number")
#             break
#         finally:
#             print("finally")
#
# print(get_int())


print("--p1--")


def p1():
    try:
        for i in['a', 'b', 'c']:
            print(i**2)
    except TypeError:
        print("its not number")
    finally:
        print("done")


print(p1())


def p2():
    x = 5
    y = 0
    try:
        z = x/y
    except ZeroDivisionError:
        print("devided with 0")
    finally:
        print("All done")


print(p2())


def p3():
    while True:
        try:
            ask = int(input("enter number"))
        except ValueError:
            print("error")
            continue
        else:
            print(ask**2)
            break
        finally:
            print("Done")
p3()


