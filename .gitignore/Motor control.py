import cv2
import numpy as np
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library

GPIO.setmode(GPIO.BOARD)

GPIO.setup(10, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)


GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(12, 100)
GPIO.setup(32, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm1 = GPIO.PWM(32, 100)
GPIO.setup(33, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm2 = GPIO.PWM(33, 100)
GPIO.setup(35, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm3 = GPIO.PWM(35, 100)

pwm.start(0)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)


GPIO.output(29,GPIO.HIGH)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
GPIO.output(31,GPIO.LOW)
GPIO.output(36,GPIO.LOW)
GPIO.output(38,GPIO.HIGH)

pwm2.ChangeDutyCycle(100)
pwm3.ChangeDutyCycle(100)

time.sleep(8)

pwm2.ChangeDutyCycle(0)
pwm3.ChangeDutyCycle(0)

GPIO.output(8,GPIO.HIGH)
GPIO.output(10,GPIO.LOW)
GPIO.output(24,GPIO.HIGH)
GPIO.output(26,GPIO.LOW)

pwm.ChangeDutyCycle(0)
pwm1.ChangeDutyCycle(100)

cap = cv2.VideoCapture(0) #Webcam Capture

while(True):
    

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
		
    template = cv2.imread('gate.jpg',0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res>threshold)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = min_loc
    bottom_right = (top_left[0]+w,top_left[1]+h)
    cv2.rectangle(frame,top_left, bottom_right, 255, 1)
    cv2.putText(frame, 'Detected Face ID: ', (top_left[0],top_left[1]-10), 
    		cv2.FONT_HERSHEY_PLAIN, 1.0, (255,255,255))
	

    cv2.imshow('Test',frame)
    cv2.imshow('result',res)

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
    
  

    if(res.all()):
        pwm.ChangeDutyCycle(100)
        pwm1.ChangeDutyCycle(100)
        time.sleep(5)
    else:
        pwm.ChangeDutyCycle(0)
        pwm1.ChangeDutyCycle(100)
        

    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break
GPIO.cleanup()
cap.release()
cv2.destroyAllWindows() 
