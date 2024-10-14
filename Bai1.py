#chúng ta sẽ sử dụng dữ liệu trong cuộc thi của thi Two Sigma Connect: Rental Listing Inquiries Kaggle competition. File train.json là dữ liệu training. Bài toán của chúng ta là cần dự báo mức độ tín nhiệm của một danh sách những người thuê mới. Chúng ta phân loại danh sách thành 3 cấp độ [‘low’, ‘medium’, ‘high’]. Để đánh giá kết quả chúng ta sử dụng hàm trung bình sai số rmse.
import json
import pandas as pd
with open('.../input/train.json',"r") as iodata
    data = json.load(iodata)
    dataset = pd.Dataframe(data)

data.head