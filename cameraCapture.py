from cv2 import *

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
		self.height, self.width, self.channels = self.img.shape
	def get_color(self, x, y):
		print self.img[x, y]
