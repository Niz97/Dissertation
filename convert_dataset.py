import tensorflow as tf
import os
import numpy as np

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img


cwd = os.getcwd()
new_path = cwd + '\\refined posture dataset - Copy' + '\\b'

# make a new folder for all bends
# if not os.path.exists(new_path):
#     os.makedirs(new_path)

# move all bends into same folder 
# rename each from 1 to number of images

dataset_location = '\\refined posture dataset - Copy'
folder_num = 1
data = cwd + dataset_location + '\postures'
current_folder = data + str(folder_num)

# load all bends

def load_and_convert(posture_type):
	posture_type = str(posture_type)
	np_data = []

	# iterate over all 'bend' folders
	for i in range(1,3	): 
		current_folder = data + str(i) + '\\' + posture_type	
		# get file names in folder
		folder = os.listdir(current_folder)

		# load and convert each image to numpy array
		for image in folder:
			img = load_img(current_folder + '\\' + image)

			# convert to numpy array
			img_array = img_to_array(img)
			np_data.append(img_array)
			
	return np_data
	
all_bends = load_and_convert('bend')
print(all_bends[0])
data = []

def load_images_to_np():
	for image in folder:
		# load image
		img = load_img(bend + '\\' + image)

		# convert to numpy array
		img_array = img_to_array(img)
		data.append(img_array)
