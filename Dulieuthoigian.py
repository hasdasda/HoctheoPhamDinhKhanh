# https://strftime.org/
# dataset['created'].apply(lambda x: x.date().weekday())
from datatime import datetime
def parser(x):
    # Để biết được định dạng strftime của một chuỗi kí tự ta phải tra trong bảng string format time
    return datetime.strptime(x,'%Y-%m-%d %H:%M:%S')

dataset['created'] = dataset['created'].map(lambda x:parser(x))
#Kiểm tra định dạng time
for i, k in zip(dataset.columns, dataset.dtypes):
    print('{}: {}'.format(i,k))