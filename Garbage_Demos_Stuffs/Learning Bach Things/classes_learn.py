from random import randint
import time


class Person:

    def __init__(self, name):
        self.x = randint(0, 100)
        self.y = randint(0, 100)
        self.name = name
        self.child = None
        print(self.name, self.x, self.y)

    def have_child(self, name):
        self.child = Person(name)

    def update(self):
        self.x += randint(-1, 1)
        self.y += randint(-1, 1)
        print(self.name, self.x, self.y)


# homes = []
# for i in range(10):
#     homes.append(person('Person: ' + str(i)))

# for i in range(10):
#     print('------')
#     for people in homes:
#         people.update()

# homes.append(person.have_child('timmy'))


timmy = Person('timmy')
timmy.have_child('jeff')

print(timmy.name)
print(timmy.child.name)
