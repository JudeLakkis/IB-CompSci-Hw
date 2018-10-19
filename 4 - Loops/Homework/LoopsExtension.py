from PIL import Image

window_size = (500, 500)
img = Image.new('RGB', window_size, color=(0, 0, 0))

x, y = 250, 250
pixel = img.load()
pixel[x, y] = (255, 255, 255)


def black_pixel(x, y):
    r, g, b = img.getpixel((x, y))
    if r == 0 and g == 0 and b == 0:
        pixel[x, y] = (255, 255, 255)
        x += 1
        print('x')
        return x + 1


while (x < 500 and x > 0) and (y < 500 and y > 0):
    r, g, b = img.getpixel((x, y))
    if r == 0 and g == 0 and b == 0:
        pixel[x, y] = (255, 255, 255)
        x += 1
        print('x')
    elif r == 255 and g == 255 and b == 255:
        pixel[x, y] = (0, 0, 0)
        y -= 1
        print('y')


img.save('Images/Ant.png')

# r, g, b = img.getpixel((x, y))
# print(r, g, b)
