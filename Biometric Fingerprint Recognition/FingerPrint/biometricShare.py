"""
This program creates two share parts of fingerprint - fp1 and fp2 
Libraries used - OpenCV and Numpy
"""

import cv2
import numpy as np
import os

folders = os.listdir("Database")

for file in folders:
	print(file)
	#Reading fingerprint image
	im = cv2.imread('Database/'+file)
	
	#Converting to grey scale
	g_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	
	#Reading datatype and dimensions of image
	dtype = str(g_im.dtype)
	dim = g_im.shape
	rows = dim[0]
	cols = dim[1]
	
	#Initializing two shares of images
	fp1 = np.zeros((rows,cols),dtype='a4')
	fp2 = np.zeros((rows,cols),dtype='a4')
	
	for i in range(rows):
		for j in range(cols):
			s = str(g_im[i, j]*9)
			if len(s) == 4:
				fp1[i,j]  = s[0:2]
				fp2[i,j]  = s[2:4]			
			elif len(s) == 3:
				fp1[i,j] = s[0:2]
				fp2[i,j] = s[2]
			elif len(s) == 2:
				fp1[i,j] = s[0]
				fp2[i,j] = s[1]
			elif len(s) == 1:
				fp1[i,j] = '0'
				fp2[i,j] = s[0]
			else:
				continue
	#Initializing temp for recovering the original image from two shared image
	temp = np.zeros((rows,cols),dtype=int)
	temp_p1 = np.zeros((rows,cols),dtype=int)
	temp_p2 = np.zeros((rows,cols),dtype=int)

	#Concetanating two shared arrays of image and dividing element wise by 9
	for i in range(rows):
		for j in range(cols):
			temp[i,j] = int(fp1[i,j]+fp2[i,j])/9
			temp_p1[i,j] = int(fp1[i,j])
			temp_p2[i,j] = int(fp2[i,j])
	s = file.replace('.bmp','')
	#Creating 8 bit channeled image for writing to disc
	az = cv2.convertScaleAbs(temp)
	cv2.imwrite('Reproduced/'+s+'_reproduced.bmp',az)
	
	az1 = cv2.convertScaleAbs(temp_p1)
	cv2.imwrite('Shares/'+s+'_share1.bmp',az1)
	
	az2 = cv2.convertScaleAbs(temp_p2)
	cv2.imwrite('Shares/'+s+'_share2.bmp',az2)
	
print(len(folders))