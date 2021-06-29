class Cat():
    def __init__(self,color, name, isTail):
        self.color = color
        self.name = name
        self.isTail = isTail


my_cat = Cat(color='black', name='Tom', isTail=True)
print(type(my_cat))

print(my_cat.color)
print(my_cat.isTail)