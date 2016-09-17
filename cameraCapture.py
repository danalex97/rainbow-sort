from cv2 import *
import cv2

from PIL import Image
from scipy import ndimage as ndi
import matplotlib.pyplot as plt

import numpy as np

class CaptureProcessor:
	def __init__(self):
		self.cam = VideoCapture(0) 
	def capture(self):
		flag, img = self.cam.read()
		if flag:
			self.img = img
		else:
			self.img = None
	def show(self):
		imshow("debug-capture", self.img)
		waitKey(0)
		destroyWindow("debug-capture")
	def prepare_pixels(self):
		self.width, self.height, self.channels = self.img.shape
	def get_color(self, x, y):
		print self.img[x, y]
	def image(self, path):
		self.img = cv2.imread(path, 3)
	# def get_position(self, th):
	# 	self.prepare_pixels()
	# 	tr, tg, tb = th
	# 	for x in range(0, self.width, 10):
	# 		for y in range(0, self.height, 10):
	# 			r, g, b = 0, 0, 0
	# 			if self.width - x  - 1 > 0 and self.height - y - 1 > 0:
	# 				r,  g,  b = self.img[self.width - x - 1,  self.height - y - 1]
	# 			if r > tr and g > tg and b > tb:
	# 				return x, y

def test(path, th):
	processor = CaptureProcessor()
	processor.image(path)
	#processor.capture()

	img = cv2.resize(processor.img, (500, 500)) 
	img = ndi.rotate(img, 270)

	gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blurred_img = ndi.gaussian_filter(gray_image, sigma=15) 
	imshow("debug-capture", blurred_img)
	waitKey(0)
	# print processor.get_position(th)

test("test/blue.jpg", (0, 0, 230))
test("test/red.jpg", (230, 0, 0))
