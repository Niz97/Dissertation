import tensorflow as tf
import os
import numpy as np

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img

def img_show(path):
	img = load_img(path)

	print(type(img))
	print(img.format)
	print(img.mode)
	print(img.size)
	# show the image
	img.show()

# load image
bend = r'C:\Users\niran\Documents\Work\Project\Build Dataset\gen\refined posture dataset\postures1\bend'
folder = os.listdir(bend)

data = []

def load_images_to_np():
	for image in folder:
		# load image
		img = load_img(bend + '\\' + image)

		# convert to numpy array
		img_array = img_to_array(img)
		data.append(img_array)

# move images from one folder to another
load_images_to_np()
print(data[0])
# all_bends = r'C:\Users\niran\Documents\Work\Project\Build Dataset\gen\refined posture dataset - Copy'
# cwd = os.getcwd()
# new_path = cwd + 'refind posture dataset - Copy' + 'b'
# print

# if not os.path.exists(new_path):
#     os.makedirs(new_path)
