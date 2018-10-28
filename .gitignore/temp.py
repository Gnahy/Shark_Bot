import cv2
import numpy as np
import matplotlib.pyplot as plt



cap = cv2.VideoCapture(0) #Webcam Capture

while(True):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


		
    template = cv2.imread('gate.jpg',0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(gray,template,cv2.TM_SQDIFF)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = min_loc
    bottom_right = (top_left[0]+w,top_left[1]+h)
    cv2.rectangle(frame,top_left, bottom_right, 255, 1)
    cv2.putText(frame, 'Detected Face ID: ', (top_left[0],top_left[1]-10), 
    		cv2.FONT_HERSHEY_PLAIN, 1.0, (255,255,255))
	

    cv2.imshow('Test',frame)

    lower_blue = np.array([100,10,10])
    upper_blue = np.array([255,100,100])
    lower_red = np.array([10,10,100])
    upper_red = np.array([100,100,255])
    lower_green = np.array([10,100,10])
    upper_green = np.array([100,255,100])
    
    mask_blue = cv2.inRange(frame, lower_blue, upper_blue)
    mask_red = cv2.inRange(frame, lower_red, upper_red)
    mask_green = cv2.inRange(frame, lower_green, upper_green)

    # Bitwise-AND mask and original image
#    res_blue = cv2.bitwise_and(frame,frame, mask_blue= mask_blue)
#    res_red = cv2.bitwise_and(frame,frame, mask_red= mask_red)
#    res_green = cv2.bitwise_and(frame,frame, mask_green= mask_green)

    cv2.imshow('Blue',mask_blue)
    cv2.imshow('Red',mask_red)
    cv2.imshow('Green',mask_green)
    
#    cv2.imshow('res',res)    


    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break

cap.release()
cv2.destroyAllWindows() 
