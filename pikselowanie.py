
from pygame import *






pic = image.load("europe2.png")
print(pic.get_rect().size)
#pic = transform.scale(pic, (WIDTH, HEIGHT))



WIDTH = pic.get_rect().size[0]
HEIGHT = pic.get_rect().size[1]
init()
screen = display.set_mode((WIDTH,HEIGHT))
clock = time.Clock()



screen.blit(pic,(0,0))

piksele = []
skok = 10
for i in range(0,WIDTH,skok):
	for j in range(0,HEIGHT,skok):
		x = i
		y = j
		col = screen.get_at((x, y))
		#if  col[0:3] != (0,0,0) and (col[0]>50 or col[1]>50 or col[2]>50):
		#	piksele.append([x,y,col])
		#else:
		piksele.append([x,y,col])

screen.fill((255, 255, 255))
for pix in piksele:
	draw.rect(screen,pix[2],Rect(pix[0],pix[1],skok,skok),0)


end = False
time = 0
while not end:
	for z in event.get():
		if z.type == QUIT:
			end = True
			
	keys=key.get_pressed()
	if keys[K_KP_PLUS]:
		screen.fill((255, 255, 255))
		screen.blit(pic,(0,0))
		piksele = [[-1,-1,(255,255,255,255)]]
		skok += 1
		for i in range(0,WIDTH,skok):
			for j in range(0,HEIGHT,skok):
				x = i
				y = j
				col = screen.get_at((x, y))
				if  col[0:3] != (0,0,0) and (col[0]>50 or col[1]>50 or col[2]>50):
					piksele.append([x,y,col])
				else:
					piksele.append([x,y,piksele[-1][2]])

		screen.fill((255, 255, 255))
		for pix in piksele:
			draw.rect(screen,pix[2],Rect(pix[0],pix[1],skok,skok),0)

	if keys[K_KP_MINUS]:
		screen.fill((255, 255, 255))
		screen.blit(pic,(0,0))
		piksele = [[-1,-1,(255,255,255,255)]]
		skok -= 1
		if skok < 1:
			skok = 1
		for i in range(0,WIDTH,skok):
			for j in range(0,HEIGHT,skok):
				x = i
				y = j
				col = screen.get_at((x, y))
				if  col[0:3] != (0,0,0) and (col[0]>50 or col[1]>50 or col[2]>50):
					piksele.append([x,y,col])
				else:
					piksele.append([x,y,piksele[-1][2]])
		screen.fill((255, 255, 255))
		for pix in piksele:
			draw.rect(screen,pix[2],Rect(pix[0],pix[1],skok,skok),0)

	display.flip()
	clock.tick(25)


