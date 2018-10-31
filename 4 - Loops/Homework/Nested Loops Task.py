# Task 1


def box():
    for i in range(5):
        print('')
        for j in range(10):
            print('*', end='')


box()
print('')
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
    for j in range(3):
            # 2n + 1
        print((height - j) * ' ', (2 * j + 1) * '*')


single_asterisk_triangle(height)

# Task 3

height = 17
width = 13
cross = 0


def rectangle_with_cross(height, width, cross):
    for i in range(width - 2):  # Range width - 2 so that it doesn't affect the sides
        print('*', end='')
        for j in range(width - 2):
            if j == cross:
                print('*', end='')
            elif width - j - 2 == cross:  # Subtracting j so the cross prints inwards
                print('*', end='')
            else:
                print('', end=' ')  # Prints the spaces inside the cross
        print('*')
        cross += 1  # Increase the  internal cross distance


rectangle_with_cross(height, width, cross)
