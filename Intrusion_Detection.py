import cv2
import numpy as np
 
cap = cv2.VideoCapture("Intrusion_1.mp4")
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
kernel_dil = np.ones((20,20), np.uint8) 
subtractor = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25, detectShadows=True)
 
while True:
    ret, frame = cap.read()

    if ret == True:
    	mask = subtractor.apply(frame)
    	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    	dilation = cv2.dilate(mask, kernel_dil, iterations=1)
    	(contours, hierarchy) = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
			area = cv2.contourArea(conrour)
			if(area>3000):
				cv2.putText(frame, "Intrusion Detected", cv2.FONT_HERSHLEY_DUPLEX, 1, (0,255,0), 2)

		cv2.imshow("Frame", frame)
		cv2.imshow("Mask", mask)
		key = cv2.waitKey(30)
		if key == 27:
			break

cap.release()
cv2.destroyAllWindows()