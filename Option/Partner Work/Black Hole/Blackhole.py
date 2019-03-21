from random import randint

grid = [['0'] * 4 for i in range(4)]
holes = [(randint(0, 3), randint(0, 3)) for i in range(3)]
prize = [randint(0, 3), randint(0, 3)]
movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Player = *, Black Hole = 1, Prize = $
for i in holes:
    grid[i[0]][i[1]] = 1
grid[0][0] = '*'
grid[3][3] = '$'


def find_player(grid):
    for i in grid:


print(grid)
print(holes)
