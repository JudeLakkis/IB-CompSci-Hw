from random import randint

point = []
points = []


def coordinates(point, points):
    a, b = randint(0, 500), randint(0, 500)
    point += a, b
    c = tuple(point)
    points.append(c)
    point[:] = []


for i in range(20):
    coordinates(point, points)

print(points)
