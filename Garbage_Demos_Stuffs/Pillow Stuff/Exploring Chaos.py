from PIL import Image 
import random
img = Image.new('RGB', (600,600), 'Black')
pixels = img.load()

for i in range(357604):
	r_colour = random.randint(1,255)
	g_colour = random.randint(1,255)
	b_colour = random.randint(1,255)
	pixels[random.randint(1,599),random.randint(1,599)] = (r_colour,g_colour,b_colour)	
	red,green,blue = pixels[250,250]


img.save('Images/dot.png')


