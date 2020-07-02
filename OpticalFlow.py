##############################################################
##########	Object Tracking using OpenCV and Python	##########
##############################################################

#############################
#####    Optical Flow	#####
#############################

#####	Importing Libraries		#####

import cv2
import numpy as np

#####	Shi-Tomasi Corner Detection Parameters	#####

st_params = dict(maxCorners = 130, qualityLevel = 0.2, minDistance = 2, blockSize = 7)

#####	Lucas-Kande Optocal Flow Parameters		#####

lk_params = dict(winSize = (15,15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_COUNT, 10, 1))

#####	Pre - Processing	#####

cap = cv2.VideoCapture("Videos/run.mp4") 																	#Video Capture
color = (0,255,0)   																				#Color of the optical flow
ret, first_frame = cap.read()   																	#get the frist frame
prev_gray = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)  											#Convert the frame to grayscale
prev = cv2.goodFeaturesToTrack(prev_gray, mask=None, **st_params)   								#Find the strongest corners of the First Frame
mask = np.zeros_like(first_frame)   																#Create a Mask

#####	Processing	#####

while(cap.isOpened()):																				#While Loop
    ret, frame = cap.read()     																	#Read
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    												#Convert to Grayscale
    next, status, error = cv2.calcOpticalFlowPyrLK(prev_gray, gray, prev, None, **lk_params)		#Optical Flow Calclation

#####	Selecting Features & Specifying Previous and Current Postions 	#####

    good_new = next[status==1]
    good_old = prev[status==1]

#####	Draw optical flow track 	#####

    for i, (new,old) in enumerate(zip(good_new,good_old)): 											
        a,b = new.ravel()																			#Drawing a line  for the Coordinates for new and old feature points
        c,d = old.ravel()
        mask = cv2.line(mask, (a, b), (c, d), color,2)												#Mask
        frame = cv2.circle(frame, (a, b), 3, color, -1)												#Drawing a filled circlle for the selected  feature points
        output = cv2.add(frame,mask)																#Overlay optical flow on original Frame

#####	Updation and Output 	#####
    
    prev_gray=gray.copy()   																		#Update video
    prev = good_new.reshape(-1, 1, 2)   															#Update features
    cv2.imshow("Optcal Flow", output)   															#Display
        
    if cv2.waitKey(300) & 0xFF == ord("q"):
            break

cap.release()																						
cv2.destroyAllWindows()																				#End
        