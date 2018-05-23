import cv2
from time import time
from matplotlib import pyplot as plt
from tuscen import *

def resize_and_gray(img,return_color=False):
	w,h,c=img.shape
	shape=(int(h/2),int(w/2))
	img=cv2.resize(img,shape)
	gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	if return_color:
		return img,gray_img
	else:
		return gray_img
def plt_show(img,title=None):
	plt.figure(figsize=(10,10)) 
	if title!=None:
		plt.title(title)
	if len(img.shape)==2:
		cmap=plt.get_cmap('gray')
		plt.imshow(img,cmap=cmap)
	else:
		plt.imshow(img)
	plt.axis('off')
cap=ccd()
i=0
begin=time()
while(i<100):
	i+=1
	img = cap.read()
	#img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
	#k = cv2.waitKey(100) 
	#cv2.imshow('img',img)
	#if k == 27:
	#	cv2.destroyAllWindows()
	#	break
print(time()-begin)
cap.stop()