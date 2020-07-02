##############################################################
##########	Object Tracking using OpenCV and Python	##########
##############################################################

#############################
#####    Optical Flow	#####
#############################

#####	Importing Libraries		#####

import cv2
import numpy as np


#####	Pre-Processing	#####

cap = cv2.VideoCapture("Videos/chaplin.mp4")										#Video Capture
ret, first_frame = cap.read()														#Get the first frame
prev_gray = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)							#Conver to Grayscale
mask = np.zeros_like(first_frame)   												#Create a Mask
mask[..., 1] = 255																	#Setting saturation to max


#####	Optical Dense Flow 	#####

while(cap.isOpened()):																#While Loop
	ret, frame = cap.read()															#Get Video
	cv2.imshow('imput', frame)														#Display the output
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)									#Conver to Grayscale
	flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)	#Farneback Optical FLow Calculation
	magn, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])						#Calculate Mag and Angle
	mask[..., 0] = angle*180/np.pi/2												#Set the Optical Flow Direction
	mask[..., 2] = cv2.normalize(magn, None, 0, 255, cv2.NORM_MINMAX)				#Normalise The Magnitude
	rgb = cv2.cvtColor(mask, cv2.COLOR_HSV2RGB)										#Convert the HSB to RGB
	cv2.imshow("Dense Optical Flow", rgb)
	
#####	UPDATION	#####

	prev_gray = gray



#####	END		#####

	if cv2.waitKey(300) & 0xFF == ord("q"):
            break

cap.release()																						
cv2.destroyAllWindows()		




