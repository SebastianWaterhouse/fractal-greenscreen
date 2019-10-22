import numpy as np
import cv2, time, sys, threading



def init(lower_greenn, upper_greenn):
	global cap, lower_green, upper_green
	cap = cv2.VideoCapture(0)
	lower_green = np.array(lower_greenn)
	upper_green = np.array(upper_greenn)

def camera(lower_greennn, upper_greennn):
	init(lower_greennn, upper_greennn)
	while(True):
		try:
			background_image_1 = cv2.imread("a.jpg")
			ret, frame = cap.read()

			mask = cv2.inRange(frame, lower_green, upper_green)
			background_image_2 = np.copy(background_image_1)

			frame[mask != 0] = [0, 0, 0]
			background_image_2[mask == 0] = [0, 0, 0]
			final_cap = background_image_2 + frame
			cv2.imwrite("a.old.jpg", background_image_1)
		except IndexError:
			print("Desync!")
			background_image_1 = cv2.imread("a.old.jpg")
			ret, frame = cap.read()

			mask = cv2.inRange(frame, lower_green, upper_green)
			background_image_2 = np.copy(background_image_1)

			frame[mask != 0] = [0, 0, 0]
			background_image_2[mask == 0] = [0, 0, 0]
			final_cap = background_image_2 + frame

		cv2.imshow('thing', final_cap)
		if cv2.waitKey(1) & 0xFF == ord('q'):
				break

	cap.release()
	cv2.destroyAllWindows()