# 255 = white
# 0 = Black

from PIL import Image
x, y = (250, 250)
window_size = (500, 500)
n, e, s, w = 1, 0, 0, 0
black = (0, 0, 0)
white = (255, 255, 255)

img = Image.new('RGB', window_size, color = (0, 0, 0))

pix = img.load()

while True:
	if x < 0 or x > 499:
		print('break')
		break
	if y < 0 or y > 499:
		print('break')
		break
	else:
		if pix[x, y] == (black):
			pix[x, y] = (255, 255, 255)
			# 90° clockwise -> move 1 forward
			if n == 1:
				n = 0
				e = 1
				x += 1
			elif e == 1:
				e = 0
				s = 1
				y += 1
			elif s == 1:
				s = 0
				w = 1
				x -= 1
			elif w == 1:
				w = 0
				n = 1
				y += 1
			print (x, y)
			print ('n = ', n, 'e = ', e, 's = ', s, 'w = ', w)

		elif pix[x, y] == (white): # White
			pix[x, y] = (black) # Black
			# 90° anti-clockwise -> move 1 forward
			if n == 1:
				n = 0
				w = 1
				x -= 1
			elif w == 1:
				w = 0
				s = 1
				y += 1
			elif s == 1:
				s = 0
				e = 1
				x += 1
			elif e == 1:
				e == 0
				n = 1
				y -= 1
			print (x, y)
			print ('n = ', n, 'e = ', e, 's = ', s, 'w = ', w)


print('Done')
img.save('Images/ant_image.bmp')