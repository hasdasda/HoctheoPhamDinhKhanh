#chúng ta sẽ sử dụng dữ liệu trong cuộc thi của thi Two Sigma Connect: Rental Listing Inquiries Kaggle competition. File train.json là dữ liệu training. Bài toán của chúng ta là cần dự báo mức độ tín nhiệm của một danh sách những người thuê mới. Chúng ta phân loại danh sách thành 3 cấp độ [‘low’, ‘medium’, ‘high’]. Để đánh giá kết quả chúng ta sử dụng hàm trung bình sai số rmse.
# import json
# import pandas as pd
# with open('.../input/train.json',"r") as iodata
#     data = json.load(iodata)
#     dataset = pd.Dataframe(data)
#
# print(data.head)
#
# from functools import reduce
# import numpy as np
#
# # Giả sử một texts có 3 câu văn là các phần tử trong list như bên dưới
# texts = [['i', 'have', 'a', 'cat'],
#          ['he', 'have', 'a', 'dog'],
#          ['he', 'and', 'i', 'have', 'a', 'cat', 'and', 'a', 'dog']]
#
# dictionary = list(enumerate(set(reduce(lambda x, y: x + y, texts))))
#
#
# # Dictionary sẽ chứa toàn bộ các từ của texts.
#
# def bag_of_word(sentence):
#     # Khởi tạo một vector có độ dài bằng với từ điển.
#     vector = np.zeros(len(dictionary))
#     # Đếm các từ trong một câu xuất hiện trong từ điển.
#     for i, word in dictionary:
#         count = 0
#         # Đếm số từ xuất hiện trong một câu.
#         for w in sentence:
#             if w == word:
#                 count += 1
#         vector[i] = count
#     return vector
#
#
# for i in texts:
#     print(bag_of_word(i))

# Các biểu diễn theo túi từ có hạn chế đó là chúng ta không phân biệt được 2 câu văn có cùng các từ bới túi từ không phân biệt thứ tự trước sau của các từ trong một câu.Chặng như ‘you have no dog’ và ‘no, you have dog’ là 2 câu văn có biểu diễn giống nhau mặc dù có ý nghĩa trái ngược nhau. Chính vì thế phương pháp N-gram sẽ được sử dụng thay thế.

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(ngram_range=(1,1))
vect.fit_transform(['you have no dog','no, you have dog']).toarray()

print(vect.vocabulary_)

# from sklearn.feature_extraction.text import CountVectorizer
# corpus = [
#     'This is the first document.',
#     'This document is the second document.',
#     'And this is the third one.',
#     'Is this the first document?',
# ]
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(corpus)
# vectorizer.get_feature_names_out()
# print(vectorizer)
# print(X.toarray())
# vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2,2))
# X2 = vectorizer2.fit_transform(corpus)
# print(vectorizer2.get_feature_names_out())
# print(X2.toarray())
