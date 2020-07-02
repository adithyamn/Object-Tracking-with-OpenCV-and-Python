##############################################################
##########	Object Tracking using OpenCV and Python	##########
##############################################################

#####################################
#####    Mean Shift Tracking	#####
#####################################

#####	Importing Libraries		#####

import cv2
import numpy as np

#####	Pre-Processing	#####

cap = cv2.VideoCapture("Videos/face_track.mp4")											#Video Capture
ret, frame = cap.read()

#####	Setup the Initial Tracking Window	#####

face_casc = cv2.CascadeClassifier('HaarCasscades/haarcascade_frontalface_default.xml')	
face_rects = face_casc.detectMultiScale(frame)

####	Convert the List to a Tuple	#####	

face_x, face_y, w, h = tuple(face_rects[0])
track_window = (face_x, face_y, w, h)

#####	Region of Interest for Tracking	#####

roi = frame[face_y:face_y+h, face_x:face_x+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)											#HSV ColorMapping
hist_roi = cv2.calcHist([hsv_roi], [0], None, [180], [0,180])							#Histogram to target on each frame for the meanshift calculation
cv2.normalize(hist_roi, hist_roi, 0, 255, cv2.NORM_MINMAX)								#Normalising the Histogram

#####	Set termination Criteria	#####

term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

#####	MeanShift Tracking	#####

while True:

	ret, fram = cap.read()
	if ret == True:
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		dest_roi = cv2.calcBackProject([hsv], [0], hist_roi, [0,180], 1)				#Calc the Actual ROI

		ret, track_window = cv2.meanShift(dest_roi, track_window, term_crit)			#Meanshift Calculation
		x,y,w,h = track_window
		image = cv2.rectangle(frame, (x, y), (x+w, y+h), (255,255,0), 3)

		cv2.imshow('FaceTracker', image)												#OUTPUT
		if cv2.waitKey(50) & 0xFF == 27:
			break
	else:
		break

	
cap.release()																						
cv2.destroyAllWindows()		