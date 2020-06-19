import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread("paper6.jpg")
img2 = cv2.imread("paper7.jpg")

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img = img[:,0:-1]
row, col = img.shape
print(col)
def filtro(img,row,col,val):
	for i in range (row):
		for j in range(col):
			if img[i,j] > val:
				img[i,j] = 255
			else:
				img[i,j] = img[i,j]

def divition(img,img2):
	img = img/img2
	cv2.imshow("in",img)	
	maxi = np.amax(img)
	print(maxi)
	#maxi = 255//maxi
	print(maxi)
	img = img*255
	filtro(img,row,col,210)
	cv2.imwrite("salida.jpg",img)


def resta(img,img2):
	img =  img2-img
	cv2.imshow("in",img)	
	maxi = np.amax(img)
	print(maxi)
	maxi = 255//maxi
	print(maxi)
	img = img*maxi
	cv2.imwrite("salida.jpg",img)

divition(img,img2)
#resta(img,img2)
#cv2.imshow("salida",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
