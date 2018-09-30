# Functions Extension Work

# Importing Site
import sys, random
from PIL import Image
sys.tracebacklimit = 0

# Variable Assignment
window_size = (500, 500)
img = Image.new('RGB', window_size, color = (0, 0, 0))

x, y = 25, 25
r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)

# List Assignment

# Function Defining
def set_pixel(img, x, y, r, g, b):
	pixel = img.load()
	pixel[x, y] = (r, g, b)
	# print(pixel[x, y])

def horizontal_line(x):
	for i in range(100):
		set_pixel(img, x, y, r, g, b)
		x += 1
	print(type(x), x)
	return x

def vertical_line(y):
	for i in range(100):
		set_pixel(img, horizontal_line(x), y, r, g, b)
		y += 1
	print(x)
	return y

def rando_line(x, y):
	for i in range(200):
		set_pixel(img, x, y, r, g, b)
		angle = random.randint(0,1)
		if angle == 0:
			x += 1
		else:
			y += 1

def rectangle():
		horizontal_line(x)
		vertical_line(y)

# Main/Body Code

set_pixel(img, x, y, r, g, b)
horizontal_line(x)
vertical_line(y)
rando_line(x, y)
# rectangle()

img.save('Pillow_Images/blackbox.bmp')