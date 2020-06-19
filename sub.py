import cv2 
import numpy as np 
from matplotlib import pyplot as plt 


img1 = cv2.imread("paper6.jpg")
img2 = cv2.imread("paper7.jpg")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
img1 = img1[:,0:-1]
row,col= img1.shape
img1 = img1.astype(int)
img2 = img2.astype(int)
img1 = img1 - img2
print(np.amin(img1))
img1 = img1 + 167
img1 = img1.astype(np.uint8)
basic = img1.copy()
aux1 = img1.copy()
aux2 = img1.copy()
def  th(img,row,col,val):
	for i in range (row):
		for j in range(col):
			value = img[i,j]
			if value > val :
				img[i,j] = 255
			else:
				img[i,j] = 0

th(img1,row,col,155)
th(aux1,row,col,161)
th(aux2,row,col,170)

f, axarr = plt.subplots(2,2)
axarr[0,0].imshow(cv2.cvtColor(basic, cv2.COLOR_GRAY2RGB))
axarr[0,0].set_title("Division + 167")
axarr[0,1].imshow(cv2.cvtColor(img1, cv2.COLOR_GRAY2RGB))
axarr[0,1].set_title("Thresholding C=155")
axarr[1,0].imshow(cv2.cvtColor(aux1, cv2.COLOR_GRAY2RGB))
axarr[1,0].set_title("Thresholding C=161")
axarr[1,1].imshow(cv2.cvtColor(aux2, cv2.COLOR_GRAY2RGB))
axarr[1,1].set_title("Thresholding C=170")
plt.show()


#cv2.imwrite("sub_salida.jpg",img1)
#cv2.imwrite("sub_salida_Thre.jpg",img1)
