##############################################################
##########	Object Tracking using OpenCV and Python	##########
##############################################################

#####################################
#####    Cam Shift Tracking		#####
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

#####	CamShift Tracking	#####

while True:
	ret, frame = cap.read()
	if ret == True:
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		dest_roi = cv2.calcBackProject([hsv], [0], hist_roi, [0,180], 1)

		ret, track_window = cv2.CamShift(dest_roi, track_window, term_crit)							#CamShift

		pts = cv2.boxPoints(ret)
		pts = np.int0(pts)

		image = cv2.polylines(frame, [pts], True, (0,255,0), 5)

		cv2.imshow("CamShift", image)

		if cv2.waitKey(50) & 0xFF == 27:
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()



