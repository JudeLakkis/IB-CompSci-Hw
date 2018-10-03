from PIL import Image

window_size = (500, 500)
img = Image.new('RGB', window_size, color=(0, 0, 0))

x, y = 250, 250
pixel = img.load()
pixel[x, y] = (255, 255, 255)

while (x < 500 and x > 0) and (y < 500 and y > 0):
    pixel[x, y] = (255, 255, 255)
    x -= 5
    y -= 5

img.save('Images/Ant.png')

# r, g, b = img.getpixel((x, y))
# print(r, g, b)
