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
    text = []
    for i in vec:
        let = int_to_chars[i]
        text.append(let)
        text = ''.join(text)
        return text

# prepare the dataset of input to output pairs encoded as intergers
seq_legth = 100
dataX = []
dataY = []
for i in range(0, n_chars - )
# import string
# #string.ascii_lowercase
# #string.punctuation
# for letter in string.punctuation:
#     print(letter, end=" ")
