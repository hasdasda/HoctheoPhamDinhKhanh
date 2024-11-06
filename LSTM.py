import numpy
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.callbacks import ModelCheckpoint
from tensorflow.python.keras.utils import np_utils
import os

filename = 'wonderland.txt'
raw_text = open(filename).read().lower()

chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
print('number of letters: ', len(char_to_int))
print(char_to_int)

import string
string.ascii_lowercase
# string.digits
# string.punctuation
chars_new = list(string.ascii_lowercase) + ['0', '.', ',', ' ', '!', '?', 'unk']
chars_to_int = dict((v, k) for k, v in enumerate(chars_new))
int_to_chars = dict((k, v) for k, v in enumerate(chars_new))
print('character to int:', chars_to_int)
print('int to character:', int_to_chars)
# def _clean_char(text):
#     return 1
n_chars = len(raw_text)
n_vocab = len(chars_new)
print('Total character:', n_chars)
print('Total Vocab', n_vocab)

def _encode_sen(text):
    text = text.lower()  # Chuyển tất cả các ký tự trong chuỗi về chữ thường.
    sen_vec = []  # Tạo một danh sách trống để chứa các chỉ số của từng ký tự.
    for let in text:  # Duyệt qua từng ký tự trong chuỗi đầu vào.
        if let in chars_new[:-1]:  # Kiểm tra nếu ký tự nằm trong bảng ký tự (trừ phần tử cuối).
            idx = char_to_int[let]  # Lấy chỉ số tương ứng từ dictionary `char_to_int`.
        else:
            idx = chars_to_int['unk']  # Nếu không, gán chỉ số của ký tự 'unk' (unknown).
        sen_vec.append(idx)  # Thêm chỉ số vào danh sách.
    return sen_vec  # Trả về danh sách các chỉ số.
x_test = _encode_sen('Alice is wonderful story. #')
print(x_test)

def _decode_sen(vec):
    text = [] # Kởi tạo ột danh sách rỗng để chứa các ký tự giải mã
    for i in vec: # Duyệt qua từng phần tử i trong vec
        let = int_to_chars[i] # Lấy ký tự từ int_to_chars dựa trên chỉ số I
        text.append(let) # Thêm ký tự đã lấy được vào danh sách text
        text = ''.join(text) # Ghép các phần tử trong text thành một chuỗi
        return text

# prepare the dataset of input to output pairs encoded as intergers
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
    # Lấy ra 100 kí tự liền trước:
    seq_in = raw_text[i: i+ seq_length]
    # Lấy ra kí tự liền sau 100 kí tự đó
    seq_out = raw_text[i+ seq_length]
    dataX.append(_encode_sen(seq_in))
    dataY.append(_encode_sen(seq_out)[0])
    n_patterns = len(dataX)
print("Total Patterns:", n_patterns)

# Reshape X to be [samples, time steps, features]
X_train = numpy.reshape(dataX, (n_patterns, seq_length, 1))
# Normalize
X_train = X_train / float(n_vocab)
# One hot encode the output variable
y_train = np_utils.to_categorical(dataY)
print('X [samples, time steps, features] shape:', X_train.shape)
print('Y shape:', y_train.shape)

print(type(X_train))
print(type(y_train))

# Thống kê ố luọng các ký tự theo nhóm
import seaborn as sn
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
sn.countplot(sn.array(dataY))
plt.xticks(np.arange(32),np.array(chars_new))


    # Lấy ra kí tự lie
# import string
# #string.ascii_lowercase
# #string.punctuation
# for letter in string.punctuation:
#     print(letter, end=" ")
