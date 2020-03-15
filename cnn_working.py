# -*- coding: utf-8 -*-
"""CNN Working.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zynuIu59H3tNmUy_YWTYIu6nTRCCXWPQ
"""

# Commented out IPython magic to ensure Python compatibility.
from __future__ import absolute_import, division, print_function, unicode_literals

try:
  # %tensorflow_version only exists in Colab.
#   %tensorflow_version 2.x
except Exception:
  pass
import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
# (train_images, train_labels), (test_images, test_labels) =tf.keras.datasets.cifar100.load_data(
#     label_mode='fine'



# Normalise pixles between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

label_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']
epochs = 100

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    # The CIFAR labels happen to be arrays, 
    # which is why you need the extra index
    plt.xlabel(label_names[train_labels[i][0]])             
plt.show()

def threeConv2D():
  model = models.Sequential()
  # cifar data is 32x32 with 3 colour channels (RGB)
  model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.MaxPooling2D((2, 2)))

  return model

def fourFoldConv():
  model = models.Sequential()
  model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))
  model.add(layers.Conv2D(64, (3, 3), activation='relu'))


  return model


def customNet():
  model = models.Sequential()
  model.add(layers.Dense(32, kernel_initializer='uniform', input_shape=(32, 32, 3)))
  model.add(layers.Activation('relu'))

  # sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
  model.compile(loss='mean_squared_error', optimizer='sgd')
  return model

def customNetWithSigmoid():
  model = models.Sequential()
  model.add(layers.Conv2D(32, (3,3), activation='sigmoid', input_shape=(32,32,3)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Dense(32, kernel_initializer='uniform', input_shape=(32, 32, 3)))
  model.add(layers.Activation('sigmoid'))

  model.compile(loss='mean_squared_error', optimizer='sgd')

  return model

# convModel = threeConv2D()
# convModel.summary()

net = fourFoldConv()
net.summary()

# Flatten layers
# create 10 output channels
def flattenLayers(model):
  model.add(layers.Flatten())
  model.add(layers.Dense(64, activation="relu"))
  model.add(layers.Dense(10, activation="softmax"))

  model.summary()
  # tf.keras.utils.plot_model(model, 'multi_input_and_output_model.png', show_shapes=True)
  return model

convNet = flattenLayers(net)
tf.keras.utils.plot_model(convNet, 'multi_input_and_output_model.png', show_shapes=True)

# Build and train the model 


# compile model https://www.tensorflow.org/guide/keras/functional 
convNet.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# fit model
history = convNet.fit(train_images, train_labels, epochs=epochs, 
                    validation_data=(test_images, test_labels))

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')

test_loss, test_acc = convNet.evaluate(test_images,  test_labels, verbose=2)
print("Loss: ", test_loss)
print("Accuracy: ", test_acc)