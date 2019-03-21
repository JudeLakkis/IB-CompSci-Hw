from random import randint

grid = [['0'] * 4 for i in range(4)]
holes = [(randint(0, 3), randint(0, 3)) for i in range(3)]
prize = [randint(0, 3), randint(0, 3)]

print(grid)

# Black Hole = 1
grid[prize[0]][prize[1]] = '$'
for i in holes:
    grid[i[0]][i[1]] = 1


print(grid)
print(holes)
