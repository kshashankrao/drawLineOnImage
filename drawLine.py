import cv2
from random import *
a = []
b = []
i = 0
def click_and_crop(event, x, y, flags, param):

	global a,b,i

	if event == cv2.EVENT_LBUTTONDBLCLK and len(a) < 3:
		cv2.circle(image,(x,y),1,(50,50,50),-1,cv2.LINE_AA)
		print (x,y)

		a.append([x,y])
		length = len(a) - 1
		if length > 0:
			cv2.line(image,(a[0][0],a[0][1]),((a[1][0],a[1][1])),(50,50,50),1)
			b = a
			with open('images/fs'+str(i)+'.txt', 'a+') as f:

	  			f.write("%s\n" % b)
			a = []




image = cv2.imread('fs.jpg')
clone = image.copy()

cv2.imshow('image',image)
cv2.imshow('image',image)
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)



while True:

	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("s"):
		#num = randint(1,10000

		cv2.imwrite('images/fs'+str(i)+'.jpg',image)
		image = clone.copy()
		i = i+1
	if key == ord('q'):
		break
	if key == ord("r"):
		#num = randint(1,10000
		a = []
		image = clone.copy()
		i = i+1
cv2.destroyWindow("image")
