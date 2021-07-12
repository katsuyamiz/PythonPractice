class Cat():
    # class object attribute
    species = 'cat'

    def __init__(self, color, name, isTail):
        self.color = color
        self.name = name
        self.isTail = isTail

    # methods
    def make_sound(self):
        print('meow')
        print('My name is {}'.format(self.name))


my_cat = Cat(color='black', name='Tom', isTail=True)
print(type(my_cat))
print(my_cat.color)
print(my_cat.isTail)
print(my_cat.species)
print(my_cat.make_sound())
