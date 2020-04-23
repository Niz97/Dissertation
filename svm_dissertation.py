# -*- coding: utf-8 -*-
"""SVM Dissertation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qzAsyU9w7ibHzTKQylQyry_1HnCcaF6w
"""

# Commented out IPython magic to ensure Python compatibility.
import os
import time
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl
from tensorflow import keras
# %matplotlib inline

from sklearn import datasets
from keras.datasets import cifar10
from sklearn.model_selection import train_test_split

# load cifar data
(train_images, train_labels), (test_images, test_labels) = keras.datasets.cifar10.load_data()

# Normalise 
train_images, test_images = train_images / 255.0, test_images / 255.0

# reshape data into the format scikit requires
train_images = np.reshape(train_images, (train_images.shape[0], -1))
train_labels = np.reshape(train_labels, (train_labels.shape[0], -1))
test_images = np.reshape(test_images, (test_images.shape[0], -1))
test_labels = np.reshape(test_labels, (test_labels.shape[0], -1))

from sklearn import svm

t_labels = np.squeeze(train_labels)

def svm_clf(c, size):
    
  # classifier = svm.SVC(decision_function_shape='ovo')
  classifier = svm.SVC(C = c)

  classifier.fit(train_images[:size], t_labels[:size])

  # pred = classifier.predict(train_images[:size])

  score = classifier.score(train_images[:size], t_labels[:size])
  print(score)
  return classifier

# regularisation parameters
reg_param = [0.1,1]

# define different training sizes
training_sizes = [1000, 2000, 3000, 4000, 50000, 10000]

for i in training_sizes:
  for c in reg_param:
    print("C: ", c, "Data size: ", i)

    t_start = time.time()
    svm_clf(c, i)
    t_end = time.time()

    t_total = t_end - t_start
    print("Elapsed time: ",t_total)

# print(net.score(train_images[:s], t_labels[:s]))
# print(netTwo.score(train_images[:s], t_labels[:s]))
