# https://strftime.org/
# dataset['created'].apply(lambda x: x.date().weekday())
from datatime import datetime
def parser(x):
    # Để biết được định dạng strftime của một chuỗi kí tự ta phải tra trong bảng string format time
return datetime.strptime