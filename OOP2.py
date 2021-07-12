import math


class Line:
    def __init__(self, co1, co2):
        self.co1 = co1
        self.co2 = co2

    def distance(self):
        return math.sqrt((self.co1[0] - self.co2[0])**2 + (self.co1[1] - self.co2[1])**2)

    def slope(self):
        return (self.co2[1] - self.co1[1])/(self.co2[0] - self.co1[0])



c1 = (3, 2)
c2 = (8, 10)

l1 = Line(c1, c2)
print(l1.distance())
print(l1.slope())


class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi*(self.radius**2)*self.height

    def surface(self):
        return 2*self.radius*math.pi*2 + 2*math.pi*self.height*self.radius


c = Cylinder(2, 3)
print(c.volume())
print(c.surface())


class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, num):
        self.balance += num
        print("D Accepted")

    def withdraw(self, num):
        if self.balance >= num:
            self.balance -= num
            print("W Accepted")
        else:
            print("Unavailable")

    def __str__(self):
        return f'Owner: {self.owner}\nBlance: {self.balance}'


a = Account("Ka", 2000)
print(a.withdraw(2000))
print(a.__str__())











