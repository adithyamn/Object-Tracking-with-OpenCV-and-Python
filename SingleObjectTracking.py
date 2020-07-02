##############################################################
##########	Object Tracking using OpenCV and Python	##########
##############################################################

#########################################
#####    Single Object Tracking		#####
#########################################

#####	Importing Libraries		#####

import cv2

#####	Tracker	#####

def Tracker():
	print("Choose Tracker API:")
	print('Enter 0 for Boosting:')
	print('Enter 1 for MIL:')
	print('Enter 2 for KCF:')
	print('Enter 3 for TLD:')
	print('Enter 4 for MEDIANFLOW:')
	print('Enter 5 for GOTURN:')
	print('Enter 6 for MOSSE:')
	print('Enter 7 for CSRT:')

	choice = input('Select Tracker:')

	if choice == '0':
		tracker = cv2.TrackerBoosting_create()
	if choice == '1':
		tracker = cv2.TrackerMIL_create()
	if choice == '2':
		tracker = cv2.TrackerKCF_create()
	if choice == '3':
		tracker = cv2.TrackerTLD_create()
	if choice == '4':
		tracker = cv2.TrackerMedianFlow_create()
	if choice == '5':
		tracker = cv2.TrackerGOTURN_create()
	if choice == '6':
		tracker = cv2.TrackerMOSSE_create()
	if choice == '7':
		tracker = cv2.TrackerCSRT_create()	

	return tracker

tracker = Tracker()
tracker_name = str(tracker).split()[0][1:]						#Get the Tracker Name

cap = cv2.VideoCapture('Videos/Vehicles.mp4')

ret, frame = cap.read()											

roi = cv2.selectROI(frame, False)								#Select ROI
ret = tracker.init(frame,roi)									#Initialise the Tracker								

while True:

	ret, frame = cap.read()										#Get Video
	sucess, roi = tracker.update(frame)							#Update Tracker
	(x,y,w,h) = tuple(map(int,roi))								#Convet from tuple to list

	if sucess:
		pt1 = (x,y)
		pt2 = (x+w, y+h)
		cv2.rectangle(frame, pt1, pt2, (255,255,0), 3)

	else:
		cv2.putText(frame, 'Fail to Track', (100,200), cv2.FONT_HERSHEY_PLAIN, 1, (25, 125, 255), 3)

	cv2.putText(frame, tracker_name, (20,400), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255,0), 3)

	cv2.imshow(tracker_name, frame)

	if cv2.waitKey(50) & 0xFF == 27:
		break

cap.release()
cv2.destroyAllWindows()


