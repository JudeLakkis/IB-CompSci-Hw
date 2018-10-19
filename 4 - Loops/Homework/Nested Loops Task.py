# Task 1


def box():
    for i in range(5):
        print('')
        for j in range(10):
            print('*', end='')


# box()

# Task 2

height = 10


def many_asterisk_triangles(height):
    print('\n')
    for i in range(height):
        print('')
        for j in range(0, i):
            # 2n + 1
            print((height - j) * ' ', (2 * j + 1) * '*')


# many_asterisk_triangles(height)


def single_asterisk_triangle(height):
    for j in range(10):
            # 2n + 1
        print((height - j) * ' ', (2 * j + 1) * '*')


# single_asterisk_triangle(height)

# Task 4

height = 7
width = 7


def rectangle_with_cross(height, width):
    for i in range(height):
        for j in range(width):
            if (i == 1 or  # For the top row of height
                i == height or  # For the bottom row of height
                j == 1 or  # For the right row of width
                j == width or  # For the left row of width
                i == j or  # Places [*] at (width, height) creating the downward part of the cross
                    j == (height - i + 1)):  # Places [*] at (width, (height - placement of * + 1)) creating the upward part of the cross

                print('*', end='')
            else:
                print(' ', end='')
        print()


rectangle_with_cross(height, width)
