from sklearn.preprocessing import StandardScaler
from scipy.stats import beta
from scipy.stats import shapiro
import statsmodels.api as sm
import numpy as np

# Tạo ra một chuỗi phân phối beta
data = beta(1,10).rvs(1000).reshape(-1,1)
print('data shape:%s'%str(data.shape))
# Sử dụng kiểm định shapiro để kiểm tra tính phân phối chuẩn
print(shapiro(data))
# Giá tr tới hạn và p-value
shapiro(StandardScaler().fit_transform(data))

#Giá trị giới hạn > p-value chúng ta bác boe giả thuyết về phân phối chuẩn

# biến đổi dữ liệu theo phân phối chuẩn:
price = np.float64(dataset.price.values)
print('Head 5 of original prices:', price[:5])
price_std = StandardScaler().fit_transform(price.reshape(-1, 1))
print('Head 5 of standard scaling prices:\n', price_std[:5])

# Biến đổi tương đương với công thức sau:
price_std = (price - price.mean())/ price.std()
print('Head 5 of standard scaling prices:\n', price_std[:5])
