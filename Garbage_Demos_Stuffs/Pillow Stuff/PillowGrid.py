from PIL import Image

window_size = (500, 500)
img = Image.new('RGB', window_size, color = (0, 0, 0))

x, y = 250, 250
pixel = img.load()
pixel[x, y] = (255, 255, 255)
print(pixel[x, y])

while (x > 0 and x < 500) or (y > 0 and y < 500):
	if pixel[x, y] == (0, 0, 0):
		pixel = img.load()
		pixel[x, y] = (255, 255, 255)
		x += 1

	if pixel[x, y] == (255, 255, 255):
		pixel = img.load()
		pixel[x, y] = (0, 0, 0)
		y -= 1



img.save('Images/ant_image.bmp')