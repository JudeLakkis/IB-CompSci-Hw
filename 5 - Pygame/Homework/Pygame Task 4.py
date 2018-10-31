'''
Okie so Pygame hates me a bunch so here is how the code would work:
1) Function below creates my points, (Ignore single letter variables), and
    puts them into a list named points
2) These points would be then placed into pygame.draw.lines() under the point
    list secetion
3) Bamn you have a bunch of points, which get turned into lines, homework complete
'''

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

'''
Pretend there is pygame involved, 
Don't worry about it
'''