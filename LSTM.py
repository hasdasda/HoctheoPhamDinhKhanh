import numpy
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.callbacks import ModelCheckpoint
from tensorflow.python.keras.utils import np_utils
import os

filename = '../input/wonderland.txt'
raw_text = open(filename).read().lower()

