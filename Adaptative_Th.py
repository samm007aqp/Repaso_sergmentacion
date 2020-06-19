import cv2
import numpy as np 
from matplotlib import pyplot as plt

# C = 20
# B = 1.02 
filename = "salida.jpg"

def mean(i,j,row,col,rang):
	lin = rang
	arriba =  i-lin
	abajo =   i+lin
	isq =	j-lin
	der = 	j+lin
	if arriba < 0:
		arriba = 0
	if abajo > row:
		abajo = row-1
	if isq < 0:
		isq = 0
	if der > col:
		der = col-1
	total = 4*lin*lin
	subimg = tmp[arriba:abajo,isq:der]
	suma = np.sum(subimg)
	return suma/total

def adap_th(img,row,col,constante,rango):
	for i in range (row):
	    for j in range(cols):
	    	value = mean(i,j,row,cols,rango)
	    	value = value - constante # assure the darknest colors to 0
	    	if img[i,j]>value:
	    		img[i,j]= 255
	    	else:
	    		img[i,j]= 0


img = cv2.imread(filename)
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
tmp = img1.copy()
img2 = img1.copy()
img3= img1.copy()
img4= img1.copy()
row,cols = img1.shape

adap_th(img1,row,cols,5,10)
adap_th(img2,row,cols,10,10)
adap_th(img3,row,cols,20,10)
adap_th(img4,row,cols,30,10)


f, axarr = plt.subplots(2,2)
axarr[0,0].imshow(cv2.cvtColor(img1, cv2.COLOR_GRAY2RGB))
axarr[0,0].set_title("Th C=5, rango 10")
axarr[0,1].imshow(cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB))
axarr[0,1].set_title("Th C=10, rango 10")
axarr[1,0].imshow(cv2.cvtColor(img3, cv2.COLOR_GRAY2RGB))
axarr[1,0].set_title("Th C=20, rango 10")
axarr[1,1].imshow(cv2.cvtColor(img4, cv2.COLOR_GRAY2RGB))
axarr[1,1].set_title("Th C=30, rango 10")
plt.show()

#cv2.imshow('output',output)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.imwrite("Adap_Thesho"+filename, img_out)
