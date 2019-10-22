from PIL import Image
import cv2, sys, threading
import tkinter as tk
from numpy import complex, array 



def init():
	global width, height, image1, pix
	cap = cv2.VideoCapture(0)
	width = int(cap.get(3)) #Should automatically get the resolution of your camera and work properly.
	height = int(cap.get(4))
	cap.release()
	image1 = Image.new("RGB", (width, height), "white")
	pix = image1.load()

zoom = 1

moveX = 0.0
moveY = 0.0



def mandelbrot(cX, cY, maxIter, uppercX, uppercY):
	for y in range(height): 
		zy = y * (uppercY - cY) / (height - 1)  + cY
		for x in range(width): 
			zx = x * (uppercX - cX) / (width - 1)  + cX 
			z = zx + zy * 1j
			c = z 
			for i in range(maxIter): 
				if abs(z) > 2.0: break
				z = z * z + c 
			image1.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))
	image1.save("a" + ".jpg", "JPEG")

def julia(ccX, ccY, maxIter):
	for x in range(width):
		for y in range(height):
			zx = 1.5*(x - width/2)/(0.5*zoom*width) + moveX
			zy = 1.0*(y - height/2)/(0.5*zoom*height) + moveY
			i = int(maxIter)
			while zx*zx + zy*zy < 4 and i > 1:
				tmp = zx*zx - zy*zy + ccX
				zy = 2*zx*zy + ccY
				zx = tmp
				i -= 1
			pix[x, y]  = (i << 21) + (i << 10) + i*8
	image1.save("a" + ".jpg", "JPEG")

def cSwitch(increment, xSign, ySign, cX, cY, lowercX, uppercX, lowercY, uppercY):
	cSwitch.xSign = xSign
	cSwitch.ySign = ySign
	cSwitch.cX = cX
	cSwitch.cY = cY
	if cSwitch.cX < lowercX:
		cSwitch.xSign = "pos"
	elif cSwitch.cX >= uppercX:
		cSwitch.xSign = "neg"
	if cSwitch.cY >= uppercY:
		cSwitch.ySign = "neg"
	elif cSwitch.cY <= lowercY:
		cSwitch.ySign = "pos"
	if cSwitch.xSign == "neg":
		cSwitch.cX -= increment
	elif cSwitch.xSign == "pos":
		cSwitch.cX += increment
	if cSwitch.ySign == "pos":
		cSwitch.cY += increment
	elif cSwitch.ySign == "neg":
		cSwitch.cY -= increment


def main(maxIter, toRun, lowercX, uppercX, lowercY, uppercY):
	init()
	z = 0
	cX = -.7
	cY = .27015
	cSwitch(.2, "neg", "pos", cX, cY, lowercX, uppercX, lowercY, uppercY)
	while True:
		z += 1
		print("frame " + str(z))
		cSwitch(.001, cSwitch.xSign, cSwitch.ySign, cSwitch.cX, cSwitch.cY, lowercX, uppercX, lowercY, uppercY)
		image1 = Image.new("RGB", (width, height), "white")
		pix = image1.load()
		if toRun == "julia":
			julia(cSwitch.cX, cSwitch.cY, maxIter)
		elif toRun == "mandelbrot":
			mandelbrot(cSwitch.cX, cSwitch.cY, maxIter, uppercX, uppercY)
		else:
			print("Unrecognized set!")
			break
		image2 = cv2.imread("a.jpg")
		cv2.imshow("fractal" + "a", image2)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break