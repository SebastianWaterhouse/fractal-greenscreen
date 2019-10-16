from PIL import Image
import cv2

#Default values, to be changeable in tkinter GUI
width = 640
height = 480
zoom = 1


moveX = 0.0
moveY = 0.0
maxIter=10

image1 = Image.new("RGB", (width, height), "white")
pix = image1.load()


def julia(ccX, ccY):
	for x in range(width):
		for y in range(height):
			zx = 1.5*(x - width/2)/(0.5*zoom*width) + moveX
			zy = 1.0*(y - height/2)/(0.5*zoom*height) + moveY
			i = maxIter
			while zx*zx + zy*zy < 4 and i > 1:
				tmp = zx*zx - zy*zy + ccX
				zy = 2*zx*zy + ccY
				zx = tmp
				i -= 1
			pix[x, y]  = (i << 21) + (i << 10) + i*8
	image1.save("a.jpg", "JPEG")

def cSwitch(increment, xSign, ySign, cX, cY):
	cSwitch.xSign = xSign
	cSwitch.ySign = ySign
	cSwitch.cX = cX
	cSwitch.cY = cY
	if cX <= -.75:
		xSign = "pos"
	elif cX >= -.65:
		cSwitch.xSign = "neg"
	if cY >= .27265:
		cSwitch.ySign = "neg"
	elif cY <= .26265:
		cSwitch.ySign = "pos"
	if cSwitch.xSign == "neg":
		cSwitch.cX -= increment
	elif cSwitch.xSign == "pos":
		cSwitch.cX += increment
	if cSwitch.ySign == "pos":
		cSwitch.cY += increment
	elif cSwitch.ySign == "neg":
		cSwitch.cY -= increment


def main():
	z = 0
	cX = -.7
	cY = .27015
	cSwitch(.005, "neg", "pos", cX, cY)
	while True:
		z += 1
		print("frame " + str(z))
		cSwitch(.001, "neg", "pos", cSwitch.cX, cSwitch.cY)
		image1 = Image.new("RGB", (width, height), "white")
		pix = image1.load()

		julia(cSwitch.cX, cSwitch.cY)

		image2 = cv2.imread("a.jpg")
		cv2.imshow("fractal", image2)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

main()