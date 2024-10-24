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
shapiro()