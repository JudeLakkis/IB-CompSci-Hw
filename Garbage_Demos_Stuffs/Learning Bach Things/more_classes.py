from random import randint


class Person():
    """docstring for Person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.child = None
        self.spouse = None
        print(self.name, self.age, self.child, self.spouse)

    def have_child(self, person_object):
        self.child = person_object

    def __str__(self):
        return self.name + str(' ') + str(self.age) + str(' ') + self.child.name


timmy = Person('Timmy', 25)
jake = Person('jake', 0)
timmy.have_child(jake)
print(timmy.child.name)
print(timmy)
