from cv2 import *

class CaptureProcessor:
	def __init__(self):
		self.cam = VideoCapture(0) # 0 - camera index
	def capture(self):
		flag, img = self.cam.read()
		if flag:
			self.img = img
		else:
			self.img = None
	def show(self):
		if self.img != None:
			imshow("debug-capture", self.img)
			waitKey(0)
			destroyWindow("debug-capture")

processor = CaptureProcessor()
processor.capture()
processor.show()