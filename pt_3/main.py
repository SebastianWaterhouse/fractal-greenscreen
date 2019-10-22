import numpy as np
import cv2, time, sys, multiprocessing
from PIL import Image

p = 0



if __name__ == "__main__":
	import test_cam, test_frac
	default_values = input("Do you want to use the default values? (Y/N): ")

	if default_values in ["Yes", "Y", "y", "yes"]:
		lower_green = [0, 100, 0]
		upper_green = [170, 255, 170]
		toRun = "julia"
		maxIter = 7
		lowercX = -0.8
		uppercX = -0.4
		lowercY = 0.1
		uppercY = 1.0
	else:
		lower_green = input("Please input a minimum RGB tuple (0 100 0): ").split()
		for x in lower_green:
			lower_green[p] = int(x)
			p += 1
		print(lower_green)
		upper_green = input("Please input a maximum RGB tuple (170 255 170): ").split()
		p = 0
		for y in upper_green:
			upper_green[p] = int(y)
			p += 1
		toRun = input("Please input which set you would like to use ('julia' or 'mandelbrot'): ")
		maxIter = int(input("Please input the maximum number of iterations (10): "))
		lowercX = float(input("Please input the lower bound for cX (-0.8): "))
		uppercX = float(input("Please input the upper bound for cX (-0.4): "))
		lowercY =float(input("Please input the lower bound for cY (0.1): "))
		uppercY = float(input("Please input the upper bound for cY (1.0): "))

	thread1 = multiprocessing.Process(target=test_frac.main, args=(maxIter, toRun, lowercX, uppercX, lowercY, uppercY))
	thread2 = multiprocessing.Process(target=test_cam.camera, args=(lower_green, upper_green))

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	print("Exited successfully.")