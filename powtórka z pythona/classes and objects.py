class Dog(object):
    def __init__(self, name, age):  # self oznacza tutaj tim
        self.name = name  # to oznacza, że tim.name =  name
        # (a name to jest to co u góy wpisaliśmy)
        self.age = age

    def speak(self):
        print('hi! I am', self.name)

    def change_age(self, age):
        self.age = age

    def add_weight(self, xd):
        self.weight = xd


tim = Dog('Tim', 26)
tim.speak()
print(tim)
tim.add_weight(20)
print(tim.weight)
print('name:', tim.name, 'age:', tim.age, 'weight:',tim.weight)
