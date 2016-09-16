from wlRGB import *
from PIL import Image

from matplotlib.pyplot import imshow
import numpy as np
from cv2 import imshow, waitKey
import os
		
class SortPreprocessor:
	def __init__(self, __list):
		self.list = __list

		self.min = min(self.list)
		self.max = max(self.list)
		
		self.perc = [(float(x - self.min) / float(self.max - self.min)) for x in self.list]

		self.wl_min = 380;
		self.wl_max = 750;

		self.wl = [(x * (self.wl_max - self.wl_min) + self.wl_min) for x in self.perc]
	def export_image(self):
		self.width = 1440
		self.height = 900
		
		self.im = Image.new("RGB", (self.width, self.height))
		self.pix = self.im.load()

		self.rgb = [wl_rgb(x) for x in self.wl]

		for x in range(self.width):
			for y in range(self.height):
				b, g, r = self.rgb[(x * len(self.list)) / self.width]
				self.pix[x, y] = r, g, b
		
		imshow("gen-capture", np.array(self.im))
		waitKey(0)
		destroyWindow("gen-capture")

preproc = SortPreprocessor(range(200))
preproc.export_image()