import numpy as np
import cv2, time, sys, threading
from PIL import Image
import test_cam, test_frac

p = 0
lower_green = input("Please input a minimum RGB tuplet (0 100 0): ").split()
for x in lower_green:
	lower_green[p] = int(x)
	p += 1
print(lower_green)
upper_green = input("Please input a maximum RGB tuplet (170 255 170): ").split()
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
width = int(input("Please input the width of your webcam: "))
height = int(input("Please input the height of your webcam: "))

test_cam.init(lower_green, upper_green)
test_frac.init(width, height)

thread1 = threading.Thread(target=test_frac.main, args=(maxIter, toRun, lowercX, uppercX, lowercY, uppercY))
thread2 = threading.Thread(target=test_cam.camera)

thread1.start()
thread2.start()

thread2.join()
thread1.join()

print("Exited successfully.")