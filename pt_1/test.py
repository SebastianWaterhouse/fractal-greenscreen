import numpy as np
import cv2, time, sys
from matplotlib import pyplot as plt

lower_green = np.array([0, 100, 0])
upper_green = np.array([140, 255, 140]) 

background_image_1 = cv2.imread(str(sys.argv[1]))

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()

	mask = cv2.inRange(frame, lower_green, upper_green)
	background_image_2 = np.copy(background_image_1)

	frame[mask != 0] = [0, 0, 0]
	crop_background = background_image_2[0:480, 0:640]
	crop_background[mask == 0] = [0, 0, 0]
	final_cap = crop_background + frame

	cv2.imshow('thing', final_cap)
	if cv2.waitKey(1) & 0xFF == ord('q'):
			break

# When everything done, release the capture
time.sleep(10)
cap.release()
cv2.destroyAllWindows()