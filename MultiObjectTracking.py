##############################################################
##########	Object Tracking using OpenCV and Python	##########
##############################################################

#########################################
#####    Multi Object Tracking		#####
#########################################

#####	Importing Libraries		#####

import cv2
import sys
from random import randint

#####	Trackers	#####

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']

#####	Tracker functiton	#####
def tracker_name(tracker_types):

	if tracker_type == tracker_types[0]:
		tracker = cv2.TrackerBoosting_create()
	elif tracker_type == tracker_types[1]:
		tracker = cv2.TrackerMIL_create()	
	elif tracker_type == tracker_types[2]:
		tracker = cv2.TrackerKCF_create()		
	elif tracker_type == tracker_types[3]:
		tracker = cv2.TrackerTLD_create()
	elif tracker_type == tracker_types[4]:
		tracker = cv2.TrackerMeidanFlow_create()
	elif tracker_type == tracker_types[5]:
		tracker = cv2.TrackerGOTURN_create()
	elif tracker_type == tracker_types[6]:
		tracker = cv2.TrackerMosse_create()
	elif tracker_type == tracker_types[7]:
		tracker = cv2.TrackerCSRT_create()

	else:
		tracker = None
		print('No Tracker Found')
		print('Choose from these trackers')
		for tr in tracker_types:
			print(ta)

	return tracker	

if __name__ == '__main__':
	print("Default Tracking Algorithm MOSSE \n"
		"Available Algorithms are: \n")

	for tr in tracker_types:
		print(tr)

	trackerType = 'MOSSE'

	cap = cv2.VideoCapture('Videos/Vehicles.mp4')
	sucess, frame = cap.read()
	if not sucess:
		print('Cannot read the Video')

	rects = []
	colors = []


	while True:

		rect_box = cv2.selectROI('MultiTracker', frame)
		rects.append(rect_box)
		colors.append((randint(64,255), randint(64,255), randint(64,255)))
		print('Press "Q" to stop selectiniig boxes and start multitracking')
		print('Press any key to select another box')

		if cv2.waitKey(0) & 0xFF == 113:
			break


	print('Selected boxes {rects}')

	multitracker = cv2.MultiTracker_create()

	for rect_box in rects:
		multitracker.add(tracker_name(tracker_type), frame, rect_box)

	while cap.isOpened():
		success, frame = cap.read()
		if not success:
			break

		success, boxes = multitracker.update(frame)


		for i, newbox in enumerate(boxes):
			pt1 = (int(newbox[0]), int(newbox[1]))
			pt2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
			cv2.rectangle(frame, pt1, pt2, colors[i], 2, 1)

			cv2.imshow('MuiltiTracker', frame)

			if cv2.waitKey(20) & 0xFF == 27:
				break

cap.release()
cv2.destroyAllWindows()








