import tensorflow as tf

from tensorflow.keras.models import Sequential #type: ignore
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D #type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator #type: ignore

import os
import numpy as np
import matplotlib.pyplot as plt

# Get project files
# !wget https://cdn.freecodecamp.org/project-data/cats-and-dogs/cats_and_dogs.zip

# !unzip cats_and_dogs.zip

PATH = 'Machine Learning with Python Projects/Cat and Dog Image Classifier/cats_and_dogs'

train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')
test_dir = os.path.join(PATH, 'test')

# Get number of files in each directory. The train and validation directories
# each have the subdirecories "dogs" and "cats".
total_train = sum([len(files) for r, d, files in os.walk(train_dir)])
total_val = sum([len(files) for r, d, files in os.walk(validation_dir)])
total_test = len(os.listdir(test_dir))

print(total_train)
print(total_val)
print(total_test)