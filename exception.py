
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")

    except D:
        print("D")


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, D, C]:
    try:
        raise cls()
    except C:
        print("C")

    except D:
        print("D")

    except B:
        print("B")


